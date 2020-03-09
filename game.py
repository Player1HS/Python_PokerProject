'''
Created on March 2, 2020
@author: Harshil Sharma, Yajat Ambati
Description: Finished all the minimum required functions and classes. Time for testing and extra features!
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
  # created specific getValue instances for A, Q, K, J
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
  # helps sort the cards, by ranking   
  def __eq__(self,other):
    return self.getValue() == other.getValue()
  def __lt__(self,other):
    return self.getValue() < other.getValue()

# make a PokerHand Class
class PokerHand(StackOfCards):
  def sort(self):
    self.cards.sort()
  def handType(self):
    # getValues of some cards to make code smoother
    plcHoldr = self.getCard(0).getValue()
    spare = self.getCard(4).getValue()
    centr = self.getCard(2).getValue()
    # Check if the suits are the same, so suit specific hand types can be tested
    if self.getCard(0).getSuit() == self.getCard(1).getSuit() and self.getCard(0).getSuit() == self.getCard(2).getSuit() and self.getCard(0).getSuit() == self.getCard(3).getSuit() and self.getCard(0).getSuit() == self.getCard(4).getSuit():
      if self.getCard(0).getValue() == 10 and self.getCard(1).getValue() == 11 and self.getCard(2).getValue() == 12 and self.getCard(3).getValue() == 13 and self.getValue(4).getValue() == 14:
        return "Royal Flush"
      elif self.getCard(1).getValue() == (plcHoldr + 1) and self.getCard(2).getValue() == (plcHoldr + 2) and self.getCard(3).getValue() == (plcHoldr + 3) and self.getCard(4).getValue() == (plcHoldr + 4):
        return "Straight Flush"
      #testing a special case of Straight Flush
      elif self.getCard(0).getValue() == 2 and self.getCard(1).getValue() == 3 and self.getCard(2).getValue() == 4 and self.getCard(3).getValue() == 5 and self.getCard(4).getValue() == 14:
        return "Straight Flush"
    # most of the hand types after are not suit specific (testing 2 cases of Four of a Kind)
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(2).getValue() == plcHoldr and self.getCard(3).getValue() == plcHoldr:
      return "Four of a Kind"
    elif self.getCard(1).getValue() == spare and self.getCard(2).getValue() == spare and self.getCard(3).getValue() == spare:
      return "Four of a Kind"
    #testing 2 cases of Full House
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(2).getValue() == plcHoldr and self.getCard(3).getValue():
      return "Full House"
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(2).getValue() == spare and self.getCard(3).getValue() == spare:
      return "Full House"
    # testiong suits for flush
    elif self.getCard(0).getSuit() == self.getCard(1).getSuit() and self.getCard(0).getSuit() == self.getCard(2).getSuit() and self.getCard(0).getSuit() == self.getCard(3).getSuit() and self.getCard(0).getSuit() == self.getCard(4).getSuit():
      return "Flush"
    elif self.getCard(1).getValue() == (plcHoldr + 1) and self.getCard(2).getValue() == (plcHoldr + 2) and self.getCard(3).getValue() == (plcHoldr + 3) and self.getCard(4).getValue() == (plcHoldr + 4):
      return "Straight"
    #testing special case of straight
    elif self.getCard(0).getValue() == 2 and self.getCard(1).getValue() == 3 and self.getCard(2).getValue() == 4 and self.getCard(3).getValue() == 5 and self.getCard(4).getValue() == 14:
        return "Straight"
    #testing 3 cases of 3 of a kind
    elif self.getCard(0).getValue() == centr and self.getCard(1).getValue() == centr:
      return "3 of a Kind"
    elif self.getCard(1).getValue() == centr and self.getCard(3).getValue() == centr:
      return "3 of a Kind"
    elif self.getCard(3).getValue() == centr and self.getCard(4).getValue() == centr:
      return "3 of a Kind"
    #testing 3 cases of 2 pairs
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(3).getValue() == centr:
      return "Two Pairs"
    elif self.getCard(1).getValue() == plcHoldr and self.getCard(3).getValue() == spare:
      return "Two Pairs"
    elif self.getCard(1).getValue() == centr and self.getCard(3).getValue() == spare:
      return "Two Pairs"
    #testing 4 cases of Jacks or better
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
  #finds out the cards player wants to hold
  def askHoldChoice(self):
    holding = input('''\nWhat cards do you want to hold (enter with the card's position in your hand like "5 1 2" or just nothing if you want to hold none)? ''')
    return holding
  
