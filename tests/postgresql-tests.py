# test if the application can connect to postgresql
import psycopg2


def test_postgres_connection():
    try:
        connection = psycopg2.connect(
            dname="ORTHANC",
            user="postgres",
            password="12343",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        assert result[0] == 1, "database connection test"
        print("database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()



def test_postgres_connection_ver():
    try:
        connection = psycopg2.connect(
            dbname="ORTHANC",
            user="postgres",
            password="12343",
            host="localhost",
            port="5432"
        )
        assert connection is not None
    except Exception as e:
        assert False, f"Failed to connect to PostgreSQL: {e}"

