class Info:  # to store details of a person that impact their carbon footprint
    method = "EPA carbon footprint calculator"


def __init__(self):
    self.member_no = 0  # number of members in your house
    self.house_size = 0  # house size in square feet
    # types of food you eat (number of types they eat non-veg)
    self.food_choice = 0
    self.water_consumption = 0  # number of types washing machine or dishwasher is used
    self.purchases = 0  # number of household items you purchase
    self.waste = 0  # the way you dispose your household waste
    # number of types of materials you recycle from the given list
    self.recycle_elements = 0
    self.personal_vehicle_distance = 0
    self.public_vehicle_distance = 0
    self.flight_score = 0
    self.result = 0  # a value to check the impact of your household on the environment


def display_info(self):  # to print your details
    print("Number of members at home: ", self.member_no)
    print("House size: ", self.house_size)
    print("Food choice : ", self.food_choice)
    print("Number of times heavy water consuming appliances are used : ",
          self.water_consumption)
    print("Number of purchases per week at home: ", self.purchases)
    print("Waste disposal method : ", self.waste)
    print("Number of recycles materials : ", self.recycle_elements)
    print("Net score:", self.result)


def info_input():
    print("Enter the following information , so that we can calculate an approximate impact your household makes in the environment")
    S = Info()
    S.member_no = int(input("Number of members at home: "))
    S.house_size = int(input("House size(in square ft): "))
    S.food_choice = int(input("Food choice: \n"
                              "Enter\n"
                              "1 if large portion of your food is prepackaged\n"
                              "2 if you eat meat daily\n"
                              "3 if you eat meat a few times a week\n"
                              "4 if you are a vegetarian or eat only locally grown food\n"
                              "5 if you are a vegan \n"
                              "choice:"))
    S.water_consumption = int(
        input("Number of times heavy water consuming appliances are used per week: "))
    S.purchases = int(
        input("Number of purchases per year at home(electronics,furniture, etc. ): "))
    S.waste = int(input("Waste disposal method : \n"
                        "Enter\n"
                        "1 if you recycle and use compost for your household waste\n"
                        "2 if you give your waste to the respective waste collection organisations \n"
                        "3 if you dump in local landfills or incinerate your waste products\n"
                        "choice:"
                        ))
    S.recycle_elements = int(input(
        "Number of recycled material types (this include glass ,plastic,paper , ""aluminium,steel ,food waste , etc.) : "))
    S.personal_vehicle_distance = int(
        input("Distance travelled per year in personal vehicle:"))
    S.public_vehicle_distance = int(
        input("Distance travelled per year in public vehicle:"))
    S.flight_score = int(input("Enter\n"
                               "0 if you don't travel by flight at all \n"
                               "1 if you travel mostly just intra-state flights\n"
                               "2 if you travel a lot of inter-state flights \n"
                               "3 if you travel a lot of international flights\n"
                               "choice:"))
    return S


def carbon_calc():  # A convenient scale to quantify the increase in
    result = 0  # carbon footprint with change in various factors mentioned in Info
    S = info_input()
    if S.member_no < 5:
        result += 12 - 2 * (S.member_no - 1)
    else:
        result += 2
    result += 12 - 2 * (S.food_choice - 1)
    if S.house_size < 1500:
        result += 2
    else:
        result += (int((int(S.house_size / 100)) / 5))
    result += int(S.water_consumption / 3)
    if S.personal_vehicle_distance == 0:
        result += 0
    elif S.personal_vehicle_distance < 1000:
        result += 4
    elif S.personal_vehicle_distance in range(1000, 10000):
        result += 6
    else:
        result += 6 + (S.personal_vehicle_distance // 5000) * 2
    if S.purchases == 0:
        result += 2
    else:
        result += 4 + int(S.purchases / 2)
    result += S.waste * 5
    result += 24 - 4 * S.recycle_elements
    if S.public_vehicle_distance == 0:
        result += 0
    elif S.public_vehicle_distance < 1000:
        result += 2
    elif S.public_vehicle_distance in range(1000, 10000):
        result += 4
    else:
        result += 4 + (S.public_vehicle_distance // 5000) * 2
    if S.flight_score == 1:
        result += 2
    elif S.flight_score == 2:
        result += 6
    elif S.flight_score == 3:
        result += 20
    if S.waste == 1:
        result += 10
    elif S.waste == 2:
        result += 20
    else:
        result += 40
    S.result = result
    return S


carbon_data = carbon_calc()
print("\nYour details are as follows\n")
display_info(carbon_data)
print("\nThe ideal net score should be around 85 for an average person living alone\n")
if carbon_data.result > 85:
    if carbon_data.result < 95:
        print("You are doing good in reducing your carbon footprint\n"
              "but you can definitely improve it :).")
    elif carbon_data.result < 110:
        print("You are doing alright in reducing your carbon footprint\n"
              "but you can definitely improve it :).")
    else:
        print("You should seriously consider the huge amount of carbon footprint you leave behind.\n"
              "Please try to reduce your carbon footprint by eating green or\n"
              "consider using public transport more \n"
              "or even make any small change in your lifestyle that reduces water and energy "
              "consumption.\n ")

if carbon_data.waste == 3:
    print("A person's waste disposal method makes a huge impact in their carbon footprint.\n"
          "Try to use composting and recycle as much as possible ,\n"
          "it drastically reduces the carbon footprint u leave behind.")
else:
    print("Your net score is really good. \n"
          "Thank you for playing your part in reducing the carbon footprint our generation leaves behind.")
print("\n\nThank you setting aside the time to take our test :) ")
