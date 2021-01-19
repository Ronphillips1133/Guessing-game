secert_word = ""
guess = ""
guess_count = 0
guess_limit = 3
guess_hint = 1
third_try = 2
guess_help = ''
second_guess = 1
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
out_of_guesses = False
enter_secert = input('Enter Secert Word: ')
secert_word = enter_secert
sentence = "Get Ready To Start"
char_freq = {}


for char in sentence:
    if char in char_freq:
        char_freq += 1


while guess != secert_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess what word I am Thinking? ")
        if guess_count > guess_count:
            guess = input("Try Again")
        if guess_count >= guess_hint:
            guess = guess_help = print(
                'Here is the First Letter:' + secert_word[0])
        if guess_count >= third_try:
            guess = guess_help = print(
                'Here is the Next Letter:' + secert_word[0:2])
        if guess_count >= guess_hint:
            guess = input("Try again: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Good Try you LOSE! Secert Word:" + secert_word)
else:
    print("You Got It!")
