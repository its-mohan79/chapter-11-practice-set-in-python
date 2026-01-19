class animal:
    pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")



d = dog()

d.bark()
