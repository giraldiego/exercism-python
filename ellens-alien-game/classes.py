"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Initializes alien instance at provided coordinates.
        Set initial health value to 3

        :param x_coordinate: int - Position on the x-axis.
        :param y_coordinate: int - Position on the y-axis.
        """

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1


    def hit(self):
        """Method that decrements the health of an alien object by 1
        health value won't go below 0"""
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        """Check is alien is alive (health above 0)

        :return: bool - is the alien alive?
        """
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        """Changes alien's coordinates to the provided ones.

        :param x_coordinate: int - Position on the x-axis.
        :param y_coordinate: int - Position on the y-axis.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


    def collision_detection(self, other_object):
        """Collision detection method to be implemented"""
        pass


def new_aliens_collection(alien_start_positions):
    """Creates a list of Alien objects, given a list of positions as tuples
    :param alien_start_positions: list of coordinates as tuples
    :return: list - alien's instances created with provided coordinates
    """
    # aliens = []
    # for position in alien_start_positions:
    #     new_alien = Alien(position[0],position[1])
    #     aliens.append(new_alien)
    # return aliens

    return [ Alien(*pos) for pos in alien_start_positions]
