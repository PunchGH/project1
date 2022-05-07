class Vihicle:
    li_code = ""
    se_code = ""
    face = ""
    def turn_air(self):
        print("turn on air")
        
class Car(Vihicle):
    pass
        
class pickup(Vihicle):
    pass

class van(Vihicle):
    pass

class estatecar(Vihicle):
    pass        




a = [Car(),pickup(),van(),estatecar()]

for i in range(4):
    a[i].turn_air()