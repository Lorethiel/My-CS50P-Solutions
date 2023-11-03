def main():
    word = input('Input: ')
    print(shorten(word))



def shorten(word):
    vowel_list = ['a','e','i','o','u','A','E','I','O','U']
    nonvowel_list = []


    input_listed = list(word)

    for letter in input_listed:
        if letter not in vowel_list:
            nonvowel_list.append(letter)

    str1 =''
    for letter in nonvowel_list:

        str1 = str1 + letter

    return str1

if __name__ == "__main__":
    main()