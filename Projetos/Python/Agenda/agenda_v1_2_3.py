import re
from email_validator import validate_email, EmailNotValidError

# Criação de um programa que grava contatos
# Versão 1.2.3
# Changelog:
# Validação de Telefone e Email e correção do retorno do tipo na função.

# Definição das variáveis
nome, telefone, endereco, email = "", "", "", ""

# Definição do dicionário de contatos
dict_contatos = {}

def menu():
    # Imprime o menu da agenda.
    print("===================================================")
    print("============= Agenda de Contatos ==================")
    print("===================================================")
    print("====== Digite 1 para Listar contatos ==============")
    print("====== Digite 2 para Adicionar contatos ===========")
    print("====== Digite 3 para Alterar contatos =============")
    print("====== Digite 4 para Excluir contato ==============")
    print("====== Digite 5 para Excluir todos os contatos ====")
    print("====== Digite 6 para sair do sistema ==============")
    print("===================================================")
    
    # Retorna a opção do menu escolhida.
    return int(input("Digite uma opção do menu: "))    


def excluir_todos_contatos():
    # Exclui todos os registros da lista de contatos.
    dict_contatos.clear()
    print("Lista de contatos apagada com sucesso!")


def excluir_contato():
    print("Qual contato deseja excluir:")
    # Realizo a impressão dos contatos para verificação 
    # dos contatos para exclusão.
    print(dict_contatos)
    telefone = preencher_telefone()
    
    del dict_contatos[telefone]
    
    if telefone not in dict_contatos:
        print("Contato excluído com sucesso!")
        

def preencher_telefone():
    return input("Digite o número de telefone do contato: ")


def preencher_email():
    return input("Digite o email do contato: ")


def preencher_nome_contato():
    return input("Digite o nome do contato: ")


def preencher_endereco():
    return input("Digite o endereço do contato: ")


def _valida_email():
    email = preencher_email()
    
    try:
        email_validado = validate_email(email, check_deliverability=False)
        email_normalizado = email_validado.email

        return email_normalizado

    except EmailNotValidError as e:
        print(f"Email inválido: {email}")

        return None    
    

def _valida_telefone():
    print("Preencher telefone no Formato: XX 9XXXX-XXXX")
    telefone = preencher_telefone()
    
    padrao = r'^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$'
    if re.match(padrao, telefone):
        # Retorna o telefone no padrão.
        return telefone
    
    # Retona false caso o telefone não esteja no padrão.
    return None

def adicionar_contato():
    # Recebe o telefone no padrão ou false para apresentar formato inválido
    # para informar novamente o valor.
    telefone = _valida_telefone()
    
    if telefone == False:
        print("Formato de telefone inválido!")
        return
    
    if telefone in dict_contatos:
        print("Telefone já cadastrado!")
        return
    
    email = _valida_email()
    if email == None:
        return
    
    dict_contatos[telefone] = {
        "nome": preencher_nome_contato(),
        "email": email,
        "endereco": preencher_endereco()
    }
    

def atualizar_contato():
    print(dict_contatos)
    print("Lista de contatos para atualização")
    telefone = preencher_telefone()
    dict_contatos[telefone]["nome"] = preencher_nome_contato()
    dict_contatos[telefone]["email"] = preencher_email()
    dict_contatos[telefone]["endereco"] = preencher_endereco()
    

while True:
    opcao = menu()

    match opcao:
        case 1:
            print("Listando...")
            
            # Verifica se existe algum contato na lista.
            if not dict_contatos:
                
                print("Lista vazia!")
                
            else:                
                print("Contatos cadastrados:")
                print(dict_contatos)
        
        case 2:
            # Chama método para adicionar contato no dicionário.
            adicionar_contato()
            
        case 3:
            # Chama o método para atualização de registros do dicionário.
            atualizar_contato()
        
        case 4:
            # Chamada do método que exclui o contato na lista.
            excluir_contato()
            
        case 5:
            # Apagando todos os itens do dicionário.
            excluir_todos_contatos()
        
        case 6:
            # Saindo do aplicativo.
            print("Saindo....")  
            break
        
        case _:
            # Entra nessa opção quando não é nenhuma das opções acima.
            print("Opção inválida!")