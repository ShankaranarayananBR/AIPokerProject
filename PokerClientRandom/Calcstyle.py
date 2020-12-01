from Player import *



class Calcstyle:
	FOLD=0.0
	CHECK=0.3
	CALL=0.5
	OPEN=0.7
	RAISE=0.8
	ALLIN=1.0
	START_VAL=0.5
	LEARN_RATE = 4.0
	NoOfOpens=0
	NoOfChecks=0
	NoOfCalls=0
	Aggresitivity=0
	NoOfAllIns=0
	NoOfFolds=0
	NoOfRaises=0
	OpenRatio=0
	#DEFAULT=0.3
	
	def __init__(self):
		self.FOLD=0.0
		self.CHECK=0.3
		self.CALL=0.5
		self.OPEN=0.7
		self.RAISE=0.8
		self.ALLIN=1.0
		self.START_VAL=0.5
		self.LEARN_RATE=4.0
		self.NoOfOpens=0
		self.NoOfChecks=0
		self.NoOfCalls=0
		self.Aggresitivity=0
		self.NoOfAllIns=0
		self.NoOfFolds=0
		self.NoOfRaises=0
		self.OpenRatio=0
		#self.DEFAULT=0.3
	
	def CalcPlayStyle(Round):
		Aggr = ( START_VAL + NoOfFolds*FOLD + NoOfChecks*CHECK + NoOfCalls*CALL + NoOfOpens*OPEN + NoOfRaises*0.6 + NoOfAllIns*ALLIN ) / ( NoOfFolds + NoOfChecks +	NoOfCalls + NoOfOpens + NoOfRaises + NoOfAllIns )
		Aggresitivity = Aggr
		if Round > LEARN_RATE:
			return Aggr
		else:
			return Aggr*( Round/LEARN_RATE )
	
	def OpenCheckRatio(Round):
		Aggr = ( ( NoOfOpens*1.0 ) / ( NoOfOpens + NoOfChecks )*1.0 )
		OpenRatio = Aggr + 0.5
		if Round>LEARN_RATE:
			return Aggr + 0.5
		else:
			return ( Aggr*( Round/LEARN_RATE ) + 0.5 )
	"""	
	def CalcRaiseCall(Player,Round):
		Accuracy=1
		if Round<=4:
			Accuracy==Round/4
		return (Player.Raise * 1.0 )/( Player.Call+Player.Raise )*Accuracy+0.5
	
	def CalcOpenCheck(Player,Round):
		Accuracy=1
		if Round<=4:
			Accuracy==Round/4
		return ( Player.Open * 1.0 )/( Player.Check + Player.Open )*Accuracy+0.5
	"""

