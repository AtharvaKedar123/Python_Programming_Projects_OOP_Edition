class Trainer:
    def __init__(self, trainer_id, trainer_name, max_sessions):
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        self.max_sessions = max_sessions
        self.available_sessions = max_sessions

    def get_trainer_id(self):
        return self.trainer_id

    def get_trainer_name(self):
        return self.trainer_name

    def check_availability(self):
        return self.available_sessions > 0

    def update_sessions(self, count):
        self.available_sessions += count



class Member:
    def __init__(self, member_id, member_name, wallet_balance):
        self.member_id = member_id
        self.member_name = member_name
        self.wallet_balance = wallet_balance
        self.booked_sessions = []

    def get_member_id(self):
        return self.member_id

    def get_member_name(self):
        return self.member_name

    def book_session(self, trainer, fee):
        if len(self.booked_sessions) >= 5:
            return -1  
        if not trainer.check_availability():
            return -1  
        if self.wallet_balance < fee:
            return -1  

        
        self.booked_sessions.append((trainer, fee))
        trainer.update_sessions(-1)
        self.wallet_balance -= fee
        return True

    def cancel_session(self, trainer):
        
        for session in self.booked_sessions:
            if session[0] == trainer:
                fee = session[1]
                self.booked_sessions.remove(session)
                trainer.update_sessions(1)
                self.wallet_balance += fee / 2  
                return True
        return -1  



class Gym:
    def __init__(self, gym_name):
        self.gym_name = gym_name

    def schedule_session(self, member, trainer, fee):
        result = member.book_session(trainer, fee)
        if result == True:
            return "Session booked successfully"
        else:
            return -1

    def cancel_session(self, member, trainer):
        result = member.cancel_session(trainer)
        if result == True:
            return "Session cancelled successfully"
        else:
            return -1





t1 = Trainer("T101", "John Doe", 3)
t2 = Trainer("T102", "Jane Smith", 2)


m1 = Member(301, "Alice", 5000)


gym = Gym("FitLife")


print(gym.schedule_session(m1, t1, 1000))  
print(gym.schedule_session(m1, t2, 1500))  
print(gym.schedule_session(m1, t1, 1000))  
print(gym.schedule_session(m1, t1, 1000))  


print(gym.cancel_session(m1, t1))          
print(gym.cancel_session(m1, t1))           

print("Wallet balance:", m1.wallet_balance)  

print("T1 available sessions:", t1.available_sessions)  
print("T2 available sessions:", t2.available_sessions)  
