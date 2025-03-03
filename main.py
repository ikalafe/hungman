import random

from hungman_art import stages
from hungman_art import logo
from hungman_world import word_list

chosen_world = random.choice(word_list)

lives = 6
print(f'{logo}')
display = []
world_length = len(chosen_world)
for _ in range(world_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(world_length):
        letter = chosen_world[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_world:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
