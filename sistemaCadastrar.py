import os
import secrets
import smtplib


nome_usuario = []
email_usuario = []
senha_usuario = []

entrada = False

while not entrada:
    try:
        nome_digitado = input('Digite o Nome: ')
        email_digitado = input('Digite o E-mail: ')
        senha_digitado = input('Digite a Senha: ')

# este primeiro bloco cria o arquivo txt e o abre em modo de escrita como uma variável chamada credenciais
# a variavel credenciais tem seu valor atribuido pelo que foi digitado no campo correspondente e as escreve no txt linha por linha

        with open('dados.txt', 'w') as credenciais: 
            credenciais.write(f'{nome_digitado}\n')
            credenciais.write(f'{email_digitado}\n')
            credenciais.write(f'{senha_digitado}\n')

# o token é uma sequencia aleatória de caracteres utilizando a biblioteca secrets
        
        token_cadastro = secrets.token_urlsafe(10)
        

# configurações necessárias para o servidor (SMTP) funcionar e o token chegar ao email do usuário
        
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login('estoquemedicohub@gmail.com', 'pifs imrb vvyo kdah')

        remetente = 'estoquemedicohub@gmail.com'
        destinatarios = email_digitado
        mensagem = token_cadastro

        servidor.sendmail(remetente, destinatarios,mensagem)
        print('Token Enviado\nUm código de verificação foi enviado ao email informado')

 # Aqui o cadastro é efetivamente concluido desde que o codigo digitado seja igual ao enviado no email do usuário
 # caso a condição seja verdadeira o programa irá abrir o txt das credenciais em modo leitura cada uma das linhas é salva em uma variavel diferente
 # cada variável por fim vai ser armazenada em sua respectiva lista.
     
        codigo_digitado = input('Digite o código recebido: ')

        if codigo_digitado == token_cadastro:
            with open('dados.txt', 'r') as credenciais:
                nome_novo_usuario = credenciais.readline().strip()
                nome_usuario.append(nome_novo_usuario)
                email_novo_usuario = credenciais.readline().strip()
                email_usuario.append(email_novo_usuario)
                senha_novo_usuario = credenciais.readline().strip()
                senha_usuario.append(senha_novo_usuario)
                print(f'Usuário Cadastrado com Sucesso\nNome = {nome_usuario[0]}\ne-mail = {email_usuario[0]}')

            os.remove('dados.txt')

# Mudando o valor da variável entrada no caso de tudo estar correto encerra o laço             
            
            entrada = True

        else:
            print(f'O codigo informado {codigo_digitado} não corresponde ao token de cadastro')

    except Exception:
        print('Ocorreu um erro!\num ou mais campos de cadastro não foram preenchidos\ne-mail informado não pode ser encontrado')

