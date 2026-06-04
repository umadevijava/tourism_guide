import { useEffect, useRef } from "react"
import { ScrollArea } from "@/components/ui/scroll-area"
import { ChatMessage, type Message } from "./chat-message"
import { MapPin, Plane, Map, Calendar } from "lucide-react"

interface ChatViewportProps {
  messages: Message[]
}

export function ChatViewport({ messages }: ChatViewportProps) {
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  return (
    <ScrollArea className="flex-1 px-4">
      {messages.length === 0 ? (
        <div className="min-h-full flex flex-col items-center justify-center py-8">
          <EmptyState />
        </div>
      ) : (
        <div className="max-w-4xl mx-auto py-8 space-y-6">
          {messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}
          <div ref={bottomRef} />
        </div>
      )}
    </ScrollArea>
  )
}

function EmptyState() {
  return (
    <div className="flex-1 flex flex-col items-center justify-center px-4">
      <div className="max-w-2xl w-full text-center space-y-8">
        {/* Logo/Icon with Animation */}
        <div className="relative mx-auto w-24 h-24">
          <div className="absolute inset-0 bg-gradient-to-r from-primary/30 via-accent/20 to-primary/30 rounded-full blur-3xl animate-pulse" />
          <div className="relative flex items-center justify-center w-full h-full rounded-full bg-gradient-to-br from-primary/20 to-accent/10 border-2 border-primary/40">
            <MapPin className="h-12 w-12 text-navy" />
          </div>
        </div>

        {/* Welcome Text */}
        <div className="space-y-3">
          <h1 className="text-4xl font-bold text-foreground tracking-tight text-balance">
            Welcome to Tourism Guide AI
          </h1>
          <p className="text-muted-foreground text-lg leading-relaxed max-w-md mx-auto text-pretty">
            Your intelligent companion for discovering amazing destinations, exploring cultural treasures, and planning unforgettable journeys.
          </p>
        </div>

        {/* Tourism Features */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4">
          {capabilities.map((cap, i) => (
            <div
              key={i}
              className="group p-5 rounded-xl bg-gradient-to-br from-secondary/60 to-secondary/30 border border-border/60 hover:border-primary/40 hover:bg-secondary/70 text-left transition-all duration-300 hover:shadow-lg hover:-translate-y-0.5"
            >
              <div className="flex items-center gap-3 mb-3">
                {cap.icon}
                <span className="text-sm font-semibold text-foreground">{cap.title}</span>
              </div>
              <p className="text-xs text-muted-foreground leading-relaxed">
                {cap.description}
              </p>
            </div>
          ))}
        </div>

        {/* Tourism Suggestions */}
        <div className="pt-6 space-y-4">
          <p className="text-sm font-medium text-foreground">What would you like to explore?</p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {suggestions.map((suggestion, i) => (
              <button
                key={i}
                className="px-5 py-3 text-sm text-foreground bg-gradient-to-r from-secondary/40 to-secondary/20 hover:from-primary/20 hover:to-accent/10 border border-border/50 hover:border-primary/40 rounded-lg transition-all duration-300 hover:shadow-md hover:-translate-y-0.5 text-left"
              >
                {suggestion}
              </button>
            ))}
          </div>
        </div>

        {/* Quick Tips */}
        <div className="pt-4 text-xs text-muted-foreground/70 space-y-1">
          <p>💡 Ask about destinations, travel tips, nearby attractions, or local experiences</p>
        </div>
      </div>
    </div>
  )
}

const capabilities = [
  {
    icon: <Plane className="h-5 w-5 text-navy" />,
    title: "Explore Destinations",
    description: "Discover travel information, culture, history, and attractions around the world.",
  },
  {
    icon: <Map className="h-5 w-5 text-navy" />,
    title: "Nearby Attractions",
    description: "Find interesting places, landmarks, and activities near your desired location.",
  },
  {
    icon: <Calendar className="h-5 w-5 text-navy" />,
    title: "Travel Planning",
    description: "Get personalized recommendations, best times to visit, and travel tips.",
  },
]

const suggestions = [
  "Tell me about the Taj Mahal",
  "What are popular destinations in Japan?",
  "Best time to visit Paris",
  "What should I pack for Egypt?",
  "Tell me about Rome's historical sites",
  "Budget-friendly destinations in Southeast Asia",
]
