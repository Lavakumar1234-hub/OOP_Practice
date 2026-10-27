from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def bike(self):
        print("bike")
class Car(Vehicle):
    def bike(self):
        print("bike class")
ob=Car()
ob.bike()

#1st Abstraction Answers
from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
class Triangle(Shape):
    def __init__(self,s1,s2,s3,height,base):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.height=height
        self.base=base
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
c=Circle(5)
print(c.area())
print(c.perimeter())
r=Rectangle(10,5)
print(r.area())
print(r.perimeter())
t=Triangle(4,4,5,5,3)
print(t.area())
print(t.perimeter())

#2nd
from abc import ABC,abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def authentication(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class UPIPayment(PaymentGateway):
    def authentication(self):
        print("UPI Authentication Successfully")
    def pay(self,amount):
        print("Paid",amount,"using UPI")
    def refund(self,amount):
        print("Refund",amount,"to UPI")
class CardPayment(PaymentGateway):
    def authentication(self):
        print("Card Authentication Successfully")
    def pay(self,amount):
        print("Paid",amount,"using Card")
    def refund(self,amount):
        print("Refund",amount,"to Card")
class NetBank(PaymentGateway):
    def authentication(self):
        print("Net Bank Authentication Successfully")
    def pay(self,amount):
        print("Paid",amount,"using Net Bank")
    def refund(self,amount):
        print("Refund",amount,"to Net Bank")
ob=[UPIPayment(),CardPayment(),NetBank()]
for i in ob:
    i.authentication()
    i.pay(1000)
    i.refund(500)
    print()

#3rd
from abc import ABC,abstractmethod
class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def steer(self):
        pass
class CarControl(VehicleControl):
    def accelerate(self):
        print("Car Acceleration")
    def brake(self):
        print("Car Brake")
    def steer(self):
        print("Car Steer")
class BikeControl(VehicleControl):
    def accelerate(self):
        print("Bike Acceleration")
    def brake(self):
        print("Bike Brake")
    def steer(self):
        print("Bike Steer")
class TruckControl(VehicleControl):
    def accelerate(self):
        print("Truck Acceleration")
    def brake(self):
        print("Truck Brake")
    def steer(self):
        print("Truck Steer")
ob=[CarControl(),BikeControl(),TruckControl()]
for i in ob:
    i.accelerate()
    i.brake()
    i.steer()
    print()

#4th
from abc import ABC,abstractmethod
class DataBaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute(self,query):
        pass
    @abstractmethod
    def close(self):
        pass
class MySQLDriver(DataBaseDriver):
    def connect(self):
        print("Connecting to MySQLDriver")
    def execute(self,query):
        print(f"MySQL Executing:{query}")
    def close(self):
        print("Closing MySQL")
class PostgresDriver(DataBaseDriver):
    def connect(self):
        print("Connecting Postgres")
    def execute(self,query):
        print(f"Postgres Executing:{query}")
    def close(self):
        print("Closing Postgres")
class SQLiteDriver(DataBaseDriver):
    def connect(self):
        print("Connecting to SQLite")
    def execute(self,query):
        print(f"SQLite Executing:{query}")
    def close(self):
        print("Closing SQLite")
#main application code
def run_sql(database):
    database.connect()
    database.execute("SELECT * FROM TABLENAME")
    database.close()
#switch database without changing run sql
ob=MySQLDriver()
run_sql(ob)
print()
ob=PostgresDriver()
run_sql(ob)
print()
ob=SQLiteDriver()
run_sql(ob)

#5th
from abc import ABC,abstractmethod
class ReportGenerator(ABC):
    @abstractmethod
    def load_data(self):
        pass
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def export(self):
        pass
    #multi step workflow
    def generate_report(self):
        self.load_data()
        self.process()
        self.export()
class PDFReport(ReportGenerator):
    def load_data(self):
        print("Loading Data From PDF Report")
    def process(self):
        print("Processing Data From PDF Report")
    def export(self):
        print("Exporting Data From PDF Report")
class ExcelReport(ReportGenerator):
    def load_data(self):
        print("Loading Data From Excel Report")
    def process(self):
        print("Processing Data From Excel Report")
    def export(self):
        print("Exporting Data From Excel Report")
ob=[PDFReport(),ExcelReport()]
for i in ob:
    i.generate_report()
    print()

#6th
from abc import ABC,abstractmethod
class RobotCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
class PickCommand(RobotCommand):
    def execute(self):
        print("Robot Pick the object")
    def undo(self):
        print("Robot puts the object back")
class PlaceCommand(RobotCommand):
    def execute(self):
        print("Robot Place the Object")
    def undo(self):
        print("Robot place back the object")
class MoveCommand(RobotCommand):
    def execute(self):
        print("Robot Moves Forward")
    def undo(self):
        print("Robot Moves Backward")
p=PickCommand()
p.execute()
p.undo()
print()
pl=PlaceCommand()
pl.execute()
pl.undo()
print()
m=MoveCommand()
m.execute()
m.undo()

#7th
from abc import ABC,abstractmethod
class MLModel(ABC):
    @abstractmethod
    def train(self,data):
        pass
    @abstractmethod
    def predict(self,x):
        pass
    @abstractmethod
    def evaluate(self,test_set):
        pass
class LinearRegressionModel(MLModel):
    def train(self,data):
        print(f"Linear Regression is Training Using {data}")
    def predict(self,x):
        print(f"Linear Regression is Predict Value {x}")
    def evaluate(self,test_set):
        print(f"Linear Regression is Evaluating {test_set}")
class DecisionTreeModel(MLModel):
    def train(self,data):
        print(f"Decision Tree is Training Using {data}")
    def predict(self,x):
        print(f"Decision Tree is Predict Value {x}")
    def evaluate(self,test_set):
        print(f"Decision Tree is Evaluating {test_set}")
#generic training loop
def run_flow(data):
    data.train("data")
    data.predict(10)
    data.evaluate("test data")
li=LinearRegressionModel()
run_flow(li)
print()
de=DecisionTreeModel()
run_flow(de)

#8th
def EmailSender(message):
    print("Sending Email:",message)
def SMSSender(message):
    print("Sending SMS:",message)
def PushSender(message):
    print("Sending Push Notification:",message)
n=input("Enter Your Notification Type: ")
if n=="email":
    EmailSender("Hii")
elif n=="sms":
    SMSSender("Hii")
elif n=="push":
    PushSender("Hii")
else:
    print("Invalid Notification Type")

from abc import ABC,abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self,message):
        pass
