import sqlite3

conexao = sqlite3.connect('banco.sqlite3') # ABRE CONEXAO COM O BANCO DE DADOS
cursor = conexao.cursor()                  # 
sql = '''
CREATE TABLE cliente4 (
 id INT NOT NULL,
 nome VARCHAR(100),
    cpf VARCHAR(11) UNIQUE,
           PRIMARY KEY (id)
 );
'''    
cursor.execute(sql)
conexao.commit()                           # SALVA TRANSAÇÕES NAS TABELAS
conexao.close                              # FECHA CONEXAO COM O BANCO
