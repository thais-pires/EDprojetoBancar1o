from banco import Cliente, Conta, Banco, Imovel, Financiamento
import random


def onInit():
    imovel1 = Imovel(1, "casa", 12000.0)
    imovel2 = Imovel(2, "apartamento", 23000.0)

    cliente1 = Cliente("nome1", "000", 22222.0)
    cliente2 = Cliente("nome2", "111", 44444.0, [])

    conta1 = Conta(111, 14000.0, cliente1)
    conta2 = Conta(222, 33500.0, cliente2)

    banco1 = Banco("Banco Impostor", [conta1, conta2], [])

    financiamento1 = Financiamento(cliente1, imovel1,  banco1, 12000.0, 0)
    financiamento2 = Financiamento(cliente2, imovel2,  banco1, 23000.0, 0)

    banco1.set_financiamentos([financiamento1, financiamento2])

    return banco1


banco = onInit()
encerrar = False

while(encerrar != True):
    inicio = int(input(f"""Bem-vindo ao {banco.get_nome_do_banco()}!

Selecione a opção desejada:
1) Já é cliente?
2) Cadastrar-se
3) Sair
"""))

    if inicio == 2:
        nome = input("Qual o seu nome?\n")
        cpf = input("Qual o seu CPF?\n")
        salario = float(input("Qual o seu salário?\n"))
        cliente = Cliente(nome, cpf, salario)
        opcao = int(input("""Você deseja adicionar algum valor na sua conta?
1) Sim
2) Não
"""))
        saldo = 0
        if opcao == 1:
            saldo = float(input("Insira o valor\n"))
        id = random.randint(0, 999)
        conta = Conta(id, saldo, cliente)

        contas = banco.get_contas()
        contas.append(conta)
        banco.set_contas(contas)

        print(f"Conta criada! Sua conta é de número {id}")
        continue

    if inicio == 1:
        while (True):
            cpf = input("Insira o seu CPF\n")
            try:
                conta = banco.buscar_conta_por_cpf(cpf)
                while (True):
                    menu = int(input("""
Escolha o número da opção desejada:
1) Transferir dinheiro para outra conta
2) Conferir financiamentos de um cliente
3) Total de valor nas contas do banco
4) Total dos financiamentos do cliente
5) Listar clientes com alto rendimento
6) Sair
"""))
                    if menu == 1:
                        cpf = input("Insira o CPF do destinatário:\n")
                        try:
                            outra_conta = banco.buscar_conta_por_cpf(cpf)
                            valor = float(input("Insira o valor:\n"))
                            outra_conta = conta.transferencia(
                                valor, outra_conta)
                            contas = []
                            for c in banco.get_contas():
                                if c.get_cliente().get_cpf() == cpf:
                                    contas.append(outra_conta)
                                else:
                                    contas.append(c)
                            banco.set_contas(contas)
                            print(f"Transferido R${valor:.2f} com sucesso".replace(
                                ".", ",")+".\n")
                            continue
                        except Exception as e:
                            print(e)
                            continue

                    if menu == 2:
                        if len(banco.get_financiamentos()) < 1:
                            print(
                                "Esse cliente não possui financiamentos")
                        for f in banco.get_financiamentos():
                            if f.get_cliente().get_cpf() == conta.get_cliente().get_cpf():
                                print(
                                    f"Imóvel do tipo {f.get_imovel().get_tipo()}, no valor de R${f.get_imovel().get_valor():.2f}")
                                continue
                        continue

                    if menu == 3:
                        valor_contas = banco.total_valor_contas()
                        print(
                            f"O valor total das contas é de R${valor_contas:.2f}".replace(
                                ".", ","))
                        continue

                    if menu == 4:
                        total_financiado_cliente = conta.get_cliente().total_financiado()
                        print(f"Valor total R${total_financiado_cliente:.2f}".replace(
                            ".", ","))

                    if menu == 5:
                        for c in banco.get_contas():
                            if c.get_cliente().get_salario() >= 20000:
                                cliente = c.get_cliente()
                                print(
                                    f"Cliente: {cliente.get_nome()}, de CPF {cliente.get_cpf()}")

                    if menu == 6:
                        break

            except Exception as e:
                print(e)
                resposta = input("Deseja inserir novamente? S/N\n").lower()
                while (resposta not in ["s", "n"]):
                    resposta = input(
                        "Opção inválida. Deseja inserir novamente? S/N\n").lower()
                if resposta == "s":
                    continue
                break
        continue
    if inicio == 3:
        print("Programa encerrado")
        encerrar = True
