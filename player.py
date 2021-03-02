"""Player Class."""

import cardhand

 
class Player:
    """Player Class."""

    def __init__(self, name):
        """Init the object and set attributes."""
        self.name = name
        self.cardhand = cardhand.Cardhand()
