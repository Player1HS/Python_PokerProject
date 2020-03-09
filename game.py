class Card:
    
    SUIT = ['♥', '♦', '♣', '♠']
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    # Returns a numerical value for cards 1-13 dependistack_of_cards the rank of the card
    def getValue(self):
        if self.rank == 'A':
            return(1)
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
    
    
    def getRank(self):   
        return(self.rank)
    
    def getSuit(self):   
        return(self.suit)
    
    def __str__(self):
        return('{}{}'.format(self.rank, self.suit)) 

class Player:

    # inputs:
    #    name - string for the player's name
    #    amount - integer for how much money the player has
    #    cards - a StackOfCards
    def __init__(self, name, amount, cards):
        '''
        Constructor
        '''
        self.name = name
        self.money = amount
        self.hand = cards
     
    # prints out name and the hand of stack_of_cards    
    def __str__(self):
        return("{}: {}".format(self.name, self.hand))
    
    def introduce(self):
        print("Hi, my name is {}".format(self.name))
        
    def getName(self):
        return(self.name)
    
    def getMoney(self):
        return self.money

    # add (or subtract) player's money    
    def addMoney(self, amount):
        self.money += amount
    
    # when player given another card, add it it player's hand    
    def addCard(self, card):
        self.hand.add(card)
        
    def getCard(self, pos):
        return self.hand.getCard(pos)
    
    def removeCard(self, pos):
        return self.hand.remove(pos)

import random


#===========================================================================
# Description: A list of Card; used for a player's hand or a deck of cards
#
# State Attributes
#     - cards - list of card; starts out empty
# Methods
#     - shuffle() - randomly shuffle all the card in the list
#     - deal() - deal the 'top' card from the hand/deck
#     - add(card) - add Card to the list of cards
#     - remove(pos) - remove and return Card at pos number
#     - size() - size of hand
#     - getCard(pos) - returns a Card at the 'pos'
#     - __str__() - returns string of all the cards in the hand like '4♣ 10♥ A♠'
#===========================================================================
class StackOfCards:

    def __init__(self):
        '''
        Constructor
        '''
        self.cards = []
        
    # returns a string of all the cards in the 'deck'
    def __str__(self):
        s = ''
        for card in self.cards:
            if len(s) == 1:
                s = s + str(card)
            else:
                s = s + ' ' + str(card)
        s = s
        return(s)
    
    # Add card to the 'bottom' of the deck of cards
    def add(self, card):
        self.cards.append(card)
                
    def remove(self, pos):
        card = self.cards.pop(pos)
        return card
               
    # Deal card from the 'top' of the deck of cards
    def deal(self):
        return self.cards.pop(0)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def size(self):
        return(len(self.cards))
    
    def getCard(self, pos):
        return(self.cards[pos])






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
    plcHoldr = self.getCard(0).getValue()
    spare = self.getCard(4).getValue()
    centr = self.getCard(2).getValue()
    if self.getCard(0).getSuit() == self.getCard(1).getSuit() and self.getCard(0).getSuit() == self.getCard(2).getSuit() and self.getCard(0).getSuit() == self.getCard(3).getSuit() and self.getCard(0).getSuit() == self.getCard(4).getSuit():
      if self.getCard(0).getValue() == 10 and self.getCard(1).getValue() == 11 and self.getCard(2).getValue() == 12 and self.getCard(3).getValue() == 13 and self.getValue(4).getValue() == 14:
        return "Royal Flush"
      elif self.getCard(1).getValue() == (plcHoldr + 1) and self.getCard(2).getValue() == (plcHoldr + 2) and self.getCard(3).getValue() == (plcHoldr + 3) and self.getCard(4).getValue() == (plcHoldr + 4):
        return "Straight Flush"
      elif self.getCard(0).getValue() == 2 and self.getCard(1).getValue() == 3 and self.getCard(2).getValue() == 4 and self.getCard(3).getValue() == 5 and self.getCard(4).getValue() == 14:
        return "Straight Flush"
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(2).getValue() == plcHoldr and self.getCard(3).getValue() == plcHoldr:
      return "Four of a Kind"
    elif self.getCard(1).getValue() == spare and self.getCard(2).getValue() == spare and self.getCard(3).getValue() == spare:
      return "Four of a Kind"
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(2).getValue() == plcHoldr and self.getCard(3).getValue():
      return "Full House"
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(2).getValue() == spare and self.getCard(3).getValue() == spare:
      return "Full House"
    elif self.getCard(0).getSuit() == self.getCard(1).getSuit() and self.getCard(0).getSuit() == self.getCard(2).getSuit() and self.getCard(0).getSuit() == self.getCard(3).getSuit() and self.getCard(0).getSuit() == self.getCard(4).getSuit():
      return "Flush"
    elif self.getCard(1).getValue() == (plcHoldr + 1) and self.getCard(2).getValue() == (plcHoldr + 2) and self.getCard(3).getValue() == (plcHoldr + 3) and self.getCard(4).getValue() == (plcHoldr + 4):
      return "Straight"
    elif self.getCard(0).getValue() == 2 and self.getCard(1).getValue() == 3 and self.getCard(2).getValue() == 4 and self.getCard(3).getValue() == 5 and self.getCard(4).getValue() == 14:
        return "Straight"
    elif self.getCard(0).getValue() == centr and self.getCard(1).getValue() == centr:
      return "3 of a Kind"
    elif self.getCard(1).getValue() == centr and self.getCard(3).getValue() == centr:
      return "3 of a Kind"
    elif self.getCard(3).getValue() == centr and self.getCard(4).getValue() == centr:
      return "3 of a Kind"
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(3).getValue() == centr:
      return "Two Pairs"
    elif self.getCard(1).getValue() == centr and self.getCard(3).getValue() == spare:
      return "Two Pairs"
    elif plcHoldr > 10 and plcHoldr == self.getCard(1).getValue():
      return "Pair (Jacks or better)"
    elif centr > 10 and centr == self.getCard(1).getValue():
      return "Pair (Jacks or better)"
    elif centr > 10 and centr == self.getCard(3).getValue():
      return "Pair (Jacks or better)"
    elif spare > 10 and spare == self.getCard(3).getValue():
      return "Pair (Jacks or better)"
    else:
      return "Nothing"
