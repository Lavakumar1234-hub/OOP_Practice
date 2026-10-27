#1st
class BankAccount:
    def __init__(self,acno,balance):
        self.acno=acno
        self.__balance=balance
    def getter(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposit Amount Successfully")
        else:
            print("Invalid Amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdraw Amount Successfully")
        else:
            print("Invalid Amount")
ob=BankAccount(123456789,2000)
#print(ob.getter())
ob.__balance=5000
ob.deposit(2000)
ob.withdraw(3000)
print(ob.getter())

#2nd
class Student:
    def __init__(self,marks):
        self.__marks=marks
    def update(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
            print("Marks Updated")
        else:
            print("Invalid Marks")
    def get(self):
        return self.__marks
ob=Student(75)
print(ob.get())
ob.update(80)
print(ob.get())

#3rd
class SecureFile:
    def __init__(self,content):
        self.__content=content
        #self.unauthorized_attempt=0
    def read(self,password):
        if password=="1234":
            return self.__content
        else:
           # self.unauthorized_attempt+=1
            return "unauthorized access"
    #def get(self):
     #   return self.unauthorized_attempt
ob=SecureFile("IT IS A SECRET CONTENT")
print(ob.read("1234"))
print(ob.read("9999"))

#4th
class Employee:
    def __init__(self,salary):
        self.__salary=salary
        self.__log=[]
    def get(self):
        self.__log.append("salary access")
        return self.__salary
    def update_salary(self,new_salary):
        if new_salary>self.__salary:
            self.__salary=new_salary
            print("salary updated")
        else:
            print("salary must be more than previous")
    def log(self):
        return self.__log
ob=Employee(50000)
print(ob.get())
ob.update_salary(60000)
print(ob.get())
ob.update_salary(6000)
print(ob.get())
print(ob.log())

#5th
class Product:
    def __init__(self,price,discount):
        self.__price=price
        self.__discount=discount
    def set_price(self,price):
        if price>=0:
            self.__price=price
        else:
            print("price cannot be negative")
    def set_discount(self,discount):
        if 0<=discount<=70:
            self.__discount=discount
        else:
            print("Discount Cannot Exceed 70%")
    def final_price_calculation(self):
        return (self.__price-(self.__price*self.__discount/100))
    def get_final_price(self):
        return self.final_price_calculation()
ob=Product(1000,70)
ob.set_price(-1)
ob.set_discount(70)
print(ob.get_final_price())

#6th
class Character:
    def __init__(self,name,health):
        self.name=name
        self.__health=health
    def get(self):
        if 0<=self.__health<=100:
            return self.__health
        else:
            return "health should be in between 0 to 100"
    def damage(self,points):
        self.__health-=points
    def heal(self,points):
        self.__health+=points
    def attack(self,other):
        other.damage(20)
suresh=Character("suresh",100)
ramesh=Character("ramesh",100)
print(suresh.get())
print(ramesh.get())
suresh.attack(ramesh)
print(ramesh.get())
ramesh.heal(40)
print(ramesh.get())

#7th
class Engine:
    def __init__(self):
        self.__temperature=100
    def cool_engine(self):
        self.__temperature-=20
        print("Engine Temperature:",self.__temperature)
class Car:
    def __init__(self):
        self.__engine=Engine()
    def start_car(self):
        print("Car is Started...")
        self.__engine.cool_engine()
ob=Car()
ob1=Engine()
ob.start_car()
ob.start_car()
ob.start_car()

#8th
class ShoppingCart:
    def __init__(self):
        self.__items=[]
    def add_item(self,item):
        self.__items.append(item)
    def remove_item(self,item):
        self.__items.remove(item)
    def get_cart_items(self):
        return self.__items.copy()
ob=ShoppingCart()
ob.add_item("laptop")
ob.add_item("phone")
ob.add_item("mouse")
print("cart items:",ob.get_cart_items())
ob.remove_item("phone")
print("After Remove:",ob.get_cart_items())

#9th
class Student:
    def __init__(self):
        self.attendance=[]
    def show_attendance(self):
        print(self.attendance)
ob=Student()
ob.attendance.append("present")
ob.attendance.append("present")
ob.show_attendance()
print(ob.attendance)
ob.attendance.append("absent")
print(ob.attendance)
class Student:
    def __init__(self):
        self.__attendance=[]
    def mark_attendance(self,other):
        if other=="present" or other=="absent":
            self.__attendance.append(other)
        else:
            print("Invalid")
    def show_attendance(self):
        print(self.__attendance)
ob=Student()
ob.mark_attendance("present")
ob.mark_attendance("present")
ob.show_attendance()
ob.mark_attendance("absent")
ob.show_attendance()

#10th
class Student:
    def __init__(self,age):
        self.__age=age
    @property
    def s_age(self):
        return self.__age
    @s_age.setter
    def s_age(self,value):
        if value>0:
            self.__age=value
        else:
            print("Age not below or Equal to Zero")
ob=Student(25)
print(ob.s_age)
ob.s_age=28
print(ob.s_age)
#using underscore prefix
ob._Student__age=50
print(ob.s_age)
#setter validation
ob.s_age=0
print(ob.s_age)






