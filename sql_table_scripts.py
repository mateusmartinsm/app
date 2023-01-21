class TableConstructorScripts:
    def tickets(self):
        return '''
            CREATE TABLE IF NOT EXISTS boletos(
                id_cliente INTEGER NOT NULL,
                id_boleto INTEGER PRIMARY KEY AUTOINCREMENT,
                numero TEXT NOT NULL,
                valor FLOAT NOT NULL,
                data_de_emissao TEXT NOT NULL,
                data_de_vencimento TEXT NOT NULL,
                situacao TEXT NOT NULL,
                foreign key(id_cliente) references clientes(id)
            )
        '''

    def clients(self):
        return '''
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_de_cadastro TEXT NOT NULL,
                cnpj TEXT UNIQUE,
                cpf TEXT UNIQUE,
                razao_social TEXT,
                nome_fantasia TEXT NOT NULL,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT,
                cep TEXT,
                logradouro TEXT,
                numero TEXT,
                bairro TEXT NOT NULL,
                cidade TEXT,
                uf TEXT,
                complemento TEXT,
                situacao INTEGER,
                categoria TEXT,
                data_de_cadastro TEXT NOT NULL,
                informacoes_adicionais TEXT
            )
        '''