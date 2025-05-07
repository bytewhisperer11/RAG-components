# usage_example.py

from database.postgres.db_pg_vector import PGVectorDB
import numpy as np

def main():
    # Initialize the database connection (Singleton pattern in action)
    db = PGVectorDB(db_type='postgresql')

    # Create the table for storing vectors if it doesn't exist
    db.create_table()
    print("Table created (if it didn't exist already).")

    # Example vector data (300-dimensional vector)
    vector_data = np.random.rand(300).tolist()
    print(f"Generated vector data: {vector_data[:5]}...")  # Print first 5 elements for brevity

    # Insert a vector into the database
    vector_id = db.insert_vector(vector_data)
    print(f"Inserted vector with ID: {vector_id}")

    # Retrieve the inserted vector by its ID
    retrieved_vector = db.get_vector(vector_id)
    print(f"Retrieved vector: {retrieved_vector[:5]}...")  # Print first 5 elements for brevity

    # Update the vector with new data
    new_vector_data = np.random.rand(300).tolist()
    db.update_vector(vector_id, new_vector_data)
    print(f"Vector with ID {vector_id} has been updated.")

    # Retrieve the updated vector
    updated_vector = db.get_vector(vector_id)
    print(f"Updated vector: {updated_vector[:5]}...")  # Print first 5 elements for brevity

    # Delete the vector from the database
    db.delete_vector(vector_id)
    print(f"Vector with ID {vector_id} has been deleted.")

    # Close the database connection
    db.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()
