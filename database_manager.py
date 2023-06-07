import sqlite3

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('parking_history.db')
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ':'+', :'.join(data.keys())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, data)
        self.connection.commit()

    def select_data(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def update_data(self, table_name, data, condition):
        columns = ', '.join(f"{key} = :{key}" for key in data.keys())
        query = f"UPDATE {table_name} SET {columns} WHERE {condition}"
        self.cursor.execute(query, data)
        self.connection.commit()

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()