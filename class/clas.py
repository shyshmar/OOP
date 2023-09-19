class Cat:
    def __init__(self, color, breed):
        self.paws_count = 5
        self.color = color
        self.breed = breed

    #def show_paws_count(self):
    #    return Cat.paws_count

siam = Cat(color='white', breed='siam')
Cat.paws_count = 6

print(siam.color)

