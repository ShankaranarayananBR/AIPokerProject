__author__ = 'fyt'

import socket
import random
import ClientBase
from Hand import *
from CardRank import CardRank
from Calcstyle import *
from Player import *
# IP address and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
#Declaration


# Agent
#POKER_CLIENT_NAME = 'Shankar1'
POKER_CLIENT_NAME='Shankar2'
CURRENT_HAND = []
#Declaration
tester=Calcstyle()
NoOfFolds=0
hand=Hand()
Players={}
Ranker=CardRank()
CurrentRound = 0
NoOfActions = 0
PlayersFolded = 0
Ante=0
Shankar=Player()
CardsLeft=[]
Raisedplayer =[]
Checkedplayer = []
Raised=0
CardsThrown=None
Checked=0
Me=0
Aggresive=0
Unaggresive=0
CHIP_VALUE=0

Bionomial=[47, 1081, 16215, 178365, 1533939]
TOTAL_MONEY=0
Evaluate=False
RankBin = [ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096 ]
Suit = [ 1, 2, 4, 8 ]
RankDec = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
CardPrime = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41 ]
CardRep=[( RankBin[0] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[0] << 8 ) + CardPrime[0],#Clubs
                              ( RankBin[1] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[1] << 8 ) + CardPrime[1],
                              ( RankBin[2] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[2] << 8 ) + CardPrime[2],
                              ( RankBin[3] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[3] << 8 ) + CardPrime[3],
                              ( RankBin[4] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[4] << 8 ) + CardPrime[4],
                              ( RankBin[5] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[5] << 8 ) + CardPrime[5],
                              ( RankBin[6] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[6] << 8 ) + CardPrime[6],
                              ( RankBin[7] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[7] << 8 ) + CardPrime[7],
                              ( RankBin[8] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[8] << 8 ) + CardPrime[8],
                              ( RankBin[9] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[9] << 8 ) + CardPrime[9],
                              ( RankBin[10] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[10] << 8 ) + CardPrime[10],
                              ( RankBin[11] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[11] << 8 ) + CardPrime[11],
                              ( RankBin[12] << 16 ) + ( Suit[3] << 12 ) + ( RankDec[12] << 8 ) + CardPrime[12],
                              ( RankBin[0] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[0] << 8 ) + CardPrime[0], # Diamonds #
                              ( RankBin[1] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[1] << 8 ) + CardPrime[1],
                              ( RankBin[2] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[2] << 8 ) + CardPrime[2],
                              ( RankBin[3] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[3] << 8 ) + CardPrime[3],
                              ( RankBin[4] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[4] << 8 ) + CardPrime[4],
                              ( RankBin[5] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[5] << 8 ) + CardPrime[5],
                              ( RankBin[6] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[6] << 8 ) + CardPrime[6],
                              ( RankBin[7] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[7] << 8 ) + CardPrime[7],
                              ( RankBin[8] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[8] << 8 ) + CardPrime[8],
                              ( RankBin[9] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[9] << 8 ) + CardPrime[9],
                              ( RankBin[10] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[10] << 8 ) + CardPrime[10],
                              ( RankBin[11] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[11] << 8 ) + CardPrime[11],
                              ( RankBin[12] << 16 ) + ( Suit[2] << 12 ) + ( RankDec[12] << 8 ) + CardPrime[12],
                              ( RankBin[0] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[0] << 8 ) + CardPrime[0], # Hearts #
                              ( RankBin[1] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[1] << 8 ) + CardPrime[1],
                              ( RankBin[2] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[2] << 8 ) + CardPrime[2],
                              ( RankBin[3] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[3] << 8 ) + CardPrime[3],
                              ( RankBin[4] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[4] << 8 ) + CardPrime[4],
                              ( RankBin[5] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[5] << 8 ) + CardPrime[5],
                              ( RankBin[6] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[6] << 8 ) + CardPrime[6],
                              ( RankBin[7] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[7] << 8 ) + CardPrime[7],
                              ( RankBin[8] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[8] << 8 ) + CardPrime[8],
                              ( RankBin[9] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[9] << 8 ) + CardPrime[9],
                              ( RankBin[10] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[10] << 8 ) + CardPrime[10],
                              ( RankBin[11] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[11] << 8 ) + CardPrime[11],
                              ( RankBin[12] << 16 ) + ( Suit[1] << 12 ) + ( RankDec[12] << 8 ) + CardPrime[12],
                              ( RankBin[0] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[0] << 8 ) + CardPrime[0], # Spades #
                              ( RankBin[1] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[1] << 8 ) + CardPrime[1],
                              ( RankBin[2] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[2] << 8 ) + CardPrime[2],
                              ( RankBin[3] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[3] << 8 ) + CardPrime[3],
                              ( RankBin[4] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[4] << 8 ) + CardPrime[4],
                              ( RankBin[5] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[5] << 8 ) + CardPrime[5],
                              ( RankBin[6] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[6] << 8 ) + CardPrime[6],
                              ( RankBin[7] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[7] << 8 ) + CardPrime[7],
                              ( RankBin[8] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[8] << 8 ) + CardPrime[8],
                              ( RankBin[9] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[9] << 8 ) + CardPrime[9],
                              ( RankBin[10] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[10] << 8 ) + CardPrime[10],
                              ( RankBin[11] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[11] << 8 ) + CardPrime[11],
                              ( RankBin[12] << 16 ) + ( Suit[0] << 12 ) + ( RankDec[12] << 8 ) + CardPrime[12]]

