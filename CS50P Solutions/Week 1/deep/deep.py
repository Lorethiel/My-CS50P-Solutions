def main():
    x = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    if answer(x):
        print('Yes')
    else:
        print('No')


def answer(n):
    return n.lower().strip() == '42' or n.lower().strip() == 'forty-two' or n.lower().strip() == 'forty two'



main()