from faker import Faker

class BaseDataGenerator:
    def __init__(self, seed=None) -> None:
        self.fake = Faker()
        # setup seed
        if seed is not None:
            self.fake.seed_instance(seed)