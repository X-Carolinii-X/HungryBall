class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 800
        self.screen_height = 600
        self.title = 'Głodna piłka'
        self.bg_color = (230, 230, 230)

        # Ustawienia czcionki.
        self.font_name = 'Courier'
        self.font_point_size = 48
        self.font_button_size = 40

        # Ustawienia dotyczące gracza.
        self.player_speed_x = 0.5
        self.player_speed_y = 0.5

        # Ustawienia dotyczące kropek zjadanych przez gracza.
        self.dot_radius = 10
        self.black_dot_color = (0, 0, 0)
        self.red_dot_color = (255, 0, 0)

        # Punkty przyznawane za zjedzenie czarnej kropki.
        self.dot_point = 1

        # Ustawienie dotyczące ilości czerwonych kropek.
        self.red_dots_amount_scale = 2

        self._init_dynamic_settings()

    def _init_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.red_dots_amount = 2

    def increase_red_dots_amount(self):
        """Zmiana ustawień dotyczących ilości czerwonych kropek."""
        self.red_dots_amount += self.red_dots_amount_scale