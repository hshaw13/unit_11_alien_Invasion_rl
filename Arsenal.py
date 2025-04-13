import pygame

class Arsenal:
    def __init__(self):
        # Available weapons
        self.weapons = {
            "laser": {
                "ammo": 999,  
                "sound": "sound/laser.mp3",
                "image": "images/laserBlast.png"
            },
            "beam": {
                "ammo": 10,
                "sound": "sound/impactSound.mp3",
                "image": "images/beams.png"
            }
        }

        self.active_weapon = "laser"

    def switch_weapon(self, weapon_name):
        """Switch to a different weapon if it exists."""
        if weapon_name in self.weapons:
            self.active_weapon = weapon_name

    def get_current_weapon_data(self):
        """Return the current weapon's data."""
        return self.weapons[self.active_weapon]

    def fire_weapon(self):
        """Try to fire current weapon; play sound and reduce ammo."""
        weapon = self.get_current_weapon_data()
        if weapon["ammo"] is None or weapon["ammo"] > 0:
            # Play sound
            pygame.mixer.Sound(weapon["sound"]).play()
            if weapon["ammo"] is not None:
                weapon["ammo"] -= 1
            return True
        return False
