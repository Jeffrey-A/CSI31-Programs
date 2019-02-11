import math
def sphereArea(radious):
    #returns the surface area of a shere having the given radius
    radious = radious * radious
    area = 4 * math.pi *radious
    return area
    
def sphereVolume(radious):
    #returns the surface area of a shere having the given radius.
    radious = radious * radious * radious
    v = 4/(3*math.pi * radious)
    return v
    
def main():
    print("This program calculates the area and volume of a sphere.")
    print()
    ra = eval(input("Enter the raious of the sphere: "))
    v = sphereVolume(ra)
    area = sphereArea(ra)
    print("The area is:",round(area,2),"and the volume is:",round(v,3)) 
    
main()