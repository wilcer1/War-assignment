"""Player Class."""

import cardhand


class Player:
    """Player Class."""

    def __init__(self, name):
        """Init the object and set attributes."""
        self.name = name
        self.cardhand = cardhand.Cardhand()

    def set_name(self, name):
        """Set player name."""
        self.name = name

    def get_name(self):
        """Return player name."""
        return self.name
