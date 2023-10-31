import mysql.connector

mydb = mysql.connector.connect(
  host="10.28.1.167",
  user="suporte",
  password="suporte",
  database="estoque_medico"
)

mycursor = mydb.cursor()

# Operações CRUD

#criando a lista banco de dados
def create_data(produto,marca,quantidade,descricao):
    sql = "INSERT INTO produto(produto,marca,quantidade,descricao) VALUES (%s, %s, %s, %s)"
    val = (produto, marca, quantidade, descricao)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Produto inserido.")

#mostrando a lista do banco de dados
def read_data():
    mycursor.execute("SELECT * FROM produto")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#atualizando a lista do banco de dados
def update_data(id,produto, marca, quantidade, descricao):
    sql = "UPDATE produto SET produto = %s, marca = %s, quantidade = %s, descricao = %s WHERE id = %s"
    val = (produto, marca, quantidade, descricao, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Produto alterado")
    

update_data(2, "rinosoro", "adidas", 30, "soro fisiologico")

mydb.close()