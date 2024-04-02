import tkinter as tk
from tkinter import ttk
import sqlite3
from db_methods import get_classes, get_signs, get_bad_classes

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
            soil_classes_list.grid_forget()
            class_name_del.grid_forget()
        
        # Удаляются все виджеты для работы с признаками
        def del_sign():
            sign_name.grid_forget()
            sign_name_entry.grid_forget()
            sign_name_add.grid_forget()
            sign_list.grid_forget()
            sign_list_label.grid_forget()
            sign_name_del.grid_forget()

        # Удаляются все виджеты для работы с возможными значениями
        def del_possible_values():
            possible_values_name.grid_forget()
            possible_values_combobox.grid_forget()
            possible_values_type.grid_forget()
            num_label.grid_forget()
            enum_label.grid_forget()
            type_frame.grid_forget()
            list_type.grid_forget()
            type_num.grid_forget()
            type_enum.grid_forget()
        
        # Удаляются все виджеты для работы с признаками класса
        def del_class_sign():
            class_sign_name.grid_forget()
            class_sign_combobox.grid_forget()
            sign.grid_forget()

        # Удаляются все виджеты для работы с значениями для класса
        def del_class_values():
            class_values_name.grid_forget()
            sign_values_name.grid_forget()
            class_values_combobox.grid_forget()
            list_sign.grid_forget()

        # Удаляются все виджеты для работы с проверкой полноты знаний
        def del_check():
            check_label.grid_forget()
            bad_classes.grid_forget()



        # Создаются необходимые виджеты для работы с классом
        def create_class_solid():
            delete_btn()
            normal_btn()
            btn_class_soil['state'] = 'disabled'

            global class_name, class_name_entry, class_name_add, class_list, soil_classes_list, class_name_del
            class_name = tk.Label(fld_frame, text='Название класса', bg='#D9D9D9')
            class_name.grid(row=0, column=0, sticky='w')
            class_name_entry = tk.Entry(fld_frame)
            class_name_entry.grid(row=1, column=0)

            # Добавление нового класса
            def add_class():
                new_class = class_name_entry.get()
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                query = '''INSERT INTO soil_class (soil_class_name)
                            VALUES
                                (:p_name)'''
                cursor.execute(query, {'p_name': new_class})

                conn.commit()
                conn.close()

                soil_classes_list.insert(tk.END, new_class)

            class_name_add = tk.Button(fld_frame, text='Добавить', command=add_class)
            class_name_add.grid(row=1, column=1, padx=5)
            class_list = tk.Label(fld_frame, text='Список классов', bg='#D9D9D9')
            class_list.grid(row=2, column=0, sticky='w')
            soil_classes_var = tk.Variable(value=get_classes())
            soil_classes_list = tk.Listbox(fld_frame, listvariable=soil_classes_var, width=30)
            soil_classes_list.grid(row=3, column=0, columnspan=2)
            
            # Удаление класса
            def del_class():
                selection = soil_classes_list.curselection()
                
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                query = '''DELETE
                            FROM soil_class
                            WHERE soil_class_name = :p_name'''
                cursor.execute(query, {'p_name': soil_classes_list.get(selection[0])})

                conn.commit()
                conn.close()

                soil_classes_list.delete(selection[0])

            class_name_del = tk.Button(fld_frame, text='Удалить', command=del_class)
            class_name_del.grid(row=4, column=1, pady=5)



        # Создаются необходимые виджеты для работы с признаками
        def create_sign():
            delete_btn()
            normal_btn()
            btn_sign['state'] = 'disabled'
            
            global sign_name, sign_name_entry, sign_name_add, sign_list_label, sign_list, sign_name_del
            sign_name = tk.Label(fld_frame, text='Название признака', bg='#D9D9D9')
            sign_name.grid(row=0, column=0, sticky='w')
            sign_name_entry = tk.Entry(fld_frame)
            sign_name_entry.grid(row=1, column=0)

            # Добавление нового признака
            def add_sign():
                new_sign = sign_name_entry.get()
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                query = '''INSERT INTO feature (feature_name)
                            VALUES
                                (:p_name)'''
                cursor.execute(query, {'p_name': new_sign})

                conn.commit()
                conn.close()

                sign_list.insert(tk.END, new_sign)

            sign_name_add = tk.Button(fld_frame, text='Добавить', command=add_sign)
            sign_name_add.grid(row=1, column=1, padx=5)
            sign_list_label = tk.Label(fld_frame, text='Список признаков', bg='#D9D9D9')
            sign_list_label.grid(row=2, column=0, sticky='w')
            sign_list_var = tk.Variable(value=get_signs())
            sign_list = tk.Listbox(fld_frame, listvariable=sign_list_var, width=30)
            sign_list.grid(row=3, column=0, columnspan=2)
            
            # Удаление признака
            def del_sign():
                selection = sign_list.curselection()
                
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                query = '''DELETE
                            FROM feature
                            WHERE feature_name = :p_name'''
                cursor.execute(query, {'p_name': sign_list.get(selection[0])})

                conn.commit()
                conn.close()

                sign_list.delete(selection[0])

            sign_name_del = tk.Button(fld_frame, text='Удалить', command=del_sign)
            sign_name_del.grid(row=4, column=1, pady=5)
        


        # Создаются необходимые виджеты для работы с возможными значениями
        def create_possible_values():
            delete_btn()
            normal_btn()
            btn_possible_values['state'] = 'disabled'

            global possible_values_name, possible_values_combobox, possible_values_type
            possible_values_name = tk.Label(fld_frame, text='Выберите признак', bg='#D9D9D9')
            possible_values_name.grid(row=0, column=0, columnspan=2, sticky='w')
            
            cur_sign = tk.StringVar()
            possible_values_combobox = ttk.Combobox(fld_frame, textvariable=cur_sign, width=30)
            possible_values_combobox['values'] = get_signs()
            possible_values_combobox.grid(row=1, column=0)

            possible_values_type = tk.Label(fld_frame, text='Тип значения', bg='#D9D9D9')
            possible_values_type.grid(row=2, column=0, columnspan=2, sticky='w')


            global type_frame, num_label, num_l2, num_e1, num_e2, num_l3, num_b, enum_label, enum_e, enum_b, list_type, type_num, type_enum

            selected_possible_values = tk.StringVar()

            # Фрэйм для красивого вывода полей ввода
            type_frame = tk.Frame(fld_frame, bg='#D9D9D9', bd=10)
            type_frame.grid(row=5, column=0, columnspan=2, sticky='we')

            # Виджеты для числового типа
            num_label = tk.Label(fld_frame, text='Возможный интервал значения', bg='#D9D9D9')
            num_l2 = tk.Label(type_frame, text='[', bg='#D9D9D9')
            num_e1 = tk.Entry(type_frame, width=5)
            num_e2 = tk.Entry(type_frame, width=5)
            num_l3 = tk.Label(type_frame, text=']', bg='#D9D9D9')
            num_b = tk.Button(type_frame, text='Добавить')

            # Виджеты для перечислимого типа
            enum_label = tk.Label(fld_frame, text='Возможное значение', bg='#D9D9D9')
            enum_e = tk.Entry(type_frame)
            enum_b = tk.Button(type_frame, text='Добавить')

            # Когда выбран числовой тип
            def select_type_num():
                enum_label.grid_forget()
                enum_e.grid_forget()
                enum_b.grid_forget()

                num_label.grid(row=4, column=0, columnspan=3, sticky='w')
                num_l2.grid(row=0, column=0, sticky='w')
                num_e1.grid(row=0, column=1, padx=3)
                num_e2.grid(row=0, column=2, padx=3)
                num_l3.grid(row=0, column=3, sticky='w')
                num_b.grid(row=0, column=4)
                list_type.grid(row=6, column=0, sticky='w')
            
            # Когда выбран перечислимый тип
            def select_type_enum():
                num_label.grid_forget()
                num_l2.grid_forget()
                num_e1.grid_forget()
                num_e2.grid_forget()
                num_l3.grid_forget()
                num_b.grid_forget()

                enum_label.grid(row=4, column=0, columnspan=3, sticky='w')
                enum_e.grid(row=0, column=0)
                enum_b.grid(row=0, column=1, padx=5)
                list_type.grid(row=6, column=0, sticky='w')
            
            # Кнопки для выбора
            type_num = tk.Radiobutton(fld_frame, text='Числовой', value='Числовой', variable=selected_possible_values, command=select_type_num, bg='#D9D9D9')
            type_num.grid(row=3, column=0)

            type_enum = tk.Radiobutton(fld_frame, text='Перечислимый', value='Перечислимый', variable=selected_possible_values, command=select_type_enum, bg='#D9D9D9')
            type_enum.grid(row=3, column=1)

            list_type = tk.Label(fld_frame, text='Список значений', bg='#D9D9D9')
            # -------------------------------------------------------------------------------Добавить список значений признаков



        # Создаются необходимые виджеты для работы с признаками класса
        def create_class_sign():
            delete_btn()
            normal_btn()
            btn_class_sign['state'] = 'disabled'

            global class_sign_name, class_sign_combobox, sign
            class_sign_name = tk.Label(fld_frame, text='Выберите класс', bg='#D9D9D9')
            class_sign_name.grid(row=0, column=0, sticky='w')

            cur_class = tk.StringVar()
            class_sign_combobox = ttk.Combobox(fld_frame, textvariable=cur_class, width=30)
            class_sign_combobox['values'] = get_classes()
            class_sign_combobox.grid(row=1, column=0)

            sign = tk.Label(fld_frame, text='Признаки', bg='#D9D9D9')
            sign.grid(row=2, column=0, sticky='w')

            # -------------------------------------------------------------------------------Добавить список признаков



        # Создаются необходимые виджеты для работы с значениями для класса
        def create_class_values():
            delete_btn()
            normal_btn()
            btn_class_values['state'] = 'disabled'

            global class_values_name, sign_values_name, class_values_combobox, list_sign
            class_values_name = tk.Label(fld_frame, text='Выберите класс', bg='#D9D9D9')
            class_values_name.grid(row=0, column=0, sticky='w')

            cur_class = tk.StringVar()
            class_values_combobox = ttk.Combobox(fld_frame, textvariable=cur_class, width=30)
            class_values_combobox['values'] = get_classes()
            class_values_combobox.grid(row=1, column=0)

            sign_values_name = tk.Label(fld_frame, text='Выберите признак', bg='#D9D9D9')
            sign_values_name.grid(row=2, column=0, sticky='w')
            # -------------------------------------------------------------------------------Добавить выбор признака
            list_sign = tk.Label(fld_frame, text='Список значений', bg='#D9D9D9')
            list_sign.grid(row=4, column=0, sticky='w')
            # -------------------------------------------------------------------------------Добавить список значений признаков



        # Создаются необходимые виджеты для работы с проверкой полноты знаний
        def create_check():
            delete_btn()
            normal_btn()
            btn_check['state'] = 'disabled'

            global check_label, bad_classes

            check_label = tk.Label(fld_frame, text='Проверку не прошли:', bg='#D9D9D9', fg='#CC0000')
            check_label.grid(row=0, column=0, sticky='w')

            bad_classes = tk.Label(fld_frame, text=get_bad_classes(), bg='#D9D9D9')
            bad_classes.grid(row=1, column=0, sticky='w')


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

    

# Окно для решения задачи
class SolveTheTask(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_solve_the_task()
    
    def init_solve_the_task(self):
        self.title('Система ввода данных')
        self.geometry('650x450+350+250')
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.grab_set()
        self.focus_set()

        back_frame = tk.Frame(self, bd=10)
        back_frame.grid(row=0, column=0, columnspan=2, sticky='we')

        sign_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        sign_frame.grid(row=1, column=0, sticky='wesn', padx=30, pady=30)

        fld_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        fld_frame.grid(row=1, column=1, sticky='wesn', padx=30, pady=30)

        btn_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        btn_frame.grid(row=2, column=0, columnspan=2, sticky='we')

        btn_back = tk.Button(back_frame, text='Назад', command=lambda: self.destroy())
        btn_back.grid()


        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)

        btn_DB = tk.Button(btn_frame, text='Просмотр базы знаний')
        btn_DB.grid(row=0, column=0)

        btn_define_class = tk.Button(btn_frame, text='Определить класс почвы')
        btn_define_class.grid(row=0, column=1)



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