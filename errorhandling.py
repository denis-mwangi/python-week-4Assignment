try:
    file = open("words.txt", "r")
    data = file.read()
    print(data)
except NameError:
    print("Check whether the variables are correctly named")
except FileNotFoundError:
    print("No such file you are trying to read")