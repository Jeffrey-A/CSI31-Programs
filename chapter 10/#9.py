from math import pi
class Geo_sol_sph:
    
    def __init__(self,radious):
        self.radious = radious
         
    def getRadious(self):
        return self.radious
    
    def surfaceArea(self):
        self.area = (4 * pi) * (self.radious**2)
        return self.area
        
    def volume(self):
        self.volume = 4/3*pi*self.radious**3
        return self.volume
    

def main():
    user = eval(input("Enter radious: "))
    result = Geo_sol_sph(user)
    print(" Area = {0} \n Volume = {1}".format(round(result.surfaceArea()),round(result.volume())))
    
main()


    
