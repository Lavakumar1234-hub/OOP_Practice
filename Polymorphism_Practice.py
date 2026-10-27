#1st
class Animal:
    def make_sound(self):
        print("Animals makes sound")
class Dog:
    def make_sound(self):
        print("Dog makes sound like Bow Bow")
class Cat:
    def make_sound(self):
        print("CAT makes sound miam")
class Cow:
    def make_sound(self):
        print("Cow make sound ambha")
animals=[Animal(),Dog(),Cat(),Cow()]
for i in animals:
    i.make_sound()

#2nd
class Car:
    def start(self):
        print("Car is a Vehicle")
class Computer:
    def start(self):
        print("Computer is a Electronic Device")
class WashingMachine:
    def start(self):
        print("Washing Machine is used for washing clothes")
def operate(device):
    device.start()
ob=Car()
ob1=Computer()
ob2=WashingMachine()
operate(ob)
operate(ob1)
operate(ob2)


#3rd
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
v1=Vector(2,3)
v2=Vector(4,5)
v3=v1+v2 #Vector(6,8)=v3
print(v3.x,v3.y)
v3=Vector(2,3)
v4=Vector(2,3)
v5=Vector(2,3)
v6=Vector(2,4)
print(v5==v6)
print(v3==v4)

#4th
class Transport:
    def move(self):
        print("Class Transport")
class Bus(Transport):
    def move(self):
        super().move()
        print("Bus is a Vehicle")
class Bike(Transport):
    def move(self):
        super().move()
        print("Bike is a Vehicle")
bus=Bus()
bus.move()
bike=Bike()
bike.move()

#5th
from abc import ABC,abstractmethod
class Notification:
    @abstractmethod
    def send(self):
        print("Notification Sending Types:")
class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")
class SMSNotification(Notification):
    def send(self):
        print("sending SMS Notification")
class PushNotification(Notification):
    def send(self):
        print("sending push Notification")
ob=[Notification(),EmailNotification(),SMSNotification(),PushNotification()]
for i in ob:
    i.send()

#6th
class Payment:
    def process(self,amount):
        print("Your Processing Payment of",amount)
class CreditCardPayment(Payment):
    def process(self,amount,card_type):
        print("Processing Payment of",amount,"Using",card_type)
        #or
    #def process(self,amount,card_type=None): #default Parameter
    #  if card_type:
    #     print("Processing Payment of",amount,"Using",card_type)
    #    else:
    #        print("Processing Payment of",amount)
#ob1=Payment()
#ob1.process(2000)
ob2=CreditCardPayment()
ob2.process(5000,"RuPay")

#7th
class Sorter:
    def change(self,strategy):
        self.strategy=strategy
class BS:
    def sort(self,data):
        print("BUBBLE SORT")
class MS:
    def sort(self,data):
        print("MERGE SORT")
class QS:
    def sort(self,data):
        print("QUICK SORT")
ob=Sorter()
ob.change(BS())
ob.strategy.sort([1,2,3])
ob.change(MS())
ob.strategy.sort([1,2,3])
ob.change(QS())
ob.strategy.sort([1,2,3])

#8th
class Account:
    def withdraw(self,amount):
        print("Account Withdraw:",amount)
class SavingsAccount(Account):
    def withdraw(self,amount):
        print("Savings Account:",amount)
class PremiumSavingsAccount(SavingsAccount):
    def withdraw(self,amount):
        super().withdraw(amount)
        print("Premium Savings Account")
a=Account()
a.withdraw(2000)
s=SavingsAccount()
s.withdraw(3000)
p=PremiumSavingsAccount()
p.withdraw(4000)

#9th Duck Typing
class Circle:
    def draw(self):
        print("Circle Class")
class Square:
    def draw(self):
        print("Square Class")
class Rectangle:
    def draw(self):
        print("Rectangle Class")
class Car:
    def draw(self):
        print("Car Class")
def draw(shape):
    shape.draw()
c=Circle()
draw(c)
s=Square()
draw(s)
r=Rectangle()
draw(r)
car=Car()
draw(car)

#10th
class UPI:
    def pay(self):
        print("Payment through UPI")
class Card:
    def pay(self):
        print("Payment through Card")
class Cash:
    def pay(self):
        print("Payment through Cash")
def payment(money):
    money.pay()
u=UPI()
payment(u)
c=Card()
payment(c)
cash=Cash()
payment(cash)
#using isinstance() its breaks the spirit of polymorphism because
#polymorphism means don't check the type just call the method.
def make_payments(money):
    if isinstance(money,UPI):
        money.pay()
    elif isinstance(money,Card):
        money.pay()
    elif isinstance(money,Cash):
        money.pay()
u=UPI()
make_payments(u)
c=Card()
make_payments(c)
cash=Cash()
make_payments(cash)