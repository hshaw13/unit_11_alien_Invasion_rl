class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)  # black background

        # Ship settings
        self.ship_speed = 1.8

        # Bullet settings
        self.bullet_speed = 3.5
        self.bullets_allowed = 5  # Max bullets on screen

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 

        # Sound and visuals
        self.default_bullet_image = "images/laserBlast.png"
        self.default_bullet_sound = "sound/laser.mp3"

        # Arsenal settings
        self.weapon_types = {
            "laser": {
                "ammo": None,  # None = unlimited
                "sound": "sound/laser.mp3",
                "image": "images/laserBlast.png"
            },
            "beam": {
                "ammo": 10,
                "sound": "sound/impactSound.mp3",
                "image": "images/beams.png"
            }
        }