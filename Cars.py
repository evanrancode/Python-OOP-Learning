
class Cars:
    default_engine_type = "Petrol"
    default_condition = "Good"

    def __init__(self, make, model, age, mileage, price):
        self.make = make
        self.model = model
        self.age = age
        self.mileage = mileage
        self.price = price

    def car_name(self):
        return f"{self.make} {self.model}"

if __name__ == "__main__":
    car_1 = Cars("Nissan", "Juke", "5 years old", 500000, 5745)
    car_2 = Cars("Toyota", "Alphard", "10 years old", 32670, 13000)
    car_3 = Cars("Lexus", "LBX", "1 year old", 12320, 17000)

    car_3.default_engine_type = "Hybrid"
    car_3.default_condition = "Damaged"

    print(f"{car_1.car_name()} — Condition: {car_1.default_condition}, Engine: {car_1.default_engine_type}")
    print(f"{car_2.car_name()} — Condition: {car_2.default_condition}, Engine: {car_2.default_engine_type}")
    print(f"{car_3.car_name()} — Condition: {car_3.default_condition}, Engine: {car_3.default_engine_type}")
