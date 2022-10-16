def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''

    # Create a string variable that contains the answer.
    answer = "cow"
    num_of_guesses = 3
    while True:

        # let the user know how many guesses they have.
        print(num_of_guesses, "guesses left!")
        # get the guess from the user
        guess = input("Guess an animal or type 'quit' to exit the game: ").lower()
        if guess == answer:
            print("Correct! Nice job.")
            break
        elif guess == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Wrong! try again.")

        # remove a guess from the count and check if we still have guesses
        num_of_guesses -= 1
        if num_of_guesses <= 0:
            print("Out of guesses!")
            break


start()