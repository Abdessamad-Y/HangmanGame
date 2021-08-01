import random
import string
def list_to_string(list):
    str = ""
    for i in list:
        str += i
    return str
def game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    choice = list(random.choice(word_list))
    s = '-' * len(choice)
    print()
    print(s)
    repeated_error = []
    s = list(s)
    x = 8
    count = 0
    while x >= 0:
        print('Input a letter: ', end="")
        letter= input()
        if len(letter)>=2:
            print("You should input a single letter")
        elif letter not in string.ascii_lowercase :
            print("Please enter a lowercase English letter")
        elif letter in s or letter not in choice:
            if letter in s:
                print("You've already guessed this letter")
                
            else:
                if letter in repeated_error:
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    repeated_error.append(letter)
                    x -= 1
                if x == 0:
                    print("You lost!")
                    break
        else:
            for i in range(len(choice)):
                if choice[i] == letter:
                    s[i] = letter
                    count += 1 
        if count == len(choice):
            print(list_to_string(s))
            print("""You guessed the word!
    You survived!""")
            break
        
        print()
        print(list_to_string(s))

print("H A N G M A N")
print('Type "play" to play the game, "exit" to quit:', end="")
menu = input()
while menu == 'play': 
    game()
    break