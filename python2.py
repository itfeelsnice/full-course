
def function1():
    try:
        input1 = input("DO YOU WANT TO START Y/N")

        if input1.lower() == "y":
            list1 = []
            print("WE WILL CREATE A LIST WITH A NAME AND AN AGE")
            input2 = input("ENTER YOUR NAME: \n")
            input3 = int(input("ENTER YOUR AGE: \n"))
            if len(input2.strip()) >= 1  and input3:
                list1.append(input2)
                list1.append(input3)
                for a in list1:
                    print("------------")
                    print(a)
                    print("------------")
        else:
            print("OK HERE WE STOP")
            exit()
    except (ValueError, TypeError):
        print("PLEASE ENTER VALID VALUES")
        exit()

print("HERE WE START THE FUNCTION")
function1()


