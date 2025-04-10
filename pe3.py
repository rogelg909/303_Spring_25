
import string 


def encode (input_text, shift):

    alphabet = list(string.ascii_lowercase)

    encoded_text = ""

    for char in input_text:
        if char.isalpha(): 

            char = char.lower()

            
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % 26


            new_char = alphabet[new_index]

        else:
            new_char = char

        encoded_text += new_char

    return (alphabet, encoded_text)

def decode(input_text, shift):

    alphabet = list(string.ascii_lowercase)

    decoded_text = ""

    for char in input_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            old_index = alphabet.index(char)
            new_index = (old_index - shift) % 26

            new_char = alphabet[new_index]
            if is_upper: 
                new_char = new_char.upper()

        else:
            new_char = char

        decoded_text += new_char

    return decoded_text



from datetime import date

class BankAccount:
    def __init__(self, name = "Rainy", ID = "1234", creation_date = date.today(), balance=0):
        if creation_date > date.today():
            raise Exception("Creation date cannot be in the future.")
        
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("withdrawl amount must be positive.")
            return
        
        if amount > self.balance:
            print("insufficient funds.")
            return
        
        self.balance -= amount
        print(f"Withdrew {amount}. New Balance: {self.balance}")

    def view_balance(self):
        print(f"Account Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, name = "Rainy", ID = "1234", creation_date = date.today(), balance = 0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        if (date.today() - self.creation_date).days < 100:
            print("Withdrawls are only allowed after the account has been in existance for 180 days.")
            return
        
        if amount > self.balance:
            print("overdrafts are not permitted.")
            return
        
        super().withdraw(amount)


class CheckingAccount(BankAccount):
    def __init__(self, name = "Rainy", ID = "1234", creation_date = date.today(), balance = 0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        self.balance -= amount
        if self.balance < 0:
            self.balance -= 30
            print("Overdraft incurred. A $30 fee has been charged.")

        print(f"Withdrew {amount}. New balance: {self.balance}")