class pokerGames(object):
    def __init__(self):
        self.PlayerName = POKER_CLIENT_NAME
        self.Chips = 0
        self.CurrentHand = []
        self.Ante = 0
        self.playersCurrentBet = 0

'''
* Gets the name of the player.
* @return  The name of the player as a single word without space. <code>null</code> is not a valid answer.
'''
def queryPlayerName(_name):
    if _name is None:
        _name = POKER_CLIENT_NAME
    return _name

'''
* Modify queryOpenAction() and add your strategy here
* Called during the betting phases of the game when the player needs to decide what open
* action to choose.
* @param minimumPotAfterOpen   the total minimum amount of chips to put into the pot if the answer action is
*                              {@link BettingAnswer#ACTION_OPEN}.
* @param playersCurrentBet     the amount of chips the player has already put into the pot (dure to the forced bet).
* @param playersRemainingChips the number of chips the player has not yet put into the pot.
* @return                      An answer to the open query. The answer action must be one of
*                              {@link BettingAnswer#ACTION_OPEN}, {@link BettingAnswer#ACTION_ALLIN} or
*                              {@link BettingAnswer#ACTION_CHECK }. If the action is open, the answers
*                              amount of chips in the anser must be between <code>minimumPotAfterOpen</code>
*                              and the players total amount of chips (the amount of chips alrady put into
*                              pot plus the remaining amount of chips).
'''
def queryOpenAction(_minimumPotAfterOpen, _playersCurrentBet, _playersRemainingChips):
    print("Player requested to choose an opening action.")
    Bet=0
    while Evaluate==False:
        PlayersLeftInBettingRound=len(Players)-NoOfActions-PlayersFolded
        
        if (_minimumPotAfterOpen-_playersCurrentBet)>=_playersRemainingChips:
            return ClientBase.BettingAnswer.ACTION_CHECK
              
        else:
            Bet=int(CHIP_VALUE*( PositionScaling( PlayersLeftInBettingRound ) )*BestHandValue*BestHandValue*BestHandValue )
            if Bet<=minimumPotAfterOpen:
               return ClientBase.BettingAnswer.ACTION_CHECK
               
            elif Bet<=minimumPotAfterOpen*1.2:
                return ClientBase.BettingAnswer.ACTION_CHECK
                
            if Bet>=playersRemainingChips:
                 return ClientBase.BettingAnswer.ACTION_ALLIN
                 
            if self.CardsThrown==False and Bet>Ante:
                return ClientBase.BettingAnswer.ACTION_OPEN, Ante+_playersCurrentBet
                
            if self.len(Players)==2:
                return ClientBase.BettingAnswer.ACTION_OPEN, Bet+_playersCurrentBet
                
    return ClientBase.BettingAnswer.ACTION_OPEN, Bet+_playersCurrentBet
    """
    # Random Open Action
    def chooseOpenOrCheck():
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            #return ClientBase.BettingAnswer.ACTION_OPEN,  iOpenBet
            return ClientBase.BettingAnswer.ACTION_OPEN,  (random.randint(0, 10) + _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10> _minimumPotAfterOpen else _minimumPotAfterOpen
        else:
            return ClientBase.BettingAnswer.ACTION_CHECK

    return {
        0: ClientBase.BettingAnswer.ACTION_CHECK,
        1: ClientBase.BettingAnswer.ACTION_ALLIN,
    }.get(random.randint(0, 2), chooseOpenOrCheck())
    """
