from passlib.context import CryptContext


class Crypt:
    """Provides crypt logic."""

    def __init__(self):
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto", default='bcrypt')

    def verify(self, value, hashed_value):
        """Verifies value to its hashed value."""

        return self.context.verify(value, hashed_value)

    def hash(self, value):
        """Gives hashed value."""

        return self.context.hash(value)
