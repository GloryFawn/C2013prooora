def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we don`t work {type(var_1)}. We need str")
    else:
        return var_1


ch1 = "123"
checker(ch1)
print(ch1)
