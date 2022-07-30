# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:41:40 2022

@author: evanq
"""
import random
import matplotlib.pyplot as plt

#52 of these with unique suits and values will be used for the deck. 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def display(self):
        suit = self.suit
        value = self.value
        if value == 1:
            value = "A"
        if value == 11:
            value = "J"
        if value == 12:
            value = "Q"
        if value == 13:
            value = "K"
        print("{} of {}s".format(value, suit))
        
#contains our deck[] of Cards and the methods (and loop) for shuffling,
#dealing, counting two, three, and four-of-a-kinds, and counting total
#number of deals.
class Deck:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.deals = 0
        self.doubles = 0
        self.triples = 0
        self.quadruples = 0
        self.build()
        
    #prints out counters, plots a pie graph
    def showCount(self):
        print("-------------")
        print(" The counts:")
        print("-------------")
        print("Total deals: {}".format(self.deals))
        print("Doubles: {}".format(self.doubles))
        print("Triples: {}".format(self.triples))
        print("Quadruples: {}".format(self.quadruples))
        pieList = ["None","Three-of-a-kind","Two-of-a-kind","Four-of-a-kind"]
        pieValues = []
        pieValues.append((self.doubles + self.triples + self.quadruples)/self.deals)
        pieValues.append(self.triples/self.deals)
        pieValues.append(self.doubles/self.deals)
        pieValues.append(self.quadruples/self.deals)
        pieColors = ["g", "y", "b", "r"]
        plt.pie(pieValues, labels=pieList, colors=pieColors, 
        startangle=90, shadow = True, explode = (0.1, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
                 
    #prints the deck out in whatever order it's in, used in testing
    def showDeck(self):
        for i in range(52):
            suit = self.deck[i].suit
            value = self.deck[i].value
            if value == 1:
                value = "A"
            if value == 11:
                value = "J"
            if value == 12:
                value = "Q"
            if value == 13:
                value = "K"
            print("{} of {}s".format(value, suit))
             
    #prints out the hand, used in testing    
    def showHand(self):
        size = len(self.hand)
        print("-------------")
        print(" Your cards:")
        print("-------------")
        for i in range(size):
            suit = self.hand[i].suit
            value = self.hand[i].value
            if value == 1:
                value = "A"
            if value == 11:
                value = "J"
            if value == 12:
                value = "Q"
            if value == 13:
                value = "K"
            print("{} of {}s".format(value, suit))
            
    #when the deck is initialized, this fills the deck[] with 13 of each suit
    def build(self):
        for suit in ["Heart", "Diamond", "Club", "Spade"]:
            for value in range(13):
                self.deck.append(Card(suit, value + 1))            
    
    #simply shuffles deck[]
    def shuffle(self):
        return random.shuffle(self.deck)
        
    #empties hand[], then copies the first 5 index's of deck[] into hand[]
    def deal(self):
        self.hand = []
        for i in range(5):
            self.hand.append(self.deck[i])
            
    #counts duplicates and adds to the counters as needed
    def addHandtoCount(self):
        #this is used to generalize the counting method, although I did not
        #generalize the deal method 
        size = len(self.hand)
        
        #this for loop compares the index i with the rest of the indexes
        #j. j will never be less than i and will never exceed the size of the
        #hand, i will never reach the last index of the hand. in this way 
        #doubles wont be counted more than once and triples and quadruples will
        #predictably raise the counter of the one below it, allowing us to 
        #correct for it easily
        for i in range(size-1):
            counter = 1
            for j in range(size-1-i):
                j = j + 1 + i
                if self.hand[i].value == self.hand[j].value:
                    counter += 1   
            if counter == 2:
                self.doubles += 1
            if counter == 3:
                self.doubles -= 1
                self.triples += 1
            if counter == 4:
                self.triples +- 1
                self.quadruples += 1

    #this loop uses the other functions to shuffle, deal, and count a specified
    #number of times
    def dealHands(self, num):
        for i in range(num):
            self.shuffle()
            self.deal()
            self.addHandtoCount()
            self.deals += 1

def main():
   deck = Deck()
   deck.dealHands(12345)
   deck.showCount()
   
if __name__ == '__main__':
    main()
                    