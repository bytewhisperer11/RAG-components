# db_layer/config.py

import os

# PostgreSQL configuration
PG_CONFIG = {
    'dbname': os.getenv('PG_DBNAME', 'vector_db'),  # Default to 'vector_db', replace with your vector database name
    'user': os.getenv('PG_USER', 'postgres'),       # Default to 'postgres' user
    'password': os.getenv('PG_PASSWORD', ''),       # Default empty password; set via environment for security
    'host': os.getenv('PG_HOST', 'localhost'),      # Default to 'localhost', change if needed
    'port': os.getenv('PG_PORT', '5432'),           # Default to PostgreSQL port (5432)
}


# Function to get configuration for a specific database
def get_db_config(db_type='postgresql'):
    """
    Returns the database configuration based on the db_type specified.
    :param db_type: Type of database ('postgresql', 'mysql', etc.)
    :return: The database configuration dictionary.
    """
    if db_type == 'postgresql':
        return PG_CONFIG

    # Add more conditions for additional databases
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
