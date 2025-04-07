class Player:
    PlayersNum = 0
    def __init__(self, name, password, balance):
        Player.PlayersNum += 1
        self.__name = name
        self.__passowrd = password
        self.__balance = balance

    # Getters
    def GetName(self):
        return self.__name
    
    def GetPassword(self):
        return self.__passowrd
    
    def GetBalance(self):
        return self.__balance
    

    # Money Mangment
    def WithDraw(self, Money):
        self.__balance -= Money

    def Deposit(self, Money):
        self.__balance += Money


