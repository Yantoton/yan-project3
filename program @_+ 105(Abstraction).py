class computer:
    def start(self):
        print("Computer is starting")
        self.__load_hardware()
        print("Computer is running")
    def __load_hardware(self):
        print("Loading hardware")
my_computer = computer()
my_computer.start()

print(dir(my_computer))
