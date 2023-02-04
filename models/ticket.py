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
    def read_all(situation: str) -> list:
        ticket_data = db.cur.execute('''
                SELECT id_cliente, data_de_vencimento, valor, numero FROM boletos
                WHERE situacao = ?
            ''', (situation,)).fetchall()
        client_ids = [value[0] for value in ticket_data]
        client_data = []
        for i in client_ids:
            db.cur.execute('''
                    SELECT nome_fantasia, nome, cnpj FROM clientes WHERE id = ?
                ''', (i,))
            client_data.append(db.cur.fetchone())
        registers = []
        for i, value in enumerate(client_data):
            list_item = \
                 list(value) + list(ticket_data[i])[1:]
            registers.append(list_item)
        return registers

    @staticmethod
    def count(situation: str):
        return db.cur.execute(
            'SELECT COUNT(1) FROM boletos WHERE situacao = ?',
            (situation,)
        ).fetchone()[0]
