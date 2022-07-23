'''
Lesson 4
Written by Adithya Solai
'''

'''
Sets
-O(1) insert, delete, search
-No concept of order/cardinality; for-loop is in non-deterministic order
-No duplicates allowed (to avoid collisions)
-Can perform familiar set operations as well (union, intersection, etc.)
'''

# Ex: Efficiently storing bank IDs
# We know that bank IDs must be unique
# We also only ever want to insert, delete, or lookup bank IDs, nothing else
bank_ids = set()
bank_ids.add(1234)
bank_ids.add(7777)
bank_ids.add(1002)

# Is 6749 in our bank?
print(6749 in bank_ids)

# Is 7777 in our bank?
print(7777 in bank_ids)

# Remove 1234 from our bank
bank_ids.remove(1234)

# Ex: Storing our high school class's roster
# Normally, we would just use lists.
# However, sets perform all necessary use cases for the roster, and faster.
roster = set(["Brad", "Jane", "John", "Molly"])

# Add students
roster.add("Kelly")

# Remove students
roster.remove("Jane")

# Search if a student is in our class (in O(1) time!)
print("Molly" in roster)

# Iterate through our roster for a roll call
for student in roster:
    print(f"{student}, are you here?")

# (Note: You can't do roll call in any particular order with sets, you would need lists for that)

# Ex: Intersection, Union, Set Subtract, etc.
roster = set(["Brad", "Jane", "John", "Molly"])
roster2 = set(["Brad", "Jack", "John", "Adam"])
print(roster.intersection(roster2), type(roster.intersection(roster2)))
print(roster.union(roster2), type(roster.intersection(roster2)))
print(roster.difference(roster2), type(roster.intersection(roster2)))

############ Exercise!! ############
# Given a list of your friends' preferences for ice cream flavors,
# find the flavors they all have in common! (and print them)
preferences = [set(["Strawberry", "Vanilla", "Rocky Road", "Chocolate"]),
               set(["Bacon", "Strawberry", "Cake Batter", "Vanilla"]),
               set(["Vanilla", "Strawberry", "Cherry", "Cookies n' Cream", "Cake Batter"]),
               set(["Peanut Butter", "Salted Caramel", "Strawberry", "Vanilla", "Toffee"])]

# Expected Answer: Strawberry & Vanilla

# A Possible Solution:
common_flavors = preferences[0]
for friend in preferences:
    common_flavors = common_flavors.intersection(friend)

print(common_flavors)

'''
Dictionaries
-Another "associative" structure like sets
-Basically a set of key-value pairs
-Keys can be any "hashable" data type
-Keys must be unique
-Collection of all Keys is basically a set (since all keys must be unique)
-Use keys to access the values they are associated with
-Values can be anything (can be duplicates, don't need to be hashable)
'''

# Ex: Efficiently store customer info
# Key: Bank ID (which we know is unique to each customer)
# Values: A list with the following structure [balance in pennies (int),
# interest rate (float), start date (string)]
bank = {}  # or bank = dict()

# Customer w/ ID 1234
bank[1234] = [6700, 0.01, "4/3/12"]
# Customer w/ ID 6749
bank[6749] = [100000, 0.01, "8/8/17"]
# Customer w/ ID 7777
bank[7777] = [25000, 0.02, "8/31/16"]

# Iterate through our customers
for key, value in bank.items():
    print(f"Customer {key}: {value}")

# Fetch Customer 7777's balance
print(bank[7777][0])

# Is Customer 8890 in our bank?
print(8890 in bank.keys())

# Is Customer 1234 in our bank?
print(1234 in bank.keys())

############ Exercise!! ############
# Store the following data efficiently using a dictionary
# Print the dictionary after storing all of the data inside it
# Data Schema for each row: [Name <str>, Tax Due <int>, Social Security Number <str>, Date of Birth <str>]
#
# (After storing the data in your dictionary database, let's use it to query information quickly in O(1))
irs_data = [["Jack", 5600, "757-00-1294", "07-07-2002"],
            ["Janie", 100000, "997-16-6694", "03-21-1997"],
            ["Lex", 2790340, "200-38-6237", "05-17-1990"],
            ["Abraham", 0, "121-49-1171", "11-01-1957"]]

