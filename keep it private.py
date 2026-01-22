class myclass:

    __privatevar = 27

    def __privmeth(self):
        print("I'm inside class myclass")
    
    def hello(self):
        print(f"Private variable value: {myclass.__privatevar}")

foo = myclass()
foo.hello()
foo.__privmeth