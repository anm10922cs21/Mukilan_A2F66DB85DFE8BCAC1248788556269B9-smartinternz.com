
class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposit Ã¢â€šÂ¹{}. New balance: Ã¢â€šÂ¹{}".format (amount,self.__account_balance))
    else:
      print("Invalid deposit amount.")
      
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -=amount
      print("withdrew Ã¢â€šÂ¹{}.New balance: Ã¢â€šÂ¹{}". format(amount,self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
      
  def display_balance(self):
      print("Account balance for {} (Account #{}): Ã¢â€šÂ¹{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))
    
account = BankAccount(account_number="11111122222444", account_holder_name="SACHIDANANTHAM", initial_balance=5000.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()