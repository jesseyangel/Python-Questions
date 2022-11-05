print ('Cadastre seu usuario!')

login = str(input('Login: '))
senha = str(input('Senha: '))

while login.lower == senha.lower: #Repetir processo se forem iguais
    print('Ops! O usuário não pode ser igual a senha, tente novamente.')
    login = str(input("Login: "))
    senha = str(input("Senha: "))
else: #Caso sejam diferentes
    print("Cadastrato efetuado com sucesso")
    
