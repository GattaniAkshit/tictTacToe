#
# Tic-Tac-Toe
#

import os
import sys

grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
char = "Z"
symbol = "X"
count = 0

# mark the tic-tac-toe board with the players symbol
def mark():
    global char, symbol
    for iD, i in enumerate(grid):
        for jD, j in enumerate(i):
            if j == char:
                grid[iD][jD] = symbol
                # alternate symbol for players
                if symbol == "X":
                    symbol = "O"
                else:
                    symbol = "X"
                break
    
    os.system("clear")
    disp()

def checkPattern():
    global char
    countSquares = 1 # if this equals 3, then the same symbol is present in tempList
    tempList = [] # contains all lists where a square can have patterns - horizontal, vertical and diagonals
    row = 0 # x-coordinate of square marked
    col = 0 # y-coordinate of square marked
    charToCoordinate = {"A": [0, 0], "B": [0, 1], "C": [0, 2], "D": [1, 0], "E": [1, 1], "F": [1, 2], "G": [2, 0], "H": [2, 1], "I": [2, 2]} # dict to map character to (x, y)
    coordinates = charToCoordinate[char]
    row = coordinates[0]
    col = coordinates[1]
    j = col
    tempList = grid[row] # for left and right
    # left
    while j > 0:
        if tempList[j] == tempList[j - 1]:
            countSquares += 1
        j -= 1
    j = col
    # right
    while j < 2:
        if tempList[j] == tempList[j + 1]:
            countSquares += 1
        j += 1
    if countSquares == 3:
        return True
    # If pattern is not found in the horizontal list reset values and look in the vertical list
    countSquares = 1
    j = col
    tempList = []
    for iD, tempi in enumerate(grid):
        for jD, tempj in enumerate(tempi):
            if jD == col:
                tempList.append(tempj)
    
    # top & bottom
    while j > 0:
        if tempList[j] == tempList[j - 1]:
            countSquares += 1
        j -= 1
    j = col
    while j < 2:
        if tempList[j] == tempList[j + 1]:
            countSquares += 1
        j += 1
    if countSquares == 3:
        return True
    # check for diagonal case
    if ((row == 0 or row == 2) and (col == 0 or col == 2)) or (row == 1 and col == 1):
        # diagonal case
        countSquares = 1
        j = col
        tempList = []
        if (row == 1 and col == 1):
            tempList2 = []
            for iD, tempi in enumerate(grid):
                for jD, tempj in enumerate(tempi):
                    if iD == jD:
                        tempList.append(jD)
            tempi = 0
            tempj = 0
            
            while tempi < 3:
                tempList2.append(grid[tempi][tempj])
                tempi += 1
                tempj -= 1

            while j > 0:
                    if tempList2[j] == tempList2[j - 1]:
                        countSquares += 1
                    j -= 1
            j = col
            while j < 2:
                if tempList2[j] == tempList2[j + 1]:
                    countSquares += 1
                j += 1
            if countSquares == 3:
                return True
            countSquares = 1
            j = col
            while j > 0:
                    if tempList2[j] == tempList2[j - 1]:
                        countSquares += 1
                    j -= 1
            j = col
            while j < 2:
                if tempList2[j] == tempList2[j + 1]:
                    countSquares += 1
                j += 1
            if countSquares == 3:
                return True
            return False # if even both diagonals dont have patterns, no pattern is there
        else:
            if row == 0:
                tempList.append(grid[row][col])
                tempList.append(grid[1][1])
                if col == 2:
                    tempList.append(grid[2][0])
                else:
                    tempList.append(grid[2][2])
            else:
                tempList.append(grid[row][col])
                tempList.append(grid[1][1])
                if col == 2:
                    tempList.append(grid[0][0])
                else:
                    tempList.append(grid[0][2])
            
            while j > 0:
                if tempList[j] == tempList[j - 1]:
                    countSquares += 1
                j -= 1
            j = col
            while j < 2:
                if tempList[j] == tempList[j + 1]:
                    countSquares += 1
                j += 1
            if countSquares == 3:
                return True
    return False # If no list has a pattern, defaults to return false

def disp():
    print()
    for iD, i in enumerate(grid):
        print(" ",end='')
        for jD, j in enumerate(i):
            print(j, end=' ')
            if jD != 2:
                print("|", end='')
            elif iD != 2:
                print()
                print("---------")

    print()
    print()
    print()

def checkInput():
    global char
    flag = 0
    for i in grid:
        for j in i:
            if char == j: # if input char is not already marked
                flag = 1
    if flag == 1:
        return True
    return False 

def main():
    global count, char
    result = False
    disp()
    print("Player 1(X), your turn-")
    char = input("Enter the square for marking: ")
    char = char.upper()
    mark()

    count += 1
    while (True):
        if count == 9:
            print("It's a draw :-(")
            sys.exit()
    
        if count % 2 != 0:
            print("Player 2(O), your turn-")
        else:
            print("Player 1(X), your turn-")
    
        char = input("Enter the square for marking: ")
        char = char.upper()
        validInput = checkInput()
        if validInput == False:
            print("INVALID INPUT\nPlease give an unmarked square!")
            continue
    
        mark()

        count += 1
        if count < 5:
            continue
        else:
            result = checkPattern()
            # Condition for win
            if result == True:
                if count % 2 == 0:
                    print("Player 2 wins!!")
                else:
                    print("Player 1 wins!!")
                sys.exit()

main()