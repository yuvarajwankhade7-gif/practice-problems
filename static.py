class Number:
    @staticmethod
    def check_even_odd(num):
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")

# Calling using class name
Number.check_even_odd(12)

# Calling using object
obj = Number()
obj.check_even_odd(17)
