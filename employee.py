"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, description):
        self.name = name
        self.pay = pay
        self.description = description

    def get_pay(self):
        return self.pay

    def __str__(self):
        return self.description

billie = Employee('Billie', 4000, "Billie works on a monthly salary of 4000. Their total pay is 4000.")
charlie = Employee('Charlie', 2500, "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.")
renee = Employee('Renee', 3800, "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.")
jan = Employee('Jan', 4410, "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.")
robbie = Employee('Robbie', 3500, "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.")
ariel = Employee('Ariel', 4200, "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.")