'''
* Modify queryCallRaiseAction() and add your strategy here
* Called during the betting phases of the game when the player needs to decide what call/raise
* action to choose.
* @param maximumBet                the maximum number of chips one player has already put into the pot.
* @param minimumAmountToRaiseTo    the minimum amount of chips to bet if the returned answer is {@link BettingAnswer#ACTION_RAISE}.
* @param playersCurrentBet         the number of chips the player has already put into the pot.
* @param playersRemainingChips     the number of chips the player has not yet put into the pot.
* @return                          An answer to the call or raise query. The answer action must be one of
*                                  {@link BettingAnswer#ACTION_FOLD}, {@link BettingAnswer#ACTION_CALL},
*                                  {@link BettingAnswer#ACTION_RAISE} or {@link BettingAnswer#ACTION_ALLIN }.
*                                  If the players number of remaining chips is less than the maximum bet and
*                                  the players current bet, the call action is not available. If the players
*                                  number of remaining chips plus the players current bet is less than the minimum
*                                  amount of chips to raise to, the raise action is not available. If the action
*                                  is raise, the answers amount of chips is the total amount of chips the player
*                                  puts into the pot and must be between <code>minimumAmountToRaiseTo</code> and
*                                  <code>playersCurrentBet+playersRemainingChips</code>.
'''
def queryCallRaiseAction(_maximumBet, _minimumAmountToRaiseTo, _playersCurrentBet, _playersRemainingChips):
    print("Player requested to choose a call/raise action.")
    while Evaluated == false:
        PlayersLeftInBettingRound = len(Players) - NoOfActions - PlayersFolded
        Bet
        AggrOfRaisPlayer
        AggrOfRaisPlayer = tester.CalcPlayStyle( Raised, self.CurrentRound )
        if playersRemainingChips <= ( maximumBet - playersCurrentBet ):
            if ( self.CardsThrown == false ) and ( BestHandValue > 0.5 ) and ( AggrOfRaisPlayer > 0.6 ):
                return ClientBase.BettingAnswer.ACTION_ALLIN

            elif ( self.CardsThrown == True ) and ( Raised.CardsThrown >= 3 ) and ( BestHandValue > 0.5 ):
                return ClientBase.BettingAnswer.ACTION_ALLIN 
            elif playersRemainingChips <= 0.1*playersCurrentBet:
                return ClientBase.BettingAnswer.ACTION_ALLIN 

            if ( self.CardsThrown == True ) and BestHandValue > 0.70 and Raised.CardsThrown != 0:
                return ClientBase.BettingAnswer.ACTION_ALLIN 
            return ClientBase.BettingAnswer.ACTION_FOLD 

        if playersRemainingChips <= ( minimumAmountToRaiseTo-playersCurrentBet ):
            if Raised.LastAction == ClientBase.BettingAnswer.ACTION_OPEN:
                Bet =  CHIP_VALUE * BestHandValue * self.PositionScaling( PlayersLeftInBettingRound ) * tester.OpenCheckRatio(CurrentRound ) 

                if Bet >= ( maximumBet-playersCurrentBet ):
                    return ClientBase.BettingAnswer.ACTION_CALL 

                if BestHandValue*Raised.OpenRatio > 0.65:
                    return ClientBase.BettingAnswer.ACTION_ALLIN 

                return ClientBase.BettingAnswer.ACTION_FOLD 

            else:
                Bet = CHIP_VALUE * BestHandValue * self.PositionScaling( PlayersLeftInBettingRound ) * tester.CalcPlayStyle( Raised, self.CurrentRound )

                if Bet >= ( maximumBet-playersCurrentBet ):
                    return ClientBase.BettingAnswer.ACTION_CALL 

                if BestHandValue*Raised.Aggresitivity > 0.35 :
                    return ClientBase.BettingAnswer.ACTION_ALLIN 
                return ClientBase.BettingAnswer.ACTION_FOLD 
        else:
            if Raised.LastAction == ClientBase.BettingAnswer.ACTION_OPEN or Raised.LastAction == ClientBase.BettingAnswer.ACTION_RAISE:
                if Raised.LastAction == ClientBase.BettingAnswer.ACTION_OPEN:
                    Bet = CHIP_VALUE * BestHandValue * BestHandValue * self.PositionScaling( PlayersLeftInBettingRound ) * Calcstyle.OpenCheckRatio( Raised, self.CurrentRound ) 
                else:
                    Bet = CHIP_VALUE * BestHandValue * BestHandValue * Calcstyle.CalcPlayStyle( Raised, self.CurrentRound )
                if Bet >= ( minimumAmountToRaiseTo-playersCurrentBet )*1.5:
                    if Bet > playersRemainingChips:
                        ClientBase.BettingAnswer.ACTION_ALLIN

                    return ClientBase.BettingAnswer.ACTION_RAISE, Bet+playersCurrentBet 

                elif  Bet >= ( maximumBet-playersCurrentBet ):
                    return ClientBase.BettingAnswer.ACTION_CALL 

                if BestHandValue > 0.7 and self.CurrentRound <= 3:
                    return ClientBase.BettingAnswer.ACTION_CALL 

                return ClientBase.BettingAnswer.ACTION_FOLD 

            elif Raised.LastAction == ClientBase.BettingAnswer.ACTION_ALLIN:
                if playersRemainingChips >= ( maximumBet-playersCurrentBet ):
                    if ( Calcstyle.CalcPlayStyle( Raised, this.CurrentRound ) > 0.5 ):
                        if BestHandValue > 0.6:
                            return ClientBase.BettingAnswer.ACTION_CALL 

                else:
                    if( ( Calcstyle.CalcPlayStyle( Raised, self.CurrentRound ) > 0.5 ) ):
                        if BestHandValue > 0.6:
                            return ClientBase.BettingAnswer.ACTION_CALL  

    return ClientBase.BettingAnswer.ACTION_FOLD
    # Random Open Action
    """
    def chooseRaiseOrFold():
        if  _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE,  (random.randint(0, 10) + _minimumAmountToRaiseTo) if _playersCurrentBet+ _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo
        else:
            return ClientBase.BettingAnswer.ACTION_FOLD
    return {
        0: ClientBase.BettingAnswer.ACTION_FOLD,
        1: ClientBase.BettingAnswer.ACTION_ALLIN,
        2: ClientBase.BettingAnswer.ACTION_CALL if _playersCurrentBet + _playersRemainingChips > _maximumBet else ClientBase.BettingAnswer.ACTION_FOLD
    }.get(random.randint(0, 3), chooseRaiseOrFold())
    """
