#1st Inheritance Set1 Answers
class Animal:
    def sound(self):
        print("Animals are better than peoples")
class Dog:
    def sound(self):
        print("Dog is a pet animal")
#ob=Animal()
#ob.sound()
#ob=Dog()
#ob.sound()

#2nd single inheritance
class A:
    def show(self):
        print("parent class")
class B(A):
    def show(self):
        print("Child class")
        super().show()
ob=B()
ob.show()

#3rd multilevel inheritance
class A:
    def display(self):
        print("This is Class A")
class B(A):
    def display(self):
        print("This is Class B")
class C(B):
    def display(self):
        print("This is Class C")
ob=C()
ob.display()

#4th hierarchical inheritance
class Vehicle:
    def wheels(self):
        print("Class Vehicle")
class Car(Vehicle):
    def wheels(self):
        print("car has 4 wheels")
class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")
ob1=Bike()
ob1.wheels()
ob2=Car()
ob2.wheels()

#5th
class Employee:
    def salary(self):
        return 45000
class Manager(Employee):
    def salary(self):
        basic=super().salary()
        incentive=5000
        total=basic+incentive
        print("Basic Salary=",basic)
        print("Incentive=",incentive)
        print("Total Salary=",total)
ob=Manager()
ob.salary()

#6th
class University:
    name="JNTU"
    @classmethod
    def college(cls):
        print(cls.name)
class College(University):
    pass
College.college()
University.college()

#7th
class Mathops:
    @staticmethod
    def add(a,b):
        return a+b
class Advancedops(Mathops):
    pass
print(Advancedops.add(10,20))

#8th multiple inheritance
class Father:
    def skills(self):
        print("Father class")
class Mother:
    def skills(self):
        print("Mother class")
class Child(Father,Mother):
    pass
ob=Child()
ob.skills()

#9th abstract class
from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area=Length * Breadth")
ob=Rectangle()
ob.area()

#10th
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,roll):
        self.roll=roll
        super().__init__(name)
    def display(self):
        print(self.name)
        print(self.roll)
ob=Student("kumar",39)
ob.display()


#1st inheritance Set2 Answers
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit:", amount)
        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


class User(Bank):
    def __init__(self, name, balance):
        super().__init__(balance)
        self.name = name

    def display(self):
        print("User Name:", self.name)


ob = User("Lava Kumar", 25000)
ob.display()
ob.check_balance()
ob.deposit(25000)
ob.withdraw(5000)
ob.check_balance()


# 2nd
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def display_total_salary(self):
        print("Bonus:", self.bonus)
        print("Total Salary:", self.salary + self.bonus)


ob = Manager("Ganesh", 45000, 5000)
ob.display()
ob.display_total_salary()


# 3rd
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


class Result(Student):
    def result(self):
        if self.marks >= 35:
            print("Result:Pass")
        else:
            print("Result:Fail")


ob = Result("Kumar", 35)
ob.display()
ob.result()


# 4th
class Restaurant:
    def menu(self, item):
        price = {"Chicken Biryani": 199,
                 "Mutton Biryani": 299,
                 "Pizza": 99,
                 "Burger": 49}
        return price.get(item, 0)


class FoodCourt(Restaurant):
    def display_menu(self):
        print("Available Food Items:")
        print("Chicken Biryani: 199Rs/-")
        print("Mutton Biryani: 299Rs/-")
        print("Pizza: 99Rs/-")
        print("Burger: 49Rs/-")
        print()

    def order(self):
        total = 0
        while True:
            item = input("Enter Food Item or Stop: ")
            if item == "stop":
                break
            price = self.menu(item)
            if price != 0:
                total += price
                print("Price:", price, "Rs/-")
            else:
                print("Item Not Available")
        print()
        self.billing(total)

    def billing(self, total):
        print("Food Bill:", total, "Rs/-")
        print("Packing Charge: 20Rs/-")
        print("Total Bill:", total + 20, "Rs/-")


class Customer(FoodCourt):
    pass


ob = Customer()
ob.display_menu()
ob.order()


