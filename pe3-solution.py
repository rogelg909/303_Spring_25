from datetime import date, timedelta

def encode(input_text, shift):
    """
    Encodes text using Caesar cipher with specified shift.
    Returns a tuple of (alphabet list, encoded text).
    """
    alphabet = [chr(i) for i in range(97, 123)]
    
    # Function to shift a single character
    def shift_char(char):
        if char.isalpha():
            # Determine case and base ascii value
            is_upper = char.isupper()
            base = ord('A' if is_upper else 'a')
            
            # Convert to 0-25 range, apply shift, wrap around, convert back to char
            shifted = (ord(char.lower()) - ord('a') + shift) % 26
            result = chr(shifted + ord('a'))
            
            return result.upper() if is_upper else result
        return char
    
    # Process each character in input text
    encoded = ''.join(shift_char(c) for c in input_text)
    
    return (alphabet, encoded)

def decode(input_text, shift):
    """
    Decodes text using Caesar cipher with specified shift.
    Returns decoded text.
    """
    # Decoding is just encoding with negative shift
    return encode(input_text, -shift)[1]

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        self.name = name
        self.ID = ID
        
        # Sets creation date, defaulting to today if None
        if creation_date is None:
            self.creation_date = date.today()
        else:
            if creation_date > date.today():
                raise Exception("Creation date cannot be in the future")
            self.creation_date = creation_date
            
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Negative deposits are not allowed")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        # Check if account is at least 180 days old
        if (date.today() - self.creation_date).days < 180:
            raise Exception("Account must be 180 days old for withdrawals")
        
        # Check for overdraft
        if self.balance - amount < 0:
            raise Exception("Overdrafts are not permitted on savings accounts")
            
        return super().withdraw(amount)

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        previous_balance = self.balance
        new_balance = super().withdraw(amount)
        
        # Apply overdraft fee if withdrawal caused negative balance
        if new_balance < 0 <= previous_balance:
            self.balance -= 30  # $30 overdraft fee
            return self.balance
            
        return new_balance
