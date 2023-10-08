from bank_accounts import *

Rangga = BankAccount(1000, "Rangga")
Falah = BankAccount(1700, "Falah")

Rangga.getBalance()
Falah.getBalance()

Rangga.deposit(200)

Falah.withdraw(10000)

Falah.transfer(1000, Rangga)
Falah.transfer(100, Rangga)

Jim = InterestRewardsAcc(1000, "Jim")


Jim.getBalance()
Jim.deposit(100)
Jim.transfer(105, Rangga)

Blaze = SavingsAcc(1000, "Blaze")

Blaze.getBalance()
Blaze.deposit(1000)
Blaze.transfer(100, Jim)