'''
* Modify queryCardsToThrow() and add your strategy to throw cards
* Called during the draw phase of the game when the player is offered to throw away some
* (possibly all) of the cards on hand in exchange for new.
* @return  An array of the cards on hand that should be thrown away in exchange for new,
*          or <code>null</code> or an empty array to keep all cards.
* @see     #infoCardsInHand(ca.ualberta.cs.poker.Hand)
'''
def queryCardsToThrow(_hand):
    print("Requested information about what cards to throw")
    print(_hand)
    CardsThrown = True
    self.NoOfActions=0
    card=[len(CardsThrown)]
    for i in range(len(CardsThrown)):
        card[i]=_hand.getCard( CardsToThrow[i]+1 )
    Evaluated = false
    return _hand[random.randint(0,4)] + ' '

# InfoFunction:

'''
* Called when a new round begins.
* @param round the round number (increased for each new round).
'''
def infoNewRound(_round):
    #_nrTimeRaised = 0
    print('Starting Round: ' + _round )
    currentRound=_round
    del Checkedplayer[:]
    del Raisedplayer[:]

'''
* Called when the poker server informs that the game is completed.
'''
def infoGameOver():
    #retester=tester.OpenCheckRatio(CurrentRound)
    Shankar.Vinay(Players.get(POKER_CLIENT_NAME),Aggresitivity=tester.OpenCheckRatio(CurrentRound))
    print('The game is over.')

'''
* Called when the server informs the players how many chips a player has.
* @param playerName    the name of a player.
* @param chips         the amount of chips the player has.
'''
def infoPlayerChips(_playerName, _chips):
    print('The player ' + _playerName + ' has ' + _chips + 'chips')
    if CurrentRound==1:
        Players.update(_playerName,Shankar.Vinay(_playerName,len(Players)))
        CHIP_VALUE=_chips
    if Players.get(_playerName!=None):
        if _chips==0:
            del Players[_playerName]
            CHIP_VALUE=TOTAL_MONEY/len(Players)
        else:
            Shankar.Vinay(Players.get(_playerName),Chips=_chips)
            Shankar.Vinay(Players.get(_playerName),InRound=True)
