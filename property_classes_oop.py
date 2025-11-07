class House:
    def __init__(self, stories, livingrooms, bathrooms, bedrooms, kitchen, garage, gardensize, driveway_size, price):
        self.stories = stories
        self.livingrooms = livingrooms
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.kitchen = kitchen
        self.garage = garage
        self.gardensize = gardensize
        self.driveway_size = driveway_size
        self.price = price


house_1 = House(
    stories=1, livingrooms=1, bathrooms=1, bedrooms=1, kitchen='open-plan', garage=False, gardensize=20, driveway_size=10, price=120000
)

house_2 = House(
    stories=2, livingrooms=2, bathrooms=2, bedrooms=2, kitchen='modern', garage=True, gardensize=50, driveway_size=25, price=250000
)

house_3 = House(
    stories=3, livingrooms=2, bathrooms=4, bedrooms=4, kitchen='gourmet', garage=True, gardensize=100, driveway_size=40, price=750000
)

house_4 = House(
    stories=1, livingrooms=1, bathrooms=1, bedrooms=1, kitchen='rustic', garage=False, gardensize=80, driveway_size=15, price=180000
)


class Bungalow(House):
    def __init__(self, livingrooms, bathrooms, bedrooms, kitchen, garage, gardensize, driveway_size, price):
        super().__init__(stories=0, livingrooms=livingrooms, bathrooms=bathrooms, bedrooms=bedrooms, kitchen=kitchen, garage=garage, gardensize=gardensize, driveway_size=driveway_size, price=price)

bungalow_1 = Bungalow(
    livingrooms=1, bathrooms=1, bedrooms=1, kitchen='open-plan', garage=False, gardensize=25, driveway_size=10, price=150000
)

bungalow_2 = Bungalow(
    livingrooms=2, bathrooms=2, bedrooms=3, kitchen='modern', garage=True, gardensize=40, driveway_size=20, price=250000
)

bungalow_3 = Bungalow(
    livingrooms=1, bathrooms=1, bedrooms=2, kitchen='galley', garage=False, gardensize=60, driveway_size=15, price=180000
)

bungalow_4 = Bungalow(
    livingrooms=3, bathrooms=2, bedrooms=4, kitchen='island-style', garage=True, gardensize=80, driveway_size=30, price=320000
)

bungalow_5 = Bungalow(
    livingrooms=2, bathrooms=1, bedrooms=2, kitchen='rustic', garage=False, gardensize=50, driveway_size=18, price=200000
)


class Apartments(House):
    def __init__(self, livingrooms, bathrooms, bedrooms, kitchen, price, floor_number, gym=None, roof_terrace=None, underground_parking=None):
        super().__init__(stories=1, livingrooms=livingrooms, bathrooms=bathrooms, bedrooms=bedrooms, kitchen=kitchen, garage=False, gardensize=0, driveway_size=0, price=price)
        self.floor_number = floor_number
        self.gym = gym
        self.roof_terrace = roof_terrace
        self.underground_parking = underground_parking


apartment_1 = Apartments(
    livingrooms=1, bathrooms=1, bedrooms=1, kitchen='open-plan', price=120000,
    floor_number=1, gym=False, roof_terrace=False, underground_parking=False
)

apartment_2 = Apartments(
    livingrooms=1, bathrooms=1, bedrooms=2, kitchen='modern', price=160000,
    floor_number=3, gym=True, roof_terrace=False, underground_parking=True
)

apartment_3 = Apartments(
    livingrooms=2, bathrooms=2, bedrooms=3, kitchen='island-style', price=240000,
    floor_number=5, gym=True, roof_terrace=True, underground_parking=True
)

apartment_4 = Apartments(
    livingrooms=1, bathrooms=1, bedrooms=1, kitchen='galley', price=110000,
    floor_number=2, gym=False, roof_terrace=False, underground_parking=False
)

apartment_5 = Apartments(
    livingrooms=1, bathrooms=2, bedrooms=2, kitchen='modern', price=190000,
    floor_number=7, gym=True, roof_terrace=True, underground_parking=True
)

apartment_6 = Apartments(
    livingrooms=2, bathrooms=2, bedrooms=3, kitchen='open-plan', price=230000,
    floor_number=8, gym=True, roof_terrace=True, underground_parking=False
)

apartment_7 = Apartments(
    livingrooms=1, bathrooms=1, bedrooms=2, kitchen='compact', price=150000,
    floor_number=4, gym=False, roof_terrace=True, underground_parking=False
)


class House_Buyer_Preference(House):
    def __init__(self, stories, livingrooms, bathrooms, bedrooms, kitchen, garage, gardensize, driveway_size, willing_to_spend):
        super().__init__(
            stories=stories, livingrooms=livingrooms, bathrooms=bathrooms, bedrooms=bedrooms, kitchen=kitchen, garage=garage, gardensize=gardensize,
            driveway_size=driveway_size,
            price=1
        )
        self.__willing_to_spend = willing_to_spend

    def get_budget(self):
        return self.__willing_to_spend


hbp_1 = House_Buyer_Preference(
    stories=2, livingrooms=2, bathrooms=2, bedrooms=3, kitchen='modern', garage=True, gardensize=40, driveway_size=20,
    willing_to_spend=300000
)

print("Buyer prefers a", hbp_1.stories, "story house.")
print("Preferred kitchen type:", hbp_1.kitchen)
print("Budget: £", hbp_1.get_budget())
