from src.database.models.bots.user import UserDomain
from src.database.seeders.generic_seeder import GenericSeeder


class UserSeeder(GenericSeeder):
    """Seeder for user needs."""
    
    def __init__(self):
        super().__init__()
        self.initial_data = {
            UserDomain: {
                UserDomain.CANARY: {"title": "canary"},
                UserDomain.REGULAR: {"title": "regular"}
            }
        }