# 5th
class Movie:
    def ticket(self, movie):
        price = {"Spirit": 249,
                 "Paradise": 199,
                 "Dragon": 249,
                 "Varanasi": 249
                 }
        return price.get(movie, 0)


class Booking(Movie):
    def display_movies(self):
        print("Available Movies:")
        print("Spirit  249Rs/-")
        print("Paradise  199Rs/-")
        print("Dragon  249Rs/-")
        print("Varanasi  249Rs/-")
        print()

    def selection(self):
        total = 0
        while True:
            movie = input("Enter Movie Name or stop: ")
            if movie == "stop":
                break
            price = self.ticket(movie)
            if price != 0:
                total += price
                print("Ticket Price:", price, "Rs/-")
            else:
                print("Movie Not Available")
        print()
        self.billing(total)

    def billing(self, total):
        print("Ticket Amount:", total, "Rs/-")
        print("Booking Charge: 30Rs/-")
        print("Total Amount:", total + 30, "Rs/-")


class Customer(Booking):
    pass


ob = Customer()
ob.display_movies()
ob.selection()


# 6th
class Course:
    def fee(self, course):
        price = {"Python Full Stack": 32000,
                 "Java Full Stack": 32000,
                 "Data Analytics": 25000,
                 "Graphic Design": 15000
                 }
        return price.get(course, 0)


class Academy(Course):
    def display(self):
        print("Available Courses:")
        print("Python Full Stack  32000Rs/-")
        print("Java Full Stack  32000Rs/-")
        print("Data Analytics  25000Rs/-")
        print("Graphic Design  15000Rs/-")
        print()

    def enroll(self):
        total = 0
        while True:
            course = input("Enter Your Course Name or stop: ")
            if course == "stop":
                break
            fee = self.fee(course)
            if fee != 0:
                total += fee
                print("Course Fee:", fee, "Rs/-")
            else:
                print("Course Not Available")
        print()
        self.billing(total)

    def billing(self, total):
        print("Fee Amount:", total, "Rs/-")
        print("Registration Fee: 100Rs/-")
        print("Total Amount:", total + 100, "Rs/-")


class Student(Academy):
    pass


ob = Student()
ob.display()
ob.enroll()


# 7th
class Cab:
    def bike(self, distance):
        return distance * 5

    def auto(self, distance):
        return distance * 10

    def car(self, distance):
        return distance * 15


class Uber(Cab):
    def menu(self):
        print("Choose Available Vehicles:")
        print("1 Bike")
        print("2 Auto")
        print("3 Car")

    def booking(self):
        self.menu()
        choose = int(input("Enter 1 For Bike,2 For Auto and 3 For Car: "))
        distance = float(input("Enter Your Distance in Km: "))
        if choose == 1:
            self.bill = self.bike(distance)
        elif choose == 2:
            self.bill = self.auto(distance)
        elif choose == 3:
            self.bill = self.car(distance)
        else:
            print("Invalid Choose")
            return
        self.billing()

    def billing(self):
        print("Bill:", self.bill, "RS/-")
        self.bill = self.bill + (self.bill * 10 / 100)
        if self.bill > 1000:
            self.bill = self.bill - (self.bill * 15 / 100)
        print("Total Bill:", self.bill, "Rs/-")


class Ola(Cab):
    def menu(self):
        print("Choose Available Vehicles:")
        print("1 Bike")
        print("2 Auto")
        print("3 Car")

    def booking(self):
        self.menu()
        choose = int(input("Enter 1 For Bike,2 For Auto and 3 For Car: "))
        distance = float(input("Enter your Distance in Km: "))
        if choose == 1:
            self.bill = self.bike(distance)
        elif choose == 2:
            self.bill = self.auto(distance)
        elif choose == 3:
            self.bill = self.car(distance)
        else:
            print("Invalid Choose")
            return
        self.billing()

    def billing(self):
        print("Bill:", self.bill, "Rs/-")
        self.bill = self.bill + (self.bill * 12 / 100)
        if self.bill > 1500:
            self.bill = self.bill - (self.bill * 20 / 100)
        print("Total Bill:", self.bill, "Rs/-")


choose = input("Choose Uber or Ola: ")
print()
if choose == "Uber":
    u = Uber()
    u.booking()
