import sqlite3

conexao = sqlite3.connect('banco_pd.sqlite')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE categoria(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100));')
#cursor.execute('CREATE TABLE clientes(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), categoria_id INT NOT NULL, CONSTRAINT categoria_fk FOREIGN KEY (categoria_id) REFERENCES categoria(id));')
#cursor.execute('INSERT INTO categoria(nome) VALUES ("Informatica")')
#cursor.execute('INSERT INTO categoria(nome) VALUES ("Cliente")')
#cursor.execute('INSERT INTO clientes(nome,categoria_id) VALUES ("Robson",1)')
#cursor.execute('INSERT INTO clientes(nome,categoria_id) VALUES ("Melissa",2)')
#cursor.execute('UPDATE clientes SET nome="Isadora" where id=1')
#
'''
nome = input("Qual nome deseja adicionar?")
categoria_id = input("Digite o número da sua categoria: ")
valores = [nome,categoria_id]
sql_inserir = 'INSERT INTO clientes (nome,categoria_id) VALUES (?,?)'
cursor.execute(sql_inserir,valores)
'''
'''
# COUNT = contabiliza o numero de ocorrencias 
dados = cursor.execute('SELECT COUNT(id) FROM clientes')
for dado in dados:
    print(dado)
'''
#SUM
dados = cursor.execute('SELECT SUM(id) FROM categoria')
for dado in dados:
    print(dado)
conexao.commit() #Enviar as informações para o banco
conexao.close