import sqlite3

conexao = sqlite3.connect('UltimaAula')
cursor = conexao.cursor()
query = 'create table cliente(id int, nome varchar(50), cpf varchar(11), datacadastro text, endereco varchar(52))'
consulta = cursor.execute(query)
conexao.commit()
conexao.close
