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
        self.grid_columnconfigure(1, weight=2)

        back_frame = tk.Frame(self, bd=10)
        back_frame.grid(row=0, column=0, columnspan=2, sticky='we')

        btn_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        btn_frame.grid(row=1, column=0)
        # btn_frame.grid_propagate(1)

        fld_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        fld_frame.grid(row=1, column=1, sticky='wesn', padx=30, pady=30)

        btn_back = tk.Button(back_frame, text='Назад', command=lambda: self.destroy())
        btn_back.grid()


        # Все кнопки приводим в нормальное состояние
        def normal_btn():
            btn_class_soil['state'] = 'normal'
            btn_sign['state'] = 'normal'
            btn_possible_values['state'] = 'normal'
            btn_class_sign['state'] = 'normal'
            btn_class_values['state'] = 'normal'
            btn_check['state'] = 'normal'

        
        # Удаляем виджеты той кнопки, которая была нажата
        def delete_btn():
            if btn_class_soil['state'] == 'disabled':
                del_class_solid()
            elif btn_sign['state'] == 'disabled':
                del_sign()
            elif btn_possible_values['state'] == 'disabled':
                del_possible_values()
            elif btn_class_sign['state'] == 'disabled':
                del_class_sign()
            elif btn_class_values['state'] == 'disabled':
                del_class_values()
            elif btn_check['state'] == 'disabled':
                del_check()

        # Удаляются все виджеты для работы с классом
        def del_class_solid():
            class_name.grid_forget()
            class_name_entry.grid_forget()
            class_name_add.grid_forget()
            class_list.grid_forget()
        
        # Удаляются все виджеты для работы с признаками
        def del_sign():
            sign_name.grid_forget()
            sign_name_entry.grid_forget()
            sign_name_add.grid_forget()
            sign_list.grid_forget()

        # Удаляются все виджеты для работы с возможными значениями
        def del_possible_values():
            pass
        
        # Удаляются все виджеты для работы с признаками класса
        def del_class_sign():
            pass

        # Удаляются все виджеты для работы с значениями для класса
        def del_class_values():
            pass

        # Удаляются все виджеты для работы с проверкой полноты знаний
        def del_check():
            pass



        # Создаются необходимые виджеты для работы с классом
        def create_class_solid():
            delete_btn()
            normal_btn()
            btn_class_soil['state'] = 'disabled'

            global class_name, class_name_entry, class_name_add, class_list
            class_name = tk.Label(fld_frame, text='Название класса', bg='#D9D9D9')
            class_name.grid(row=0, column=0, sticky='w')
            class_name_entry = tk.Entry(fld_frame)
            class_name_entry.grid(row=1, column=0)
            class_name_add = tk.Button(fld_frame, text='Добавить')
            class_name_add.grid(row=1, column=1, padx=5)
            class_list = tk.Label(fld_frame, text='Список классов', bg='#D9D9D9')
            class_list.grid(row=2, column=0, sticky='w')

        # Создаются необходимые виджеты для работы с признаками
        def create_sign():
            delete_btn()
            normal_btn()
            btn_sign['state'] = 'disabled'
            
            global sign_name, sign_name_entry, sign_name_add, sign_list
            sign_name = tk.Label(fld_frame, text='Название признака', bg='#D9D9D9')
            sign_name.grid(row=0, column=0, sticky='w')
            sign_name_entry = tk.Entry(fld_frame)
            sign_name_entry.grid(row=1, column=0)
            sign_name_add = tk.Button(fld_frame, text='Добавить')
            sign_name_add.grid(row=1, column=1, padx=5)
            sign_list = tk.Label(fld_frame, text='Список признаков', bg='#D9D9D9')
            sign_list.grid(row=2, column=0, sticky='w')
        
        # Создаются необходимые виджеты для работы с возможными значениями
        def create_possible_values():
            delete_btn()
            normal_btn()
            btn_possible_values['state'] = 'disabled'

        # Создаются необходимые виджеты для работы с признаками класса
        def create_class_sign():
            delete_btn()
            normal_btn()
            btn_class_sign['state'] = 'disabled'

        # Создаются необходимые виджеты для работы с значениями для класса
        def create_class_values():
            delete_btn()
            normal_btn()
            btn_class_values['state'] = 'disabled'

        # Создаются необходимые виджеты для работы с проверкой полноты знаний
        def create_check():
            delete_btn()
            normal_btn()
            btn_check['state'] = 'disabled'


        btn_class_soil = tk.Button(btn_frame, text='Класс почвы', command=create_class_solid)
        btn_class_soil.grid(row=0, sticky='we', pady=5)
        btn_sign = tk.Button(btn_frame, text='Признаки', command=create_sign)
        btn_sign.grid(row=1, sticky='we', pady=5)
        btn_possible_values = tk.Button(btn_frame, text='Возможные значения', command=create_possible_values)
        btn_possible_values.grid(row=2, sticky='we', pady=5)
        btn_class_sign = tk.Button(btn_frame, text='Признаки класса', command=create_class_sign)
        btn_class_sign.grid(row=3, sticky='we', pady=5)
        btn_class_values = tk.Button(btn_frame, text='Значения для класса', command=create_class_values)
        btn_class_values.grid(row=4, sticky='we', pady=5)
        btn_check = tk.Button(btn_frame, text='Проверка полноты \nзнаний', command=create_check)
        btn_check.grid(row=5, sticky='we', pady=5)

        # При открытии окна кнопка "Класс почвы" уже нажата. Окно готово к работе с классами
        create_class_solid()

        # bt2 = tk.Button(fld_frame, text='bt2')
        # bt2.grid()

        

    

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