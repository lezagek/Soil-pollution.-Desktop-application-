import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('soil_pollution.sqlite')
cursor = conn.cursor()

cursor.executescript(
    '''
        INSERT INTO feature (feature_name, feature_type)
        VALUES
            ('ИНДЕКС БГКП', 0),
            ('ИНДЕКС ЭНТЕРОКОККОВ', 0),
            ('ЛИЧИНКИ МУХ', 1),
            ('КУКОЛКИ МУХ', 1)
    '''
)

cursor.executescript(
    '''
        INSERT INTO possible_num_feature (feature_id, left_border_value)
        VALUES
            (1, 1),
            (2, 1)
    '''
)

cursor.executescript(
    '''
        INSERT INTO possible_enum_feature (feature_id, possible_enum_value)
        VALUES
            (3, 'НЕТ'),
            (3, 'ЕСТЬ'),
            (4, 'НЕТ'),
            (4, 'ЕСТЬ')
    '''
)

cursor.executescript(
    '''
        INSERT INTO soil_class (soil_class_name)
        VALUES
            ('ЧИСТАЯ'),
            ('ОПАСНАЯ'),
            ('УМЕРЕННО ОПАСНАЯ'),
            ('ЧРЕЗВЫЧАЙНО ОПАСНАЯ')
    '''
)

cursor.executescript(
    '''
        INSERT INTO soil_class_feature (soil_class_id, feature_id)
        VALUES
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 1),
            (2, 2),
            (2, 3),
            (2, 4),
            (3, 1),
            (3, 2),
            (3, 3),
            (3, 4),
            (4, 1),
            (4, 2),
            (4, 3),
            (4, 4)
    '''
)

cursor.executescript(
    '''
        INSERT INTO soil_class_num_feature (soil_class_feature_id, left_border_value, right_border_value)
        VALUES
            (1, 1, 10),
            (2, 1, 10),
            (5, 10, 100),
            (6, 10, 100),
            (9, 100, 1000),
            (10, 100, 1000),
            (13, 1000, NULL),
            (14, 1000, NULL)
    '''
)

cursor.executescript(
    '''
        INSERT INTO soil_class_enum_feature (soil_class_feature_id, possible_enum_feature_id)
        VALUES
            (3, 'НЕТ'),
            (4, 'НЕТ'),
            (7, 'ЕСТЬ'),
            (8, 'НЕТ'),
            (11, 'ЕСТЬ'),
            (12, 'ЕСТЬ'),
            (15, 'ЕСТЬ'),
            (16, 'ЕСТЬ')
    '''
)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()