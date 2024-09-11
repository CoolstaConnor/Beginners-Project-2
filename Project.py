import random
import time

right = 1
wrong = 0
completed_challenges = 

def load():
    print("Loading .")
    time.sleep(1)
    print("Loading ..")
    time.sleep(1)
    print("Loading ...")
    time.sleep(1)
    print("Done!")

def progress():
    while True:
        choice = input("Do you want to continue (c), or end it there (e)? ").strip().lower()
        if choice == 'e':
            print("Thanks for playing!")
            exit()
        elif choice == 'c':
            load()
            break
        else:
            print("Invalid choice. Please enter 'c' or 'e'.")

# Function to check how many "banana" guesses are correct
def get_correct_banana_guesses(guesses):
    # Convert all guesses to lowercase and count how many are "banana"
    correct_count = sum(1 for guess in guesses if guess.lower() == 'banana')
    return correct_count

def foresttreasurehunt():
    global right, wrong, completed_challenges
    load()
    
    input("Welcome to the forest! {Press enter to continue}")
    input("You have been tasked with going on a treasure hunt. {Press enter to continue}")
    input("It's somewhere within this forest, but it's not that easy! {Press enter to continue}")
    input("You will have to guess the fruit this wild monkey wants 5 times! 🐒 {Press enter to continue}")

    correct_count = 0
    
    while correct_count < 5:
        guess_list = []
        for _ in range(5):
            guess = input("Guess a fruit: ").strip()
            guess_list.append(guess)
        
        correct_count = get_correct_banana_guesses(guess_list)
        
        if correct_count == 5:
            print("Congratulations! You guessed 'banana' correctly 5 times and passed the first challenge!")
            completed_challenges += 1
            progress()
            hungrytiger()
        else:
            print(f"You've guessed 'banana' correctly {correct_count} times. Please guess again!")

def pythonquiz():
    global right, wrong, completed_challenges
    input("You're going to be given some multiple-choice questions on Python. {Press enter to continue}")
    input("These 6 questions will range in difficulty from easy to hard. {Press enter to continue}")
    input("Proceeding this you will get your first question. {Press enter to continue}")
    
    questions = [
        ("What does Python use for a statement terminator?", "A: A semi colon (;).", "B: A colon (:).", "C: An underscore (_)", "D: A new line ()", 'D'),
        ("How do you ask the user a question in Python?", "A: Input", "B: Question", "C: Query", "D: Scan", 'A'),
        ("How old was the creator of Python when it was made?", "A: 18-21", "B: 24-27", "C: 33-35", "D: 46-49", 'C'),
        ("During what holiday break was Python created in?", "A: School Holidays", "B: Christmas", "C: Easter", "D: New Years", 'B'),
        ("Python is named after what?", "A: A game.", "B: A coffee.", "C: A cheese.", "D: A snake.", 'D'),
        ("Which of the following is NOT part of Python's core philosophy in The Zen of Python?", "A: Readability counts.", "B: Flat is better than nested.", "C: Special cases aren't special enough to break the rules.", "D: Code execution speed takes priority over simplicity.", 'D')
    ]
    
    for q in questions:
        print(q[0])
        print(q[1])
        print(q[2])
        print(q[3])
        print(q[4])
        answer = input("Enter your letter: ").strip().upper()
        if answer == q[5]:
            right += 1
        else:
            wrong += 1
    
    print(f"You scored {right} out of 6!")
    
    # Feedback based on score
    if right == 6:
        print("Congratulations! You got all questions correct!")
    elif right >= 4:
        print("Good job! You got most of the questions right.")
    elif right >= 2:
        print("Not bad. You got a few questions right.")
    else:
        print("Better luck next time. You might want to study more.")

def hungrytiger():
    global completed_challenges
    input("There's a hungry tiger. {Press enter to continue}")
    input("The only way out is to cross a river inputting your height. {Press enter to continue}")
    input("If your height is within the right range you will live, otherwise you will drown or get eaten! {Press enter to continue}")
    
    while True:
        try:
            height = int(input("Enter your height: "))
            if height > 160 and height < 180:
                print("You have survived!")
                completed_challenges += 1
                break
            elif height <= 160:
                print("You have drowned!")
                break
            elif height >= 180:
                print("The tiger spots and eats you!")
                break
        except ValueError:
            print("Invalid input. Please enter a number for your height.")
    
    progress()
    pythonquiz()

# Main game logic
def main():
    global right, wrong, completed_challenges
    gameenter = random.randint(1, 2)
    
    if gameenter == 1:
        foresttreasurehunt()
        hungrytiger()
    elif gameenter == 2:
        pythonquiz()
        foresttreasurehunt()
        hungrytiger()
    
    if completed_challenges == 3:
        print("You have completed all of the challenges. Well done!")

if __name__ == "__main__":
    main()
