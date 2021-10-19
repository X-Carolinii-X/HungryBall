import pygame

class Player():
    """Klasa przeznaczona do zarządzania piłką, sterowaną przez
    gracza."""

    def __init__(self, hb_game):
        """Inicjalizacja piłki i jej położenia początkowego."""
        self.screen = hb_game.screen
        self.screen_rect = hb_game.screen.get_rect()

        # Wczytanie obrazu piłki i pobranie jej położenia.
        self.image = pygame.image.load('res/images/black_ball.png')
        self.rect = self.image.get_rect()

        # Każda nowa piłka pojawia się na środku ekranu.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Wyświetlenie piłki w jej aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)
