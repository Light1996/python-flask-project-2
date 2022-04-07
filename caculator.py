
class Cal:
    # Here is the constructor Method
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    # here are the methods below
    def addition(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def devide(self):
        return self.number1 / self.number2

    # Example of User Choosen method we can call is as Recursion
    def decision(self, user_decision):
        if user_decision == '+':
            return self.addition()
        elif user_decision == '-':
            return self.subtract()
        elif user_decision == '*':
            return self.multiply()
        elif user_decision == '/':
            return self.devide()


user_input = ' 2 + 2 '
user_input = user_input.strip().split(" ")
number_1 = int(user_input[0])
number_2 = int(user_input[2])
decision = user_input[1]

cal = Cal(number_1, number_2)
print(cal.decision(decision))

cal = Cal(1, 3)
print(cal.addition())

cal1 = Cal(1, 3)
print(cal.subtract())

cal2 = Cal(1, 3)
print(cal.multiply())

cal3 = Cal(1, 3)
print(cal.devide())


