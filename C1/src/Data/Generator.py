from faker import Faker
import json
import random as rd
class Generator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = {}
        self.index = 0

    def generate_data(self, cant):
        fake = Faker()
        users = {}
        sizes = [["L", "X"], ["XL", "M"], ["L", "S"]]
        colors = [["Blue", "Purple"], ["White", "Black"], ["Red", "Blue", "Black", "White"]]

        for index in range(cant):
            products = {}
            for i in range(3):
                products[i] = {"qty" : rd.randint(1,10),
                               "size": rd.choice(sizes[i]),
                               "color": rd.choice(colors[i])}

            user = {"name": fake.name(),
                    "email": fake.email(),
                    "phone": fake.phone_number(),
                    "password": fake.password(),
                    "used": False,
                    "address": fake.address(),
                    "city": fake.city(),
                    "code": fake.postcode(),
                    "products": products}
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




data_generator = Generator("dataInput")
cant = int(input("How much random data do you want to create? "))
data_generator.generate_data(cant)
data_generator.save_json()
