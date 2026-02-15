## Practice Problem 9

Cashless Transaction System

---

## Problem Statement

Informatica, a consultancy services company has planned to offer cashless transaction service to its employees. The employees can use their smart cards for any transaction (credit/debit).

Write a Python program to implement the class diagram given below.

---

# Class Diagram

                         +----------------------------------+
                         |            SmartCard              |
                         +----------------------------------+
                         | - card_no : str                  |
                         | - account_balance : float        |
                         +----------------------------------+
                         | + __init__(card_no)              |
                         | + get_card_no() : str            |
                         | + get_account_balance() : float  |
                         | + set_account_balance(balance)   |
                         +----------------------------------+


                                      1
                                      |
                                      | Aggregation (Has-A)
                                      ◇
                                      |
                                      |
                                      1
                         +----------------------------------+
                         |             Employee             |
                         +----------------------------------+
                         | - employee_id : int              |
                         | - employee_name : str            |
                         | - smart_card : SmartCard         |
                         +----------------------------------+
                         | + __init__(id,name,smart_card)   |
                         | + get_employee_id() : int        |
                         | + get_employee_name() : str      |
                         | + validate_employee_id() : bool  |
                         | + validate_card_no() : bool      |
                         +----------------------------------+



                         +----------------------------------+
                         |            Transaction           |
                         +----------------------------------+
                         | - transaction_id : str           |
                         +----------------------------------+
                         | + __init__()                     |
                         | + get_transaction_id() : str     |
                         | + top_up_card(emp, amount)       |
                         | + make_payment(emp, amount)      |
                         +----------------------------------+
                                      |
                                      |
                                      | Association (Uses)
                                      |
                                      v
                                   Employee


---

# Class Description

## SmartCard Class

### Attributes:
- card_no
- account_balance

### Methods:

1. __init__(card_no)
   - Initialize the smart card number.
   - Set account_balance to 500 by default.

2. get_card_no()
   - Return the card number.

3. get_account_balance()
   - Return the current account balance.

4. set_account_balance(account_balance)
   - Set the account balance to the given value.

---

## Employee Class

### Attributes:
- employee_id
- employee_name
- smart_card (object of SmartCard class)

### Methods:

1. __init__(employee_id, employee_name, smart_card)
   - Initialize employee id, name and smart card object.

2. get_employee_id()
   - Return employee id.

3. get_employee_name()
   - Return employee name.

4. validate_employee_id()
   - Employee id should be in the range of 1000 (not inclusive) to 700000 (inclusive).
   - If valid return True.
   - Else return False.

5. validate_card_no()
   - Validate employee's smart card number.
   - Smart card number should have 9 characters.
   - It should begin with "INF".
   - It should not contain alphabets in any other positions.
   - If all rules are satisfied, return True.
   - Else return False.

---

## Transaction Class

### Attribute:
- transaction_id

### Methods:

1. __init__()
   - Initialize transaction_id as None.

2. get_transaction_id()
   - Return transaction id.

---

### 1. top_up_card(employee, amount)

Accept the employee object whose smart card should be topped up with the given amount.

Rules:

a. If the given amount is between 500 and 10000 (both inclusive):
   - If employee.employee_id and employee.smart_card.card_no are valid:
     - Add the given amount to employee.smart_card.account_balance
   - Else return -1
b. Else return -1

Return updated balance if successful.

---

### 2. make_payment(employee, amount)

Debit the given amount from the employee’s smart card and auto-generate transaction_id starting with:

"T" followed by:
- First digit of employee id
- First two numeric values of the card number

Transaction should be processed only if:

a. Enough balance should be present in employee’s smart card.
b. employee.employee_id should be valid.
c. employee.smart_card.account_balance should remain at least Rs.500 after transaction.

If all the above rules are satisfied:
- Deduct the amount.
- Generate transaction_id as specified.
- Return the generated transaction_id.

If any rule fails:
- Return -1.

---

# Additional Instructions

1. Create an object of SmartCard class.
2. Create an object of Employee class using the SmartCard object.
3. Create an object of Transaction class.
4. Invoke:
   - make_payment()
   - top_up_card()
5. Display the details.

---

# Constraints

1. All validations must be strictly followed.
2. Minimum balance of Rs.500 must always be maintained.
3. Card number validation must strictly follow format rules.
4. If any validation fails, return -1.
5. Default smart card balance must be Rs.500.

---

# Expected Behavior

- If top-up is successful → return updated balance.
- If payment is successful → return generated transaction id.
- If any condition fails → return -1.