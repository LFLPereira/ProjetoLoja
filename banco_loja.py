import sqlite3

def criar_tabela(cursor):

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loja (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        qde INTEGER NOT NULL,
        preco REAL NOT NULL
        )
    '''
    )

def main():
    conn = sqlite3.connect('loja.db')

    cursor = conn.cursor()

    criar_tabela(cursor)

    while True:
        print("Menu:")
        print("")
        print("1 - Adicionar Produto") #Feito
        print("2 - Listar Produtos") #Feito
        print("3 - Atualizar Produto")
        print("4 - Remover Produto") #Feito
        print("5 - Buscar Produto") #Feito
        print("0 - Fechar") #Feito
        print("")

        menu = input("Escolha a opção: ")

        match menu:
            case "1":
                nome_add = input("Nome: ")
                qde_add = input("Quantidade: ")
                preco_add = input("Preço: ")

                cursor.execute('INSERT INTO loja (nome, qde, preco) VALUES (?, ?, ?)',(nome_add, qde_add, preco_add))
                cursor.execute('SELECT * FROM loja')
                conn.commit()
                lista_loja = cursor.fetchall()
                print(lista_loja[len(lista_loja)-1])

            case "2":
                cursor.execute('SELECT * FROM loja')
                lista_loja = cursor.fetchall()
                for i in lista_loja:
                    print(i)

            case "3":
                id_update = input("ID: ")
                cursor.execute(f'SELECT * FROM loja WHERE id = {id_update}')
                lista_loja = cursor.fetchall()
                print(lista_loja[len(lista_loja)-1])
                nome_update = input("Novo nome: ")
                qde_update = input("Nova quantidade: ")
                preco_update = input("Novo preço: ")

                cursor.execute(f"UPDATE loja SET nome = '{nome_update}', qde = {qde_update}, preco = {preco_update} WHERE id = {id_update}")
                conn.commit()
                cursor.execute(f'SELECT * FROM loja WHERE id = {id_update}')
                lista_loja = cursor.fetchall()
                print(lista_loja[len(lista_loja)-1])
                print("Atualizado com sucesso!")


            case "4":
                id_remove = input("ID: ")
                cursor.execute(f'SELECT * FROM loja WHERE id = {id_remove}')
                lista_loja = cursor.fetchall()
                cursor.execute(f'DELETE FROM loja WHERE id = {id_remove}')
                conn.commit()
                print(lista_loja[len(lista_loja)-1])
                print("Removido com sucesso!")


            case "5":
                id_nome = input("Procurar por ID? (S/N) ")

                if id_nome.lower() == "s":

                    search = input("ID: ")
                    cursor.execute(f'SELECT * FROM loja WHERE id = {search}')
                    lista_loja = cursor.fetchall()
                    print(lista_loja[len(lista_loja)-1])

                else:

                    search = input("Nome: ")
                    cursor.execute(f"SELECT * FROM loja WHERE nome = '{search}'")
                    lista_loja = cursor.fetchall()
                    print(lista_loja[len(lista_loja)-1])

            case "0":
                break

            case _:
                pass





    # conn.commit()  
    # print(cursor.fetchall())  

    # conn.close()


if __name__ == "__main__":
    main()