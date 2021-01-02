import math


class TPTriangle:
    def __init__(self, katet_1, katet_2):
        self.katet_1 = katet_1
        self.katet_2 = katet_2

    def enter(self, katet_1, katet_2):
        if katet_1 >=0:
            self.katet_1 = katet_1
        else:
            raise Exception("Value<0")
        self.katet_2 = katet_2

    def print(self):
        print("перший катет=", self.katet_1)
        print("другий катет=", self.katet_2)

    def S(self):
        return (self.katet_1 * self.katet_2) / 2

    def P(self):
        return self.katet_1 + self.katet_2 + math.sqrt((self.katet_1) ** 2 + (self.katet_2) ** 2)

    def compare(self, other):
        if ((self.katet_1 * self.katet_2) / 2) < ((other.katet_1 * other.katet_2) / 2):
            print("площа першого <")
        elif ((self.katet_1 * self.katet_2) / 2) > ((other.katet_1 * other.katet_2) / 2):
            print("площа першого >")
        else:
            print("рівні")

    def __add__(self,item):
        return TPTriangle(self.katet_1 + item.katet_1,self.katet_2 + item.katet_2)

    def __sub__(self,item):
        return TPTriangle(self.katet_1 - item.katet_1, self.katet_2 - item.katet_2)
    def __mul__(self,number):
        return TPTriangle(self.katet_1*number,self.katet_2*number)


katet_1 = int(input("катет1="))
katet_2 = int(input("катет2="))
katet_3 = int(input("катет3="))
katet_4 = int(input("катет4="))

a = TPTriangle(katet_1, katet_2)
a.print()
print("Площа=",a.S())
print("Периметр=",a.P())

b = TPTriangle(katet_3, katet_4)

a.compare(b)
summ=a+b
print(summ)
sub=a-b
print(sub)
number=int(input("number="))
two=b*number
one=a*number
print(two)
print(one)