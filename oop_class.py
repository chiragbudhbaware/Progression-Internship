# # class Robo:
# #     name = "Chitti"
# #     category = "AI Humanoid"
# #     language = "Multilingual"
# #     power = "Super Strength"

# # robo1 = Robo()
# # print(f"Robo Name: {robo1.name}")
# # print(f"Robo Category: {robo1.category}")

# class Robo:
#     # Shared properties
#     category = "AI Humanoid"
#     language = "Multilingual"
#     power = "Super Strength"

#     # Constructor with self
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year

# robo1 = Robo("Chitti", "V2.0", 2025)
# robo2 = Robo("Sparky", "X1", 2023)

# print("🤖 Chitti:")
# print("Name:", robo1.name)
# print("Model:", robo1.model)
# print("Year:", robo1.year)
# print("Category:", robo1.category)
# print("Language:", robo1.language)
# print("Power:", robo1.power)

# print("\n🤖 Sparky:")
# print("Name:", robo2.name)
# print("Model:", robo2.model)
# print("Year:", robo2.year)
# print("Category:", robo2.category)
# print("Language:", robo2.language)
# print("Power:", robo2.power)


class Robo:
    # Class attributes
    category = "AI Humanoid"
    language = "Multilingual"
    power = "Super Strength"

    # Constructor to set unique details
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    # Method 1: Singing
    def sing(self):
        print(f"{self.name} is singing a melodious tune... 🎵")

    # Method 2: Dancing
    def dance(self):
        print(f"{self.name} is performing a cool dance move! 💃🤖")

    # Method 3: Cooking
    def cook(self):
        print(f"{self.name} is cooking delicious biryani! 🍲")

    # Create robots
chitti = Robo("Chitti", "V2.0", 2025)
sparky = Robo("Sparky", "X1", 2023)

# Let them show their talents!
chitti.sing()
chitti.dance()

sparky.cook()