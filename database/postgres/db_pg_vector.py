# db_layer/db_layer_pg.py

import psycopg2
from postgres.config import get_db_config
import numpy as np

class PGVectorDB:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, db_type='postgresql'):
        """
        Implements Singleton pattern. This ensures only one instance of PGVectorDB is created.

        :param db_type: The type of database to connect to ('postgresql', etc.).
        :return: The single instance of the PGVectorDB class.
        """
        if cls._instance is None:
            cls._instance = super(PGVectorDB, cls).__new__(cls)
            cls._instance._init(db_type)
        return cls._instance

    def _init(self, db_type='postgresql'):
        """
        Initializes the connection to the specified database type.
        
        :param db_type: The type of database to connect to ('postgresql', etc.).
        """
        self.db_config = get_db_config(db_type)
        self.connection = psycopg2.connect(**self.db_config)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """
        Creates a table with an ID and a vector column.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS vector_data22 (
            id SERIAL PRIMARY KEY,
            vector vector(300)  
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_vector(self, vector):
        """
        Insert a vector into the table.

        :param vector: List or numpy array representing the vector data.
        """
        vector_str = np.array(vector).tolist()  # Convert to list if it's a numpy array
        insert_query = """
        INSERT INTO vector_data2 (vector) 
        VALUES (%s) RETURNING id;
        """
        self.cursor.execute(insert_query, (vector_str,))
        self.connection.commit()
        vector_id = self.cursor.fetchone()[0]
        return vector_id

    def get_vector(self, vector_id):
        """
        Retrieve a vector by its ID.

        :param vector_id: ID of the vector to retrieve.
        :return: The vector data as a list.
        """
        select_query = "SELECT vector FROM vector_data2 WHERE id = %s;"
        self.cursor.execute(select_query, (vector_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def update_vector(self, vector_id, new_vector):
        """
        Update a vector by its ID.

        :param vector_id: ID of the vector to update.
        :param new_vector: List or numpy array representing the new vector data.
        """
        vector_str = np.array(new_vector).tolist()
        update_query = """
        UPDATE vector_data2 
        SET vector = %s 
        WHERE id = %s;
        """
        self.cursor.execute(update_query, (vector_str, vector_id))
        self.connection.commit()

    def delete_vector(self, vector_id):
        """
        Delete a vector by its ID.

        :param vector_id: ID of the vector to delete.
        """
        delete_query = "DELETE FROM vector_data2 WHERE id = %s;"
        self.cursor.execute(delete_query, (vector_id,))
        self.connection.commit()

    def close(self):
        """
        Close the database connection and cursor.
        """
        self.cursor.close()
        self.connection.close()

