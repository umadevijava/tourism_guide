import { useState, useCallback, useMemo, useEffect } from 'react';
import { ChatHeader, ChatViewport, ChatInput, type Message, type ChatModes } from '@/components/chat';
import { useChat } from '@/hooks/useChat';
import { useDocuments } from '@/hooks/useDocuments';
import { AlertCircle } from 'lucide-react';

function App() {
  const [modes, setModes] = useState<ChatModes>({
    rag: false,
    reasoning: false,
    webSearch: false,
  });
  const [backendAvailable, setBackendAvailable] = useState(true);

  const { messages: rawMessages, isStreaming, sendMessage, clearMessages, backendError } = useChat();
  const { documents, uploading, setDocuments, setUploading, setError } = useDocuments();

  useEffect(() => {
    setBackendAvailable(!backendError);
  }, [backendError]);

  // Map hook's Message shape to template's Message shape
  const messages: Message[] = useMemo(
    () =>
      rawMessages.map((msg) => ({
        id: String(msg.id),
        role: msg.sender === 'user' ? ('user' as const) : ('assistant' as const),
        content: msg.text,
        isStreaming: msg.isStreaming,
      })),
    [rawMessages],
  );

  const handleSend = useCallback(
    (content: string) => {
      sendMessage(content, modes.rag);
    },
    [sendMessage, modes.rag],
  );

  const handleNewChat = useCallback(() => {
    clearMessages();
  }, [clearMessages]);

  const handleUploadStart = useCallback(
    (filename: string) => {
      setError(null);
      setUploading({ filename, progress: 0 });
    },
    [setError, setUploading],
  );

  const handleUploadProgress = useCallback(
    (filename: string, progress: number) => {
      setUploading({ filename, progress });
    },
    [setUploading],
  );

  const handleUploadEnd = useCallback(() => {
    setUploading(null);
  }, [setUploading]);

  const handleError = useCallback(
    (message: string) => {
      setError(message);
    },
    [setError],
  );

  return (
    <div className="flex flex-col min-h-dvh bg-background">
      <ChatHeader onNewChat={handleNewChat} disabled={isStreaming} />
      
      {!backendAvailable && (
        <div className="px-4 py-3 bg-amber-500/10 border-b border-amber-500/30 flex items-center gap-2">
          <AlertCircle className="h-4 w-4 text-amber-600" />
          <div className="flex-1">
            <p className="text-sm text-amber-700 font-medium">
              Backend server is not available. Make sure the backend is running on {import.meta.env.VITE_API_URL || 'localhost:8000'}
            </p>
          </div>
        </div>
      )}

      <main className="flex-1 flex flex-col min-h-0">
        <ChatViewport messages={messages} />

        <div className="sticky bottom-0 z-10 shrink-0 border-t border-border/30 bg-background/95 backdrop-blur-md">
          <ChatInput
            onSend={handleSend}
            isLoading={isStreaming}
            modes={modes}
            onModesChange={setModes}
            documents={documents}
            uploading={uploading}
            onDocumentsChange={setDocuments}
            onUploadStart={handleUploadStart}
            onUploadProgress={handleUploadProgress}
            onUploadEnd={handleUploadEnd}
            onError={handleError}
          />
        </div>
      </main>
    </div>
  );
}

export default App;
