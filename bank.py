from bank_accounts import *

Ayse = BankAccount(1000, "Ayse")

Dilan = BankAccount(2000, "Dilan")

Ayse.getBalance()

Dilan.getBalance()

Ayse.deposit(500)

Dilan.withdraw(10000)

Dilan.withdraw(10)

Ayse.transfer(10000, Dilan)

Ayse.transfer(100, Dilan)

Zeynep = InterestRewardsAcct(1000, "Jim")

Zeynep.getBalance()

Zeynep.deposit(100)

Zeynep.transfer(100, Ayse)

Zehra = SavingsAcct(1000, "Zehra")

Zehra.getBalance()

Zehra.deposit(100)

Zehra.transfer(10000, Dilan)

Zehra.transfer(100, Dilan)