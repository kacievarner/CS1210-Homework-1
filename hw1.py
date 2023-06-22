# CS1210 Homework1
#
# This file should contain only your own work; there are no partners
# assigned or permitted for Homework assignments.
#
# I certify that the entirety of this file contains only my own work.
# I have not shared the contents of this file with anyone in any form,
# nor have I obtained or included code from any other source aside
# from the code contained in the original homework template file.
from random import randint

######################################################################
# Edit the following function definition so it returns a tuple
# containing a single string, your hawkid.
#
# THE AUTOGRADER WILL FAIL TO ASSIGN A GRADE IF YOUR HAWKID IS NOT
# PROPERLY INCLUDED IN THIS FUNCTION. CAVEAT EMPTOR.
######################################################################
def hawkid():
    return(("kvarnr",))

######################################################################
# createDeck() produces a new, cannonically ordered, |S|*N card
# deck. A deck is implemented as a list of cards: each card is a
# tuple, (v, s), where 0 < v < N is the value of the card and s is the
# suit of the card. So, for example:
#
# >>> createDeck(1)
# [(1, 'spades'), (1, 'hearts'), (1, 'clubs'), (1, 'diamonds')]
# >>> createDeck(2)
# [(1, 'spades'), (2, 'spades'), (1, 'hearts'), (2, 'hearts'), (1, 'clubs'), (2, 'clubs'), (1, 'diamonds'), (2, 'diamonds')]
# >>> createDeck()
# [(1, 'spades'), (2, 'spades'), (3, 'spades'), ... (12, 'diamonds'), (13, 'diamonds')]
#
# where the second example above has been edited for clarity. Note
# that the default, N=13, is to produce a standard 52 card deck having
# the standard four suits specified in the function signature.
def createDeck(N=13, S=('spades', 'hearts', 'clubs', 'diamonds')):
    return[(i,j) for i in range(1,N+1) for j in S]              #Creates a list of tuples containing an int 1-13 and one of the four suites

######################################################################
# Construct the representation of a given card using special unicode
# characters for hearts, diamonds, clubs, and spades.
#
# This function is provided for you; it need not be changed.
def displayCard(c):
    suits = {'spades':'\u2660', 'hearts':'\u2661', 'diamonds':'\u2662', 'clubs':'\u2663'}
    return(''.join( [ str(c[0]), suits[c[1]] ] ))               

######################################################################
# simpleShuffle(D) takes a deck, D, and modifies it to scramble the
# order of the cards. There is a significant literature on
# constructing "fair" random permutations of a sequence; what we are
# after here is simple to implement but may not be entirely fair (for
# an example of a fair shuffling algorithm, see the Fisher-Yates-Knuth
# algorithm).
#
# simpleShuffle(D) takes as input list of elements. It should step
# through the list, at each point exchanging the current element with
# an element chosen at random from the remainder of the list
# (including the present element). In other words, if we are
# considering the 3rd element of a 10 element list (0-indexed as
# usual), we select an index between 3 and 9, inclusive, and exchange
# list[3] with list[0] before advancing to the 4th element of the list
# and repeating the process.
#
# simpleShuffle(D) should return the permuted deck.
#
# Note that you will need to use the randint() function, which has
# been imported for you from the random module at the top of this
# file.
def simpleShuffle(D):
    for i in range(len(D)-1):   #Selects the numbers from i to the length of the deck minus 1
        x = randint(i,len(D)-1) #Assigns x to be a random int between i and the deck length - 1
        D[i],D[x] = D[x],D[i]   #Takes the deck indexted at both the i and x positions and flips them around
                                    #in turn shuffling the deck
    return D                    #Returns the shuffled deck
    
