class Player:
    Name = 0
    Position = 0
    CardsThrown=0
    LastAction=0
    NoOfOpens=0
    NoOfChecks=0
    NoOfFolds=0
    NoOfCalls=0
    NoOfRaises=0
    NoOfAllIns=0
    Chips=200
    InRound=True
    Position=Position
    OpenRatio=0
    Aggresitivity=0
    
    def __init__(self):
        self.Name
        self.CardsThrown
        self.LastAction
        self.NoOfOpens
        self.NoOfChecks
        self.NoOfFolds
        self.NoOfCalls
        self.NoOfRaises
        self.NoOfAllIns
        self.Chips
        self.InRound
        self.Position
        self.OpenRatio
        self.Aggresitivity
    
    
    def Vinay(self,name,Position):
        self.Name = name
        self.NoOfOpens = 0
        self.NoOfChecks = 0
        self.NoOfFolds = 0
        self.NoOfCalls = 0
        self.NoOfAllIns = 0
        self.NoOfRaises = 0
        self.LastAction = -1
        self.Chips = 200
        self.InRound = True
        self.Position = Position
        self.CardsThrown=0
        
    def getname(self):
        return self.Name