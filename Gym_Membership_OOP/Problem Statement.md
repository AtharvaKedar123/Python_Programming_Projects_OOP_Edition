##### Problem Statement







FitLife Gym wants to automate the process of managing members, trainers, and gym sessions. Each member can book sessions with a trainer, and the system should track session availability, member limits, and payments.  



You are required to implement this system using Python \*\*OOP concepts\*\*, following the class diagram and rules provided.



---



\## Class Diagram



&nbsp;                +-------------------------------+

&nbsp;                |           Trainer             |

&nbsp;                +-------------------------------+

&nbsp;                | - trainer\_id : str            |

&nbsp;                | - trainer\_name : str          |

&nbsp;                | - max\_sessions : int          |

&nbsp;                | - available\_sessions : int    |

&nbsp;                +-------------------------------+

&nbsp;                | + \_\_init\_\_(id, name, max\_sessions) |

&nbsp;                | + get\_trainer\_id() : str      |

&nbsp;                | + get\_trainer\_name() : str    |

&nbsp;                | + check\_availability() : bool|

&nbsp;                | + update\_sessions(count)      |

&nbsp;                +-------------------------------+



&nbsp;                        1

&nbsp;                        |

&nbsp;                        | Aggregation (Has-A)

&nbsp;                        ◇

&nbsp;                        |

&nbsp;                        |

&nbsp;                +-------------------------------+

&nbsp;                |            Member             |

&nbsp;                +-------------------------------+

&nbsp;                | - member\_id : int             |

&nbsp;                | - member\_name : str           |

&nbsp;                | - booked\_sessions : list      |

&nbsp;                | - wallet\_balance : float      |

&nbsp;                +-------------------------------+

&nbsp;                | + \_\_init\_\_(id, name, balance) |

&nbsp;                | + get\_member\_id() : int       |

&nbsp;                | + get\_member\_name() : str     |

&nbsp;                | + book\_session(trainer, fee) |

&nbsp;                | + cancel\_session(trainer)     |

&nbsp;                +-------------------------------+



&nbsp;                        ^

&nbsp;                        |

&nbsp;                        | Association (Uses)

&nbsp;                        |

&nbsp;                +-------------------------------+

&nbsp;                |            Gym                |

&nbsp;                +-------------------------------+

&nbsp;                | - gym\_name : str              |

&nbsp;                +-------------------------------+

&nbsp;                | + \_\_init\_\_(name)              |

&nbsp;                | + schedule\_session(member, trainer, fee) |

&nbsp;                | + cancel\_session(member, trainer)        |

&nbsp;                +-------------------------------+





---



\## Class Descriptions

#### 

#### \### Trainer Class



\*\*Attributes:\*\*

\- `trainer\_id` – Unique identifier for the trainer.  

\- `trainer\_name` – Name of the trainer.  

\- `max\_sessions` – Maximum sessions the trainer can conduct.  

\- `available\_sessions` – Current available sessions.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(id, name, max\_sessions)` – Initializes trainer and sets available sessions = max\_sessions.  

2\. `get\_trainer\_id()` – Returns trainer ID.  

3\. `get\_trainer\_name()` – Returns trainer name.  

4\. `check\_availability()` – Returns `True` if `available\_sessions > 0`.  

5\. `update\_sessions(count)` – Add/subtract sessions.  



---



#### \### Member Class



\*\*Attributes:\*\*

\- `member\_id` – Unique identifier for the member.  

\- `member\_name` – Name of the member.  

\- `booked\_sessions` – List of Trainer objects the member has booked.  

\- `wallet\_balance` – Amount available for paying sessions.  



**\*\*Methods:\*\***

1\. `\_\_init\_\_(id, name, balance)` – Initializes member and empty `booked\_sessions`.  

2\. `get\_member\_id()` – Returns member ID.  

3\. `get\_member\_name()` – Returns member name.  

4\. `book\_session(trainer, fee)` – Books a session with trainer if:  

&nbsp;  - Trainer has availability.  

&nbsp;  - Member has enough wallet balance to pay fee.  

&nbsp;  - Member has less than 5 booked sessions.  

&nbsp;  Returns `True` if successful, else `-1`.  

5\. `cancel\_session(trainer)` – Cancels booked session:  

&nbsp;  - Adds back trainer’s available session.  

&nbsp;  - Refunds half of session fee to wallet.  

&nbsp;  Returns `True` if successful, else `-1`.  



---



#### \### Gym Class



\*\*Attributes:\*\*

\- `gym\_name` – Name of the gym.  



\*\*Methods:\*\*

1\. `\_\_init\_\_(name)` – Initializes gym name.  

2\. `schedule\_session(member, trainer, fee)` – Uses `Member` and `Trainer` objects to book a session. Returns `"Session booked successfully"` or `-1`.  

3\. `cancel\_session(member, trainer)` – Uses `Member` and `Trainer` objects to cancel session. Returns `"Session cancelled successfully"` or `-1`.  



---



\## Rules and Constraints



1\. Each member can \*\*book at most 5 sessions\*\*.  

2\. Trainer cannot exceed \*\*max\_sessions\*\*.  

3\. Member must have \*\*enough balance\*\* for session fee.  

4\. Cancelled session refunds \*\*half the session fee\*\*.  

5\. All validations must be strictly followed.  

6\. Use \*\*aggregation\*\* between Member and Trainer.  

7\. Gym uses association to handle booking and cancellation.  



---



\## Expected Behavior



| Scenario | Output |

|----------|--------|

| Successful booking | `"Session booked successfully"` |

| Booking more than 5 sessions | `-1` |

| Booking when trainer unavailable | `-1` |

| Booking without enough balance | `-1` |

| Successful cancellation | `"Session cancelled successfully"` |

| Cancelling a session not booked | `-1` |



---



\## Sample Usage



```python

\# Create Trainer objects

t1 = Trainer("T101", "John Doe", 3)

t2 = Trainer("T102", "Jane Smith", 2)



\# Create Member object

m1 = Member(301, "Alice", 5000)



\# Create Gym object

gym = Gym("FitLife")



\# Book sessions

print(gym.schedule\_session(m1, t1, 1000))  # Session booked successfully

print(gym.schedule\_session(m1, t2, 1500))  # Session booked successfully

print(gym.schedule\_session(m1, t1, 1000))  # Session booked successfully

print(gym.schedule\_session(m1, t1, 1000))  # -1 (trainer full or max 5 sessions)



\# Cancel sessions

print(gym.cancel\_session(m1, t1))           # Session cancelled successfully

print(gym.cancel\_session(m1, t1))           # -1 (already cancelled)



\# Check member wallet balance

print(m1.wallet\_balance)  # 5000 - 1000 - 1500 - 1000 + 500 (half refund) = 2000

