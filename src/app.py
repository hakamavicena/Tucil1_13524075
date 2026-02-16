import flet as ft
import logic, utils, image_process


async def main(page: ft.Page):
    page.title = "Queens Game by Brute Force Algorithm"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.window_width = 1000
    page.window_height = 800

    state = {
        "board": None,
        "n": 0,
        "boardDict": {},
        "is_running": False,
        "solution": None
    }

    status_text = ft.Text("Pilih file atau masukkan teks board...", italic=True)
    step_counter = ft.Text("Langkah: 0", weight="bold")
    duration_text = ft.Text("Durasi: 0 ms")
    
    file_name_input = ft.TextField(label="Nama File", hint_text="Contoh: board.txt", expand=True)
    manual_input = ft.TextField(label="Atau Paste Board di sini", multiline=True, min_lines=3)
    
    pure_bt_switch = ft.Switch(label="Pure Brute Force (Tanpa Backtrack)", value=True)
    
    grid_display = ft.Container(
        content=ft.Column(), 
        alignment=ft.alignment.Alignment(0, 0), 
        padding=20
    )
    
    def render_board(board_data, solution=None):
        n = len(board_data)
        state["n"] = n
        state["boardDict"] = utils.convert_dict(board_data, n)
        
        color_map = {
            'A': ft.Colors.RED_400,
            'B': ft.Colors.BLUE_400,
            'C': ft.Colors.GREEN_400,
            'D': ft.Colors.PURPLE_400,
            'E': ft.Colors.ORANGE_400,
            'F': ft.Colors.CYAN_400,
            'G': ft.Colors.PINK_400,
            'H': ft.Colors.TEAL_400,
            'I': ft.Colors.LIME_400,
            'J': ft.Colors.AMBER_400,
            'K': ft.Colors.INDIGO_400,
            'L': ft.Colors.DEEP_ORANGE_400,
            'M': ft.Colors.LIGHT_GREEN_400,
            'N': ft.Colors.DEEP_PURPLE_400,
            'O': ft.Colors.YELLOW_400,
            'P': ft.Colors.LIGHT_BLUE_400,
            'Q': ft.Colors.BROWN_400,
            'R': ft.Colors.BLUE_GREY_400,
            'S': ft.Colors.RED_300,
            'T': ft.Colors.GREEN_300,
            'U': ft.Colors.PURPLE_300,
            'V': ft.Colors.ORANGE_300,
            'W': ft.Colors.CYAN_300,
            'X': ft.Colors.PINK_300,
            'Y': ft.Colors.TEAL_300,
            'Z': ft.Colors.LIME_300
        }
        
        rows = []
        state["grid_cells"] = [] 
        
        for y in range(n):
            row_controls = []
            for x in range(n):
                char = board_data[y][x]
                is_queen = solution and (x, y) in solution
                
                cell = ft.Container(
                    content=ft.Text("Q" if is_queen else "", size=20, weight="bold", color="white"),
                    bgcolor=color_map[char],
                    width=45, height=45,
                    alignment=ft.alignment.Alignment(0, 0), 
                    border=ft.border.all(1, "black12"),
                    border_radius=4
                )
                row_controls.append(cell)
            rows.append(ft.Row(controls=row_controls, spacing=5, alignment=ft.MainAxisAlignment.CENTER))
        
        grid_display.content = ft.Column(controls=rows, spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.update()

    def load_board(e):
        try:
            if file_name_input.value:
                board = utils.file_to_board(file_name_input.value)
            else:
                board = [line.strip() for line in manual_input.value.split("\n") if line.strip()]
            
            valid, msg = utils.validate_board(board)
            status_text.value = msg
            if valid:
                state["board"] = board
                render_board(board)
            page.update()
        except Exception as ex:
            status_text.value = f"Error: {str(ex)}"
            page.update()

    async def start_game(e):
        if not state["board"]:
            status_text.value = "Load board dulu!"
            page.update()
            return

        state["is_running"] = True
        status_text.value = "Sedang mencari solusi..."
        page.update()

        if pure_bt_switch.value:
            answer, duration, step = await logic.play_pure(state["boardDict"], state["n"], page, render_board)
        else:
            answer, duration, step = await logic.play_bt(state["boardDict"], state["n"], page, render_board)

        if answer is None:
            status_text.value = "Tidak ada jawabannya, berikan board lain ya :)"
            state["solution"] = None
        else:
            status_text.value = "Solusi Ditemukan!"
            state["solution"] = answer  
            render_board(state["board"], answer)
        
        duration_text.value = f"Permainan berlangsung selama {duration * 1000:.2f} ms"
        step_counter.value = f"Permainan berlangsung dengan banyaknya konfigurasi: {step}"
        state["is_running"] = False
        page.update()

    def export_to_txt(e):
        if not state['board']:
            status_text.value="Tidak ada board untuk diekspor!"
            page.update()
            return
        try:
            solution = state.get('solution')
            board = state.get('board')
            n = state.get('n')

            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"queens_solution_{timestamp}.txt"


            with open(output_path, 'w') as f:
                for row in board:
                    f.write(row + '\n')
                
                f.write('\n')
                
                if solution:
                    f.write("Solution:\n")
                    result = [list(row) for row in board]
                    for (x, y) in solution:
                        result[y][x] = '#'
                    
                    for row in result:
                        f.write(''.join(row) + '\n')
                else:
                    f.write("Tidak/Belum ada solusi yang memenuhi. Harap jalankan programnya terlebih dahulu untuk mengetahui.\n")
            
            status_text.value = f"File disimpan: {output_path}"
            page.update()
        except Exception as ex:
            status_text.value = f"Error ekspor: {str(ex)}"
            page.update()


    
    def export_to_image(e):
        if not state["board"]:
            status_text.value = "Tidak ada board untuk diekspor!"
            page.update()
            return
        
        try:
            solution = state.get('solution')
            color_map = state.get('color_map')  
            
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"queens_solution_{timestamp}.png"
            
            saved_path = image_process.board_to_image(state["board"], solution, output_path, color_map=color_map)
            
            status_text.value = f"Gambar disimpan: {saved_path}"
            page.update()
            
        except Exception as ex:
            status_text.value = f"Error ekspor: {str(ex)}"
            page.update()

    page.add(
        ft.Row([
            ft.Column([
                ft.Text("Queens Visualizer", size=28, weight="bold"),
                grid_display,
            ], expand=2, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            ft.Column([
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("Konfigurasi Input", weight="bold"),
                            ft.Row([file_name_input, ft.IconButton(ft.Icons.REFRESH, on_click=load_board)]),
                            manual_input,
                            ft.ElevatedButton("Load Board", on_click=load_board, icon=ft.Icons.UPLOAD),
                           
                        ]), padding=15
                    )
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("Kontrol Algoritma", weight="bold"),
                            pure_bt_switch,
                            ft.Divider(),
                            status_text,
                            duration_text,
                            step_counter,
                            ft.FilledButton("MULAI PENCARIAN", icon=ft.Icons.PLAY_ARROW, 
                                           on_click=start_game, width=300, height=50),
                            ft.OutlinedButton("Ekspor ke Gambar", icon=ft.Icons.DOWNLOAD,
                                            on_click=export_to_image, width=300),
                            ft.OutlinedButton("Ekspor ke File Txt", icon=ft.Icons.DOWNLOAD,
                                            on_click=export_to_txt, width=300),
                        ]), padding=15
                    )
                )
            ], expand=1)
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)