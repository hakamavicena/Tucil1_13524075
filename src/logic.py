def validate_position(x, y, cc, storageColor, storagePoint, storageRow,storageCol):
    if x in storageRow or y in storageCol:
        return False
    if cc in storageColor:
        return False
    neighbor = [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    for n in neighbor:
        if n in storagePoint:
            return False
    return True

def play(board, n):
    storagePoint = set()
    storageRow =  set()
    storageCol =  set()
    storageColor =  set()
    queenPoints = []

    def searchPoints(y):
            if y == n:
                 return True
            for x in range(n):
                color = board[(x,y)]
                validPosition = validate_position(x, y, color, storageColor,storagePoint, storageRow, storageCol)
                if(validPosition):
                    storagePoint.add((x, y))
                    storageRow.add(x)
                    storageCol.add(y)
                    storageColor.add(color)
                    queenPoints.append((x,y))
                    if(searchPoints(y+1)):
                         return True
                    else:
                         storageCol.remove(y)
                         storagePoint.remove((x,y))
                         storageRow.remove(x)
                         storageColor.remove(color)
                         queenPoints.pop()
            return False
    
    
    if(searchPoints(0)):
         return queenPoints
    else:
         return None