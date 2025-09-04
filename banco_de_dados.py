import mysql.connector
from mysql.connector import Error

try:
    # Conectar ao banco
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="meu_banco"  
    )

    if db.is_connected():
        print("✅ Conexão realizada com sucesso!")

        cursor = db.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)

        # Buscar todos os registros
        resultados = cursor.fetchall()

        print("📋 Usuários cadastrados:")
        for linha in resultados:
            print(linha)

except Error as e:
    print(f"❌ Erro ao conectar: {e}")

finally:
    if db.is_connected():
        cursor.close()
        db.close()
        print("🔒 Conexão encerrada.")
