import random
import time


# list of 10 three-word quotes
quotes_list = [
    ['always', 'be', 'yourself'],
    ['keep', 'it', 'cool'],
    ['dream', 'big', 'achieve'],
    ['love', 'laugh', 'live'],
    ['never', 'give', 'up'],
    ['learn', 'grow', 'evolve'],
    ['stay', 'true', 'you'],
    ['live', 'love', 'laugh'],
    ['life', 'is', 'beautiful'],
    ['think', 'positive', 'thoughts']
]


def random_quote(quotes_list):
    """
    this function randomizes a number in range of the length of the quotes_list
    """
    random_index = random.randrange(0, len(quotes_list))
    return quotes_list[random_index]


def create_new_list(quote):
    """
    this function creates a list with underscores for each word in the quote
    """
    guess = []
    for word in quote:
        guess.append('_' * len(word))
    return guess


def update_new_list(new_list, quote, letter):
    """
    this function updates the hidden list with the guessed letter at the specified indexes
    """
    for i in range(len(quote)):
        for j in range(len(quote[i])):
            if quote[i][j] == letter:
                # if the condition is True split the current word and add the letter
                # in the index it should be and then add the rest of the word to it
                new_list[i] = new_list[i][:j] + letter + new_list[i][j+1:]
    return new_list


def game():
    """
    this function is the main code game
    """
    # creating an empty list that will contain all the user's guesses
    guesses_list = []
    # randomizing one quote using random_quote function
    quote = random_quote(quotes_list)
    # creating a new underscore list for the user
    # using the create_new_list function
    new_list = create_new_list(quote)
    correct_guesses = 0
    wrong_guesses = 0
    print("Welcome to the Guess-the-Word game!")
    print("Try to guess the three-word quote:")
    # starting the timer
    start_time = time.time()
    # the loop will keep going as long as the new_list
    # is not filled with the entire quote
    while quote != new_list:
        print(new_list)
        guess = input("Enter a letter: ").lower()
        # updating the underscore list using the update_new_list function
        update_new_list(new_list, quote, guess)
        # if the user's guess is not in the guesses list and the user's guess exists in the new_list
        if guess not in ' '.join(guesses_list) and guess in ' '.join(new_list):
            # add the guess into the guess list
            guesses_list.append(guess)
            # the user gets 5 points
            correct_guesses += 5
        else:
            # the user loses 1 point
            wrong_guesses -= 1
    # getting the score conclusion
    total_points = correct_guesses + wrong_guesses
    # ending the timer
    end_time = time.time()
    # getting the total time
    total_time = end_time - start_time
    # if the user won in less than 30 seconds
    if total_time < 30:
        # the user gets 100 points more
        total_points += 100
    print(f"Congratulations! You guessed the quote!, the quote is {new_list}")
    print(f"Total points: {total_points}")


game()
