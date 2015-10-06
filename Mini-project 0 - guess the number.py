import simplegui
import random

# helper function to start and restart the game
def new_game():
    global secret_number, tries, rang

# global variable rang determines Range

    if rang == 1:									
        print "New game. Range is [0,100)"
        print "Number of remaining guesses is 7"
        print ""
        tries = 7
        secret_number = int(random.randrange(0, 100))
    elif rang == 2:
        print "New game. Range is [0,1000)"
        print "Number of remaining guesses is 10"
        print ""
        tries = 10
        secret_number = int(random.randrange(0, 1000))


# define event handlers for control panel
def range100():
    global rang
    rang = 1	#sets variable rang to 1
    new_game()
    # button that changes the range to [0,100) and starts a new game


def range1000():
    global rang
    rang = 2	#sets variable rang to 2
    new_game()
    # button that changes the range to [0,1000) and starts a new game


def input_guess(guess):
    global secret_number, tries
    
    guess = int(guess)
    tries = tries - 1

    print "Guess was %d" % guess
    print "Number of remaining guesses is %d" % tries
    
    if guess < secret_number:
        print "Higher!"
    elif guess > secret_number:
        print "Lower!"
    else:
        print "Correct!!"
        print ""
        new_game()
    
    print ""
    
    if tries == 0:
        print "No more tries left, starting new game!"
        print ""
        new_game()
        



# frame
f = simplegui.create_frame("Guess the number", 300, 300)
f.add_button("Range is [0,100)", range100)
f.add_button("Range is [0,1000)", range1000)
f.add_input('Value', input_guess, 100)
f.start()


#rang first value
global rang
rang = 1

# call new_game
new_game()
