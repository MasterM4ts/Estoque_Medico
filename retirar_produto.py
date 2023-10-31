import mysql.connector

mydb = mysql.connector.connect(
  host="10.28.1.198",
  user="suporte",
  password="suporte",
  database="estoque_medico"
)

mycursor = mydb.cursor()

# Operações C R U D
#Create = criar o banco de dados
#Read = select, mostrar o dados do banco
#Update = atualizar dados no banco
#Delete = deletar alguma tabela ou item

# CREATE
def create_database (produto,marca,quantidade):
    sql = "INSERT INTO produto (produto, marca, quantidade) VALUES (%s, %s, %s)"
    val = (produto, marca, quantidade)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Produto(s) inserido(s).")

# READ
def read_database():
    mycursor.execute("SELECT * FROM produto")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# UPDATE
def update_database (produto, marca, quantidade, where):
    sql = "UPDATE produto SET produto = %s, marca = %s, quantidade = %s WHERE quantidade = %s"
    val = (produto, marca, quantidade,where)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Produto(s) alterado(S)")

# DELETE
def delete_database(id):
    sql = "DELETE FROM produto WHERE id = %s"
    val = (id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "produto(s) excluído(s).")


delete_database(2)

mydb.close()


    
    