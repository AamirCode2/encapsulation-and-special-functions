class Reverse:
    def __init__(self, input):
        self.input = input
    def reversed(self):
        self.splitted_list = []
        self.reversed_list = []
        self.splitted_list = self.input.split()

        for items in self.splitted_list:
            self.reversed_list.append(items[::-1])
        return " ".join(self.reversed_list)

the_input = Reverse(input("Enter a string which you want reversed: "))
print("The reversed string: ", the_input.reversed())