'''
* Called when the ante has changed.
* @param ante  the new value of the ante.
'''
def infoAnteChanged(_ante):
    print('The ante is: ' + _ante)

'''
* Called when a player had to do a forced bet (putting the ante in the pot).
* @param playerName    the name of the player forced to do the bet.
* @param forcedBet     the number of chips forced to bet.
'''
def infoForcedBet(_playerName, _forcedBet):
    print("Player "+ _playerName +" made a forced bet of "+ _forcedBet + " chips.")


'''
* Called when a player opens a betting round.
* @param playerName        the name of the player that opens.
* @param openBet           the amount of chips the player has put into the pot.
'''
def infoPlayerOpen(_playerName, _openBet):
    print("Player "+ _playerName + " opened, has put "+ _openBet +" chips into the pot.")
    Shankar.Vinay(Players.get(_playerName),NoOfOpens+1)
    Shankar.Vinay(Players.get(_playerName),LastAction=ClientBase.BettingAnswer.ACTION_OPEN)
    NoOfActions=1
    Raised=Player(Players.get(_playerName))
'''
* Called when a player checks.
* @param playerName        the name of the player that checks.
'''
def infoPlayerCheck(_playerName):
    print("Player "+ _playerName +" checked.")
    Shankar.Vinay(Players.get(_playerName),NoOfChecks+1)
    Shankar.Vinay(Players.get(_playerName),LastAction=ClientBase.BettingAnswer.ACTION_CHECK)
    NoOfActions+1
'''
* Called when a player raises.
* @param playerName        the name of the player that raises.
* @param amountRaisedTo    the amount of chips the player raised to.
'''
def infoPlayerRise(_playerName, _amountRaisedTo):
    print("Player "+_playerName +" raised to "+ _amountRaisedTo+ " chips.")
    Shankar.Vinay(Players.get(_playerName),NoOfRaises+1)
    Players.get(_playerName).LastAction=ClientBase.BettingAnswer.ACTION_RAISE
    NoOfActions = 1
    Raised=Shankar.Vinay(Players.get( playerName ))

'''
* Called when a player calls.
* @param playerName        the name of the player that calls.
'''
def infoPlayerCall(_playerName):
    print("Player "+_playerName +" called.")
    Shankar.Vinay(Players.get(_playerName),NoOfCalls+1)
    Shankar.Vinay(Players.get(_playerName),LastAction=ClientBase.BettingAnswer.ACTION_CALL)
    NoOfActions+1

'''
* Called when a player folds.
* @param playerName        the name of the player that folds.
'''
def infoPlayerFold(_playerName):
    print("Player "+ _playerName +" folded.")
    Shankar.Vinay(Players.get(_playerName ),1)
    Shankar.Vinay(Players.get(_playerName ),False)
    Shankar.Vinay(Players.get(_playerName),ClientBase.BettingAnswer.ACTION_FOLD)
    PlayersFolded+1
'''
* Called when a player goes all-in.
* @param playerName        the name of the player that goes all-in.
* @param allInChipCount    the amount of chips the player has in the pot and goes all-in with.
'''
def infoPlayerAllIn(_playerName, _allInChipCount):
    print("Player "+_playerName +" goes all-in with a pot of "+_allInChipCount+" chips.")
    if Shankar.Vinay(Players.get(_playerName),Shankar.Chips>=Ante):
        Shankar.Vinay(Players.get(_playerName ),Shankar.NoOfAllIns+1)
        Shankar.NoOfActions = 1
        Raised=Shankar.Vinay(Players.get(_playerName ))
        Shankar.Vinay(Players.get(_playerName ),ClientBase.BettingAnswer.ACTION_ALLIN)
    else:
        Shankar.Vinay(Players.get(_playerName ),ClientBase.BettingAnswer.ACTION_OPEN)
'''
* Called when a player has exchanged (thrown away and drawn new) cards.
* @param playerName        the name of the player that has exchanged cards.
* @param cardCount         the number of cards exchanged.
'''
def infoPlayerDraw(_playerName, _cardCount):
    print("Player "+ _playerName + " exchanged "+ _cardCount +" cards.")
    Shankar.Vinay(Players.get(_playerName ),Shankar.CardsThrown== _cardCount)
