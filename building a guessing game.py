secret_blud = "only in ohio"
le_guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while le_guess != secret_blud and not(out_of_guesses):
    if guess_count < guess_limit:
        le_guess = input("Enter your guess blud: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print ("You goofy ahh")
else:
    print ("You Win!")