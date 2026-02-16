import time ,  asyncio

def validate_position_pure(combinations):
    for i in range(len(combinations)):
        for j in range(i + 1, len(combinations)):
            q1, q2 = combinations[i], combinations[j]
            if abs(q1[0] - q2[0]) == 1 and abs(q1[1] - q2[1]) == 1:
                return False
    return True

async def play_pure(board, n, page, render_board):
    start = time.process_time()
    cnt = 0
    
    board_list = []
    for y in range(n):
        row = ""
        for x in range(n):
            row += board[(x, y)]
        board_list.append(row)
    
    color_groups = {}
    for pos, color in board.items():
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(pos)
    
    colors = sorted(color_groups.keys())
    
    if len(colors) != n:
        end = time.process_time()
        return None, end - start
    
    color_cell_lists = [color_groups[c] for c in colors]
    
    group_sizes = [len(cells) for cells in color_cell_lists]
   

    combinations = [0 for _ in range(n)]
    
    found = True
    while found:
        cnt += 1
        
        solutions = [color_cell_lists[i][combinations[i]] for i in range(n)]
        
        
        rows = [q[1] for q in solutions]
        if len(set(rows)) == n:
            cols = [q[0] for q in solutions]
            if len(set(cols)) == n:
                if validate_position_pure(solutions):
                    end = time.process_time()
                    render_board(board_list, solutions)
                    await asyncio.sleep(0)
                    return solutions, end - start, cnt
        
        if cnt % 1000 == 0:
            render_board(board_list, solutions)
            await asyncio.sleep(0)
        
      
        i = n - 1
        while i >= 0 and combinations[i] == group_sizes[i] - 1:
            i -= 1
        
        if i < 0:
            found = False
        else:
            combinations[i] += 1
            for j in range(i + 1, n):
                combinations[j] = 0
    
    end = time.process_time()
    return None, end - start, cnt

def validate_position_bt(x, y, cc, storageColor, storagePoint, storageRow,storageCol):
    if x in storageRow or y in storageCol:
        return False
    if cc in storageColor:
        return False
    neighbor = [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    for n in neighbor:
        if n in storagePoint:
            return False
    return True

async def play_bt(board, n, page, render_board):
    storagePoint = set()
    storageRow =  set()
    storageCol =  set()
    storageColor =  set()
    queenPoints = []
    step = [0]
    board_list = []
    for y in range(n):
        row = ""
        for x in range(n):
            row += board[(x, y)]
        board_list.append(row)
    async def searchPoints(index,count):
            step[0]+=1
            if count == n:
                 return True
            if index >= n*n:
                 return False
            x = index % n
            y = index // n
            color = board[(x, y)]
            if step[0] % 1000 == 0:
                render_board(board_list, queenPoints)
                await asyncio.sleep(0)
            if validate_position_bt(x, y, color, storageColor, storagePoint, storageRow, storageCol):
                storagePoint.add((x, y))
                storageRow.add(x)
                storageCol.add(y)
                storageColor.add(color)
                queenPoints.append((x, y))

                if await searchPoints(index + 1, count + 1):
                    return True

                storagePoint.remove((x, y))
                storageRow.remove(x)
                storageCol.remove(y)
                storageColor.remove(color)
                queenPoints.pop()

            
            if await searchPoints(index + 1, count):
                return True
                         
            return False
    
    start = time.process_time()
    if(await searchPoints(0,0)):
         end = time.process_time()
         return queenPoints, end-start, step[0]
    else:
        end = time.process_time()
        return None, end-start, step[0]