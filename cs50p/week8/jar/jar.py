class Jar:
    def __init__(self, capacity = 12):
        while True:
            if capacity < 0:
                raise ValueError("try again")
            else:
                self._capacity = capacity
                self.cookies = 0
                break

    def __str__(self):
        return f"🍪" * self.cookies

    def deposit(self, n):
        if n + self.cookies > self._capacity:
            raise ValueError("Added cookies exceeds capacity")
        else :
            self.cookies = n + self.cookies

    def withdraw(self, n):
        if 0 > self.cookies - n:
            raise ValueError("Not enough cookies")
        else :
            self.cookies = self.cookies - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