# A Possible Solution
irs_data_dict = {}
for row in irs_data:
    irs_data_dict[row[2]] = row[0:2] + [row[3]]


'''
Classes
-Object-Oriented Programming
-Abstraction
-Cleaner way to store data together, and modify as you go along
-Cleaner way to hand bundles of data over to many different functions/processes
'''

# Ex: A better way to store our irs data from before:


class irsPerson:
    # explicitly stating the argument types doesn't really help here
    def __init__(self, name: str, ssn: str, dob: str, tax_due: int):
        self.name = name
        self.ssn = ssn
        self.dob = dob
        self.tax_due = tax_due


class irsDatabase:
    def __init__(self):
        self.data = {}

    # explicitly stating that the `person` arg is an `irsPerson` type is super helpful here
    # (again, not needed as Python is an interpreted language, but this is good style and helps you code)
    def addPerson(self, person: irsPerson):
        self.data[person.ssn] = person

    def getPerson(self, ssn: str):
        return self.data[ssn]

    def isPersonInDatabase(self, ssn: str):
        return ssn in self.data.keys()

    def removePerson(self, ssn: str):
        del self.data[ssn]

# That's it! We have a fully-functioning, fast database now
# Let's use our database


# Define Person objects first
jack = irsPerson(
    name="Jack",
    ssn="757-00-1294",
    dob="07-07-2002",
    tax_due=5600)
# don't need to explicitly write the argument name if you remember the order
janie = irsPerson("Janie", "997-16-6694", "03-21-1997", 100000)
lex = irsPerson("Lex", "200-38-6237", "05-17-1990", 2790340)
abraham = irsPerson("Abraham", "121-49-1171", "11-01-1957", 0)

# Initialize our database
irs_data = irsDatabase()

# Add our people to the database
irs_data.addPerson(jack)
irs_data.addPerson(janie)
irs_data.addPerson(lex)
irs_data.addPerson(abraham)

# Get Jack's Tax Due is now very intuitive. Don't need to remember any indexes.
print(irs_data.getPerson("757-00-1294").tax_due)

############ Exercise!! ############
# Design & build a computer network
'''
Network is made up of users

Users:
-IP Address (unique to each user) (string)
-Home Address (string)
-Logs: A list of logs that show a User's activity
-Each Log's Structure: Timestamp (extremely precise, unique) (string), URL (str), Port (int)

Actions:
-Add Users to Network
-Remove Users from Network
-Ask if a User is in the Network
-Add Logs to a User
-Ask what a User did at a particular timestamp

'''

# A Possible Solution:
'''
Design:

Network = dict<IP, User>
User = (home address, dict<timestamp,[URL, port]>)
'''


class networkUser:
    # Don't need to define any variables up top here like Java.
    # You can if you want. Better to just define in the constructor below.

    # The constructor.
    # All functions in this class need `self` as first parameter
    # Non-self functions will not be able to access variables global to the
    # class
    def __init__(self, IP, home_address):
        self.IP = IP
        self.home = home_address
        # A dictionary that will contain lists of activity logs of this network user,
        # with timestamp as the key, and a list of [URL, port] as the value
        self.logs = {}

    def add_log(self, timestamp, URL, port):
        self.logs[timestamp] = [URL, port]

    def get_logs(self):
        return self.logs

    def get_logs_by_timestamp(self, timestamp):
        if timestamp in self.logs.keys():
            return self.logs[timestamp]
        else:
            return None

# Classes + Dictionaries are super powerful!


class network:
    def __init__(self):
        # The whole network can now just be represented as a dict with IP address as key,
        # and a networkUser object as value (which itself is a dict as
        # described above)
        self.users = {}

    def add_user(self, IP, home_address):
        self.users[IP] = networkUser(IP, home_address)

    def add_log(self, IP, timestamp, URL, port):
        if IP in self.users.keys():
            self.users[IP].add_log(timestamp, URL, port)
        else:
            return None

    def delete_user(self, IP):
        del self.users[IP]

    def get_log(self, IP, timestamp):
        return self.users[IP].get_logs_by_timestamp(timestamp)
