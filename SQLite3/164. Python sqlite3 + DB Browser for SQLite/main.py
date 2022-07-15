import sqlite3

class AgendaDB:
    def __init__(self, arquivo_base_de_dados) -> None:
        self.conexao = sqlite3.connect(arquivo_base_de_dados)
        self.cursor = self.conexao.cursor()
        
    def inserir(self, nome, telefone):
        """Primeiro temos a consulta SQL, depois o cursor executa a consulta e envia o nome e telefone
        por fim ele commita as coisas para salvar

        Args:
            nome (_type_): _description_
            telefone (_type_): _description_
        """
        # consulta = 'INSERT INTO agenda (nome, telefone) VALUES (?, ?)'
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'  # insira ou ignore É BOM TER UM UNIQUE ATIVO!
        self.cursor.execute(consulta, (nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conexao.commit()
        
    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))  # como é uma tupla, tem que deixar um , no final
        self.conexao.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')  # como é uma tupla, tem que deixar um , no final
        for line in self.cursor.fetchall():
            print(line)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))  # como é uma tupla, tem que deixar um , no final
        # o % busca qualquer coisa que seja igual para a esquerda ou direita

        for line in self.cursor.fetchall():
            print(line)


    def fechar(self):
        self.cursor.close()
        self.conexao.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Gabriel', '111111')
    # agenda.inserir('Mário', '113222')
    # agenda.inserir('Josiel', '344121')
    agenda.inserir('Raquel', '9223123')
    agenda.inserir('Raquele Pereira', '745894')
    agenda.inserir('Geovana Raquelina', '998587')
    agenda.inserir('Luiza Raquel Pereira da Silva Santos', '7845711')
    # agenda.editar('Francisco', '908987', 5)
    # agenda.excluir(5)
    agenda.buscar('Raquel')
    # agenda.listar()














"""
164. Python sqlite3 + DB Browser for SQLite


fazendo como na aula 161 mas com ajuda do db browser

Aqui faremos uma agenda que tem nome e telefone

"""