# make a PokerPlayer Class
class PokerPlayer(Player):
  def askHoldChoice(self):
    holding = input('''\nWhat cards do you want to hold (enter with the card's position in your hand like "5 1 2" or just nothing if you want to hold none)? ''')
    return holding
  
# make a playRound function
import sys
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
        holdstr=holdstr+str(ch)
    for i in range(1,6):
      if str(i) not in holdstr:
        handlist.pop(i)
        handlist.append(deck.deal())
  handlist.sort()
  print("\nYour final hand:",end=" ")
  for cards in handlist:
    print(cards,end="\t")
  HAND=PokerHand()
  for card in handlist:
    HAND.add(card)
  print(HAND.handType())
  if HAND.handType()=="Royal Flush":
    player.addMoney(250)
  elif HAND.handType()=="Straight Flush":
    player.addMoney(50)
  elif HAND.handType()=="Four of a Kind":
    player.addMoney(25)
  elif HAND.handType()=="Full House":
    player.addMoney(9)
  elif HAND.handType()=="Straight":
    player.addMoney(4)
  elif HAND.handType()=="3 of a Kind":
    player.addMoney(3)
  elif HAND.handType()=="Two Pairs":
    player.addMoney(2)
  elif HAND.handType()=="Straight Flush":
    player.addMoney(50)
  elif HAND.handType()=="Pair (Jacks or better)":
    player.addMoney(1)
  if player.money==0:
    print("You went bankrupt!")
    newround=False
    sys.exit()
  else:
    print("Your credits:",player.money)
    
# make a PokerGame function
def PokerGame():
  print("Welcome to Video Poker!")
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
      print("See you soon!")
      newround=False

def main():
    PokerGame()
    
if __name__ == "__main__":
    main()
    
PokerGame()
