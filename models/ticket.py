from connector import db
from datetime import date, timedelta

class Ticket:
    '''API para operações na tabela cobrança do banco de dados'''
    def create(self,
        id_cliente: int,
        numero: str,
        valor: float,
        data_de_emissao: str = str(date.today()),
        data_de_vencimento: str = str(date.today() + timedelta(days=15)),
        situacao: str = 'pendente'
    ) -> None:
        db.cur.execute(
            'INSERT INTO boletos VALUES(?, ?, ?, ?, ?, ?, ?)', (
                id_cliente, None, numero, valor, data_de_emissao,
                data_de_vencimento, situacao
            )
        )
        db.con.commit()

    def read(self, id_boleto: int) -> dict:
        colunas = [
            'id_cliente', 'id_boleto', 'numero', 'valor', 'data_de_emissao',
            'data_de_vencimento', 'situacao'
        ]
        data_tuple = db.cur.execute(
            'SELECT * FROM boletos WHERE id_boleto = ?', (id_boleto,)
        ).fetchall()[0]

        data_dict = {}
        for i, col in enumerate(colunas):
            data_dict[col] = data_tuple[i]
        return data_dict

    def update(self, id_boleto: int, **kwargs) -> None:
        for kw in kwargs:
            db.cur.execute(
                f'UPDATE boletos SET {kw} = ? WHERE id_boleto = ?',
                (kwargs[kw], id_boleto) 
            )
        db.con.commit()

    def delete(self, id_boleto: int) -> None:
        db.cur.execute('DELETE FROM boletos WHERE id_boleto = ?', (id_boleto,))

    def read_all(self):
        query = db.cur.execute('''
            SELECT nome_fantasia, nome, cnpj FROM clientes
            UNION
            SELECT data_de_vencimento, valor, numero FROM boletos
        ''').fetchall()
        return list(query[0]) + list(query[1])