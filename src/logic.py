import time , utils

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
    step = [0]

    def searchPoints(index,count):
            step[0]+=1
            if count == n:
                 return True
            if index >= n*n:
                 return False
            x = index % n
            y = index // n
            color = board[(x, y)]
            if step[0] % 1000 == 0:
                print(f"\n[Langkah ke-{step[0]}]")
                utils.interface(board, queenPoints, n)
            if validate_position(x, y, color, storageColor, storagePoint, storageRow, storageCol):
                storagePoint.add((x, y))
                storageRow.add(x)
                storageCol.add(y)
                storageColor.add(color)
                queenPoints.append((x, y))

                if searchPoints(index + 1, count + 1):
                    return True

                storagePoint.remove((x, y))
                storageRow.remove(x)
                storageCol.remove(y)
                storageColor.remove(color)
                queenPoints.pop()

            
            if searchPoints(index + 1, count):
                return True

            # for x in range(n):
                step[0]+=1 
                if step[0] % 1000 == 0:
                    print(f"\n[Langkah ke-{step[0]}]")
                    utils.interface(board, queenPoints, n)
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
    
    start = time.process_time()
    if(searchPoints(0,0)):
         end = time.process_time()
         return queenPoints, end-start
    else:
        end = time.process_time()
        return None, end-start