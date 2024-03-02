import tkinter as tk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        btn_frame = tk.Frame()
        btn_frame.grid(row=0, column=0)

        btn_open_editor = tk.Button(btn_frame, text='Редактировать \nбазу знаний', command=self.open_editor, width=20)
        btn_open_editor.grid(sticky='we', pady=10)

        btn_open_solve = tk.Button(btn_frame, text='Решить задачу', command=self.open_solve)
        btn_open_solve.grid(sticky='we', pady=10)
        

    def open_editor(self):
        EditorDB()
    
    def open_solve(self):
        SolveTheTask()

class EditorDB(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_editorDB()

    def init_editorDB(self):
        self.title('Редактор базы знаний')
        self.geometry('650x450+350+250')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

class SolveTheTask(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_solve_the_task()
    
    def init_solve_the_task(self):
        self.title('Система ввода данных')
        self.geometry('650x450+350+250')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.grid()
    root.title('Выбор пользователя')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()