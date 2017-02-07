#LISTS (35PTS TOTAL)
#In these exercises you write functions. Of course, you should not only write the functions,
#you should also write code to test them. For practice, you should also comment your
#functions as explained above.
#
import random

#PROBLEM 1 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

'''
number = random.randrange(20)
print(str(input("Have a yes or no question? Ask the magic 8 ball! ")))
print(answer_list[number])
'''
# PROBLEM 2 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
import random
suit_list = ["hearts", "diamonds", "clubs", "spades"]
value_list = [2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King", "Ace"]
deck = []

cards = 0
for i in range(1000):
    suit = random.choice(suit_list)
    value = random.choice(value_list)
    card = (value, "of", suit)
    deck.append(card)
    deck.reverse()
    if deck.count(card) == 2:
        deck.pop(0)
        continue
    cards += 1
    if cards == 53:
        break
print(deck)

def shuffled():
    random.shuffle(deck)
    print(deck)
shuffled()



# PROBLEM 3 (The sieve of Eratosthenes - 10pts)
# The sieve of Eratosthenes is a method to find all prime numbers between
# 1 and a given number using a list. This works as follows: Fill the list with the sequence of
# numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime.
# Now loop over the list. Find the next number on the list that is not zero,
# which, at the start, is the number 2. Now set all multiples of this number to zero.
# Then find the next number on the list that is not zero, which is 3.
# Set all multiples of this number to zero. Then the next number, which is 5
# (because 4 has already been set to zero), and do the same thing again.
# Process all the numbers of the list in this way. When you have finished,
# the only numbers left on the list are primes.
# Use this method to determine all the primes between 1 and 1000.

number_list = []
prime_list = []
for i in range(1,1001):
    number_list.append(i)
number_list[0] = 0
print(number_list)
for i in range(len(number_list)):
    if (i + 1) % 2 == 0:
        number_list[i] = 0
        number_list.append(i)

    if (i + 1) % 3 == 0:
        number_list[i] = 0
        number_list.append(i)

    if (i + 1) % 5 == 0:
        number_list[i] = 0
        number_list.append(i)

    if (i + 1) % 7 == 0:
        number_list[i] = 0
        number_list.append(i)

number_list[1] = 2
number_list[2] = 3
number_list[4] = 5
number_list[6] = 7

print(number_list)


# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

# The main program will be something along the lines of (in pseudo-code):
# display board
# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player


#Having a lot of issues with getting each move to show up. The "x" or "o" only appears on the board like half the time. Also a lot of redundancy

row_1 = [4 * " " + "|" + 4 * " " + "|" + 4 * " "]
row_2 = [4 * " " + "|" + 4 * " " + "|" + 4 * " "]
row_3 = [4 * " " + "|" + 4 * " " + "|" + 4 * " "]
def draw_board():

    print(row_1[0])
    print(14 * "-")
    print(row_2[0])
    print(14 * "-")
    print(row_3[0])


    '''
    print(4 * " " + "|" + 4 * " " + "|" + 4 * " ")
    print(4 * " " + "|" + 4 * " " + "|" + 4 * " ")
    print(14 * "-")
    print(4 * " " + "|" + 4 * " " + "|" + 4 * " ")
    print(4 * " " + "|" + 4 * " " + "|" + 4 * " ")
    print(14 * "-")
    print(4 * " " + "|" + 4 * " " + "|" + 4 * " ")
    print(4 * " " + "|" + 4 * " " + "|" + 4 * " ")
    '''


place_list = []
done = False


turns = 0
x_list = []
y_list = []
player = "x"
while True:
    draw_board()
    row = int(input("Enter a row, 1, 2, or 3: "))
    column = int(input("Enter a column, 1, 2, or 3: "))
    place = row, column
    place_list.append(place)
    print(place_list)
    if place_list.count(place) == 1:

        if turns % 2 == 0:
            player = "x"
        if turns % 2 != 0:
            player = "o"
        if place == (1,1):
            row_1 = [2 * " " + player + " " + "|" + 4 * " " + "|" + 4 * " "]
            if player == "x":
                x_list.append(1)
            if player == "y":
                y_list.append(1)
            print(x_list)
        elif place == (1,2):
            row_1 = [4 * " " + "|" + 2 * " " + player + " " + "|" + 4 * " "]
            if player == "x":
                x_list.append(2)
            if player == "y":
                y_list.append(2)
        elif place == (1,3):
            row_1 = [4 * " " + "|" + 4 * " " + "|" + 2 * " " + player + " "]
            if player == "x":
                x_list.append(3)
            if player == "y":
                y_list.append(3)
        elif place == (2,1):
            row_2 = [2 * " " + player + " " + "|" + 4 * " " + "|" + 4 * " "]
            if player == "x":
                x_list.append(4)
            if player == "y":
                y_list.append(4)
        elif place == (2,2):
            row_2 = [4 * " " + "|" + 2 * " " + player + " " + "|" + 4 * " "]
            if player == "x":
                x_list.append(5)
            if player == "y":
                y_list.append(5)
        elif place == (2,3):
            row_2 = [4 * " " + "|" + 4 * " " + "|" + 2 * " " + player + " "]
            if player == "x":
                x_list.append(6)
            if player == "y":
                y_list.append(6)
        elif place == (3,1):
            row_3 = [2 * " " + player + " " + "|" + 4 * " " + "|" + 4 * " "]
            if player == "x":
                x_list.append(7)
            if player == "y":
                y_list.append(7)
        elif place == (3,2):
            row_3 = [4 * " " + "|" + 2 * " " + player + " " + "|" + 4 * " "]
            if player == "x":
                x_list.append(8)
            if player == "y":
                y_list.append(8)
        elif place == (3,3):
            row_3 = [4 * " " + "|" + 4 * " " + "|" + 2 * " " + player + " "]
            if player == "x":
                x_list.append(9)
            if player == "y":
                y_list.append(9)
    if place_list.count(place) != 1:
        print("That has already been done! You lose your turn")

    turns += 1
    if turns == 9:
        print("Tie game! Neither player wins")
        break

    if x_list.count(1) == 1 and x_list.count(2) == 1 and x_list.count(3) == 1:
        print("X WINS!")
        break
    if x_list.count(4) == 1 and x_list.count(5) == 1 and x_list.count(6) == 1:
        print("X WINS!")
        break
    if x_list.count(7) == 1 and x_list.count(8) == 1 and x_list.count(9) == 1:
        print("X WINS!")
        break
    if x_list.count(1) == 1 and x_list.count(4) == 1 and x_list.count(7) == 1:
        print("X WINS!")
        break
    if x_list.count(2) == 1 and x_list.count(5) == 1 and x_list.count(8) == 1:
        print("X WINS!")
        break
    if x_list.count(3) == 1 and x_list.count(6) == 1 and x_list.count(9) == 1:
        print("X WINS!")
        break
    if x_list.count(1) == 1 and x_list.count(5) == 1 and x_list.count(9) == 1:
        print("X WINS!")
        break
    if x_list.count(3) == 1 and x_list.count(5) == 1 and x_list.count(7) == 1:
        print("X WINS!")
        break

    #This is sooooo redundant and I dont really know how to make it quicker right now


#


# CHALLENGE PROBLEM 5 (Battleship NO CREDIT, JUST IF YOU WANT TO TRY IT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
