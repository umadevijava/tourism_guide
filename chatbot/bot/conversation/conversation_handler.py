import re
from typing import Any

from chatbot.entities.document import Document
from chatbot.helpers.log import get_logger

from chatbot.bot.client.lama_cpp_client import LamaCppClient
from chatbot.bot.conversation.chat_history import ChatHistory
from chatbot.bot.conversation.ctx_strategy import BaseSynthesisStrategy

logger = get_logger(__name__)


async def refine_question(
    llm: LamaCppClient, question: str, chat_history: ChatHistory, max_new_tokens: int = 128
) -> str:
    """
    Returns the original question without modification.

    Args:
        llm (LlmClient): The language model client for conversation-related tasks.
        question (str): The original question.
        chat_history (List[Tuple[str, str]]): A list to store the conversation
        history (maintained for potential future use but NOT used to influence refinement).
        max_new_tokens (int, optional): The maximum number of tokens to generate in the answer.
            Defaults to 128.

    Returns:
        str: The original question unchanged, ensuring focus on current user input.
        
    Notes:
        The method now returns the question as-is to ensure the chatbot responds to what
        the user actually asked without modification based on previous conversation context.
        This prevents the model from misinterpreting the current question based on prior history.
    """
    
    logger.info("--- Using original question for retrieval (no refinement based on history) ---")
    logger.debug(f"--- Original Question: {question} ---")
    
    # Return the question as-is, ensuring focus on the user's current input
    return question


async def answer(llm: LamaCppClient, question: str, chat_history: ChatHistory, max_new_tokens: int = 512) -> Any:
    """
    Generates an answer to the given question focusing on the current question only.

    Args:
        llm (LlmClient): The language model client for conversation-related tasks.
        question (str): The input question for which an answer is generated.
        chat_history (List[Tuple[str, str]]): A list to store the conversation
        history (maintained for potential future use but NOT used to influence current answer).
        max_new_tokens (int, optional): The maximum number of tokens to generate in the answer.
            Defaults to 512.

    Returns:
        A streaming iterator (Any) for progressively generating the answer.

    Notes:
        The method generates a response based ONLY on the current question.
        The chat_history parameter is maintained for backward compatibility and future use,
        but the response is generated independently of previous messages to ensure the chatbot
        responds to the user's current input without being influenced by prior questions.
    """
    
    logger.info("--- Answer the current question independently ---")
    
    # Generate answer based on CURRENT question only, ignoring chat history
    prompt = llm.generate_qa_prompt(question=question)
    logger.debug(f"--- Prompt:\n {prompt} \n---")
    streamer = await llm.async_start_answer_iterator_streamer(prompt, max_new_tokens=max_new_tokens)
    return streamer


async def answer_with_context(
    llm: LamaCppClient,
    ctx_synthesis_strategy: BaseSynthesisStrategy,
    question: str,
    chat_history: ChatHistory,
    retrieved_contents: list[Document],
    max_new_tokens: int = 512,
):
    """
    Generates an answer to the given question using a context synthesis strategy and retrieved contents.
    If the content is not provided generates an answer based on the chat history or a direct prompt.

    Args:
        llm (LlmClient): The language model client for conversation-related tasks.
        ctx_synthesis_strategy (BaseSynthesisStrategy): The strategy to use for context synthesis.
        question (str): The input question for which an answer is generated.
        chat_history (List[Tuple[str, str]]): A list to store the conversation
        history as tuples of questions and answers.
        retrieved_contents (list[Document]): A list of documents retrieved for context.
        max_new_tokens (int, optional): The maximum number of tokens to generate in the answer. Defaults to 512.

    Returns:
        tuple: A tuple containing the answer streamer and formatted prompts.
    """
    if not retrieved_contents:
        return await answer(llm, question, chat_history, max_new_tokens=max_new_tokens), []

    streamer, fmt_prompts = await ctx_synthesis_strategy.generate_response(
        retrieved_contents, question, max_new_tokens=max_new_tokens
    )

    return streamer, fmt_prompts


def extract_content_after_reasoning(text: str, reasoning_stop_tag: str) -> str:
    """
    Extracts and strips the text that follows the `reasoning_stop_tag` tag.

    Args:
        text: The input string containing the tag.
        reasoning_stop_tag: The tag after which the text should be extracted.

    Returns:
        The text after the `reasoning_stop_tag` tag, stripped of whitespace, or an empty string
        if the tag is not found.
    """
    try:
        _, content = re.split(reasoning_stop_tag, text, maxsplit=1, flags=re.IGNORECASE)

        if content == "":
            logger.warning(f"Reasoning stop tag '{reasoning_stop_tag}' found but no content after it.")
        else:
            logger.info(f"Extracted content after reasoning stop tag '{reasoning_stop_tag}': {content}")

        return content.strip()
    except ValueError:
        logger.warning(f"Reasoning stop tag '{reasoning_stop_tag}' not found in the text. Returning empty content.")
        return ""


# TODO: Use it later
async def stream_response_with_reasoning(
    llm: LamaCppClient, user_input: str, chat_history: ChatHistory, max_new_tokens: int
) -> tuple[str, str]:
    """
    Streams a response from the language model (LLM) to the user input, including reasoning, and
    updates the UI in real-time.

    Args:
        llm (LamaCppClient): The language model client used to generate responses.
        user_input (str): The input provided by the user.
        chat_history (ChatHistory): The conversation history to provide context for the response.
        max_new_tokens (int): The maximum number of tokens to generate in the response.

    Returns:
        tuple[str, str]: A tuple containing:
            - full_response (str): The full response generated by the LLM.
            - reasoning_response (str): The reasoning portion of the response.

    Notes:
        - The function uses a placeholder to display the response progressively in the UI.
        - The reasoning portion is identified and displayed separately using start and stop tags.
        - The response is updated token by token, with a cursor ("▌") indicating ongoing generation.
    """
    full_response = ""
    reasoning_response = ""
    inside_think = False
    for token in await answer(llm=llm, question=user_input, chat_history=chat_history, max_new_tokens=max_new_tokens):
        parsed_token = llm.parse_token(token)
        stripped_token = parsed_token.strip()

        if stripped_token == llm.model_settings.reasoning_start_tag:
            inside_think = True
            reasoning_response += parsed_token
            continue

        if stripped_token == llm.model_settings.reasoning_stop_tag:
            inside_think = False
            reasoning_response += parsed_token
            continue

        if inside_think:
            reasoning_response += parsed_token
        else:
            full_response += llm.parse_token(token)

    return full_response, reasoning_response
