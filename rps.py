import random
moves = ["rock", "paper", "scissor"]
name = input("Enter name: ")
print("""
Choose:
1. ROCK
2. PAPER
3. SCISSOR
""")
win = lose = draw = 0
while True:
    user_choice = input("Enter choice: ")
    try:
        user_choice = int(user_choice)
        if user_choice not in [1,2,3]:
            continue
    except:
        print("Please enter an integer between 1-3")
        continue
    comp_choice = random.choice(moves)
    print(f"\nUser chose    : {moves[user_choice - 1]}")
    print(f"Computer chose: {comp_choice}\n")
    for i, j in enumerate(moves):
        if moves[user_choice - 1] == j:
            if comp_choice == j:
                print("\nDRAW\n")
                draw += 1
            elif comp_choice == moves[(i+1)%3]:
                print("\nYOU LOSE\n")
                lose += 1
            else:
                print("\nYOU WIN\n")
                win += 1
    while True:
        exit_loop = input("\nDo you want to continue (y/n)?: ")
        if len(exit_loop) ==  1 and exit_loop.lower() in ['y','n']:
            break
        else:
            print("\nINVALID CHOICE")
    if exit_loop.lower() == 'n':
        break

print(f"""
{name}'s SCORE:
WINS   : {win}
LOSE   : {lose}
DRAW   : {draw}
""")


        
