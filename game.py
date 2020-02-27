'''
Created on Feb 25, 2020

@author: Harshil Sharma, Yajat Ambati

Description: ______

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
    return self.getValue()==other.getValue()
  def __lt__(self,other):
    return self.getValue()<other.getValue()

# make a PokerHand Class
class PokerHand(StackOfCards):
  def handType(self):
    if 
  

# make a PokerPlayer Class
class PokerPlayer(Player):
  def askHoldChoice(self):
    holding=input("What cards do you want to hold (enter with the card's position in your hand like "5 1 2" or just nothing if you want to hold none)?")
    return holding
    
# make a PokerGame function
def PokerGame():
        
    # make the player
    #player = PokerPlayer("Player", 1)
    
    # make a deck of card
    # deck = PokerHand()  # make empty deck
    # add the 52-cards and shuffle
    
    # make rest of the game
    print("Poker Game!! Let's Go!")
    
# add any other helper functions to organize your code nicely
    
def main():
    PokerGame()
    
if __name__ == "__main__":
    main()
    
        

