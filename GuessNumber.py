import random
def guess_numb(play,guess=0):
    while play=="a" :
        ans=input("enter a number less than 10:")
        if ans.isdigit():
            ans=int(ans)
        if ans in [1,2,3,4,5,6,7,8,9,10]:
            random_num = random.randint(0, 10)
            print("the random number is :", random_num, "and ur numb is:", ans)
            guess+=1
            if random_num==ans:
                print("number matched :)")
                print("you got it in", guess, "guesses")
                break

            else:
                print("wrong guess")
                print("please guess again")
        else:
            print("please enter a number between 1-10")

    else:
        print("okay!")

if __name__ == "__main__":
    print("Welcome to the game!!!")
    instructions = """-->In this game computer will randomly guess a number between 1 - 10
-->you have to guess that computers random number
-->when a match is found.., you will win"""
    print(instructions)
    play = input("""Are you ready to guess a number?
         a)yes b)no 
         enter a/b:
         """).lower()
    while True:
        if play in ["a","b"]:
            guess_numb(play)
            break
        else:
            play=input("please enter either a/b")


