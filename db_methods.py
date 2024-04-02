import sqlite3

# Считывание классов
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

# Считывание признаков
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