class SmartCard:
    def __init__(self, card_no):
        self.card_no = card_no
        self.account_balance = 500  

    def get_card_no(self):
        return self.card_no

    def get_account_balance(self):
        return self.account_balance

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance


class Employee:
    def __init__(self, employee_id, employee_name, smart_card):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.smart_card = smart_card

    def get_employee_id(self):
        return self.employee_id

    def get_employee_name(self):
        return self.employee_name

    def validate_employee_id(self):
        if 1000 < self.employee_id <= 700000:
            return True
        else:
            return False

    def validate_card_no(self):
        card_no = self.smart_card.get_card_no()

        
        if len(card_no) != 9:
            return False

        
        if not card_no.startswith("INF"):
            return False

      
        remaining = card_no[3:]
        if not remaining.isdigit():
            return False

        return True


class Transaction:
    def __init__(self):
        self.transaction_id = None

    def get_transaction_id(self):
        return self.transaction_id

    def top_up_card(self, employee, amount):

        
        if 500 <= amount <= 10000:

          
            if employee.validate_employee_id() and employee.validate_card_no():

                current_balance = employee.smart_card.get_account_balance()
                new_balance = current_balance + amount
                employee.smart_card.set_account_balance(new_balance)

                return new_balance
            else:
                return -1
        else:
            return -1

    def make_payment(self, employee, amount):

        
        if not employee.validate_employee_id():
            return -1

       
        if not employee.validate_card_no():
            return -1

        current_balance = employee.smart_card.get_account_balance()

        
        if current_balance < amount:
            return -1

       
        if (current_balance - amount) < 500:
            return -1

       
        employee.smart_card.set_account_balance(current_balance - amount)

    
        emp_id_str = str(employee.get_employee_id())
        first_digit_emp_id = emp_id_str[0]

        card_no = employee.smart_card.get_card_no()
        numeric_part = card_no[3:]  # After INF
        first_two_digits = numeric_part[:2]

        self.transaction_id = "T" + first_digit_emp_id + first_two_digits

        return self.transaction_id



card = SmartCard("INF123456")


emp = Employee(1500, "Rahul", card)


txn = Transaction()


print("Top-up Result:", txn.top_up_card(emp, 2000))


print("Transaction ID:", txn.make_payment(emp, 1000))

print("Remaining Balance:", emp.smart_card.get_account_balance())
