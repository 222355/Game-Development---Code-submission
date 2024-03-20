

chance = 0
finalArray = [
    1,2,3,
    4,5,6,
    7,8,9]
turn = True
def checkWinner():
    row =[ [ 1,2,3], [4,5,6], [7,8,9] ]
    colum =[ [1,4,7], [2,5,8], [3,6,9] ]
    diagonal = [ [1,5,9], [3,5,7] ] 
    stop = False
    for rowElement in range(len(row)):
        if finalArray[row[rowElement][0]-1] == finalArray[row[rowElement][1]-1] == finalArray[row[rowElement][2]-1]:
            print('The winner is ',finalArray[row[rowElement][0]-1])
            return True
    for colElement in range(len(colum)):
        if finalArray[colum[colElement][0]-1] == finalArray[colum[colElement][1]-1] == finalArray[colum[colElement][2]-1]:
            print('The winner is ',finalArray[colum[colElement][0]-1])
            return True
    for diaElement in range(len(diagonal)):
        if finalArray[diagonal[diaElement][0]-1] == finalArray[diagonal[diaElement][1]-1] == finalArray[diagonal[diaElement][2]-1]:
            print('The winner is ',finalArray[diagonal[diaElement][0]-1])
            return True
    return False
while chance < 9 :
    chance +=1
    print(finalArray)
    if turn:
        index = input('Player 1 choose Your Box number') # 2
        finalArray[int(index)-1] = 'X'
        if checkWinner():
            break;
        
    else:
        index = input('Player 2 choose Your Box number') # 2
        finalArray[int(index)-1] = 'O'
        if checkWinner():
            break;
    turn = not turn
  
        
        
        