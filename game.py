'''
Created on Feb 28, 2020
@author: Harshil Sharma, Yajat Ambati
Description: Finished all 3 base classes (PokerCard, PokerHand, & PokerPlayer)
'''
from card import Card
from stack_of_cards import StackOfCards
from player import Player

# These are the winning hands in order of strength
WINNING_HANDS = [ "Royal Flush", \
                  "Straight Flush", \
                  "Four of a Kind", \
                  "Full House", \
                  "Flush", \
                  "Straight", \
                  "3 of a Kind", \
                  "Two Pairs", \
                  "Pair (Jacks or better)" ]

# make a PokerCard Class inherit from Card
class PokerCard(Card):
  def getValue(self):
        if self.rank == 'A':
            return(14)
        elif self.rank == 'J':
            return(11)
        elif self.rank == 'Q':
            return(12)
        elif self.rank == 'K':
            return(13)
        elif self.rank in '23456789' or self.rank == '10':
            return(int(self.rank))
        else:
            raise ValueError('{} is of unkwown value'.format(self.rank))
  def __eq__(self,other):
    return self.getValue() == other.getValue()
  def __lt__(self,other):
    return self.getValue() < other.getValue()

# make a PokerHand Class
class PokerHand(StackOfCards):
  def sort(self):
    self.cards.sort()
  def handType(self):
    plcHoldr = self[0].getValue()
    spare = self[4].getValue()
    centr = self[2].getValue()
    if self[0].suit() == self[1].suit() and self[0].suit() == self[2].suit() and self[0].suit() == self[3].suit() and self[0].suit() == self[4].suit():
      if self[0].getValue() == 10 and self[1].getValue() == 11 and self[2].getValue() == 12 and self[3].getValue() == 13 and self[4].getValue() == 14:
        return "Royal Flush"
      elif self[1].getValue() == (plcHoldr + 1) and self[2].getValue() == (plcHoldr + 2) and self[3].getValue() == (plcHoldr + 3) and self[4].getValue() == (plcHoldr + 4):
        return "Straight Flush"
      elif self[0].getValue() == 2 and self[1].getValue() == 3 and self[2].getValue() == 4 and self[3].getValue() == 5 and self[4].getValue() == 14:
        return "Straight Flush"
    elif self[1].getValue() == plcHoldr and self[2].getValue() == plcHoldr and self[3].getValue() == plcHoldr:
      return "Four of a Kind"
    elif self[1].getValue() == spare and self[2].getValue() == spare and self[3].getValue() == spare:
      return "Four of a Kind"
    elif self[1].getValue() == plcHoldr and self[2].getValue() == plcHoldr and self[3].getValue() == spare:
      return "Full House"
    elif self[1].getValue() == plcHoldr and self[2].getValue() == spare and self[3].getValue() == spare:
      return "Full House"
    elif self[0].suit() == self[1].suit() and self[0].suit() == self[2].suit() and self[0].suit() == self[3].suit() and self[0].suit() == self[4].suit():
      return "Flush"
    elif self[1].getValue() == (plcHoldr + 1) and self[2].getValue() == (plcHoldr + 2) and self[3].getValue() == (plcHoldr + 3) and self[4].getValue() == (plcHoldr + 4):
      return "Straight"
    elif self[0].getValue() == 2 and self[1].getValue() == 3 and self[2].getValue() == 4 and self[3].getValue() == 5 and self[4].getValue() == 14:
        return "Straight"
    elif self[0].getValue() == centr and self[1].getValue() == centr:
      return "3 of a Kind"
    elif self[1].getValue() == centr and self[3].getValue() == centr:
      return "3 of a Kind"
    elif self[3].getValue() == centr and self[4].getValue() == centr:
      return "3 of a Kind"
    elif self[1].getValue() == plcHoldr and self[3].getValue() == centr:
      return "Two Pairs"
    elif self[1].getValue() == centr and self[3].getValue() == spare:
      return "Two Pairs"
    elif plcHoldr > 10 and plcHoldr == self[1].getValue():
      return "Pair (Jacks or better)"
    elif centr > 10 and centr == self[1].getValue():
      return "Pair (Jacks or better)"
    elif centr > 10 and centr == self[3].getValue():
      return "Pair (Jacks or better)"
    elif spare > 10 and spare == self[3].getValue():
      return "Pair (Jacks or better)"
    else:
      return "Nothing"
# make a PokerPlayer Class
class PokerPlayer(Player):
  def askHoldChoice(self):
    holding = input('''\nWhat cards do you want to hold (enter with the card's position in your hand like "5 1 2" or just nothing if you want to hold none)? ''')
    return holding
  
# make a playRound function
def playRound(player,deck):
  player.addMoney(-1)
  handlist=[]
  holdstr=" "
  for dealcards in range(5):
    handlist=handlist+[deck.deal()]
  handlist.sort()
  print("Your hand:",end=" ")
  for card in handlist:
    print(card,end="\t")
  hold=player.askHoldChoice()
  if hold=="":
    print("You held nothing")
    for idx in range(5):
      handlist.pop(idx)
      handlist.append(deck.deal())
  else:
    print("You held:",end=" ")
    for ch in hold:
      if ch in "12345":
        posinhand=int(ch)-1
        print(handlist[posinhand],end="\t")
        holdstr=holdstr+str(posinhand)
    for ch in hold:
      if ch not in holdstr:
        handlist.pop(int(ch))
        handlist.append(deck.deal())
  handlist.sort()
  print("\nYour final hand:",end=" ")
  for cards in handlist:
    print(cards,end="\t")
  HAND=PokerHand()
  for card in handlist:
    HAND.add(card)
  print(HAND.handType())
  print("Your credits:",player.money)
    
# make a PokerGame function
def PokerGame():
  print("Poker Game!! Let's Go!")
  newround=True
  #introduction
  name=input("Enter your name: ")
  print("Hello, %s" % (name))
  money=int(input("How many credits would you like to start with? "))
  
  #make deck
  deck = PokerHand()
  for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
    for suit in ['♥', '♦', '♣', '♠']:
       newCard = PokerCard(rank, suit)
       deck.add(newCard)
  deck.shuffle()

  #make player
  player = PokerPlayer(name, money, deck)

  while newround:
    playRound(player, deck)
    playagain=input("Would you like to play again? (y/n)")
    if playagain=="y":
      newround=True
    else:
      newround=False
# add any other helper functions to organize your code nicely, ADD MAIN FUNCTION
    
PokerGame()
