import tkinter as tk

# Главное окно
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
        
    # Открытие редактора БД
    def open_editor(self):
        EditorDB()
    
    # Решение задачи
    def open_solve(self):
        SolveTheTask()

# Окно для заполнения БД
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

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        back_frame = tk.Frame(self, bg='grey', bd=10)
        back_frame.grid(row=0, column=0, columnspan=2, sticky='we')

        btn_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        btn_frame.grid(row=1, column=0)

        fld_frame = tk.Frame(self, bg='#D9D9D9', bd=110)
        fld_frame.grid(row=1, column=1)

        btn_back = tk.Button(back_frame, text='Назад')
        btn_back.grid()
        
        btn_class_soil = tk.Button(btn_frame, text='Класс почвы')
        btn_class_soil.grid(row=0, sticky='we', pady=5)
        btn_sign = tk.Button(btn_frame, text='Признаки')
        btn_sign.grid(row=1, sticky='we', pady=5)
        btn_possible_values = tk.Button(btn_frame, text='Возможные значения')
        btn_possible_values.grid(row=2, sticky='we', pady=5)
        btn_class_sign = tk.Button(btn_frame, text='Признаки класса')
        btn_class_sign.grid(row=3, sticky='we', pady=5)
        btn_class_values = tk.Button(btn_frame, text='Значения для класса')
        btn_class_values.grid(row=4, sticky='we', pady=5)
        btn_check = tk.Button(btn_frame, text='Проверка полноты \nзнаний')
        btn_check.grid(row=5, sticky='we', pady=5)

        bt2 = tk.Button(fld_frame, text='bt2')
        bt2.grid()

    # По нажатию кнопок в btn_frame будут отображаться данные в fld_frame
    def create_field():
        pass

# Окно для решения задачи
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
    root.config()
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()