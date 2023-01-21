from connector import db
from datetime import date

class Client:
    '''Forma segura de manipular dados da tabela clientes.'''
    def create(self,
               tipo_de_cadastro: str,
               nome_fantasia: str,
               nome: str,
               bairro: str,
               telefone: str,
               cep: str = None,
               logradouro: str = None,
               numero: str = None,
               cidade: str = None,
               uf: str = None,
               situacao: int = None,
               complemento: str = None,
               cnpj: str = None,
               cpf: str = None,
               razao_social: str = None,
               email: str = None,
               categoria: str = None,
               informacoes_adicionais: str = None
               ) -> None:
        '''Os valores deverão ser passados como parâmetro com exceção da data_de_cadastro, esta recebe a data de hoje automaticamente.'''
        db.cur.execute('''
            INSERT INTO clientes(
                tipo_de_cadastro, nome_fantasia, nome, bairro, telefone, cep,
                logradouro, numero, cidade, uf, complemento, situacao,
                data_de_cadastro, cnpj, cpf, razao_social, email, categoria,
                informacoes_adicionais
            ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
            tipo_de_cadastro, nome_fantasia, nome, bairro, telefone, cep,
            logradouro, numero, cidade, uf, complemento, situacao,
            date.today(), cnpj, cpf, razao_social, email, categoria,
            informacoes_adicionais
        )
                       )
        db.con.commit()

    def read(self, id: int) -> dict:
        '''Retorna um dicionário com os dados do cliente'''
        columns = [
            'id', 'tipo_de_cadastro', 'cnpj', 'cpf', 'razao_social',
            'nome_fantasia', 'nome', 'email', 'cep', 'logradouro', 'numero',
            'bairro', 'cidade', 'uf', 'complemento', 'situacao', 'categoria',
            'data_de_cadastro', 'informacoes_adicionais'
        ]
        data_tuple = db.cur.execute(
            'SELECT * FROM clientes WHERE id = ?', (id,)
        ).fetchall()[0]

        data_dict = {}
        for i, col in enumerate(columns):
            data_dict[col] = data_tuple[i]
        return data_dict

    def update(self, id: int, **kwargs) -> None:
        for kw in kwargs:
            db.cur.execute(
                f'UPDATE clientes SET {kw} = ? WHERE id = ?',
                (kwargs[kw], id)
            )
        db.con.commit()


    def delete(self, id: int) -> None:
        db.cur.execute('DELETE FROM clientes WHERE id = ?', (id,))

    def read_all(self):
        client_data = db.cur.execute('''SELECT
            nome_fantasia, nome, bairro, telefone FROM clientes
        ''').fetchall()
        return client_data