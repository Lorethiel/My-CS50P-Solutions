import validators

def main():
    print(is_valid(input("What's your email adress? ")))




def is_valid(email):
    if validators.email(email) == True:
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == '__main__':
    main()