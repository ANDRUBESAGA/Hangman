import random


while True:
    condition = input('Type "play" to play the game, "exit" to quit: ')
    if condition != 'exit' and condition != 'play':
        continue
    elif condition == "exit":
        break
    else:

        words = ['python', 'java', 'kotlin', 'javascript']
        chosen = random.choice(words)
        hiddendword = list(len(chosen) * "-")
        typedword = []
        print("H A N G M A N")
        attems = 8
        while attems != 0:
            print()
            print("".join(hiddendword))
            letter = input("Input a letter: ")
            if len(letter) > 1 or letter == "":
                print("You should input a single letter")
            elif letter in hiddendword and letter !="-":
                print("You already typed this letter")
            elif letter.islower() and letter.isalpha():
                if letter in typedword:
                    print("You already typed this letter")
                elif letter not in chosen:
                    print("No such letter in the word")
                    attems -= 1
                    typedword.append(letter)
                else:
                    for i in range(len(chosen)):
                        if chosen[i] == letter:
                            hiddendword[i] = letter
                            typedword.append(letter)
                if "".join(hiddendword) == chosen:
                    print("You guessed the word!")
                    print("You survived!")
                    break
                else:
                    if attems == 0:
                        print("You are hanged!")
                print("\n")
            else:
                print("It is not an ASCII lowercase letter")