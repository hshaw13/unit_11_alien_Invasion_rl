import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('images/ship_clean.png')
        self.image = pygame.transform.rotate(self.image, 270) 

        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright  

        self.y = float(self.rect.y)


        # Movement flags
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_up and self.rect.top > 0:
           self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
           self.y += self.settings.ship_speed

        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)
