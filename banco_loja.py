import sqlite3
import locale
import os

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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
        clear()
        print('''
        
        
        ''')
        print('''\u001b[31m▓█████  ██▓███   ▄▄▄       ███▄ ▄███▓ ██▓ ███▄    █  ▒█████   ███▄    █ ▓█████▄  ▄▄▄        ██████      ██████ ▄▄▄█████▓ ▒█████   ██▀███  ▓█████ 
▓█   ▀ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▒████▄    ▒██    ▒    ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ 
▒███   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒██  ▀█▄  ░ ▓██▄      ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▒███   
▒▓█  ▄ ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██   ▒   ██▒     ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▒▓█  ▄ 
░▒████▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒░██░▒██░   ▓██░░ ████▓▒░▒██░   ▓██░░▒████▓  ▓█   ▓██▒▒██████▒▒   ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒░▒████▒
░░ ▒░ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░
 ░ ░  ░░▒ ░       ▒   ▒▒ ░░  ░      ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░▒  ░ ░   ░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░
   ░   ░░         ░   ▒   ░      ░    ▒ ░   ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░   ░   ▒   ░  ░  ░     ░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░    ░   
   ░  ░               ░  ░       ░    ░           ░     ░ ░           ░    ░          ░  ░      ░           ░               ░ ░     ░        ░  ░
                                                                         ░                                                                       \u001b[0m''')
        
        print('''
        
        
        ''')
        print("Menu:")
        print("")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Remover Produto")
        print("5 - Buscar Produto")
        print("6 - Vender Produto")
        print("0 - Fechar")
        print("")

        menu = input("Escolha a opção: ")

        match menu:
            case "1":
                nome_add = input("Nome: ")
                qde_add = inputplus(False,"Quantidade: ")
                preco_add = inputplus(True,"Preço: ")

                cursor.execute('INSERT INTO loja (nome, qde, preco) VALUES (?, ?, ?)',(nome_add, qde_add, preco_add))
                cursor.execute('SELECT * FROM loja')
                conn.commit()
                lista_loja = cursor.fetchall()
                exibir_vetor(lista_loja[len(lista_loja)-1])
                input("Pressione Enter para continuar. ")

            case "2":
                cursor.execute('SELECT * FROM loja')
                lista_loja = cursor.fetchall()
                for i in lista_loja:
                    exibir_vetor(i)
                cursor.execute('SELECT qde*preco FROM loja')
                valor_total = 0
                valores_loja = cursor.fetchall()
                for j in valores_loja:
                    valor_total += j[0]
                print("Valor Total do estoque:",locale.currency(valor_total, grouping=True))
                input("Pressione Enter para continuar. ")

            case "3":
                id_update = inputplus(False,"ID: ")
                cursor.execute(f'SELECT * FROM loja WHERE id = {id_update}')
                lista_loja = cursor.fetchall()
                if len(lista_loja) > 0:
                    exibir_vetor(lista_loja[len(lista_loja)-1])
                    nome_update = input("Novo nome: ")
                    qde_update = inputplus(False,"Nova quantidade: ")
                    preco_update = inputplus(True,"Novo preço: ")

                    cursor.execute(f"UPDATE loja SET nome = '{nome_update}', qde = {qde_update}, preco = {preco_update} WHERE id = {id_update}")
                    conn.commit()
                    cursor.execute(f'SELECT * FROM loja WHERE id = {id_update}')
                    lista_loja = cursor.fetchall()
                    exibir_vetor(lista_loja[len(lista_loja)-1])
                    print("Atualizado com sucesso!")
                    input("Pressione Enter para continuar. ")
                else:
                    print("Produto não encontrado")
                    input("Pressione Enter para continuar. ")

            case "4":
                id_remove = inputplus(False,"ID: ")
                cursor.execute(f'SELECT * FROM loja WHERE id = {id_remove}')
                lista_loja = cursor.fetchall()
                if len(lista_loja) > 0:
                    cursor.execute(f'DELETE FROM loja WHERE id = {id_remove}')
                    conn.commit()
                    exibir_vetor(lista_loja[len(lista_loja)-1])
                    print("Removido com sucesso!")
                    input("Pressione Enter para continuar. ")
                else:
                    print("Produto não encontrado")
                    input("Pressione Enter para continuar. ")

            case "5":
                id_nome = input("Procurar por ID? (S/N) ")

                if id_nome.lower() == "s":

                    search = inputplus(False,"ID: ")
                    cursor.execute(f'SELECT * FROM loja WHERE id = {search}')
                    lista_loja = cursor.fetchall()
                    if len(lista_loja)>0:
                        exibir_vetor(lista_loja[len(lista_loja)-1])
                        input("Pressione Enter para continuar. ")
                    else:
                        print("Produto não encontrado")
                        input("Pressione Enter para continuar. ")

                else:

                    search = input("Nome: ")
                    cursor.execute(f"SELECT * FROM loja WHERE nome = '{search}'")
                    lista_loja = cursor.fetchall()
                    if len(lista_loja)>0:
                        exibir_vetor(lista_loja[len(lista_loja)-1])
                        input("Pressione Enter para continuar. ")
                    else:
                        print("Produto não encontrado")
                        input("Pressione Enter para continuar. ")
            
            case "6":
                id_nome = input("Procurar por ID? (S/N) ")

                if id_nome.lower() == "s":

                    search = inputplus(False,"ID: ")
                    cursor.execute(f'SELECT * FROM loja WHERE id = {search}')
                    lista_loja = cursor.fetchall()
                    if len(lista_loja)>0:
                        exibir_vetor(lista_loja[len(lista_loja)-1])

                else:
                    search = input("Nome: ")
                    cursor.execute(f"SELECT * FROM loja WHERE nome = '{search}'")
                    lista_loja = cursor.fetchall()
                    
                    if len(lista_loja)>0:
                        vetor_nome = lista_loja[len(lista_loja)-1]
                        exibir_vetor(vetor_nome)
                        search = vetor_nome[0]         
                    
                if len(lista_loja)>0:
                    vetor_venda = lista_loja[len(lista_loja)-1]
                    qde_vendida = inputplus(False, "Quantidade vendida: ")
                    if qde_vendida <= vetor_venda[2]:
                        qde_nova = vetor_venda[2] - qde_vendida
                        valor_venda = qde_vendida*vetor_venda[3]
                        cursor.execute(f"UPDATE loja SET qde = {qde_nova} WHERE id = {search}")
                        conn.commit()
                        print("Valor da venda:", locale.currency(valor_venda, grouping=True))
                        cursor.execute(f'SELECT * FROM loja WHERE id = {search}')
                        lista_loja = cursor.fetchall()
                        exibir_vetor(lista_loja[len(lista_loja)-1])
                        input("Pressione Enter para continuar. ")
                    else:
                        print("Quantidade não disponível!")
                        input("Pressione Enter para continuar. ")


                else:
                    print("Produto não encontrado")
                    input("Pressione Enter para continuar. ")

            case "0":
                break

            case _:
                pass

def inputplus(int_or_float,string_question):
    inplus = -1
    while inplus < 0:
        inp = input(string_question)
        try:
            if int_or_float == True:
                if float(inp) >= 0:
                    inplus = float(inp)
                    return inplus
                else:
                    print("Valor invalido!")
            else:
                if int(inp) >= 0:
                    inplus = int(inp)
                    return inplus
                else:
                    print("Valor invalido!")
        except ValueError:
            print("Valor invalido!")

def exibir_vetor(vetor):

    print("ID:", vetor[0],"- Descrição:", vetor[1],"- Quantidade:", vetor[2], "- Valor:", locale.currency(vetor[3], grouping=True))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()