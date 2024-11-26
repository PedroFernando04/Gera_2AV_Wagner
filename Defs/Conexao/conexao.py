import psycopg2

def conexao():
    try:
        conn = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = 'postgres',
            host = 'localhost',
            port = '5432'
        )
        #print("SUCESSO!")
        return conn
    
    except Exception as e:
        print(f"DEU PAU: {e}")
        return None
