# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

import random

class trian():

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self , fro , to):
        print(f"Ticket Is Booked in train no:{self.trainNo} From {fro} to {to}")

    def getstatus(self):
        print(f"Train  no:{self.trainNo} Train Is Runnig On Time!!")

    def getfare(self , fro , to):
        print(f"Ticket Fare in train no:{self.trainNo} From {fro} to {to} is {random.randint(222,888)}")

t = trian(12333)
t.book("Sambhaji Nagar", "Shrirampur")
t.getstatus()
t.book("Sambhaji Nagar", "Shrirampur")