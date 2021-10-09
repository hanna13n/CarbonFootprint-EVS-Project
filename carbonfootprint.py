import time
class Info:  # to store details of a person that impact their carbon footprint
    method = "EPA carbon footprint calculator"


    def __init__(self):
        fancy_print("Enter the following information, so that we can calculate an approximate impact your household makes in the environment")
        self.member_no = int(input("Number of members at home: "))
        self.house_size = int(input("House size(in square ft): "))
        self.food_choice = int(input("Food choice: \n"
                                "Enter\n"
                                "1 if large portion of your food is prepackaged\n"
                                "2 if you eat meat daily\n"
                                "3 if you eat meat a few times a week\n"
                                "4 if you are a vegetarian or eat only locally grown food\n"
                                "5 if you are a vegan \n"
                                "choice: "))
        self.water_consumption = int(
            input("Number of times heavy water consuming appliances are used per week: "))
        self.purchases = int(
            input("Number of purchases per year at home (electronics, furniture etc. ): "))
        self.waste = int(input("Waste disposal method : \n"
                            "Enter\n"
                            "1 if you recycle and use compost for your household waste\n"
                            "2 if you give your waste to the respective waste collection organisations \n"
                            "3 if you dump in local landfills or incinerate your waste products\n"
                            "choice: "
                            ))
        self.recycle_elements = int(input(
            "Number of recycled material types (this include glass, plastic, paper, aluminium, steel, food waste, etc.): "))
        self.personal_vehicle_distance = int(
            input("Distance travelled per year in personal vehicle: "))
        self.public_vehicle_distance = int(
            input("Distance travelled per year in public vehicle: "))
        self.flight_score = int(input("Enter\n"
                                "0 if you don't travel by flight at all \n"
                                "1 if you travel mostly just intra-state flights\n"
                                "2 if you travel a lot of inter-state flights \n"
                                "3 if you travel a lot of international flights\n"
                                "choice: "))


    def carbon_calc(self):  # A convenient scale to quantify the increase in
        result = 0  # carbon footprint with change in various factors mentioned in Info
        if self.member_no < 5:
            result += 12 - 2 * (self.member_no - 1)
        else:
            result += 2
        result += 12 - 2 * (self.food_choice - 1)
        if self.house_size < 1500:
            result += 2
        else:
            result += ((self.house_size // 100) // 5)
        result += self.water_consumption // 3
        if self.personal_vehicle_distance == 0:
            result += 0
        elif self.personal_vehicle_distance < 1000:
            result += 4
        elif self.personal_vehicle_distance in range(1000, 10000):
            result += 6
        else:
            result += 6 + (self.personal_vehicle_distance // 5000) * 2
        if self.purchases == 0:
            result += 2
        else:
            result += 4 + self.purchases // 2
        result += self.waste * 5
        result += 24 - 4 * self.recycle_elements
        if self.public_vehicle_distance == 0:
            result += 0
        elif self.public_vehicle_distance < 1000:
            result += 2
        elif self.public_vehicle_distance in range(1000, 10000):
            result += 4
        else:
            result += 4 + (self.public_vehicle_distance // 5000) * 2
        if self.flight_score == 1:
            result += 2
        elif self.flight_score == 2:
            result += 6
        elif self.flight_score == 3:
            result += 20
        if self.waste == 1:
            result += 10
        elif self.waste == 2:
            result += 20
        else:
            result += 40
        self.result = result


    def display_info(self):  # to fancy_print your details
        fancy_print("Number of members at home: ", self.member_no)
        fancy_print("House size: ", self.house_size)
        fancy_print("Food choice: ", self.food_choice)
        fancy_print("Number of times heavy water consuming appliances are used: ",
            self.water_consumption)
        fancy_print("Number of purchases per week at home: ", self.purchases)
        fancy_print("Waste disposal method: ", self.waste)
        fancy_print("Number of recycles materials: ", self.recycle_elements)
        fancy_print("Net score: ", self.result)


def fancy_print(*args):
    for s in args:
        for i in str(s):
            print(i, sep='', end='')
            time.sleep(0.005)
        # time.sleep(1)
    time.sleep(1)
    print()



carbon_data = Info()
carbon_data.carbon_calc()
fancy_print("\nYour details are as follows\n")
carbon_data.display_info()
fancy_print("\nThe ideal net score should be around 85 for an average person living alone\n")
if carbon_data.result > 85:
    if carbon_data.result < 95:
        fancy_print("\033[1;32;40m You are doing good in reducing your carbon footprint\n"
            "but you can definitely improve it :).")
    elif carbon_data.result < 110:
        fancy_print("\033[1;33;40mYou are doing alright in reducing your carbon footprint\n"
            "but you can definitely improve it :).")
    else:
        fancy_print("\033[1;31;40mYou should seriously consider the huge amount of carbon footprint you leave behind.\n"
            "Please try to reduce your carbon footprint by eating green or\n"
            "consider using public transport more \n"
            "or even make any small change in your lifestyle that reduces water and energy "
            "consumption.\n ")

if carbon_data.waste == 3:
    fancy_print("\033[1;31;40mA person's waste disposal method makes a huge impact on their carbon footprint.\n"
        "Try to use composting and recycle as much as possible ,\n"
        "it drastically reduces the carbon footprint u leave behind.")
else:
    fancy_print("\033[1;32;40mYour net score is really good. \n"
        "Thank you for playing your part in reducing the carbon footprint our generation leaves behind.")
fancy_print("\n\nThank you for setting aside the time to take our test :) ")
