#!/bin/python3

from random import choice # GET RANDOM FROM A LIST


Players = []
file = open('player.text', 'r')    # OPEN A FILE FOR READING IT
Players = file.read().splitlines() # READ THAT FILE LINE BY LINE
print(Players)
for i in Players:
	print(i)

teamA = []
teamB = []

while len(Players) > 0:
	playerA = choice(Players) # CHOICE RANDOM FROM A LIST
	print(playerA)
	teamA.append(playerA)
	Players.remove(playerA)
	print("Players left: ", Players)
	
	if Players == []: # FIX BUG IF THERE'S AN ODD NUMBER OF PLAYERS
	  break           # SO THE PROGRAM WILL RUN NOMAL

	playerB = choice(Players)
	print(playerB)
	teamB.append(playerB)
	Players.remove(playerB)
	print("Players left: ", Players)
	
print("Team A: ", teamA)
print("Team B: ", teamB)
  
