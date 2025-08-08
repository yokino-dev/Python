senha_correta = "python123"  # Define a senha correta que o usuário deve digitar

while True:  # Loop infinito que só termina quando a senha correta for digitada
    senha = input("Digite a senha: ")  # Pede para o usuário digitar uma senha

    if senha == senha_correta:  # Verifica se a senha digitada é igual à senha correta
        print("Senha correta! Acesso liberado.")  # Mensagem de sucesso
        break  # Sai do loop, encerrando o programa

    else:  # Caso a senha digitada esteja incorreta
        print("Senha incorreta. Tente novamente.")  # Mensagem de erro, volta a pedir a senha

