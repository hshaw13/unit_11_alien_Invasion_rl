import pygame
from pygame.font import Font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.font = Font(None, 36)

        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = f"Score: {self.stats.score}"
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect(topleft=(10, 10))

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect(topleft=(10, 40))

    def prep_ships(self):
        """Turn ships left into a rendered image."""
        ships_str = f"Ships: {self.stats.ships_left}"
        self.ships_image = self.font.render(ships_str, True, self.text_color)
        self.ships_rect = self.ships_image.get_rect(topleft=(10, 70))

    def show_score(self):
        """Draw the scores and level to the screen."""
        self.prep_score()
        self.prep_level()
        self.prep_ships()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_image, self.ships_rect)
