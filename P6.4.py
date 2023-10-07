def check(num):
    if str(num)[-1] == '5':
        raise Exception(f"Number 5! Alarm!")
    else:
        print("Good number!")


for i in range(3):
    ch = int(input("Enter number: "))
    check(ch)
