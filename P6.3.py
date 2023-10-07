def face_control(name):
    if name == 'Vasya' or name == "Vasilyi":
        raise TypeError(f'No {name}. We don`t need {name}')
    else:
        return name


ch = int(input("How many people? "))
for i in range(ch):
    name = input("What is your name? ")
    face_control(name)
    print(f"Welcome {name}")
