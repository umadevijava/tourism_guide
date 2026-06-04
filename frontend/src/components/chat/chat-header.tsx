import { Button } from "@/components/ui/button"
import { Compass, Plus, History, Settings, Globe } from "lucide-react"

interface ChatHeaderProps {
  onNewChat: () => void
  disabled?: boolean
}

export function ChatHeader({ onNewChat, disabled }: ChatHeaderProps) {
  return (
    <header className="shrink-0 border-b border-border/50 bg-gradient-to-r from-background via-background to-background/80 backdrop-blur-md">
      <div className="h-16 max-w-7xl mx-auto px-4 flex items-center justify-between">
        {/* Logo & Branding */}
        <div className="flex items-center gap-3">
          <div className="relative group">
            <div className="absolute inset-0 bg-primary/25 rounded-xl blur-lg group-hover:blur-xl transition-all duration-300" />
            <div className="relative flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-primary/20 to-primary/10 border border-primary/30 group-hover:border-primary/50 transition-colors">
              <Compass className="h-6 w-6 text-navy" />
            </div>
          </div>
          <div className="flex flex-col gap-0.5">
            <div className="flex items-center gap-2">
              <h1 className="font-bold text-lg text-foreground tracking-tight">Tourism Guide AI</h1>
              <Globe className="h-4 w-4 text-navy/70" />
            </div>
            <p className="text-xs text-muted-foreground/80">Explore. Discover. Travel.</p>
          </div>
        </div>

        {/* Actions */}
        <div className="flex items-center gap-1.5">
          <Button
            variant="ghost"
            size="sm"
            className="text-muted-foreground hover:text-foreground hover:bg-secondary/50 transition-colors"
            title="View chat history"
          >
            <History className="h-4 w-4 mr-2" />
            <span className="hidden sm:inline text-xs">History</span>
          </Button>
          <Button
            variant="ghost"
            size="sm"
            onClick={onNewChat}
            disabled={disabled}
            className="text-muted-foreground hover:text-foreground hover:bg-secondary/50 transition-colors disabled:opacity-50"
            title="Start a new conversation"
          >
            <Plus className="h-4 w-4 mr-2" />
            <span className="hidden sm:inline text-xs">New Chat</span>
          </Button>
          <Button
            variant="ghost"
            size="icon"
            className="text-muted-foreground hover:text-foreground hover:bg-secondary/50 transition-colors"
            title="Settings"
          >
            <Settings className="h-4 w-4" />
            <span className="sr-only">Settings</span>
          </Button>
        </div>
      </div>
    </header>
  )
}
