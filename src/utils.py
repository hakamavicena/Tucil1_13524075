def is_connected(board):
    n = len(board)
    
    colors = set(char for row in board for char in row)
    
    for color in colors:
        start_node = None
        color_cells_count = 0
        for r in range(n):
            for c in range(n):
                if board[r][c] == color:
                    color_cells_count += 1
                    if not start_node:
                        start_node = (r, c)
        
        queue = [start_node]
        seen_in_bfs = {start_node}
        while queue:
            curr_r, curr_c = queue.pop(0)
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < n and 0 <= nc < n and \
                   board[nr][nc] == color and (nr, nc) not in seen_in_bfs:
                    seen_in_bfs.add((nr, nc))
                    queue.append((nr, nc))
        
        if len(seen_in_bfs) != color_cells_count:
            return False, f"Warna {color} terpecah/tidak menyatu!"
            
    return True, "Semua wilayah terkoneksi dengan baik."

def validate_board(board):
    n = len(board)
    for row in board:
        if len(row) != n:
            return False, "Papan tidak persegi!"
        
    warna = set(char for row in board for char in row)
    if len(warna) != n:
        return False,f"Jumlah warna ({len(warna)}) tidak sama dengan ukuran papan {n}!"
    valid, pesan = is_connected(board)
    if (not valid):
        return valid, pesan
    return True, 'Papan Valid!'

def file_to_board(path):
    try:
        with open (path) as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except:
          print("Gagal membaca file :(")
    
def convert_dict(board, n):
    points = [(x, y) for x in range(n) for y in range(n) ]
    boardDict = {}
    for x in range(n*n):
        x_coor, y_coor = points[x]
        color = board[y_coor][x_coor]
        boardDict[(x_coor, y_coor)] = color
    return boardDict

def interface(board,solution, n):
    for  y in range(n):
        for x in range(n):
            if (x, y) in solution:
                print('#', end='')
            else:
                print(f'{board[(x,y)]}', end='')
        print()
    print()


