
"""
State representation for Cosmic Discovery.
"""
class State:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def __eq__(self, other):
        if not isinstance(other, State):
            return False

        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()
