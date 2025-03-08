class Plane:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def display(self):
        print(f'{self.name} {self.model}')

        
plane1 = Plane('Sukhoi', 1991)
plane1.display()