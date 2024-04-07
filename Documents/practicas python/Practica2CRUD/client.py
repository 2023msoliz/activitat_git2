import psycopg

def db_client():
    try:
        dbname = 'postgres'
        user = 'user_postgres'
        password = 'pass_postgres'
        host = 'localhost'
        port = '5432'

        return psycopg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
    )
    except Exception as e:
        return {"Status": -1, "message": f"Error al conectarse a la BBDD:{e}"}