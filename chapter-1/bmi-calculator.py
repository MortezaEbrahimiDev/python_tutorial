# global variables and imports


# get data from input

def get_data_from_user():
    weight=float(input('enter your weight(kg):'))
    height=float(input('enter your height(m):'))
    return weight,height

# calculate data

def get_bmi_level(bmi):
    if bmi<18.5:
        return "Under weight"
    elif bmi<24.9:
        return "Normal"
    elif bmi<29.9:
        return "Over weight"
    elif bmi<34.9:
        return "Obese"
    else:
        return "Extermely obese"




def calculate_bmi(weight,height):
    bmi=(weight/(height**2))
    res=get_bmi_level(bmi)
    return res


def main():
    weight,height=get_data_from_user()
    print(calculate_bmi(weight,height))



main()
