from faker import Faker


class User:
    def __init__(self, email: str, first_name: str, last_name: str,
                 age: int, address: str, gender: str, job: str, has_children_under_16: bool):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.gender = gender
        self.job = job
        self.has_children_under_16 = has_children_under_16
    
    def to_json(self) -> dict:
        return self.__dict__
    
    @staticmethod
    def generate_random_user():
        fake = Faker()
        fake_gender = fake.random_element(elements=('F', 'M'))
        fake_age = fake.pyint(min_value=12, max_value=78, step=1)
        fake_first_name = fake.first_name_female() if fake_gender == 'F' else fake.first_name_male()
        fake_last_name = fake.last_name_female() if fake_gender == 'F' else fake.last_name_male()
        return User(
            first_name=fake_first_name,
            last_name=fake_last_name,
            age=fake_age,
            gender=fake_gender,
            email=fake.email(),
            address=fake.address(),
            job=fake.job(),
            has_children_under_16=fake.pybool() if 19 < fake_age < 60 else False
        )