class EmailSender(Notifier):
    def send(self,message):
        print(f"Sending Email Message {message}")
class SMSSender(Notifier):
    def send(self,message):
        print(f"Sending SMS Message {message}")
class PushSender(Notifier):
    def send(self,message):
        print(f"Sending Push Message {message}")
def notify(chat,message):
    chat.send(message)
    print()
e=EmailSender()
notify(e,"Hii")
s=SMSSender()
notify(s,"Hii")
p=PushSender()
notify(p,"Hii")

#9th
from abc import ABC,abstractmethod
class MediaPlayer(ABC):
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class MP3Player(MediaPlayer):
    def load(self):
        print("Loading MP3Player")
    def play(self):
        print("Playing MP3Player")
    def stop(self):
        print("Stoping MP3Player")
class WAVPlayer(MediaPlayer):
    def load(self):
        print("Loading WAVPlayer")
    def play(self):
        print("Playing WAVPlayer")
    def stop(self):
        print("Stoping WAVPlayer")
class AACPlayer(MediaPlayer):
    def load(self):
        print("Loading AACPlayer")
    def play(self):
        print("Playing AACPlayer")
    def stop(self):
        print("Stoping ACCPlayer")
def use_player(player):
    player.load()
    player.play()
    player.stop()
    print()
m=MP3Player()
use_player(m)
w=WAVPlayer()
use_player(w)
a=AACPlayer()
use_player(a)

#10th
from abc import ABC,abstractmethod
class Sensor(ABC):
    @abstractmethod
    def read_value(self):
        pass
    @abstractmethod
    def calibrate(self):
        pass
    def get_reading(self):
        self.calibrate()
        return self.read_value()
class TemperatureSensor(Sensor):
    def __init__(self):
        self.__raw_reading=24
        self.__calibrate_factor=1.1
    def calibrate(self):
        self.__raw_reading=self.__raw_reading * self.__calibrate_factor
    def read_value(self):
        return self.__raw_reading
class PressureSensor(Sensor):
    def __init__(self):
        self.__raw_reading=100
        self.__calibrate_factor=1.1
    def calibrate(self):
        self.__raw_reading=self.__raw_reading * self.__calibrate_factor
    def read_value(self):
        return self.__raw_reading
class HumiditySensor(Sensor):
    def __init__(self):
        self.__raw_reading=35
        self.__calibrate_factor=0.1
    def calibrate(self):
        self.__raw_reading=self.__raw_reading * self.__calibrate_factor
    def read_value(self):
        return self.__raw_reading
t=TemperatureSensor()
print(t.get_reading())
p=PressureSensor()
print(p.get_reading())
h=HumiditySensor()
print(h.get_reading())

