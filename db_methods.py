import sqlite3

# Получение всех классов
def get_classes():
    classes = []
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_name 
                FROM soil_class'''
    cursor.execute(query)

    for soil_class in cursor.fetchall():
        classes.append(soil_class[0])
    
    conn.commit()
    conn.close()

    return classes

# Получение всех признаков
def get_signs():
    signs = []
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT feature_name 
                FROM feature'''
    cursor.execute(query)

    for sign in cursor.fetchall():
        signs.append(sign[0])
    
    conn.commit()
    conn.close()

    return signs

# Получение айди признака
def get_sign_id(feature_name):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT feature_id
                FROM feature
                WHERE feature_name = :p_name'''
    cursor.execute(query, {'p_name': feature_name})

    id = cursor.fetchall()[0]
    conn.commit()
    conn.close()
    return id

# Получение типа и айди признака
def get_sign_type(feature_name):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT feature_type, feature_id
                FROM feature
                WHERE feature_name = :p_name'''
    cursor.execute(query, {'p_name': feature_name})

    res = cursor.fetchall()[0]
    conn.commit()
    conn.close()
    return res

# Получение возможных значений для числового признака
def get_sign_num_value(feature_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT possible_num_feature_id, left_border_value, right_border_value
                FROM possible_num_feature
                WHERE feature_id = :p_id'''
    cursor.execute(query, {'p_id': feature_id})
    
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

# Получение возможных значений для перечислимого признака
def get_sign_enum_value(feature_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT possible_enum_feature_id, possible_enum_value
                FROM possible_enum_feature
                WHERE feature_id = :p_id'''
    cursor.execute(query, {'p_id': feature_id})
    
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

# Получение айди класса
def get_class_id(soil_class_name):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_id
                FROM soil_class
                WHERE soil_class_name = :p_name'''
    cursor.execute(query, {'p_name': soil_class_name})

    id = cursor.fetchall()[0]
    conn.commit()
    conn.close()
    return id

# Получение признаков класса
def get_class_signs(soil_class_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT feature_id, feature_name
                FROM soil_class_feature
                LEFT JOIN feature USING (feature_id)
                WHERE soil_class_id = :p_id'''
    cursor.execute(query, {'p_id': soil_class_id})
    
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

# Получение признаков, которых нет в классе
def get_signs_not_in_class(soil_class_id):
    signs = []
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT DISTINCT feature_name
                FROM feature
                LEFT JOIN soil_class_feature USING (feature_id)
                WHERE feature_id NOT IN(
                    SELECT soil_class_feature.feature_id
                    FROM soil_class_feature
                    WHERE soil_class_id = :p_id
                )
                '''
    cursor.execute(query, {'p_id': soil_class_id})
    
    for sign in cursor.fetchall():
        signs.append(sign[0])

    conn.commit()
    conn.close()
    return signs

# Получение возможных значений для числового признака класса
def get_class_sign_num_value(soil_class_id, feature_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_num_feature_id, left_border_value, right_border_value
                FROM soil_class_num_feature
                WHERE soil_class_feature_id = (
                    SELECT soil_class_feature_id
                    FROM soil_class_feature
                    WHERE soil_class_id = :p_c_id AND feature_id = :p_f_id 
                )'''
    cursor.execute(query, {'p_c_id': soil_class_id, 'p_f_id': feature_id})
    
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

# Получение возможных значений для перечислимого признака класса
def get_class_sign_enum_value(soil_class_id, feature_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_enum_feature_id, possible_enum_value
                FROM soil_class_enum_feature
                LEFT JOIN possible_enum_feature USING (possible_enum_feature_id)
                WHERE soil_class_feature_id = (
                    SELECT soil_class_feature_id
                    FROM soil_class_feature
                    WHERE soil_class_id = :p_c_id AND feature_id = :p_f_id 
                )'''
    cursor.execute(query, {'p_c_id': soil_class_id, 'p_f_id': feature_id})
    
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

# Получение незаполненных классов
def get_bad_classes():
    classes = []
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_name
                FROM soil_class t1
                WHERE NOT EXISTS (
                    SELECT t2.soil_class_id
                    FROM soil_class_feature t2
                    WHERE t2.soil_class_id = t1.soil_class_id
                )'''
    cursor.execute(query)
    
    for soil_class in cursor.fetchall():
        classes.append(soil_class[0])

    classes = ', '.join(classes)
    conn.commit()
    conn.close()

    return classes

# Получение признаков с незаполненными значениями
def get_bad_signs():
    signs = []
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT feature_name
                FROM feature
                WHERE feature_type IS NULL'''
    cursor.execute(query)
    
    for sign in cursor.fetchall():
        signs.append(sign[0])
    
    signs = ', '.join(signs)
    conn.commit()
    conn.close()

    return signs

# Получение классов с незаполненными значениями признаков
def get_bad_classes_sign():
    classes = []
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_name, feature_name
                FROM soil_class
                LEFT JOIN soil_class_feature USING (soil_class_id)
                LEFT JOIN feature USING (feature_id)
                WHERE soil_class_feature_id NOT IN(
                    SELECT soil_class_num_feature.soil_class_feature_id
                    FROM soil_class_num_feature
                ) AND soil_class_feature_id NOT IN(
                    SELECT soil_class_enum_feature.soil_class_feature_id
                    FROM soil_class_enum_feature
                ) '''
    cursor.execute(query)

    for soil_class in cursor.fetchall():
        classes.append(f'{soil_class[0]} - {soil_class[1]}')

    classes = '; '.join(classes)
    conn.commit()
    conn.close()

    return classes

# Получение айди всех классов
def get_classes_id():
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_id
                FROM soil_class'''
    cursor.execute(query)
    
    ids = []
    for id in cursor.fetchall():
        ids.append(id[0])
    conn.commit()
    conn.close()
    return ids

# Получение айди таблицы soil_class_feature по feature_id
def get_soil_class_feature_id_and_soil_class_id(feature_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_feature_id, soil_class_id
                FROM soil_class_feature
                WHERE feature_id = :p_id'''
    cursor.execute(query, {'p_id': feature_id})
    
    ids = cursor.fetchall()
    conn.commit()
    conn.close()
    return ids

# Получение имени класса по его айди
def get_soil_class_name(soil_class_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT soil_class_name
                FROM soil_class
                WHERE soil_class_id = :p_id'''
    cursor.execute(query, {'p_id': soil_class_id})
    
    name = cursor.fetchall()[0]
    conn.commit()
    conn.close()
    return name

# Получение имени признака по soil_class_feature_id
def get_sign_name_from_soil_class_feature_id(soil_class_feature_id):
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT feature_name
                FROM feature
                LEFT JOIN soil_class_feature USING(feature_id)
                WHERE soil_class_feature_id = :p_id'''
    cursor.execute(query, {'p_id': soil_class_feature_id})
    
    name = cursor.fetchall()[0]
    conn.commit()
    conn.close()
    return name