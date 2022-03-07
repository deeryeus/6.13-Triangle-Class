import math

class Triangle():
    def __init__(self, base, side1, side2):
        self.base = base
        self.side1 = side1
        self.side2 = side2
    
    def perimeter(self):
        return self.base + self.side1 + self.side2
    
    def area(self):
        s = (self.base + self.side1 + self.side2)/2
        inner_root = s * (s - self.base) * (s - self.side1) * (s - self.side2)
        a = round(math.sqrt(inner_root),3)
        return a
    
    def scale(self, scale_factor):
        return Triangle(scale_factor * self.base, scale_factor * self.side1, scale_factor * self.side2)

    def is_valid(self):

        if self.base + self.side1 > self.side2 \
            and self.side1 + self.side2 > self.base \
                and self.base + self.side2 > self.side1:
            return True
        return False
    
    def is_right(self):
        #determine 'c' for the Pythagorean Theorem
        all_sides = [self.base, self.side1, self.side2]
        hypotenuse = max(all_sides)

        #remove 'c' from the list, the 2 remaining sides are the 'legs'
        all_sides.remove(hypotenuse)
        leg1 = all_sides[0]
        leg2 = all_sides[1]
        
        #proceed with calculation
        if leg1 ** 2 + leg2 ** 2 == hypotenuse ** 2:
            return True
        else:
            return False 

a = Triangle(12, 7, 6)

print("Perimeter = %f" %a.perimeter())
print("Area = %f" %a.area())

b = a.scale(3)
print(b.base, b.side1, b.side2)

print(a.is_valid())

t = Triangle(1, 3, 5)
print(t.is_valid())

print(a.is_right())

r = Triangle(3, 4, 5)
print(r.is_right())