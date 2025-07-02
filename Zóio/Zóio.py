# simbora

import random

computer = random.randint(1, 3)


print('===============')
print('ROCK PAPER SCISSORS')
print('===============')

print('1) ✊')
print('2) ✋')
print('2) ✌')

player = int(input("pick a number "))


if player == 1 and computer == 2:
    print('you chose: ✊')
    print('Cpu chose: ✊')
    print('tie')
if player == 2 and computer == 2:
    print('you chose: ✋')
    print('Cpu chose: ✋')
    print('tie')
if player == 3 and computer == 3:
    print('you chose: ✌')
    print('Cpu chose: ✌')
    print('tie')
elif player == 2 and computer == 1:
    print('you chose: ✋')
    print('Cpu chose: ✊')
    print('you won')
elif player == 3 and computer == 1:
    print('you chose: ✌')
    print('Cpu chose: ✊')
    print('you lose')
elif player == 1 and computer == 2:
    print('you chose: ✌')
    print('Cpu chose: ✋')
    print('you win')
elif player == 1 and computer == 3:
    print('you chose: ✊')
    print('Cpu chose: ✌')
    print('you win')
else:
    print('error')
    