elif choose == "Ola":
    o = Ola()
    o.booking()
else:
    print("Invalid Choose")


# 8th
class Grocery:
    def rice(self):
        return 100

    def sugar(self):
        return 12

    def oil(self):
        return 250


class Dmart(Grocery):
    def items(self):
        print("Available Items:")
        print("1 Rice")
        print("2 Sugar")
        print("3 Oil")

    def shopping(self):
        self.items()
        choose = int(input("Enter 1 For Rice,2 For Sugar and 3 For Oil: "))
        quantity = int(input("Enter Your Quantity: "))
        if choose == 1:
            self.bill = self.rice() * quantity
        elif choose == 2:
            self.bill = self.sugar() * quantity
        elif choose == 3:
            self.bill = self.oil() * quantity
        else:
            print("Invalid Choose")
            return
        self.billing()

    def billing(self):
        print("Bill:", self.bill, "Rs/-")
        self.bill = self.bill + (self.bill * 5 / 100)
        if self.bill > 2000:
            self.bill = self.bill - (self.bill * 10 / 100)
        print("Total Bill:", self.bill, "Rs/-")


class RelianceSmart(Grocery):
    def items(self):
        print("Available Items:")
        print("1 Rice")
        print("2 Sugar")
        print("3 Oil")
        print()

    def shopping(self):
        self.items()
        choose = int(input("Enter 1 For Rice,2 For Sugar and 3 For Oil: "))
        quantity = int(input("Enter Your Quantity: "))
        if choose == 1:
            self.bill = self.rice() * quantity
        elif choose == 2:
            self.bill = self.sugar() * quantity
        elif choose == 3:
            self.bill = self.oil() * quantity
        else:
            print("Invalid Choose")
            return
        self.billing()

    def billing(self):
        print("Bill:", self.bill, "Rs/-")
        self.bill = self.bill + (self.bill * 5 / 100)
        if self.bill > 2500:
            self.bill = self.bill - (self.bill * 15 / 100)
        print("Total Bill:", self.bill, "Rs/-")


choose = input("Choose Your Supermarket (Dmart or RelianceSmart): ")
print()
if choose.lower() == "dmart":
    d = Dmart()
    d.shopping()
elif choose.lower() == "reliancesmart":
    r = RelianceSmart()
    r.shopping()
else:
    print("Invalid Choose")


# 9th
class Bus:
    def sleeper(self):
        return 1500

    def semi_sleeper(self):
        return 1000

    def ac(self):
        return 2000


class RedBus(Bus):
    def routes(self):
        print("Available Routes:")
        print("1 Sleeper")
        print("2 Semi Sleeper")
        print("3 AC")

    def booking(self):
        self.routes()
        choose = int(input("Enter 1 For Sleeper,2 For Semi Sleeper and 3 For Ac: "))
        tickets = int(input("Enter Number of Tickets: "))
        if choose == 1:
            self.bill = self.sleeper() * tickets
        elif choose == 2:
            self.bill = self.semi_sleeper() * tickets
        elif choose == 3:
            self.bill = self.ac() * tickets
        else:
            print("Invalid Choose")
            return
        print()
        self.billing()

    def billing(self):
        print("Amount:", self.bill, "Rs/-")
        self.bill = self.bill + (self.bill * 10 / 100)
        print("GST:10%")
        print("Reservation Charge: 30Rs/-")
        print("Total Amount:", self.bill + 30, "Rs/-")


class AbhiBus(Bus):
    def routes(self):
        print("Available Routes:")
        print("1 Sleeper")
        print("2 Semi Sleeper")
        print("3 AC")

    def booking(self):
        self.routes()
        choose = int(input("Enter 1 For Sleeper,2 For Semi Sleeper and 3 For Ac: "))
        tickets = int(input("Enter Number of Tickets: "))
        if choose == 1:
            self.bill = self.sleeper() * tickets
        elif choose == 2:
            self.bill = self.semi_sleeper() * tickets
        elif choose == 3:
            self.bill = self.ac() * tickets
        else:
            print("Invalid Choose")
            return
        self.billing()

    def billing(self):
        print("Amount:", self.bill, "Rs/-")
        self.bill = self.bill + (self.bill * 10 / 100)
        print("GST:10%")
        print("Reservation Charge: 20Rs/-")
        print("Total Amount:", self.bill + 20, "Rs/-")


