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

    query = '''SELECT feature_name
                FROM feature
                LEFT JOIN soil_class_feature USING (feature_id)
                WHERE soil_class_feature.feature_id IS NULL
                '''
    cursor.execute(query, {'p_id': soil_class_id})
    
    for sign in cursor.fetchall():
        signs.append(sign[0])

    conn.commit()
    conn.close()
    return signs

# Получение незаполненных классов
def get_bad_classes():
    classes = ''
    conn = sqlite3.connect('soil_pollution.sqlite')
    cursor = conn.cursor()

    query = '''SELECT *
                FROM soil_class t1
                WHERE NOT EXISTS (
                    SELECT t2.soil_class_id
                    FROM soil_class_feature t2
                    WHERE t2.soil_class_id = t1.soil_class_id
                )'''
    cursor.execute(query)
    for soil_class in cursor.fetchall():
        classes += soil_class[1] + '\n'
    
    conn.commit()
    conn.close()

    return classes