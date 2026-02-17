from PIL import Image, ImageDraw, ImageFont


def generate_color_map(characters):
    base_colors = [
        (239, 83, 80),
        (66, 165, 245),
        (102, 187, 106),
        (156, 39, 176),
        (255, 167, 38),
        (38, 198, 218),
        (236, 64, 122),
        (38, 166, 154),
        (212, 225, 87),
        (255, 193, 7),
        (92, 107, 192),
        (255, 87, 34),
        (156, 204, 101),
        (103, 58, 183),
        (255, 235, 59),
        (79, 195, 247),
        (141, 110, 99),
        (120, 144, 156),
        (229, 115, 115),
        (129, 199, 132),
        (171, 71, 188),
        (255, 183, 77),
        (77, 208, 225),
        (240, 98, 146),
        (77, 182, 172),
        (220, 231, 117),
    ]

    color_map = {}
    for i, char in enumerate(characters):
        color_map[char] = base_colors[i % len(base_colors)]

    return color_map


def board_to_image(board_data, solution=None, output_path="solution.png", cell_size=80, color_map=None):
    n = len(board_data)
    img_size = n * cell_size

    img = Image.new('RGB', (img_size, img_size), 'white')
    draw = ImageDraw.Draw(img)

    if color_map is None:
        unique_chars = sorted(set(char for row in board_data for char in row))
        color_map = generate_color_map(unique_chars)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", cell_size // 2)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", cell_size // 4)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", cell_size // 2)
            label_font = ImageFont.truetype("arial.ttf", cell_size // 4)
        except:
            font = ImageFont.load_default()
            label_font = ImageFont.load_default()

    for y in range(n):
        for x in range(n):
            char = board_data[y][x] 
            color = color_map.get(char, (200, 200, 200))

            x1 = x * cell_size
            y1 = y * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            draw.rectangle([x1, y1, x2, y2], fill=color, outline='black', width=2)
            draw.text((x1 + 5, y1 + 5), char, fill='white', font=label_font)

            if solution and (x, y) in solution:
                text = "Q"
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                text_x = x1 + (cell_size - text_width) // 2
                text_y = y1 + (cell_size - text_height) // 2
                draw.text((text_x, text_y), text, fill='white', font=font)

    img.save(output_path)
    print(f"Image saved: {output_path}")
    return output_path


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
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
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
        for char in row:
            if not char.isalpha():
                return False, f"Karakter terlarang ditemukan: '{char}'. Hanya alfabet (A-Z) yang diperbolehkan!"

    warna = set(char for row in board for char in row)
    if len(warna) != n:
        return False, f"Jumlah warna ({len(warna)}) tidak sama dengan ukuran papan {n}!"

    valid, pesan = is_connected(board)
    if not valid:
        return valid, pesan
    return True, 'Papan Valid!'


def file_to_board(path):
    try:
        with open(path) as f:
            result = []
            for line in f.readlines():
                line = line.strip().replace(' ', '')
                if not line:
                    continue
                result.append(list(line))
                
            return result
    except FileNotFoundError:
        return None
    except:
        print("Gagal membaca file :(")
        return None

def convert_dict(board, n):
    points = [(x, y) for x in range(n) for y in range(n)]
    boardDict = {}
    for i in range(n * n):
        x_coor, y_coor = points[i]
        color = board[y_coor][x_coor]  
        boardDict[(x_coor, y_coor)] = color
    return boardDict
