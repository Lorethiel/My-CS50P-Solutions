class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪'* self.size

    def deposit(self, n):
        if not self.size + n > self.capacity:
            self.size = self.size + n
        else:
            raise ValueError('not enough room for all those cookies')

    def withdraw(self, n):
        if not self.size - n < 0:
            self.size = self.size - n
        else:
            raise ValueError('not enough cookies')

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('a jar that has never existed')
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError('too much cookies')
        self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(1)
    print(jar)
    jar.deposit(5)
    print(jar)

if __name__ == '__main__':
    main()

#it was much easier than i expected i had a crisis when reading through the instructions but with the help of lecture notes i solved it quickly

