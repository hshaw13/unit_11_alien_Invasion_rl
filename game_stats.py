class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False  # Start in inactive state

    def reset_stats(self):
        """Reset statistics that change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
