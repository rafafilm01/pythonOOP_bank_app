class BalanceException(Exception): 
    pass
    #special class to be used for verifying if there are enough funds on the account , no code goes here , only the code exception code will be generated when the class is triggered.
    #suggestion to have separate classes for error codes , also listed at the top of the doc for easier access and better readability  
    

class BankAccount:
    def __init__ (self, initialAmount, accName):
        self.balance =initialAmount
        self.name = accName
        print (f"\nAccount '{self.name}' created. \nCurrent balance = ${self.balance:.2f}")
        #additional formatting :.2f added to the balance variable adding 2 decimals when displaying the print statement 
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
        
        #making  a deposit and changing already existing value for balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        # print(f"Thank you for depositing ${amount}")
        print ("\nDeposit completed successfully !")    
        self.getBalance()
        #once balance of the account has been updated with the deposit we can call the method that already exists to show us the new balance (DRY code principle)
    
    

    #withdraw method needs a check to see if there is enough funds for the operation to be completed , use of BalanceException class. The viableTransaction to be used in the withdraw method 
    #viableTransaction is a very trimmed down method that is used in various other methods in the class. It should be as straightforward as possible        
    def viableTransaction (self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nAccount '{self.name} only has got ${self.balance:.2f}")
        
    def withdraw (self, amount):
        #validate if there is enough money in the account using the try block with viableTransaction method
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete !")
            self.getBalance()
            
        except BalanceException as error: 
            print(f"\nWithdraw failed: {error}") 
            
        
    #transfer method used for sending money across accounts . Also utilizes viableTransaction to make sure the transfer can go ahead 
    def transfer(self, amount, account):
        try:
            print('\n*******\n\nBeginning Transfer... ')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer has been completed ! ✅\n\n*******")
        except BalanceException as error:
            print(f'\nTransfer failed ❌: {error}')
            
 #InterestRewardsAccount is inheriting from BankAccount therefore it will have access to all attributes and methods from the parent class. deposit method is making changes to the OG method as the intrestRate account gives extra 5% for each deposit         
class InterestRewardsAcc (BankAccount):
    #no __init__ method as there are no new attributes but we will overwrite  the deposit  attribute (by adding % to the top)
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit complete !')
        self.getBalance()
        
        
class SavingsAcc (InterestRewardsAcc):
    #we are creating new attributes for the class and therefore need to create a __init__ method 
    def __init__ (self, initialAmount, accName):
        super().__init__(initialAmount, accName) #first refer to the parent class to pull the attributes we need , secondly , add new attributes that are only for SavingsAcc class
        self.fee = 5
        
    #overwrite the withdraw method as we apply a fee each time money is taken out of the account 
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee) #new value for the viableTransaction that includes the additional fee
            self.balance = self.balance - (self.fee + amount)
            print("\nWithdraw complete !")
            self.getBalance()
        except BalanceException as error: 
            print(f"Withdraw failed !: {error}")
        
    