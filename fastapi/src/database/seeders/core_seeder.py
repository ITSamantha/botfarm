from src.database.models.core.env import Env
from src.database.seeders.generic_seeder import GenericSeeder


class CoreSeeder(GenericSeeder):
    def __init__(self):
        super().__init__()
        self.initial_data = {
            Env: {
                Env.STAGE: {"title": "stage"},
                Env.PROD: {"title": "prod"},
                Env.PREPROD: {"title": "preprod"}
            }
        }
