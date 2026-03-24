# Criação de um programa que grava contatos
# Versão 1.0

# Definição das variáveis
nome, telefone, endereco, email = "","","",""

# Definição do dicionário de contatos
dict_contatos = {}

print("=======================================")
print("========= Agenda de Contatos ==========")
print("=======================================")

def menu():
    print("===================================================")
    print("====== Digite 1 para Listar contatos ==============")
    print("====== Digite 2 para Adicionar contatos ===========")
    print("====== Digite 3 para Alterar contatos =============")
    print("====== Digite 4 para Excluir contato ==============")
    print("====== Digite 5 para Excluir todos os contatos ====")
    print("====== Digite 6 para sair do sistema ==============")
    print("===================================================")

def excluir_contato(telefone):
    del dict_contatos[telefone]
    
    if telefone not in dict_contatos:
        print("Contato excluído com sucesso!")


def adicionar_contato():

    nome = input("Digite o nome do contato: ").strip()

    telefone = input("Digite o Telefone do contato: ").strip()    
    if telefone in dict_contatos:
        print("Telefone já cadastrado!")
        return

    email = input("Digite o email do contato: ").strip()
    endereco = input("Digite o endereço do contato: ").strip() 
    
    dict_contatos[telefone] = {
        "nome": nome,
        "email": email,
        "endereco": endereco
    }

while True:
    menu()
    opcao = int(input("Digite a opção do menu: "))    

    match opcao:
        case 1:
            print("Listando...")
            if not dict_contatos:
                print("Lista vazia!")
                
            else:                
                print("Contatos cadastrados:")
                print(dict_contatos)
                print("=====================================================")
        
        case 2:
            # Chama método para adicionar contato no dicionário
            adicionar_contato()
        
        case 4:
            print("Qual contato deseja excluir:")
            print(dict_contatos)
            contato = input("Digite o número do telefone para exclusão: ")
            excluir_contato(contato)
            
        case 5:
            # Apagando todos os itens do dicionário
            print("Lista de contatos apagada com sucesso!")
            dict_contatos.clear()
        
        case 6:
            print("Saindo....")  
            break
        
        case _:
            print("Opção inválida!")