'''
* Called during the showdown when a player shows his hand.
* @param playerName        the name of the player whose hand is shown.
* @param hand              the players hand.
'''
def infoPlayerHand(_playerName, _hand):
    print("Player "+ _playerName +" hand " + str(_hand))

'''
* Called during the showdown when a players undisputed win is reported.
* @param playerName    the name of the player whose undisputed win is anounced.
* @param winAmount     the amount of chips the player won.
'''
def infoRoundUndisputedWin(_playerName, _winAmount):
    print("Player "+ _playerName +" won "+ _winAmount +" chips undisputed.")

'''
* Called during the showdown when a players win is reported. If a player does not win anything,
* this method is not called.
* @param playerName    the name of the player whose win is anounced.
* @param winAmount     the amount of chips the player won.
'''
def infoRoundResult(_playerName, _winAmount):
    print("Player "+ _playerName +" won " + _winAmount + " chips.")

def infoCardsInHand(hand):
    print("The cards in hand is" + hand + ".")
    self.hand=hand
    BestHandValue = -1
    NoOfActions = 0
    CardsLeft=[52]
    CardRep=CardsLeft
    if self.CurrentRound==1:
        TOTAL_MONEY = CHIP_VALUE * len(Players)
    for i in range(1,5):
        a=hand.getCard( i+1 ).getRank() + ( hand.getCard(i+1).getSuit() * 13)
        CardsLeft[hand.getCard( i+1 ).getRank() + ( hand.getCard( i+1 ).getSuit() * 13 )]=0
        CardRepHand[ i ]=CardRep[hand.getCard( i+1 ).getRank() + ( hand.getCard( i+1 ).getSuit() * 13 )]
    if CardsThrown == true:
        BestHandValue = 1 - Ranker.rank( CardRepHand )/7462.0
    else:
        this.ThrowCalculator()
    Evaluated = true

def ThrowCalculator():
  TempHand = [5]
  Card1 = 0
  Card2 = 0
  Card3 = 0
  Card4 = 0
  Card5 = 0
  CardsToThrowEval=[]
  CardsToThrow = [0]
  Count = 0
  Value

  BestHandValue = 1 - Ranker.rank( CardRepHand )/7462.0

  for i in range(1,32):
    System.arraycopy(CardRepHand, 0, TempHand, 0, 5)
    Card1 =  1 if ( i and 0x1 ) == 0x1 else 0
    Card2 = 1 if (i and 0x2)  == 0x2 else 0
    Card3 = 1 if (i and 0x4)  == 0x4 else 0
    Card4 = 1 if (i and 0x8 ) == 0x8 else 0
    Card5 = 1 if (i and 0x10 ) == 0x10 else 0

    CardsToThrowEval = [ Card1 + Card2 + Card3 + Card4 + Card5 ]
    Count = 0

    if Card1 == 1:
      CardsToThrowEval[ Count ] = 0
      Count+1

    if Card2 == 1:
      CardsToThrowEval[ Count ] = 1
      Count+1
      
    if Card3 == 1 :
      CardsToThrowEval[ Count ] = 2
      Count+1

    if Card4 == 1:
      CardsToThrowEval[ Count ] = 3
      Count+1

    if Card5 == 1:
      CardsToThrowEval[ Count ] = 4

    Value = Evaluate( TempHand, CardsToThrowEval, 0, CardsToThrowEval.length-1 )
    Value /= Bionomial[ CardsToThrowEval.length-1 ]

    if Value > BestHandValue:
      CardsToThrow =[ Card1 + Card2 + Card3 + Card4 + Card5 ]
      System.arraycopy( CardsToThrowEval, 0, CardsToThrow, 0, CardsToThrowEval.length )
      BestHandValue = Value


def Evaluate(TempHand,CardsToThrow,LoopCnt,Depth ):
  Value = 0
  for i in range(LoopCnt,52-Depth):
    while CardsLeft[ i ] == 0:
      i+1
      if i == 52-Depth:
        return Value;

    TempHand[ CardsToThrow[ Depth ] ] = CardsLeft[ i ]

    if Depth > 0:
      Value += Evaluate( TempHand, CardsToThrow, i+1, Depth-1 )

    else:
      Value += ( 1 - Ranker.rank( TempHand )/7462.0 )

  return Value



def PositionScaling(Position ):
  RetVal = ( 1-(Position-1)*0.4/len(Players))

  if RetVal < 0.6 or RetVal > 1:
    return 0
  return RetVal  


            


