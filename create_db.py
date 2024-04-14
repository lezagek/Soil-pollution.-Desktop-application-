import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('soil_pollution.sqlite')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.executescript(
    '''
        CREATE TABLE feature (
            feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature_name VARCHAR(30) UNIQUE,
            feature_type BOOLEAN
        )
    '''
)

cursor.executescript(
    '''
        CREATE TABLE possible_num_feature (
            possible_num_feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature_id INTEGER,
            left_border_value INTEGER,
            right_border_value INTEGER,

            CONSTRAINT possible_num_feature_unique UNIQUE (feature_id, left_border_value, right_border_value),

            FOREIGN KEY (feature_id) REFERENCES feature (feature_id) ON DELETE CASCADE
        )
    '''
)

cursor.executescript(
    '''
        CREATE TABLE possible_enum_feature (
            possible_enum_feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
            feature_id INTEGER,
            possible_enum_value VARCHAR(30),

            CONSTRAINT possible_enum_feature_unique UNIQUE (feature_id, possible_enum_value),

            FOREIGN KEY (feature_id) REFERENCES feature (feature_id) ON DELETE CASCADE
        )
    '''
)

cursor.executescript(
    '''
        CREATE TABLE soil_class (
            soil_class_id INTEGER PRIMARY KEY AUTOINCREMENT,
            soil_class_name VARCHAR(30) UNIQUE
        )
    '''
)

cursor.executescript(
    '''
        CREATE TABLE soil_class_feature (
            soil_class_feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
            soil_class_id INTEGER,
            feature_id INTEGER,

            CONSTRAINT class_feature_unique UNIQUE (soil_class_id, feature_id),

            FOREIGN KEY (soil_class_id) REFERENCES soil_class (soil_class_id) ON DELETE CASCADE,
            FOREIGN KEY (feature_id) REFERENCES feature (feature_id) ON DELETE CASCADE
        )
    '''
)

cursor.executescript(
    '''
        CREATE TABLE soil_class_num_feature (
            soil_class_num_feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
            soil_class_feature_id INTEGER,
            left_border_value INTEGER,
            right_border_value INTEGER,

            CONSTRAINT soil_class_num_feature_unique UNIQUE (soil_class_feature_id, left_border_value, right_border_value),

            FOREIGN KEY (soil_class_feature_id) REFERENCES soil_class_feature (soil_class_feature_id) ON DELETE CASCADE
        )
    '''
)

cursor.executescript(
    '''
        CREATE TABLE soil_class_enum_feature (
            soil_class_enum_feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
            soil_class_feature_id INTEGER,
            possible_enum_feature_id INTEGER,

            CONSTRAINT soil_class_enum_feature_unique UNIQUE (soil_class_feature_id, possible_enum_feature_id),

            FOREIGN KEY (soil_class_feature_id) REFERENCES soil_class_feature (soil_class_feature_id) ON DELETE CASCADE,
            FOREIGN KEY (possible_enum_feature_id) REFERENCES possible_enum_feature (possible_enum_feature_id) ON DELETE CASCADE
        )
    '''
)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()