# import sqlite3
#
# #Подключение к базе данных
# connection = sqlite3.connect('my_users.db')
# #Переводчик с Питона на SQL
# sql = connection.cursor()
#
# #Создание таблицы
# sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT);')
# #Добавление новых данных
# sql.execute('INSERT INTO users (user_id, username) VALUES (0, "@pav_ok");')
# #Вывести колонку user_id
# sql.execute('SELECT user_id FROM users;')
# #Запрос с фильтрацией
# sql.execute('SELECT username FROM users WHERE user_id=0;')
# #Обновитьданные
# sql.execute('UPDATE users SET username="@pasha23" WHERE user_id=0;')
# #Удаление данных
# sql.execute('DELETE FROM users WHERE user_id=0;')
# #Фиксируем изменения
# connection.commit()
# #получит все результаты и сделает список (так мы можем проверить есть ли элемент в базе
# # пример
# # "print(sql.execute('SELECT username FROM users WHERE user_id=0;').fetchall())"
# sql.fetchall()
# #закрывает подключение
# connection.close()

