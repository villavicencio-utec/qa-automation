from faker import Faker
import json

class Generator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = {}
        self.index = 0

    def generate_data(self, cant):
        fake = Faker()
        users = {}
        for index in range(cant):
            user = {"name": fake.name(), "email": fake.email(), "password": fake.password(), "used": False}
            users[index] = user

        self.data = users

    def save_json(self):
        with open(self.file_name + ".json", 'w') as outfile:
            json.dump(self.data, outfile)

    def read_json(self):
        with open(self.file_name + ".json", 'r') as f:
            self.data = json.load(f)

    def update_data(self):
        self.data[self.index]["used"] = True

    def get_data_random(self):
        self.read_json()
        users = self.data
        for key in users:
            user = users[key]
            if user["used"] is False:
                self.index = key
                print(self.index)
                self.update_data()
                self.save_json()
                return user

        print("There is no more data to be selected.")




# data_generator = Generator("dataInput")
# cant = int(input("How much random data do you want to create? "))
# data_generator.generate_data(cant)
# data_generator.save_json()
