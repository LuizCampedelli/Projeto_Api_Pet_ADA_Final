def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input("Nome do pet: ")

    # Coleta da raça do pet
    raca = input("Raça do pet: ")

    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    # Coleta da informação de vacinação
    vacinado = input("O pet está vacinado? (sim/não): ").strip().lower()
    if vacinado not in ["sim", "não"]:
        print("Por favor, responda com 'sim' ou 'não'.")
        vacinado = input("O pet está vacinado? (sim/não): ").strip().lower()

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Raça: {raca}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")
    print(f"Vacinado: {'Sim' if vacinado == 'sim' else 'Não'}")

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
