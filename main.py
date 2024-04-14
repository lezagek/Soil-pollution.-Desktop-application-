import tkinter as tk
from tkinter import ttk
import sqlite3
from db_methods import get_classes, get_signs, get_sign_id, get_sign_type, get_sign_num_value, get_sign_enum_value, get_class_id, \
    get_class_signs, get_signs_not_in_class, get_class_sign_num_value, get_class_sign_enum_value, get_bad_classes, get_bad_signs, get_bad_classes_sign, \
    get_soil_class_feature_id_and_soil_class_id, get_soil_class_name, get_sign_name_from_soil_class_feature_id

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
            list_type_label.grid_forget()
            type_num.grid_forget()
            type_enum.grid_forget()
            possible_values_button.grid_forget()
            sign_num_value_list.grid_forget()
            sign_enum_value_list.grid_forget()
            possible_values_del.grid_forget()
        
        # Удаляются все виджеты для работы с признаками класса
        def del_class_sign():
            class_sign_name.grid_forget()
            class_sign_combobox.grid_forget()
            class_sign_button.grid_forget()
            sign.grid_forget()
            sign_combobox.grid_forget()
            class_sign_add_button.grid_forget()
            class_sign.grid_forget()
            class_sign_list.grid_forget()
            class_sign_del.grid_forget()

        # Удаляются все виджеты для работы с значениями для класса
        def del_class_values():
            class_values_name.grid_forget()
            sign_values_name.grid_forget()
            class_values_combobox.grid_forget()
            class_sign_values_button.grid_forget()
            class_sign_values_combobox.grid_forget()
            class_values_button.grid_forget()
            list_sign_label.grid_forget()
            num_value_label.grid_forget()
            num_value_l2.grid_forget()
            num_value_e1.grid_forget()
            num_value_e2.grid_forget()
            num_value_e2.grid_forget()
            num_value_l3.grid_forget()
            num_value_b.grid_forget()
            enum_value_label.grid_forget()
            enum_value_e.grid_forget()
            enum_value_b.grid_forget()
            class_sign_num_value_list.grid_forget()
            class_sign_enum_value_list.grid_forget()
            class_sign_values_del.grid_forget()
            error_message.grid_forget()
            if_type_none_label.grid_forget()

        # Удаляются все виджеты для работы с проверкой полноты знаний
        def del_check():
            check_label.grid_forget()
            bad_classes_label.grid_forget()
            bad_classes.grid_forget()
            bad_signs_label.grid_forget()
            bad_signs.grid_forget()
            bad_classes_sign_label.grid_forget()
            bad_classes_sign.grid_forget()



        # Создаются необходимые виджеты для работы с классом
        def create_class_solid():
            delete_btn()
            normal_btn()
            btn_class_soil['state'] = 'disabled'

            global class_name, class_name_entry, class_name_add, class_list, soil_classes_list, class_name_del
            class_name = tk.Label(fld_frame, text='Название класса', bg='#D9D9D9')
            class_name.grid(row=0, column=0, sticky='w')
            class_name_entry = tk.Entry(fld_frame, width=30)
            class_name_entry.grid(row=1, column=0)

            # Добавление нового класса
            def add_class():
                if class_name_entry.get():
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
            soil_classes_list.grid(row=3, column=0)
            
            # Удаление класса
            def del_class():
                selection = soil_classes_list.curselection()
                
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()
                cursor.execute("PRAGMA foreign_keys = ON")

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
            sign_name_entry = tk.Entry(fld_frame, width=30)
            sign_name_entry.grid(row=1, column=0)

            # Добавление нового признака
            def add_sign():
                if sign_name_entry.get():
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
            sign_list.grid(row=3, column=0)
            
            # Удаление признака
            def del_sign():
                selection = sign_list.curselection()
                
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()
                cursor.execute("PRAGMA foreign_keys = ON")

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

            global type_frame, num_label, num_l2, num_e1, num_e2, num_l3, num_b, enum_label, enum_e, enum_b, list_type_label,  type_num, type_enum, \
                possible_values_button, sign_num_value_list, sign_enum_value_list, possible_values_del

            # Фрэйм для красивого вывода полей ввода
            type_frame = tk.Frame(fld_frame, bg='#D9D9D9', bd=10)

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
                list_type_label.grid(row=6, column=0, sticky='w')
            
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
                list_type_label.grid(row=6, column=0, sticky='w')

            # Вывод возможных значений
            def view_possible_value():
                if cur_sign.get():
                    possible_values_type.grid(row=2, column=0, columnspan=2, sticky='w')
                    type_frame.grid(row=5, column=0, columnspan=2, sticky='we')
                    type_num.grid(row=3, column=0)
                    type_enum.grid(row=3, column=1)
                    global sign_type, sign_id, sign_value
                    sign_type, sign_id = get_sign_type(cur_sign.get())
                    sign_num_value_list.delete(first=0, last=tk.END)
                    sign_enum_value_list.delete(first=0, last=tk.END)
                    
                    # Для числового типа
                    if sign_type == 0:
                        select_type_num()
                        sign_enum_value_list.grid_forget()
                        sign_value = get_sign_num_value(sign_id)
                        
                        for i in range(len(sign_value)):
                            if sign_value[i][2] == None:
                                sign_value[i] = [sign_value[i][0], sign_value[i][1], '+inf']
                            
                            temp = f'[{sign_value[i][1]}, {sign_value[i][2]}]'
                            sign_num_value_list.insert(tk.END, temp)
                        
                        sign_num_value_list.grid(row=7, column=0)
                        possible_values_del.grid(row=8, column=1, pady=5)

                    # Для перечислимого типа
                    elif sign_type == 1:
                        select_type_enum()
                        sign_num_value_list.grid_forget()
                        sign_value = get_sign_enum_value(sign_id)

                        for i in range(len(sign_value)):
                            sign_enum_value_list.insert(tk.END, sign_value[i][1])

                        sign_enum_value_list.grid(row=7, column=0)
                        possible_values_del.grid(row=8, column=1, pady=5)


            # Добавление нового возможного значения числового признака
            def add_num_value():
                new_left = num_e1.get()
                new_right = num_e2.get()

                sign_id = get_sign_id(cur_sign.get())[0]

                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                query = '''UPDATE feature
                            SET feature_type = 0
                            WHERE feature_id = :p_id'''
                cursor.execute(query, {'p_id': sign_id})

                if new_right == '':
                    query = '''INSERT INTO possible_num_feature (feature_id, left_border_value)
                                VALUES
                                    (:p_id, :p_left)'''
                    cursor.execute(query, {'p_id': sign_id, 'p_left': new_left})
                    new_right = '+inf'
                else:
                    query = '''INSERT INTO possible_num_feature (feature_id, left_border_value, right_border_value)
                                VALUES
                                    (:p_id, :p_left, :p_right)'''
                    cursor.execute(query, {'p_id': sign_id, 'p_left': new_left, 'p_right': new_right})
                conn.commit()
                conn.close()

                view_possible_value()
            
            # Добавление нового возможного значения перечислимого признака
            def add_enum_value():
                new_enum_value = enum_e.get()

                sign_id = get_sign_id(cur_sign.get())[0]

                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                query = '''UPDATE feature
                            SET feature_type = 1
                            WHERE feature_id = :p_id'''
                cursor.execute(query, {'p_id': sign_id})

                query = '''INSERT INTO possible_enum_feature (feature_id, possible_enum_value)
                            VALUES
                                (:p_id, :p_value)'''
                cursor.execute(query, {'p_id': sign_id, 'p_value': new_enum_value})
                conn.commit()
                conn.close()

                view_possible_value()

            # Виджеты для числового типа
            num_label = tk.Label(fld_frame, text='Возможный интервал значения', bg='#D9D9D9')
            num_l2 = tk.Label(type_frame, text='[', bg='#D9D9D9')
            num_e1 = tk.Entry(type_frame, width=5)
            num_e2 = tk.Entry(type_frame, width=5)
            num_l3 = tk.Label(type_frame, text=']', bg='#D9D9D9')
            num_b = tk.Button(type_frame, text='Добавить', command=add_num_value)

            # Виджеты для перечислимого типа
            enum_label = tk.Label(fld_frame, text='Возможное значение', bg='#D9D9D9')
            enum_e = tk.Entry(type_frame)
            enum_b = tk.Button(type_frame, text='Добавить', command=add_enum_value)
            
            selected_possible_values = tk.StringVar()
            # Кнопки для выбора
            type_num = tk.Radiobutton(fld_frame, text='Числовой', value='Числовой', variable=selected_possible_values, command=select_type_num, bg='#D9D9D9')
            type_enum = tk.Radiobutton(fld_frame, text='Перечислимый', value='Перечислимый', variable=selected_possible_values, command=select_type_enum, bg='#D9D9D9')
            
            list_type_label = tk.Label(fld_frame, text='Список значений', bg='#D9D9D9')
            
            sign_num_value_list = tk.Listbox(fld_frame, width=30, height=5)
            sign_enum_value_list = tk.Listbox(fld_frame, width=30, height=5)

            possible_values_button = tk.Button(fld_frame, text='Список значений', command=view_possible_value)
            possible_values_button.grid(row=1, column=1, padx=5)

            # Удаление возможного значения признака
            def del_possible_value():
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                # Для числового типа
                if sign_type == 0:
                    selection = sign_num_value_list.curselection()
                    query = '''DELETE
                                FROM possible_num_feature
                                WHERE possible_num_feature_id = :p_id'''
                    cursor.execute(query, {'p_id': sign_value[selection[0]][0]})

                    conn.commit()
                    conn.close()

                    sign_num_value_list.delete(selection[0])
                
                # Для перечислимого типа
                elif sign_type == 1:
                    selection = sign_enum_value_list.curselection()
                    query = '''DELETE
                                FROM possible_enum_feature
                                WHERE possible_enum_feature_id = :p_id'''
                    cursor.execute(query, {'p_id': sign_value[selection[0]][0]})

                    conn.commit()
                    conn.close()

                    sign_enum_value_list.delete(selection[0])

            possible_values_del = tk.Button(fld_frame, text='Удалить', command=del_possible_value)



        # Создаются необходимые виджеты для работы с признаками класса
        def create_class_sign():
            delete_btn()
            normal_btn()
            btn_class_sign['state'] = 'disabled'

            global class_sign_name, class_sign_combobox, class_sign_button, sign, sign_combobox, class_sign_add_button, class_sign, class_sign_list, class_sign_del
            class_sign_name = tk.Label(fld_frame, text='Выберите класс', bg='#D9D9D9')
            class_sign_name.grid(row=0, column=0, sticky='w')

            cur_class = tk.StringVar()
            class_sign_combobox = ttk.Combobox(fld_frame, textvariable=cur_class, width=30)
            class_sign_combobox['values'] = get_classes()
            class_sign_combobox.grid(row=1, column=0)

            def view_class_signs():
                if cur_class.get():
                    sign.grid(row=2, column=0, sticky='w')
                    sign_combobox.grid(row=3, column=0)
                    class_sign_add_button.grid(row=3, column=1, padx=5, sticky='w')
                    class_sign.grid(row=4, column=0, sticky='w')
                    class_sign_list.delete(first=0, last=tk.END)

                    global class_id, class_signs
                    class_id = get_class_id(cur_class.get())[0]
                    
                    class_signs = get_class_signs(class_id)
                    for i in range(len(class_signs)):
                        class_sign_list.insert(tk.END, class_signs[i][1])

                    class_sign_list.grid(row=5, column=0)
                    class_sign_del.grid(row=6, column=1, pady=5, sticky='w')

                    sign_combobox['values'] = get_signs_not_in_class(class_id)

            class_sign_button = tk.Button(fld_frame, text='Посмотреть признаки класса', command=view_class_signs)
            class_sign_button.grid(row=1, column=1, padx=5)

            sign = tk.Label(fld_frame, text='Признаки', bg='#D9D9D9')

            cur_sign = tk.StringVar()
            sign_combobox = ttk.Combobox(fld_frame, textvariable=cur_sign, width=30)

            # Добавление признака у класса
            def add_class_sign():
                if cur_sign.get():
                    class_sign_id = get_sign_id(cur_sign.get())[0]

                    conn = sqlite3.connect('soil_pollution.sqlite')
                    cursor = conn.cursor()

                    query = '''INSERT INTO soil_class_feature (soil_class_id, feature_id)
                                VALUES
                                    (:p_c_id, :p_f_id)'''
                    cursor.execute(query, {'p_c_id': class_id, 'p_f_id': class_sign_id})

                    conn.commit()
                    conn.close()

                    view_class_signs()

            class_sign_add_button = tk.Button(fld_frame, text='Добавить', command=add_class_sign)

            class_sign = tk.Label(fld_frame, text='Признаки класса', bg='#D9D9D9')
            class_sign_list = tk.Listbox(fld_frame, width=30)

            # Удаление признака у класса
            def del_class_sign():
                selection = class_sign_list.curselection()
                class_sign_id = get_sign_id(class_sign_list.get(selection[0]))[0]

                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                query = '''DELETE
                            FROM soil_class_feature
                            WHERE soil_class_id = :p_c_id AND feature_id = :p_f_id'''
                cursor.execute(query, {'p_c_id': class_id, 'p_f_id': class_sign_id})

                conn.commit()
                conn.close()

                class_sign_list.delete(selection[0])

            class_sign_del = tk.Button(fld_frame, text='Удалить', command=del_class_sign)



        # Создаются необходимые виджеты для работы с значениями для класса
        def create_class_values():
            delete_btn()
            normal_btn()
            btn_class_values['state'] = 'disabled'

            global class_values_name, sign_values_name, class_values_combobox, class_sign_values_button, class_sign_values_combobox, class_values_button, \
                type_frame_values, list_sign_label, class_sign_num_value_list, class_sign_enum_value_list, class_sign_values_del, error_message, if_type_none_label
            class_values_name = tk.Label(fld_frame, text='Выберите класс', bg='#D9D9D9')
            class_values_name.grid(row=0, column=0, sticky='w')

            cur_class = tk.StringVar()
            class_values_combobox = ttk.Combobox(fld_frame, textvariable=cur_class, width=30)
            class_values_combobox['values'] = get_classes()
            class_values_combobox.grid(row=1, column=0)
            
            cur_sign = tk.StringVar()
            class_sign_values_combobox = ttk.Combobox(fld_frame, textvariable=cur_sign, width=30)

            def view_class_values_signs():
                if cur_class.get():
                    sign_values_name.grid(row=2, column=0, sticky='w')
                    global class_id, class_signs
                    class_id = get_class_id(cur_class.get())[0]

                    class_signs = get_class_signs(class_id)
                    signs = []
                    for i in range(len(class_signs)):
                        signs.append(class_signs[i][1])

                    class_sign_values_combobox['values'] = signs
                    class_sign_values_combobox.grid(row=3, column=0)
                    class_values_button.grid(row=3, column=1, padx=5)

            class_sign_values_button = tk.Button(fld_frame, text='Посмотреть признаки класса', command=view_class_values_signs)
            class_sign_values_button.grid(row=1, column=1, padx=5)

            sign_values_name = tk.Label(fld_frame, text='Выберите признак', bg='#D9D9D9')

            # Фрэйм для красивого вывода полей ввода
            type_frame_values = tk.Frame(fld_frame, bg='#D9D9D9', bd=10)

            # Когда выбран числовой тип
            def select_type_num():
                enum_value_label.grid_forget()
                enum_value_e.grid_forget()
                enum_value_b.grid_forget()

                num_value_label.grid(row=4, column=0, columnspan=3, sticky='w')
                num_value_l2.grid(row=0, column=0, sticky='w')
                num_value_e1.grid(row=0, column=1, padx=3)
                num_value_e2.grid(row=0, column=2, padx=3)
                num_value_l3.grid(row=0, column=3, sticky='w')
                num_value_b.grid(row=0, column=4)
                list_sign_label.grid(row=6, column=0, sticky='w')
            
            # Когда выбран перечислимый тип
            def select_type_enum():
                num_value_label.grid_forget()
                num_value_l2.grid_forget()
                num_value_e1.grid_forget()
                num_value_e2.grid_forget()
                num_value_l3.grid_forget()
                num_value_b.grid_forget()

                enum_value_label.grid(row=4, column=0, columnspan=3, sticky='w')
                enum_value_e.grid(row=0, column=0)
                enum_value_b.grid(row=0, column=1, padx=5)
                list_sign_label.grid(row=6, column=0, sticky='w')

            # Вывод возможных значений
            def view_class_signs_values():
                if cur_sign.get():
                    type_frame_values.grid(row=5, column=0, columnspan=2, sticky='we')
                    
                    global sign_type, sign_id, sign_value
                    sign_type, sign_id = get_sign_type(cur_sign.get())
                    
                    # Если признак не заполнен
                    if sign_type == None:
                        if_type_none_label.grid(row=4, column=0)
                        
                    # Для числового типа
                    elif sign_type == 0:
                        if_type_none_label.grid_forget()
                        select_type_num()
                        class_sign_enum_value_list.grid_forget()
                        class_sign_num_value_list.delete(first=0, last=tk.END)
                        sign_value = get_class_sign_num_value(class_id, sign_id)
                        
                        for i in range(len(sign_value)):
                            if sign_value[i][2] == None:
                                sign_value[i] = [sign_value[i][0], sign_value[i][1], '+inf']
                            
                            temp = f'[{sign_value[i][1]}, {sign_value[i][2]}]'
                            class_sign_num_value_list.insert(tk.END, temp)
                        
                        class_sign_num_value_list.grid(row=7, column=0)
                        class_sign_values_del.grid(row=8, column=1, pady=5)

                    # Для перечислимого типа
                    elif sign_type == 1:
                        if_type_none_label.grid_forget()
                        select_type_enum()
                        class_sign_num_value_list.grid_forget()
                        class_sign_enum_value_list.delete(first=0, last=tk.END)
                        sign_value = get_class_sign_enum_value(class_id, sign_id)

                        for i in range(len(sign_value)):
                            class_sign_enum_value_list.insert(tk.END, sign_value[i][1])

                        class_sign_enum_value_list.grid(row=7, column=0)
                        class_sign_values_del.grid(row=8, column=1, pady=5)

            class_values_button = tk.Button(fld_frame, text='Посмотреть значения класса', command=view_class_signs_values)
            if_type_none_label = tk.Label(fld_frame, text='Признак не заполнен!', bg='#D9D9D9', fg='#CC0000')
            
            # Добавление нового возможного значения числового признака класса
            def add_class_num_value():
                new_left = num_value_e1.get()
                new_right = num_value_e2.get()

                sign_value = get_sign_num_value(sign_id)
                sign_new_value = []

                # Предел значений признака для сообщения ошибки 
                range_error = ''

                for i in range(len(sign_value)):
                    if sign_value[i][2] == None:
                        sign_new_value.append([sign_value[i][0], sign_value[i][1], '+inf'])
                    else:
                        sign_new_value.append([sign_value[i][0], sign_value[i][1], sign_value[i][2]])
                    range_error += f'[{sign_new_value[i][1]}, {sign_new_value[i][2]}]'

                # Если введённые значения выходят за диапазон значений признака
                if new_left == '' or int(new_left) < sign_value[0][1] or (sign_value[0][2] != None and new_right == None) or \
                    (sign_value[0][2] != None and int(new_right) > sign_value[0][2]):
                    error_message['text'] = f'Значение должно быть в диапазоне {range_error}'
                    error_message.grid(row=9, column=0, sticky='w')
                else:
                    error_message.grid_forget()
                    conn = sqlite3.connect('soil_pollution.sqlite')
                    cursor = conn.cursor()

                    query = '''SELECT soil_class_feature_id
                                FROM soil_class_feature
                                WHERE soil_class_id = :p_c_id AND feature_id = :p_f_id'''
                    cursor.execute(query, {'p_c_id': class_id, 'p_f_id': sign_id})

                    soil_class_feature_id = cursor.fetchall()[0][0]

                    if new_right == '':
                        query = '''INSERT INTO soil_class_num_feature (soil_class_feature_id, left_border_value)
                                    VALUES
                                        (:p_id, :p_left)'''
                        cursor.execute(query, {'p_id': soil_class_feature_id, 'p_left': new_left})
                        new_right = '+inf'
                    else:
                        query = '''INSERT INTO soil_class_num_feature (soil_class_feature_id, left_border_value, right_border_value)
                                    VALUES
                                        (:p_id, :p_left, :p_right)'''
                        cursor.execute(query, {'p_id': soil_class_feature_id, 'p_left': new_left, 'p_right': new_right})
                    
                    conn.commit()
                    conn.close()

                    view_class_signs_values()
            
            # Добавление нового возможного значения перечислимого признака класса
            def add_class_enum_value():
                new_enum_value = enum_value_e.get()

                sign_value = get_sign_enum_value(sign_id)
                sign_new_value = []

                is_in_feature = False

                for i in range(len(sign_value)):
                    if new_enum_value == sign_value[i][1]:
                        is_in_feature = True
                    sign_new_value.append(sign_value[i][1])

                # Предел значений признака для сообщения ошибки 
                range_error = ', '.join(sign_new_value)

                # Если введённые значения выходят за диапазон значений признака
                if not is_in_feature:
                    error_message['text'] = f'Значение должно совпадать с одним из значений признака: \n{range_error}'
                    error_message.grid(row=9, column=0, columnspan=2, sticky='w')
                else:
                    error_message.grid_forget()
                    conn = sqlite3.connect('soil_pollution.sqlite')
                    cursor = conn.cursor()

                    query = '''SELECT soil_class_feature_id
                                FROM soil_class_feature
                                WHERE soil_class_id = :p_c_id AND feature_id = :p_f_id'''
                    cursor.execute(query, {'p_c_id': class_id, 'p_f_id': sign_id})

                    soil_class_feature_id = cursor.fetchall()[0][0]

                    query = '''SELECT possible_enum_feature_id
                                FROM possible_enum_feature
                                WHERE feature_id = :p_id AND possible_enum_value = :p_name'''
                    cursor.execute(query, {'p_id': sign_id, 'p_name': new_enum_value})

                    possible_enum_feature_id = cursor.fetchall()[0][0]

                    query = '''INSERT INTO soil_class_enum_feature (soil_class_feature_id, possible_enum_feature_id)
                                VALUES
                                    (:p_c_id, :p_f_id)'''
                    cursor.execute(query, {'p_c_id': soil_class_feature_id, 'p_f_id': possible_enum_feature_id})

                    conn.commit()
                    conn.close()

                    view_class_signs_values()

            global num_value_label, num_value_l2, num_value_e1, num_value_e2, num_value_e2, num_value_l3, num_value_b, enum_value_label, enum_value_e, enum_value_b
            # Виджеты для числового типа
            num_value_label = tk.Label(fld_frame, text='Возможный интервал значения', bg='#D9D9D9')
            num_value_l2 = tk.Label(type_frame_values, text='[', bg='#D9D9D9')
            num_value_e1 = tk.Entry(type_frame_values, width=5)
            num_value_e2 = tk.Entry(type_frame_values, width=5)
            num_value_l3 = tk.Label(type_frame_values, text=']', bg='#D9D9D9')
            num_value_b = tk.Button(type_frame_values, text='Добавить', command=add_class_num_value)

            # Виджеты для перечислимого типа
            enum_value_label = tk.Label(fld_frame, text='Возможное значение', bg='#D9D9D9')
            enum_value_e = tk.Entry(type_frame_values, width=30)
            enum_value_b = tk.Button(type_frame_values, text='Добавить', command=add_class_enum_value)
            
            list_sign_label = tk.Label(fld_frame, text='Список значений', bg='#D9D9D9')

            class_sign_num_value_list = tk.Listbox(fld_frame, width=30, height=5)
            class_sign_enum_value_list = tk.Listbox(fld_frame, width=30, height=5)

            # Удаление возможного значения признака класса
            def del_class_possible_value():
                error_message.grid_forget()
                conn = sqlite3.connect('soil_pollution.sqlite')
                cursor = conn.cursor()

                # Для числового типа
                if sign_type == 0:
                    selection = class_sign_num_value_list.curselection()
                    query = '''DELETE
                                FROM soil_class_num_feature
                                WHERE soil_class_num_feature_id = :p_id'''
                    cursor.execute(query, {'p_id': sign_value[selection[0]][0]})

                    conn.commit()
                    conn.close()

                    class_sign_num_value_list.delete(selection[0])
                
                # Для перечислимого типа
                elif sign_type == 1:
                    selection = class_sign_enum_value_list.curselection()
                    query = '''DELETE
                                FROM soil_class_enum_feature
                                WHERE soil_class_enum_feature_id = :p_id'''
                    cursor.execute(query, {'p_id': sign_value[selection[0]][0]})

                    conn.commit()
                    conn.close()

                    class_sign_enum_value_list.delete(selection[0])

            class_sign_values_del = tk.Button(fld_frame, text='Удалить', command=del_class_possible_value)
            error_message = tk.Label(fld_frame, bg='#D9D9D9', fg='#CC0000')



        # Создаются необходимые виджеты для работы с проверкой полноты знаний
        def create_check():
            delete_btn()
            normal_btn()
            btn_check['state'] = 'disabled'

            global check_label, bad_classes_label, bad_classes, bad_signs_label, bad_signs, bad_classes_sign_label, bad_classes_sign

            check_label = tk.Label(fld_frame, text='Проверку не прошли:', bg='#D9D9D9', fg='#CC0000')
            check_label.grid(row=0, column=0, sticky='w')

            bad_classes_label = tk.Label(fld_frame, text='Классы, у которых нет признаков:', bg='#D9D9D9')
            bad_classes_label.grid(row=1, column=0, sticky='w')
            bad_classes = tk.Label(fld_frame, text=get_bad_classes(), bg='#D9D9D9')
            bad_classes.grid(row=2, column=0, sticky='w')

            bad_signs_label = tk.Label(fld_frame, text='Признаки с незаполненными значениями:', bg='#D9D9D9')
            bad_signs_label.grid(row=3, column=0, sticky='w')
            bad_signs = tk.Label(fld_frame, text=get_bad_signs(), bg='#D9D9D9')
            bad_signs.grid(row=4, column=0, sticky='w')

            bad_classes_sign_label = tk.Label(fld_frame, text='Классы с незаполненными значениями признаков:', bg='#D9D9D9')
            bad_classes_sign_label.grid(row=5, column=0, sticky='w')
            bad_classes_sign = tk.Label(fld_frame, text=get_bad_classes_sign(), bg='#D9D9D9')
            bad_classes_sign.grid(row=6, column=0, sticky='w')

            


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
        self.geometry('400x430+350+250')
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.grab_set()
        self.focus_set()

        back_frame = tk.Frame(self, bd=10)
        back_frame.grid(row=0, column=0, columnspan=2, sticky='we')

        fld_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        fld_frame.grid(row=1, column=0, sticky='wesn', padx=30, pady=30)

        btn_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        btn_frame.grid(row=2, column=0, columnspan=2, sticky='we')

        btn_back = tk.Button(back_frame, text='Назад', command=lambda: self.destroy())
        btn_back.grid()

        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)

        btn_DB = tk.Button(btn_frame, text='Просмотр базы знаний', command=self.open_viewer)
        btn_DB.grid(row=0, column=0)
        btn_define_class = tk.Button(btn_frame, text='Определить класс почвы', command=self.open_solution)
        btn_define_class.grid(row=0, column=1)

        sign_label = tk.Label(fld_frame, text='Выберите признак', bg='#D9D9D9')
        sign_label.grid(row=0, column=0, sticky='w')

        cur_sign = tk.StringVar()
        sign_values_combobox = ttk.Combobox(fld_frame, textvariable=cur_sign, width=30)
        sign_values_combobox['values'] = get_signs()
        sign_values_combobox.grid(row=1, column=0)

        global num_data, enum_data
        # Списки введённых данных
        num_data = {}
        enum_data = {}

        # Фрэйм для красивого вывода полей ввода
        type_frame = tk.Frame(fld_frame, bg='#D9D9D9', bd=10)

        # Когда выбран числовой тип
        def select_type_num():
            enum_e.grid_forget()
            enum_b.grid_forget()

            num_e.grid(row=0, column=0)
            num_b.grid(row=0, column=1, padx=5)
            # help_label['text'] = f'Значение в диапазоне '
            # help_label.grid(row=4, column=0)
            list_data_label.grid(row=5, column=0, sticky='w')
        
        # Когда выбран перечислимый тип
        def select_type_enum():
            num_e.grid_forget()
            num_b.grid_forget()

            enum_e.grid(row=0, column=0)
            enum_b.grid(row=0, column=1, padx=5)
            # help_label['text'] = f'Значение в диапазоне '
            # help_label.grid(row=4, column=0)
            list_data_label.grid(row=5, column=0, sticky='w')

        # Вывод введённых значений
        def view_entered_values():
            if cur_sign.get():
                type_frame.grid(row=3, column=0, columnspan=2, sticky='we')
                sign_type, sign_id = get_sign_type(cur_sign.get())
                sign_value_label.grid(row=2, column=0, columnspan=2, sticky='w')

                data_list.delete(first=0, last=tk.END)
                data_del.grid(row=7, column=1, pady=5)
                
                # Для числового типа
                if sign_type == 0:
                    select_type_num()

                # Для перечислимого типа
                elif sign_type == 1:
                    select_type_enum()

                for sign in num_data:
                    data_list.insert(tk.END, f'{sign} | {num_data[sign]}')

                for sign in enum_data:
                    data_list.insert(tk.END, f'{sign} | {enum_data[sign]}')

                data_list.grid(row=6, column=0)
        
        # Добавление значение числового признака в список
        def add_to_numdata_list():
            if num_e.get() == '':
                num_data[cur_sign.get()] = '+inf'
            else:
                num_data[cur_sign.get()] = num_e.get()

            view_entered_values()
        
        # Добавление значение перечислимого признака в список
        def add_to_enumdata_list():
            enum_data[cur_sign.get()] = enum_e.get()
            view_entered_values()

        sign_value_label = tk.Label(fld_frame, text='Введите значение', bg='#D9D9D9')
        # Виджеты для числового типа
        num_e = tk.Entry(type_frame, width=5)
        num_b = tk.Button(type_frame, text='Добавить', command=add_to_numdata_list)

        # Виджеты для перечислимого типа
        enum_e = tk.Entry(type_frame)
        enum_b = tk.Button(type_frame, text='Добавить', command=add_to_enumdata_list)

        sign_values_button = tk.Button(fld_frame, text='Ввести значение', command=view_entered_values)
        sign_values_button.grid(row=1, column=1, padx=5)

        # Возможно сделаю позже
        # help_label = tk.Label(fld_frame, bg='#D9D9D9', fg='#606060')

        list_data_label = tk.Label(fld_frame, text='Введённые данные', bg='#D9D9D9')
        data_list = tk.Listbox(fld_frame, width=30, height=5)

        # Удаление данных из списка
        def del_data():
            selection = data_list.curselection()
            sign = data_list.get(selection[0]).split('|')[0][:-1]
            
            if sign in num_data:
                del num_data[sign]
            else:
                del enum_data[sign]

            data_list.delete(selection[0])

        data_del = tk.Button(fld_frame, text='Удалить', command=del_data)
    
    # Открытие просмотра БД
    def open_viewer(self):
        ViewerDB()

    # Открытие просмотра БД
    def open_solution(self):
        Solution()



