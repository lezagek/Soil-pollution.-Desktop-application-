import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('soil_pollution.sqlite')
cursor = conn.cursor()

cursor.executescript(
    '''
        DROP TABLE IF EXISTS soil_class;
        DROP TABLE IF EXISTS soil_class_feature;
        DROP TABLE IF EXISTS soil_class_num_feature;
        DROP TABLE IF EXISTS soil_class_enum_feature;
        DROP TABLE IF EXISTS feature;
        DROP TABLE IF EXISTS possible_num_feature;
        DROP TABLE IF EXISTS possible_enum_feature;
    '''
)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()