'''
Project 2: Bank
Written by Adithya Solai
'''

'''
In this project, students will model a bank system using Python. This project is intended to
give students an opportunity to architect a more complex system of classes & objects
than what is done in problem sets and lesson exercises so far. In addition to
classes, students are also encouraged to use dictionaries and sets to store and use
data efficiently.

Required functionality of this bank model:
-Every bank account has 4 features--a unique bank ID, a human name, an account password,
 and (of course) the remaining balance in the bank account.
-In order to access the human name, password, or balance of any given bank account, the
 user must provide BOTH the bank ID and password for that account.
-The bank model should allow users to deposit & withdraw money from their accounts, as
 well as change the password for their accounts. (Bank ID & human name can't be changed)
-The bank model should also allow users to add a new account and close an existing account.
-To re-iterate, most functionality (deposit, withdraw, change password, and close account)
 requires both the bank ID AND password for the account.
-Opening a new bank account requires a human name, password, and starting balance from the user.
 The unique bank ID should be randomly generated for the new account.
-In addition to individual user interactions, we also want to be able to get holistic information
 about our bank (if we were the bank owners). Write functions that return the name and balance
 of the bank account with the smallest balance. Do the same for the bank account with the highest
 balance. Also, write a function that returns the mean/average balance of the entire bank.

Implementation suggestions:
-The student is free to implement the bank however they want.
-Students are suggested to have a `Bank` class and a separate `BankAccount` class, and figure
 out how those two classes interact with each other. Some starter code for these classes is
 given below. BankAccount is declared first so that the Python interpreter will allow you to
 use BankAccount within the Bank class (hint hint).

Some assumptions we make to simplify this bank model:
-This is a commercial bank, and customers only have one type of account (not both a checking
 and savings account like most commercial banks).

How this project will be assessed:
-There are some public test cases below. These test cases are not written as code, because
 the student could implement the Bank (and/or Account) classes different.
-There will also be a private set of test cases not exposed to the student that will be
 used to further evaluate the bank model. Students are encouraged to write their own
 test cases to predict what these hidden test cases might be, and make their Bank model
 more prepared.
'''


class BankAccount:
    def __init__(self):
        None


class Bank:
    def __init__(self):
        None


# -----------------------------------------------------------------------

# Public Test Case 1: Average use case tests
#
# Add a new account with $5,000 starting balance.
# You shouldn't need to provide a unique Bank ID, it should
# be generated automatically.
#
# Deposit $1000 to this account. Check that there is now $6000 in the balance.
#
# Withdraw $500 from this account. Check that there is now $5500 in the
# balance.

# -----------------------------------------------------------------------

# Public Test Case 2: Nonsense deposit/withdraw tests
#
# Add a new account with $5,000 starting balance.
# You shouldn't need to provide a unique Bank ID, it should
# be generated automatically.
#
# Try to deposit -$500 to the account. This should not be allowed
#
# Try to withdraw -$10 from the account. This should not be allowed

# -----------------------------------------------------------------------

# Public Test Cast 3: Stress Testing
#
# Use a for-loop to add 10,000 users to the bank with random strings
# as names and random starting balances between $5 and $100. Also
# generate random password strings for all 10,000 users, and store these.
#
# Check that no two users have the same unique Bank ID.
#
# Use the passwords to conduct a deposit of $10 on all 10,000 accounts.
