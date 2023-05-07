print("=======================================================\n" +
      "===       ====     ====       ===        ====     =====\n" +
      "===  ===  ==  =====  ==  ====  =====  =====  =====  ===\n" +
      "===  ===  ==  =====  ==  ===  ======  =====  =====  ===\n" +
      "===       ==  =====  ==  =  ========  =====  =====  ===\n" +
      "===  =======  =====  ==  ===  ======  =====  =====  ===\n" +
      "===  =========     ====  ====  =====  =======     =====\n" +
      "=======================================================\n\n" +
      "Bem vindo a Porto! Antes de iniciarmos o seu atendimento, precisamos de alguns dados para confirmar seu cadastro.\n")

fullname = input("Digite seu nome completo: ")
email = input("Digite seu email: ")
cpf = input("Digite seu CPF: ")

name = fullname.split(" ")[0]

option = ""
requestedCarPlate = ''
requestedAddress = ''

while option != "5":
  print("\n\n==== MENU ==========================\n" +
        "Bem vindo de volta, {}!\n".format(name) +
        "Selecione uma das opções:\n\n" +
        "1. Solicitar guincho\n" +
        "2. Cancelar solicitação de gincho\n" +
        "3. Visualizar dados da sua solicitação\n" +
        "4. Falar com um atendente\n" +
        "5. Falar com um atendente\n")

  option = input("Digite o identificador de uma das opções: ")

  match option:
    case '1':
      carPlate = input("\nDigite a placa do carro: ")

      if requestedCarPlate != '' and requestedCarPlate == carPlate:
        print("\n\nJá existe uma solicitação em aberto para a placa informada")
      else:
        requestedCarPlate = carPlate
        requestedAddress = input(
            "\nAgora, informe o endereço ou as coordenadas geográficas que devemos encontrar você: ")

        print("\n\nGuincho solicitado com sucesso! Aguarde até que um de nossos parceiros se encaminhe ao endereço indicado.")
    case '2':
      carPlate = input("\nDigite a placa do carro: ")

      if requestedCarPlate != '' and requestedCarPlate == carPlate:
        carPlate = ''
        requestedCarPlate = ''
        requestedAddress = ''
        print("\n\nSua solicitação foi cancelada com sucesso")
      else:
        print("\n\nNão foi encontrado uma solicitação em aberto para a placa informada")
    case '3':
      carPlate = input("\nDigite a placa do carro: ")

      if requestedCarPlate != '' and requestedCarPlate != carPlate:
        print("\n\nNão foi encontrado uma solicitação em aberto para a placa informada")
      else:
        print("\n\nCliente: {}".format(name) +
              "\nEmail: {}".format(email) +
              "\nCPF: {}".format(cpf) +
              "\n\nPlaca do carro: {}".format(requestedCarPlate) +
              "\nEndereço para retirada: {}\n".format(requestedAddress))
    case '4':
      print("\nRedirecionando você para um atendente..." +
            "Nossos servidores estão congestionados no momento! Tente novamente mais tarde.")
      break
    case '5':
      print("\nAté logo!")
    case _:
      print("\nOpção inválida")
