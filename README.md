# Bank Account Management System

## Overview
This project is a simple Bank Account Management System implemented in Python. It includes basic banking functionalities such as deposit, withdrawal, balance checking, and account transfers. Additionally, it introduces two specialized account types: `InterestRewardsAcct` and `SavingsAcct`, which provide unique features.

## Features
- **Create a Bank Account** with an initial balance and account name.
- **Deposit Money** into the account.
- **Withdraw Money**, ensuring sufficient balance.
- **Transfer Money** between accounts.
- **InterestRewardsAcct** provides a 5% bonus on deposits.
- **SavingsAcct** charges a withdrawal fee.

## Classes
### 1. `BalanceException`
A custom exception raised when an account has insufficient funds for a transaction.

### 2. `BankAccount`
The base class representing a bank account.
#### Methods:
- `__init__(initialAmount, acctName)`: Initializes an account with a balance and name.
- `getBalance()`: Displays the account balance.
- `deposit(amount)`: Adds the amount to the balance.
- `viableTransaction(amount)`: Checks if the account has enough funds for a transaction.
- `withdraw(amount)`: Withdraws money from the account after validating balance.
- `transfer(amount, account)`: Transfers money to another account.

### 3. `InterestRewardsAcct`
A subclass of `BankAccount` that provides a 5% bonus on every deposit.
#### Methods:
- `deposit(amount)`: Deposits money with a 5% reward.

### 4. `SavingsAcct`
A subclass of `InterestRewardsAcct` that includes a withdrawal fee.
#### Methods:
- `__init__(initialAmount, acctName)`: Initializes with an additional withdrawal fee.
- `withdraw(amount)`: Withdraws money, deducting a fixed fee.

## Example Usage
```python
# Creating accounts
acc1 = BankAccount(1000, "John's Account")
acc2 = InterestRewardsAcct(500, "Rewards Account")
acc3 = SavingsAcct(800, "Savings Account")

# Performing transactions
acc1.deposit(200)
acc1.withdraw(300)
acc1.transfer(400, acc2)
acc2.deposit(100)
acc3.withdraw(100)
```

## Requirements
- Python 3.x

## How to Run
1. Copy the script into a Python environment.
2. Create instances of `BankAccount`, `InterestRewardsAcct`, or `SavingsAcct`.
3. Perform transactions using the available methods.

## License
This project is licensed under the MIT License.

