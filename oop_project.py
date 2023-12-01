#file that will pull all other .py files ino it 

from bank_accounts import *

Dave = BankAccount (1000, 'Dave')
Sarah = BankAccount (2000, 'Sarah')
Mike = BankAccount (1500, 'Mike')

# show_mike = Mike.getBalance()

# Mike.deposit(300)
# Mike.withdraw(2000)

 
# Dave.transfer(100, Mike)
# Jim_the_money_saver = InterestRewardsAcc(1000, 'jim')

# Jim_the_money_saver.getBalance()

# Jim_the_money_saver.deposit(500)
# Jim_the_money_saver.transfer(500, Dave)

Stacey_the_saver = SavingsAcc(1000, 'Stacey')
Stacey_the_saver.getBalance()
Stacey_the_saver.withdraw(100)
Stacey_the_saver.withdraw(1200)
Stacey_the_saver.deposit(200)
Stacey_the_saver.transfer(250, Sarah)
Stacey_the_saver.transfer(900, Sarah)