from connector import db
from datetime import date, timedelta


class Ticket:
    """API para operações na tabela cobrança do banco de dados"""
    @staticmethod
    def create(
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

    @staticmethod
    def read(
        client_id: int,
        return_type: type[list[dict] | list[list]]
    ) -> list[dict] | list[list]:
        columns = [
            'id_cliente', 'id_boleto', 'numero', 'valor', 'data_de_emissao',
            'data_de_vencimento', 'situacao'
        ]
        client_registers = db.cur.execute(
            'SELECT * FROM boletos WHERE id_cliente = ?', (client_id,)
        ).fetchall()
        if not client_registers:
            return [['', 'Nenhum boleto cadastrado']]
        data_dict = []
        for i, register in enumerate(client_registers):
            data_dict.append({})
            for j, col in enumerate(columns):
                data_dict[i][col] = register[j]
        if return_type is type[list[dict]]:
            return data_dict
        return [[data_dict[i]['data_de_vencimento'],
                 data_dict[i]['valor'],
                 data_dict[i]['numero']] for i in range(len(data_dict))]

    @staticmethod
    def update(id_boleto: int, **kwargs) -> None:
        for kw in kwargs:
            db.cur.execute(
                f'UPDATE boletos SET {kw} = ? WHERE id_boleto = ?',
                (kwargs[kw], id_boleto) 
            )
        db.con.commit()

    @staticmethod
    def delete(id_boleto: int) -> None:
        db.cur.execute('DELETE FROM boletos WHERE id_boleto = ?', (id_boleto,))

    @staticmethod
    def read_all() -> list:
        query = db.cur.execute('''
            SELECT nome_fantasia, nome, cnpj FROM clientes
            UNION
            SELECT data_de_vencimento, valor, numero FROM boletos
        ''').fetchall()
        return list(query[1]) + list(query[0])
