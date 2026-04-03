import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="shield_db",
        user="postgres",
        password="postgres"
    )
