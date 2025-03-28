# Inicializa as variáveis para contar mulheres, homens e pessoas maiores de 18 anos
mulheres = homens = maiores = 0

# Inicia um loop infinito para cadastrar pessoas
while True:
    print("-"*20)  # Imprime uma linha separadora
    print("CADASTRE UMA PESSOA")  # Título do cadastro
    print("-"*20)  # Imprime outra linha separadora
    
    # Solicita a idade da pessoa e converte para inteiro
    idade = int(input("Idade: "))
    
    # Solicita o sexo da pessoa, remove espaços, converte para maiúsculo e pega apenas a primeira letra
    sexo = input("Sexo [M/F]: ").strip().upper()[0]
    
    # Verifica se a idade é maior que 18 e incrementa o contador de maiores de idade
    if idade > 18:
        maiores += 1
    
    # Verifica se o sexo é masculino e incrementa o contador de homens
    if sexo == 'M':
        homens += 1
    
    # Verifica se o sexo é feminino e a idade é menor que 20, incrementando o contador de mulheres jovens
    if sexo == 'F' and idade < 20:
        mulheres += 1
    
    # Pergunta ao usuário se deseja continuar, remove espaços, converte para maiúsculo e pega a primeira letra
    continuar = input("Quer continuar? [S/N]: ").strip().upper()[0]
    
    # Se o usuário escolher 'N', o loop é interrompido
    if continuar == 'N':
        break

# Exibe os resultados finais
print("-"*20)  # Linha separadora
print(f"Total de pessoas maiores de 18 anos: {maiores}")  # Total de pessoas maiores de 18 anos
print(f"Ao todo temos {homens} homens cadastrados.")  # Total de homens cadastrados
print(f"E temos {mulheres} mulheres com menos de 20 anos.")  # Total de mulheres com menos de 20 anos