######################################################################
# A game is represented as a dictionary with keys:
#   stacks = list of player stacks, where each stack is a list of cards
#   table = list of cards currently on table (initially [])
#   next = index of player next to play (0 or 1, initially 0)
#   debt = penalty cards owed by next player (initially 0)
#
# newGame() should first create a new shuffled deck using createDeck()
# and simpleShuffle().  It should then return a dictionary describing
# the initial state of the current game, where the shuffled deck has
# been evenly divided amongst the players. So, for example (linefeed
# added for clarity):
#
# >>> newGame(2, S=('spades', 'hearts'))
# { 'table':[], 'next':0, 'debt':0,
#   'stacks':[[(2, 'spades'), (1, 'hearts')], [(2, 'hearts'), (1, 'spades')]]}
#
# Note the division of the shuffled deck into two equal stacks, one
# for player 0 and one for player 1.
def newGame(N=13, S=('spades', 'hearts', 'clubs', 'diamonds')):
    D = createDeck(N, S)    #Assigns D to create a deck using given numbers and suits
    D = simpleShuffle(D)    #Assigns D to be the deck created in the last line, but the shuffled version
    return {'table':[], 'next':0, 'debt':0,
            'stacks': [D[:len(D)//2], D[len(D)//2:]]} #Returns empty / 0 values to start the new game
                                                      #'stacks' splits the deck (D) in half and gives player
                                                      #0 the first half of the deck, and player 1 the 2nd half

######################################################################
# describeGame(G) takes a game description G (a dictionary of the type
# produced by newGame()) and returns a string that, when printed,
# describes the state of the game. 
#
# >>> G = newGame(2, S=('spades', 'hearts'))
# >>> describeGame(G)
# 'Player:0 Stacks:[2, 2] Table:0 Debt:0'
#
# The string or description returned is quite terse; it will still be
# useful in helping you debug how the game is progressing. It tells
# you who the next player to play is, what the sizes of the individual
# player stacks are, the number of cards on the table, and any debt
# that is due from the next player to play.
def describeGame(G):
    return ('Player:' + str(G['next']) + ' Stacks:' + str([len(G['stacks'][0]), len(G['stacks'][1])]) #Returns updated game positions by indexing the dictionary
           + ' Table:' + str(len(G['table'])) + ' Debt:' + str(G['debt']))                            #at specific keywords
######################################################################
# current(G) should take a game description G (a dictionary of the
# type produced by newGame()) and return the index of the player who
# is currently playing (indicated by the G['next'] value).
def current(G):
    return(G['next']) #Returns the current value of 'next' in dictionary G

# opponent(G) should take a game description G (a dictionary of the
# type produced by newGame()) and return the index of the player who
# is not currently playing (hint: an appropriate solution might employ
# the % operator).
def opponent(G):
    return(3%(G['next']+2)) #Mods the value of G at 'next' + 2 to return the number of the player that is not currently playing (ie. player 0 or 1)

# advancePlayer(G) should take a game description G (a dictionary of 
# the type produced by newGame()) and modify G so as to "flip" the 
# next player field. So if the next player was player 0, it should now
# become player 1 and vice versa (hint: make use of the opponent(G)
# function just implemented).
def advancePlayer(G):
    G['next'] = opponent(G) #Converts the current player (G['next']) into the opponent
    return G

######################################################################
# Plays the game until a winner emerges. By default, generates a new
# game with all default values for, e.g., deck size and suits.
#
# A skeleton of this function is provided so that you don't get too
# confused. Essentially, we iterate forever using a while loop
# (unbounded iteration) with each iteration representing a player's
# turn. Successive iterations should "flip" the current player in the
# game structure, representing alternating player turns. Each act of
# game play should modify the game structure, G, that keeps track of
# the state of play. The game ends when the next player to move has no
# cards in his/her stack. At this point the game is over, and the
# other player wins.
#
# If there were no penalties, this function would be quite
# straightforward. The game would simply consist of the two players
# taking turns adding cards to the center of the table.
#
# With penalties, of course, it changes the flow of the game. Once you
# recognize that a penalty card has been played, you should
# immediately mark a "debt" in the current game structure, then
# terminate the present iteration and execute the other player's turn.
# If a "debt" is present at the beginning of the player's turn, they
# will have to "pay their debt" which may involve adding multiple
# cards to the table. Once the debt is paid, the cards are removed
# from the table, added to the other player's stack, who then takes
# his/her turn by playing a card to the table.
#
# Note that penalty cards that are played while "paying a debt"
# abrogate the remainder of the debt and impose a new debt on the
# other player.
#
# Note also that if a player runs out of cards while paying a debt,
# he/she loses the game.
def play(G=newGame()):

    turn = 0
    penalty = {1:4, 11:1, 12:2, 13:3}               #Assigns penalty a dictionary of keys as the cards, and values as the debt value of those cards
   
    while len(G['stacks'][current(G)]) > 0:         #While the current players stack of cards is greater than 0
        print("Turn {}: {}".format(turn, describeGame(G))) #Print the turn number and state of the game
        if G['debt'] > 0:                           #If there is a debt greater than 0
            print("Turn {}: Player {} is paying a debt.".format(turn, current(G))) #Print the turn and how much the debt is
            G['table'].append((G['stacks'][current(G)]).pop(0)) #Puts the top card of the person that owes the debt onto the table
            i = G['table'][-1]                      #Assigns i to the last card that was put on the table
            print(displayCard(i))                   #Prints the last card
            if i[0] in penalty:                     #If the last card that was put on the table while paying the debt was a penalty card
                G['debt'] = penalty[i[0]]           #Change the debt to encompass the new penalty
                if len(G['stacks'][current(G)]) != 0:#If the current players' stack is not 0
                    advancePlayer(G)                #Resume regular gameplay
            else:
                G['debt'] = G['debt'] - 1           #If the last card put on the table while paying the debt wasn't a penalty card then subtract 1 from the debt counter
                if G['debt'] == 0:                   #If there is no debt
                    if len(G['stacks'][current(G)]) != 0:#and if the current player has no debt and their stack does not equal 0 cards
                        advancePlayer(G)            #Continue normal play
                    G['stacks'][current(G)] = G['stacks'][current(G)] + (G['table'])#Else add the table cards to the current players stack
                    G['table'] = []                 #Sets table to empty
        else:
            print("Turn {}: Player {}...".format(turn, current(G)))
            G['table'].append((G['stacks'][current(G)]).pop(0))
            i = G['table'][-1]                      #Sets i to the last value that was played in the table
            print(displayCard(i))                   #Prints the last card that was flipped onto the table
            if i[0] in penalty:                     #If i was a penalty card then...
                G['debt'] = penalty[i[0]]           #Change the debt to the value of the penalty
                advancePlayer(G)                    #Then resume normal gameplay
            else:
                advancePlayer(G)                    #If i is not a penalty card then continue normal gameplay
        turn = turn + 1                             #Adds 1 to the turn counter 
    print("Player {} wins in {} turns.".format(opponent(G), turn)) #Prints a string saying which player won and in how many turns
    return(G)                                       #Returns the game dictionary
