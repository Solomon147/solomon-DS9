"""
Making a function to keep track of our dogs age
"""

class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("bark bark!")
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
    def birthday(self):
        self.age +=1
        
        
"""Name of  States"""

class states:
    """List of 2 great states"""
    def __init__(self, fl = "Florida", tx = "Texas"):
        self.fl = fl
        self.tx = tx
        
    def states_names(self):
        """Print the full meaning of the States"""
        print(self.fl, self.tx)
        
        
        
"""Basic Television Channels"""

class channels:
    
    def __init__(self, cnn, bet, msnbc, tbs):
        self.cnn = cnn
        self.bet = bet
        self.msnbc = msnbc
        self.tbs = tbs
        
    def top_channels:
        
        """Print the top channels"""
        print(self.cnn,self.bet,self.msnbc,self.tbs)
    
    