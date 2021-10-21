class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 800
        self.screen_height = 600
        self.title = 'Głodna piłka'
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące gracza.
        self.player_speed_x = 0.2
        self.player_speed_y = 0.2

        # Ustawienie dotyczące kropek zjadanych przez gracza.
        self.dot_radius = 10
        self.black_dot_color = (0, 0, 0)
        self.red_dot_color = (255, 0, 0)
        self.red_dots_amount = 2
