# Practice Problem 18

## Problem Statement

A bank wants to model different types of accounts using inheritance.

Write a python program to implement the class diagram given below.

------------------------------------------------------------------------

## Class Diagram

                     +----------------------+
                     |        Account       |
                     +----------------------+
                     | - account_number     |
                     | - balance            |
                     +----------------------+
                     | + __init__(account_number,balance)
                     | + deposit(amount)
                     | + withdraw(amount)
                     | + get_balance()
                     +----------------------+
                            ▲
                            │
             ---------------|----------------
             |                               |
    +--------------------+       +---------------------+
    |  SavingsAccount    |       |   CurrentAccount   |
    +--------------------+       +---------------------+
    | - interest_rate    |       | - overdraft_limit  |
    +--------------------+       +---------------------+
    | + __init__(account_number, | + __init__(account_number,
    |   balance,interest_rate)   |   balance,overdraft_limit)
    | + calculate_interest()     | + withdraw(amount)
    +--------------------+       +---------------------+

------------------------------------------------------------------------

## Class Description

### Account class:

1.  account_number: Unique account number\
2.  balance: Current account balance\
3.  deposit(amount): Add amount to balance\
4.  withdraw(amount): Deduct amount if sufficient balance\
5.  get_balance(): Return current balance

------------------------------------------------------------------------

### SavingsAccount class:

1.  interest_rate: Rate of interest\
2.  calculate_interest(): Return balance \* interest_rate / 100

------------------------------------------------------------------------

### CurrentAccount class:

1.  overdraft_limit: Maximum overdraft allowed\
2.  Override withdraw(amount): Allow withdrawal within overdraft_limit

------------------------------------------------------------------------

Create objects of SavingsAccount and CurrentAccount classes, invoke
appropriate methods and test your program.
