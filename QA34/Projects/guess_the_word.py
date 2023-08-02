import random
import time
# List of 10 three-word quotes
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
    # Randomize a number in range of the length of the quotes_list
    random_index = random.randrange(0, len(quotes_list))
    print(quotes_list[random_index])    # using it only to check
    return quotes_list[random_index]

def create_new_list(quote):
    guess = []
    # Create a list with underscores for each word in the quote
    for word in quote:
        guess.append('_' * len(word))
    return guess

def update_new_list(new_list, quote, letter):
    # Update the hidden list with the guessed letter at the specified indexes
    for i in range(len(quote)):
        for j in range(len(quote[i])):
            if quote[i][j] == letter:
                # if the condition is True split the current word and add the letter
                # in the index it should be and than add the rest of the word to it
                new_list[i] = new_list[i][:j] + letter + new_list[i][j+1:]
    return new_list

def game():
    # Playing the game
    guesses_list = []
    quote = random_quote(quotes_list)
    new_list = create_new_list(quote)
    correct_guesses = 0
    wrong_guesses = 0
    print("Welcome to the Guess-the-Word game!")
    print("Try to guess the three-word quote:")
    start_time = time.time()
    while quote != new_list:
        print(new_list)
        guess = input("Enter a letter: ").lower()
        update_new_list(new_list, quote, guess)
        if guess not in ' '.join(guesses_list) and guess in ' '.join(new_list):
            guesses_list.append(guess)
            correct_guesses += 5
        else:
            wrong_guesses -= 1
    total_points = correct_guesses + wrong_guesses
    end_time = time.time()
    total_time = end_time - start_time
    if total_time < 30:
        total_points += 100
    print(f"Congratulations! You guessed the quote!, the quote is {new_list}")
    print(f"Total points: {total_points}")

game()
