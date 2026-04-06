'''
1 for snake
-1 for water
0 for gun
'''
import random

# Initialize scores
user_score = 0
comp_score = 0

youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

print("--- Welcome to Snake, Water, Gun: 5 Round Match! ---")

round_num = 1

while round_num <= 5:
    print(f"\nRound {round_num}/5:")
    youstr = input("Enter your choice (s,w,g): ")

    if youstr not in youDict:
        print("Invalid input! Please choose s, w, or g.")
        continue
    
    computer = random.choice([-1, 0, 1])
    you = youDict[youstr]
    print("You chose:", reverseDict[you])
    print("Computer chose:", reverseDict[computer])

    if(computer == you):
       print("It's a draw")

    else:
        if(computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round!")
            comp_score += 1
       
    round_num += 1  # only increase after valid input
    
# Final Result
print("\n" + "-"*40)
print(f"FINAL SCORE - You: {user_score} | Computer: {comp_score}")

if user_score > comp_score:
    print("CONGRATULATIONS! You won the match!")
elif user_score < comp_score:
    print("GAME OVER! The computer won the match.")
else:
    print("It's a tie match!")
print("-"*40)