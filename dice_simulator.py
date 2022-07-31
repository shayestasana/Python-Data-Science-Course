
from random import randint
win_count = 0
lose_count = 0

dice = ['1', '2', '3', '4', '5', '6']

while True:
    input("Press enter to Roll a Dice")
    out=randint(1,6)
    print(f'🎲 => {dice[out-1]}')
    n=0
    while(n<3):
        if out == 6:
            win_count += 1
        elif out == 1:
            lose_count += 1
        n=n+1


    if win_count==3:
        print("You Win 🤴")
        break
    elif lose_count ==3:
        print("You Lose 😞")
        break