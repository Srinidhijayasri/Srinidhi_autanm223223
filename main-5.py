class BankAccount:
  def_init_(self,account_number,account_holder_name,initial_balance=0.0):
    self.account_number = account_number
    self.account_holder_name = account_holder_name
    self._account_balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self._account_balance+=amount
      print("deposit$().New balance:$()".format(amount,self._account_balance))
  else:
    print("invalid deposit amount.please deposit a positive amount.")
    def wwithdraw(self,amount):
    if amount>0and amount<=self._account_balance:
self._account_balance_=amount
print("withdraw$().New balance:$()".format(amount,self._account_balance))
else:
print("invalid withdraw amount or insufficient balance.")
def display_balance(self):
print("Account Balance for{}(amount#{}:${}".format(self._account_holder_name,self._sccount_number,self._account_balance))
account=BankAccount(account_number="987654321",account_holder_name="priya",initial_balance=5000.0)
account.dispaly_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()


    
