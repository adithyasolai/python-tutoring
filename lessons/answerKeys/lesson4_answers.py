############ Exercise!! ############
# Given a list of your friends' preferences for ice cream flavors,
# find the flavors they all have in common! (and print them)
preferences = [set(["Strawberry", "Vanilla", "Rocky Road", "Chocolate"]),
               set(["Bacon", "Strawberry", "Cake Batter", "Vanilla"]),
               set(["Vanilla", "Strawberry", "Cherry",
                   "Cookies n' Cream", "Cake Batter"]),
               set(["Peanut Butter", "Salted Caramel", "Strawberry", "Vanilla", "Toffee"])]

# Expected Answer: Strawberry & Vanilla

# A Possible Solution:
common_flavors = preferences[0]
for friend in preferences:
    common_flavors = common_flavors.intersection(friend)

print(common_flavors)

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
# Any correct solution must use Social Security Number as the dictionary key, since that is the only
# unique identifier for each row of data.
irs_data_dict = {}
for row in irs_data:
    irs_data_dict[row[2]] = row[0:2] + [row[3]]

print(irs_data_dict)

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