# make a playRound function
import sys
def playRound(player,deck):
  player.addMoney(-1)
  handlist=[]
  finalhandlist=[]
  holdstr=" "
  for dealcards in range(5):
    handlist=handlist+[deck.deal()]
  handlist.sort()
  print("\nYour hand:",end="\t")
  for card in handlist:
    print(card,end="\t")
  # numbers below the hand to indicate positions
  print("\n\t\t1\t2\t3\t4\t5")
  
  hold=player.askHoldChoice()
  if hold=="":
    print("You held nothing",end="")
    for newhand in range(5):
      finalhandlist.append(deck.deal())
  else:
    print("You held:",end=" ")
    for ch in hold:
      if ch in "12345":
        posinhand=int(ch)-1
        print(handlist[posinhand],end="\t")
        finalhandlist=finalhandlist+[handlist[posinhand]]
    while len(finalhandlist)<5:
      finalhandlist=finalhandlist+[deck.deal()]
  finalhandlist.sort()
  print("\nYour final hand:",end="\t")
  for cards in finalhandlist:
    print(cards,end="\t")
  HAND=PokerHand()
  for card in finalhandlist:
    HAND.add(card)
  print(HAND.handType())
  #in case the player bought alcohol for this round
  if drunk:
    if HAND.handType()=="Royal Flush":
      player.addMoney(500)
      print("You earned 500 credits!")
    elif HAND.handType()=="Straight Flush":
      player.addMoney(100)
      print("You earned 100 credits!")
    elif HAND.handType()=="Four of a Kind":
      player.addMoney(50)
      print("You earned 50 credits!")
    elif HAND.handType()=="Full House":
      player.addMoney(18)
      print("You earned 18 credits!")
    elif HAND.handType()=="Flush":
      player.addmoney(12)
      print("You earned 12 credits!")
    elif HAND.handType()=="Straight":
      player.addMoney(8)
      print("You earned 8 credits!")
    elif HAND.handType()=="3 of a Kind":
      player.addMoney(6)
      print("You earned 6 credits!")
    elif HAND.handType()=="Two Pairs":
      player.addMoney(4)
      print("You earned 4 credits!")
    elif HAND.handType()=="Pair (Jacks or better)":
      player.addMoney(2)
      print("You earned 2 credits!")
    elif HAND.handType()=="Nothing":
      print('''Your hangover was literally "wasted."''')
    drunk=False
  else:
    if HAND.handType()=="Royal Flush":
      player.addMoney(250)
      print("You earned 250 credits!")
    elif HAND.handType()=="Straight Flush":
      player.addMoney(50)
      print("You earned 50 credits!")
    elif HAND.handType()=="Four of a Kind":
      player.addMoney(25)
      print("You earned 25 credits!")
    elif HAND.handType()=="Full House":
      player.addMoney(9)
      print("You earned 9 credits!")
    elif HAND.handType()=="Flush":
      player.addmoney(6)
      print("You earned 6 credits!")
    elif HAND.handType()=="Straight":
      player.addMoney(4)
      print("You earned 4 credits!")
    elif HAND.handType()=="3 of a Kind":
      player.addMoney(3)
      print("You earned 3 credits!")
    elif HAND.handType()=="Two Pairs":
      player.addMoney(2)
      print("You earned 2 credits!")
    elif HAND.handType()=="Pair (Jacks or better)":
      player.addMoney(1)
      print("You earned 1 credit!")
  
  if player.money<=0:
      print("You went bankrupt!")
      newround=False
      sys.exit()
  else:
      print("Your credits:",player.money)
    
# make a PokerGame function
def PokerGame():
  print("Welcome to Video Poker!")

  #introduction to the game
  name=input("\nEnter your name: ")
  print("Hello, %s" % (name))
  money=int(input("How many credits would you like to start with? "))
  
  #creation of a deck
  deck = PokerHand()
  for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
    for suit in ['♥', '♦', '♣', '♠']:
       newCard = PokerCard(rank, suit)
       deck.add(newCard)

  #creation of a player
  player = PokerPlayer(name, money, deck)

  #function to make the user "keep playing"
  def keepplaying():
    newround=True
    while newround:
      deck.shuffle()
      playRound(player, deck)
      playagain=input("What would you like to do next (shop, new round, or quit)? ")
      if playagain.lower()=="new round":
        newround=True
      elif playagain.lower()=="shop":
        shop()
      else:
        print("See you soon!")
        newround=False
        sys.exit()

  #a game shop
  def shop():
    print("\n-----------SHOP-----------")
    print("Alcohol - 15 credits")
    print("Cheeseburger - 20 credits")
    print("Poker Trophy - 1000 credits")
    answers()

  #a function that analyzes the player's possible inputs for what to do next
  def answers():
      ans=input("\nWhat would you like to do next? (new round, info [item], buy [item], quit) ")
      if ans.lower()=="info alcohol":
        print("Doubles your winnings for the next round. Costs 15 credits.")
        answers()
      elif ans.lower()=="info cheeseburger":
        print("A delicious snack. Costs 20 credits.")
        answers()
      elif ans.lower()=="info poker trophy":
        print("A reward for only the best Poker players.")
        answers()
      elif ans.lower()=="quit":
        print("See you soon!")
        sys.exit()
      elif ans.lower()=="new round":
        keepplaying()
      elif ans.lower()=="buy alcohol":
        player.addMoney(-15)
        drunk=True
        answers()
      elif ans.lower()=="buy cheeseburger":
        player.addMoney(-20)
        print("You ate a cheeseburger. Yummy!")
        answers()
      elif ans.lower()=="buy poker trophy":
        player.addMoney(-1000)
        print("You are hailed as the greatest Poker player in the land... and you live happily ever after")
        sys.exit() #buying a trophy will allow the player to "beat" the game
  
  drunk=False
  keepplaying()
  answers()

def main():
    PokerGame()
    
if __name__ == "__main__":
    main()
    
PokerGame()
