class Reverse:
    def __init__(self, input):
        self.input = input
    def reversed(self):
        return self.input[0:0:-1]

the_input = Reverse(input("Enter a string which you want reversed: "))
print("The reversed string: ", the_input.reversed)