
import dotenv
import os
import logging



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

dotenv.load_dotenv()


USERS_TABLE = """ CREATE TABLE IF NOT EXISTS users (
    id SERIAL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""


query_insert = """ INSERT INTO users (username, email, password) VALUES (%s, %s, %s) """

query_delete = """ DELETE FROM users WHERE id = %s """

values = ('enano', 'enano@gmail.com', '12345678')

users = [
    ('user1', 'user1@example.com', 'password1'),
    ('user2', 'user2@example.com', 'password2'),
    ('user3', 'user3@example.com', 'password3'),
    ('user4', 'user4@example.com', 'password4'),
    ('user5', 'user5@example.com', 'password5'),
    ('user6', 'user6@example.com', 'password6')
]


query_select = """ SELECT * FROM users """






def main():
    try:
        conn = conn_db_postgresql()

        with conn.cursor() as cursor:
            cursor.execute(USERS_TABLE)
            # cursor.execute(query_insert, values)
            # cursor.executemany(query_insert, users)
            
            #* Delete
            # cursor.execute(query_delete, (5,))
            conn.commit()
            
            # rows = cursor.execute(query_select)
            # logging.info(f'Rows: {rows}')

            #* Fetchall obtiene todas las filas
            # for row in cursor.fetchall():
            #     logging.info(row)

            #* Fetchmany recibe un parametro que es la cantidad de filas que queremos obtener
            # for row in cursor.fetchmany(2):
            #     logging.info(row)
            
            #* Fetchone obtiene una sola fila
            # row = cursor.fetchone()
            # logging.info(row)


            

            logging.info('Connection established')
    except Exception as e:
        logging.error(f'Error: {e}')
    else:
        cursor.close()
        conn.close()
        logging.info('Connection closed')

# if __name__ == '__main__':
#     main()