#!/usr/bin/python3
import random
print("Dice Generator\n\nRules:-\n1. Two players can play the game\n2. The first to get a 6 will win\n")
input("Press Enter key to start")
player1 = input("Input first player's name ")
player2 = input("Input second player's name ")
c1 = 1
c2 = 1
while(c1 != 6 and c2 != 6):
	print(player1,"'s turn press enter to throw",end=' ')
	input()
	c1 = random.choice(range(6)) + 1
	print(player1,"  got ",c1)
	if(c1 == 6):
		print("congrats ",player1," won")
		break
	print(player2,"'s turn press enter to throw",end=' ')
	input()
	c2 = random.choice(range(6)) + 1
	print(player2," got ",c2)
	if(c2==6):
		print("congrats ",player2," won")
		break

