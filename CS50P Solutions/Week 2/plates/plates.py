def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if  6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():

        for letter in s:
            if letter.isdigit():
                index = s.index(letter)
                if int(letter) != 0:

                    if not s[index:].isdigit():
                        return False
                elif int(letter) == 0:

                        if not s[index - 1].isdigit():
                            return False


        return True









main()