choose = input("Choose The Platform (RedBus or AbhiBus): ")
if choose.lower() == "redbus":
    r = RedBus()
    r.booking()
elif choose.lower() == "abhibus":
    a = AbhiBus()
    a.booking()
else:
    print("Invalid Choose")


# 10th
class SBI:
    balance = 4000

    def deposit(self, amount):
        SBI.balance += amount
        print("Deposit Amount:", amount, "Rs/-")

    def check_balance(self):
        print("Current Balance:", SBI.balance, "Rs/-")


class UnionBank:
    def withdraw(self, amount):
        SBI.balance -= amount
        print("Withdraw Amount:", amount, "Rs/-")

    def mini_statament(self):
        print("Mini Statement:")
        print("Current Balance:", SBI.balance, "Rs/-")


class ATM(SBI, UnionBank):
    def menu(self):
        print("Choose Available Choices:")
        print("1 Deposit")
        print("2 Withdraw")
        print("3 Check Balance")
        print("4 Mini Statement")
        print("5 Exit")

    def transaction(self):
        while True:
            self.menu()
            choose = int(
                input("Enter 1 For Deposit,2 For Withdraw,3 For Check Balance,4 For Mini Statement,5 For Exit: "))
            if choose == 1:
                amount = int(input("Enter Your Amount For Deposit: "))
                self.deposit(amount)
            elif choose == 2:
                amount = int(input("Enter Your Amount For Withdraw: "))
                self.withdraw(amount)
            elif choose == 3:
                self.check_balance()
            elif choose == 4:
                self.mini_statement()
            elif choose == 5:
                print("Thank You Visiting")
                break
            else:
                print("Invalid Choose")
                return


ob = ATM()
ob.transaction()


# 11th
class MobileRecharge:
    def recharge_plans(self):
        print("Recharge Plans:")
        print("1. 299Rs/-  1.5GB/Day")
        print("2. 349Rs/-  2.0GB/Day")
        print("3. 399Rs/-  2.5GB/Day")

    def mobile_recharge(self):
        number = int(input("Enter Your Mobile Number: "))
        amount = int(input("Enter Your Recharge Amount: "))
        print("Recharge Successfully:")
        print("Mobile Number:", number)
        print("Recharge Amount:", amount, "Rs/-")


class BusTicketBooking:
    def display_buses(self):
        print("Available Buses:")
        print("1. Srikakulam to Vizag")
        print("2. Srikakulam to Hyderabad")
        print("3. Hyderabad to Srikakulam")

    def book_ticket(self):
        bus_route = input("Enter Your Bus Route: ")
        print("Bus Ticket Booked:", bus_route)


class ElectricityBills:
    def bill_details(self):
        print("Electricity Bill:")
        units = int(input("Enter Your Units Consumed: "))
        amount = units * 5
        print("Electricity Bill Amount:", amount, "Rs/-")

    def pay_bill(self):
        amount = int(input("Enter Your Electricity Bill Amount: "))
        print("Electricity Bill Paid:", amount, "Rs/- Successfully")


class Paytm(MobileRecharge, BusTicketBooking, ElectricityBills):
    def menu(self):
        print("Available Services:")
        print("1. Mobile Recharge")
        print("2. Bus Ticket Booking")
        print("3. Electricity Bill")
        print("4. Exit")

    def services(self):
        self.menu()
        while True:
            choose = int(
                input("Enter 1 For Mobile Recharge,2 For Bus Ticket Booking,3 For Electricity Bill,4 For Exit: "))
            if choose == 1:
                self.recharge_plans()
                self.mobile_recharge()
            elif choose == 2:
                self.display_buses()
                self.book_ticket()
            elif choose == 3:
                self.bill_details()
                self.pay_bill()
            elif choose == 4:
                print("Thank You For Visiting")
                break
            else:
                print("Invalid Choose")


ob = Paytm()
ob.services()















