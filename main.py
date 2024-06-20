import psycopg2
from psycopg2 import sql

# Configurações de conexão
conn_info = {
    'dbname': 'postgres',
    'port': 6543 
}

# Conectar ao banco de dados
try:
    conn = psycopg2.connect(**conn_info)
    cursor = conn.cursor()

    # Criar a tabela
    create_table_query = '''
        CREATE TABLE usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cpf VARCHAR(11) NOT NULL UNIQUE
        );
    '''

    cursor.execute(create_table_query)
    print("Tabela 'usuarios' criada com sucesso.")

    # Inserir dados
    insert_data_query = '''
    INSERT INTO usuarios (nome, cpf) VALUES
    (%s, %s),
    (%s, %s);
    '''
    cursor.execute(insert_data_query, ('João Silva', '12345678901', 'Maria Oliveira', '10987654321'))
    '''
    INSERT INTO usuarios (nome, cpf) VALUES
    ('João Silva', '12345678901'),
    ('Maria Oliveira', '10987654321');
    '''
    print("Dados inseridos com sucesso.")

    # Commit para salvar as alterações no banco de dados
    conn.commit()

    # Verificar dados inseridos
    select_query = 'SELECT * FROM usuarios;'
    cursor.execute(select_query)
    rows = cursor.fetchall()

    print("Dados na tabela 'usuarios':")
    for row in rows:
        print(row)

except Exception as e:
    print(f"OXI MEU REI... deu ruim aqui: {e}")

