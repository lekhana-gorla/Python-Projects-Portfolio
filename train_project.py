# This program simulates booking train tickets. It has four classes: Train, Passenger, Ticket and Account.

# The Train class represents a train with its train number, source, destination, and the number of seats available. It has methods to display the train information and book tickets.

# The Passenger class represents a passenger with their name, age, gender, and phone number. It has a method to display passenger information.

# The Ticket class represents a ticket with the train, source, destination, passengers, and PNR (Passenger Name Record) number. It has a method to display ticket information.

# Class called Account is defined with a constructor that takes two arguments: username and password. The class also defines a method called check_password which takes a single argument password and returns a boolean indicating whether the input password matches the stored password.

# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------
import random
#We  use import random module because, we need to get some random pnr values
class Train():
    def __init__(self,train_num, source, destination, seats):
        self.train_num=train_num
        self.source=source
        self.destination=destination
        self.seats=seats
#we defined the class with 4 parameters
    def display_info(self):
        print(f"The train number is :{self.train_num}")
        print(f"The source is: {self.source}")
        print(f"The destination is:{self.destination}")
        print(f"The no.of seats are:{self.seats}")
        print()#Line break for each train info displayed
#we defined the displayed info method for train class, which diaplys of all 4 parameters
    def book_tickets(self,num_tickets):
        if num_tickets>self.seats:
            return None
        else:
            pnr_list=[]
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000,999999))
            self.seats-=num_tickets
            return pnr_list
#Here we defined book_tickets method() where it generates random pnr list, if the no.of seats
#are available and updates no.of avaible seats, otherwise returns None
class Passenger():
    def __init__(self,name,age,gender,phone):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
#we defined the class passenger method with 4 parameters
    def display_info(self):
        print(f"The name of person is :{self.name}")
        print(f"The age of person is:{self.age}")
        print(f"The gender is:{self.gender}")
        print(f"The phone number is:{self.phone}")
#we defined the display info method() that provied all the info of the class
class Ticket():
    def __init__(self, train, source, destination, passenger, pnr):
        self.train=train
        self.source=source
        self.destination=destination
        self.passengers=passenger
        self.pnr=pnr
#We defined another Class ticket method() which has 5 parameters in it
    def display_info(self):
        print(f"The train:{self.train.train_num}")
        print(f"The source is:{self.source}")
        print(f"The destination is:{self.destination}")
        print(f"The passenger is:{self.passengers}")
        print(f"The pnr is:{self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()
        print()
#We defined the display_info method() to display the info for each passenger
class Account():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def check_password(self,password):
        return self.password == password
#The class called account is defined with two arguments to Login to the account.The class also 
# defines a method called check password with single parameter, to check whether the input matches
#the stored value or not
accounts=[
    Account('user1','password1'),
    Account('user2','password2')
]
#A list called accounts intialized with arguments already in it
logged_in_account=None
# A variable called logged_in_account is initialized to None. This variable will be used later to
#keep track of the currently logged in account
while True:
    print("\n1.Create an account \n2.Login")
    Choice=input('enter your choice:')
    if Choice =='1':
        username=input('enter the username:')
        password=input('enter the password:')
        accounts.append(Account(username,password))
#If user chose 1, then need to enter the username nad passowrd to create account succesfully, 
#the inputted details will append into the Accounts List
        print("Account created succesfully")
    elif Choice=='2':
        username=input('enter the username:')
        password=input('enter the password:')
        for account in accounts:
            if account.username==username and account.check_password(password):
                logged_in_account=account
                break
        if logged_in_account is None:
                print("Invalid credentials")
#If user choice=2, they enter the details. The program iterates to the account and check whether 
#stored accounts match the given inputs. If yes, the corresponding Account object is 
# assigned to the logged_in_account variable and the loop is broken or else it shows invalid 
#credentials.
        else:
            print(f"\n Logged in as {logged_in_account.username}\n\n-----Available train details----\n")

            break
    else:
        print("Invalid choice.")
        
if logged_in_account is not None:
    trains = [
        Train("12737", "Tadepalligudem", "Secunderabad", 40),
        Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
        Train("22863", "Vijayawada", "Bangalore", 1),
        
    ]
# The program creates a list of Train objects, with each train having a unique train number, source,
#destination, and the number of seats available.

#Display available trains
    for train in trains:
            train.display_info()
    while True:
            try:
                train_num=input("enter the train number:")
                num_tickets=int(input("enter the no.of tickets:"))
                if num_tickets<=0:
                    raise ValueError("The no.of tickets should be greater than zero")
                for train in trains:
                    if train.train_num==train_num:
                        if num_tickets>train.seats:
                            raise ValueError("The no.of tickets are more than available seats")
                        break
                else:
                    raise ValueError('invalid train number')
                break
            except ValueError as e:
                print(f"invalid input: {e}")
#This program asks the passenger to give the valid  train number with no.of tickets they wanted
#to book
    train=None
    for t in trains:
            t.train_num=train_num
            train=t
            break
#The program searches for the train object with corresponding train number given by thr passenger
    if train is None:
            print("invalid train number")
    
    else:
        passengers=[]
        for i in range(num_tickets):
            print(f"\n enter the details of the passenger {i+1}:")
            while True:
                try:
                    name=input("name:")
                    if not name:
                        raise ValueError("name cannot be empty")
                    age=int(input("age:"))
                    if age <=0 or age >120:
                        raise ValueError("invalid age")
                    gender=input("gender:")
                    phone=input("phone:")
                    if not phone or len(phone) !=10 or not phone.isdigit():
                        raise ValueError("invalid phone number")
                    passenger=Passenger(name,age,gender,phone)
                    passengers.append(passenger)
                    break
                except ValueError as e:
                    print(f"Invalid Input: {e}")
#If the train number is valid then it prompts the user to enter the details of the passenger
#For each passenger, it creates a name,age,gender,phone number entered by passenger and it appends 
#this the list caleed passengers
    pnr_list=train.book_tickets(num_tickets)
    if pnr_list is None:
            print("Tickets are not available")
#The program calls the book_tickets method to book the no.of tickets, if there are available seats 
#then it will generates a pnr_number 
#If it is None then it prints not available
    else:
            print("\n --------------Booking successful------------\n\nTicket Details: \n")
            for i in range(num_tickets):
                ticket=Ticket(train, train.source,train.destination, [
                          passengers[i]],pnr_list[i])
                ticket.display_info()
                print("\n--------Thank you--------\n-----------Have a safe journey-----------")
#The tickets are booked, the program prints program successfull
1