# Окно для просмотра БД
class Solution(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_editorDB()
    
    def init_editorDB(self):
        self.title('Решение задачи')
        self.geometry('650x450+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        back_frame = tk.Frame(self, bd=10)
        back_frame.grid(row=0, column=0, sticky='we')

        fld_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        fld_frame.grid(row=1, column=0, sticky='wesn', padx=30, pady=30)

        btn_back = tk.Button(back_frame, text='Назад', command=lambda: self.destroy())
        btn_back.grid()


        text_if_empy = tk.Label(fld_frame, text='Введите данные в предыдущем окне', bg='#D9D9D9')
        good_frame = tk.Frame(fld_frame, bg='#D9D9D9')
        good_frame.grid(row=1, column=0, sticky='we')
        bad_frame = tk.Frame(fld_frame, bg='#D9D9D9')
        bad_frame.grid(row=2, column=0, sticky='we')

        # Получение классов, которые не подходят по введённым данным
        def get_bad_classes_solution(list_of_classes, dict_for_bad_classes):
            # Проверка по числовым признакам
            for sign in num_data.keys():
                sign_id = get_sign_id(sign)[0]
                ids = get_soil_class_feature_id_and_soil_class_id(sign_id)

                for record in ids:
                    soil_class_feature_id = record[0]
                    soil_class_id = record[1]
                    # Записываем подходящий класс (тот, у которого есть введённый признак)
                    list_of_classes.append(soil_class_id)

                    # Получаем возможные значения признака у данного класса
                    class_sign_values = get_class_sign_num_value(soil_class_id, sign_id)[0]

                    if soil_class_id not in dict_for_bad_classes:
                        if (class_sign_values[2] != None and num_data[sign] == '+inf') or (class_sign_values[2] != None and int(num_data[sign]) > class_sign_values[2]) or \
                            (num_data[sign] != '+inf' and int(num_data[sign]) < class_sign_values[1]):
                                dict_for_bad_classes[soil_class_id] = [sign_id, soil_class_feature_id, class_sign_values]
                            
                    
            # Проверка по перечислимым признакам
            for sign in enum_data.keys():
                sign_id = get_sign_id(sign)[0]
                ids = get_soil_class_feature_id_and_soil_class_id(sign_id)

                for record in ids:
                    soil_class_feature_id = record[0]
                    soil_class_id = record[1]
                    # Записываем подходящий класс (тот, у которого есть введённый признак)
                    list_of_classes.append(soil_class_id)

                    # Получаем возможные значения признака у данного класса
                    class_sign_values = get_class_sign_enum_value(soil_class_id, sign_id)[0]

                    if soil_class_id not in dict_for_bad_classes:
                        if enum_data[sign] == '' or enum_data[sign] != class_sign_values[1]:
                            dict_for_bad_classes[soil_class_id] = [sign_id, soil_class_feature_id, class_sign_values]
            
            return set(list_of_classes), dict_for_bad_classes

        # Функция для вывода решения
        def text_solution():
            if not num_data and not enum_data:
                text_if_empy.grid(row=0, column=0)
            else:
                # Список для классов, у которых есть выбранные признаки
                list_of_classes = []
                # Словарь для неподходящих классов (ключ - айди класса; значение - данные, из-за которых класс не подошёл)
                dict_for_bad_classes = {}
                list_of_classes, dict_for_bad_classes = get_bad_classes_solution(list_of_classes, dict_for_bad_classes)

                # Индексы строк для вывода решения
                row_good_id = 0
                row_bad_id = 0
                if dict_for_bad_classes:
                    for soil_class_id in list_of_classes:
                        # Если класс подходит по введённым данным
                        if soil_class_id not in dict_for_bad_classes:
                            name = get_soil_class_name(soil_class_id)[0]
                            tk.Label(good_frame, text=f'По введённым данным подходит класс: {name}', bg='#D9D9D9').grid(row=row_good_id, column=0, sticky='w')
                            row_good_id +=1
                            
                        # Если класс не подходит по введённым данным
                        else:
                            class_name = get_soil_class_name(soil_class_id)[0]
                            sign_name = get_sign_name_from_soil_class_feature_id(dict_for_bad_classes[soil_class_id][1])[0]
                            sign_type= get_sign_type(sign_name)[0]

                            # Вывод решения для числовых признаков
                            if sign_type == 0:
                                tk.Label(bad_frame, text=f'По введённым данным не подходит класс: {class_name}, так как', bg='#D9D9D9').grid(row=row_bad_id, column=0, sticky='w')
                                tk.Label(bad_frame, text=f'значение признака {sign_name} должен быть в диапазоне [{dict_for_bad_classes[soil_class_id][2][1]}, {dict_for_bad_classes[soil_class_id][2][2]}]', bg='#D9D9D9').grid(row=row_bad_id+1, column=0, sticky='w')
                                row_bad_id += 2
                            
                            # Вывод решения для перечислимых признаков
                            elif sign_type == 1:
                                tk.Label(bad_frame, text=f'По введённым данным не подходит класс: {class_name}, так как', bg='#D9D9D9').grid(row=row_bad_id, column=0, sticky='w')
                                tk.Label(bad_frame, text=f'значение признака {sign_name} должно совпадать со значением {dict_for_bad_classes[soil_class_id][2][1]}', bg='#D9D9D9').grid(row=row_bad_id+1, column=0, sticky='w')
                                row_bad_id += 2
                
                if row_good_id == 0:
                    tk.Label(fld_frame, text='Класс почвы не удалось определить. Вероятно знания, позволяющие определить класс почвы \nданного образца, не были добавлены в систему. Для разрешения ситуации обратитесь к эксперту. \nВсе классы почвы не рассматриваются по следующим причинам:', bg='#D9D9D9').grid(row=0, column=0, sticky='w')
                elif row_bad_id != 0:
                    tk.Label(good_frame, text='Другие классы почвы не рассматриваются по следующим причинам:\n\n', bg='#D9D9D9').grid(row=row_good_id, column=0, sticky='w')
        
        # Функция для вывода решения
        text_solution()




# Окно для просмотра БД
class ViewerDB(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_editorDB()
    
    def init_editorDB(self):
        self.title('Просмотр базы знаний')
        self.geometry('480x320+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        back_frame = tk.Frame(self, bd=10)
        back_frame.grid(row=0, column=0, sticky='we')

        fld_frame = tk.Frame(self, bg='#D9D9D9', bd=10)
        fld_frame.grid(row=1, column=0, sticky='wesn', padx=30, pady=30)

        btn_back = tk.Button(back_frame, text='Назад', command=lambda: self.destroy())
        btn_back.grid()


        class_values_name = tk.Label(fld_frame, text='Выберите класс', bg='#D9D9D9')
        class_values_name.grid(row=0, column=0, sticky='w')

        cur_class = tk.StringVar()
        class_values_combobox = ttk.Combobox(fld_frame, textvariable=cur_class, width=30)
        class_values_combobox['values'] = get_classes()
        class_values_combobox.grid(row=1, column=0)
        
        cur_sign = tk.StringVar()
        class_sign_values_combobox = ttk.Combobox(fld_frame, textvariable=cur_sign, width=30)

        def view_class_values_signs():
            if cur_class.get():
                sign_values_name.grid(row=2, column=0, sticky='w')
                global class_id, class_signs
                class_id = get_class_id(cur_class.get())[0]

                class_signs = get_class_signs(class_id)
                signs = []
                for i in range(len(class_signs)):
                    signs.append(class_signs[i][1])

                class_sign_values_combobox['values'] = signs
                class_sign_values_combobox.grid(row=3, column=0)
                class_values_button.grid(row=3, column=1, padx=5)

        class_sign_values_button = tk.Button(fld_frame, text='Посмотреть признаки класса', command=view_class_values_signs)
        class_sign_values_button.grid(row=1, column=1, padx=5)

        sign_values_name = tk.Label(fld_frame, text='Выберите признак', bg='#D9D9D9')

        # Вывод возможных значений
        def view_class_signs_values():
            if cur_sign.get():
                
                global sign_type, sign_id, sign_value
                sign_type, sign_id = get_sign_type(cur_sign.get())

                # Для числового типа
                if sign_type == 0:
                    class_sign_enum_value_list.grid_forget()
                    class_sign_num_value_list.delete(first=0, last=tk.END)
                    sign_value = get_class_sign_num_value(class_id, sign_id)
                    
                    for i in range(len(sign_value)):
                        if sign_value[i][2] == None:
                            sign_value[i] = [sign_value[i][0], sign_value[i][1], '+inf']
                        
                        temp = f'[{sign_value[i][1]}, {sign_value[i][2]}]'
                        class_sign_num_value_list.insert(tk.END, temp)
                    
                    class_sign_num_value_list.grid(row=7, column=0)

                # Для перечислимого типа
                elif sign_type == 1:
                    class_sign_num_value_list.grid_forget()
                    class_sign_enum_value_list.delete(first=0, last=tk.END)
                    sign_value = get_class_sign_enum_value(class_id, sign_id)

                    for i in range(len(sign_value)):
                        class_sign_enum_value_list.insert(tk.END, sign_value[i][1])

                    class_sign_enum_value_list.grid(row=7, column=0)

        class_values_button = tk.Button(fld_frame, text='Посмотреть значения класса', command=view_class_signs_values)

        class_sign_num_value_list = tk.Listbox(fld_frame, width=30, height=5)
        class_sign_enum_value_list = tk.Listbox(fld_frame, width=30, height=5)

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