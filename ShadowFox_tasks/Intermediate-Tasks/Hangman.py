import random
#words grouped into categories
categories = {
"Animals": ["lion","giraffe","tiger","elephant","wolf","dolphin","cat","horse",
        "monkey","cheetah","sheep","dog","kangaroo","goat","rat","frog",
        "anaconda","sparrow","squirrel","pigeon","cricket","fish","bear",
        "camel","shark","otter","peacock","jaguar","falcon","porcupine",
        "zebra","owl","mouse","gorilla","panther","rabbit","turtle",
        "fox","koala","leopard","whale","panda","snake","penguin","duck"],
"Food": ["chocolate","mango","burger","orange","icecream","berries","sushi",
        "potato","cookie","grapes","vegetable","tea","coffee","cake",
        "apple","banana","pizza","strawberry"],
"Object": ["utensils","keyboard","printer","brush","laptop","pencil","mirror",
        "television","charger","mobile","monitor","camera","notebook",
        "table","chair","computer","copy"],
"Places": ["Delhi","Switzerland","Australia","library","school","France","India",
        "mountain","river","forest","galaxy","planet","ground","market"],
"People/Occupation": ["pilot","student","teacher","engineer","doctor","carpenter"],
"Abstract/Concepts": [ "mystery","science","adventure","artificial","memory",
        "travel","birthday","clouds"],
"Emotion": ["happiness","sadness","excitement","exhaustion","friendship",
        "gratitude","love","serenity","pride","amusement"]
}
#dictionary of key:() 
hangman_art = {0: ("  ",
                   "  ",
                   "  "), 
               1: (" o ",
                   "  ",
                   "  "), 
               2: (" o ",
                   " | ",
                   "  "), 
               3: (" o ",
                   "/| ",
                   "  "), 
               4: (" o ",
                  "/|\\ ",
                   "  "), 
            5: (" o ",
               "/|\\ ",
               "/ "), 
            6: (" o ",
               "/|\\ ",
               "/ \\")}
#list of hints
hints = ["Animal", "Food"]
def display_man(wrong_guesses):
    print("********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("********")
def display_hint(hint):
    print(" ".join(hint))
def display_word(word):
    print("The word was: "," ".join(word))
def play_game():
    #choose a random category first as hint
    category = random.choice(list(categories.keys()))
    #then choose a random word from that category
    word = random.choice(categories[category])
    hint = ['_'] * len(word)
    wrong_guesses = 0
    guessed_letters = set()
    is_Running = True
    print(f"Hint: This word belongs to the category -> [{category}]\n") #Initial hint
    while is_Running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("The input you gave was invalid.You must enter a letter at a time.")
            continue
        if guess in guessed_letters:
            print(f"you have already guess the letter {guess}.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            for i in range(len(word)):
                 if word[i] == guess:
                     hint[i] = guess
        else:
            wrong_guesses = wrong_guesses + 1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_word(word)
            print("Congratulations! YOU WIN.")
            is_Running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_word(word)
            print("Unfortunetly! YOU LOOSE.")
            is_Running = False
if __name__ == "__main__":
    while True: #restart the game
        play_game()
        play_again = input("Do you want to play again?(y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing")
            break