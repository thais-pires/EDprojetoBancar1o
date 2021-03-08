from banco import Cliente, Conta, Banco, Imovel, Financiamento
import random


def onInit():
    imovel1 = Imovel(1, "casa", 12000.0)
    imovel2 = Imovel(2, "apartamento", 23000.0)

    cliente1 = Cliente("João", "000", 22222.0)
    cliente2 = Cliente("Maria", "111", 44444.0, [])

    conta1 = Conta(111, 14000.0, cliente1)
    conta2 = Conta(222, 33500.0, cliente2)

    banco1 = Banco("Banco Thief", [conta1, conta2], [])

    financiamento1 = Financiamento(cliente1, imovel1,  banco1, 12000.0, 0)
    financiamento2 = Financiamento(cliente2, imovel2,  banco1, 23000.0, 0)

    banco1.set_financiamentos([financiamento1, financiamento2])

    return banco1


banco = onInit()
encerrar = False

while(encerrar != True):
    inicio = int(input(f"""====================================
\033[1;33mBem-vindo ao {banco.get_nome_do_banco()}!\033[m

\033[1;34mDigite o número da opção desejada:\033[m
\033[1;33m1\033[m  Já é cliente?
\033[1;33m2\033[m  Cadastrar-se
\033[1;33m3\033[m  Sair
====================================
"""))

    if inicio == 2:
        nome = input("\n\033[1;33mQual o seu nome?\033[m\n")
        cpf = input("\n\033[1;33mQual o seu CPF?\033[m\n")
        salario = float(input("\n\033[1;33mQual o seu salário?\033[m\n"))
        cliente = Cliente(nome, cpf, salario)
        opcao = int(input("""\n\033[1;33mVocê deseja adicionar algum valor na sua conta?
1) Sim
2) Não\033[m
"""))
        saldo = 0
        if opcao == 1:
            saldo = float(input("\n\033[1;33mInsira o valor\033[m\n"))
        id = random.randint(0, 999)
        conta = Conta(id, saldo, cliente)

        contas = banco.get_contas()
        contas.append(conta)
        banco.set_contas(contas)

        print(
            f"\n\033[1;33mConta criada! Sua conta é de número\033[m \033[1;34m{id}\033[m\n")
        continue

    if inicio == 1:
        while (True):
            cpf = input(
                "\n\033[1;33mInsira o seu CPF (pra agilizar, pode usar\033[m \033[1;34m000\033[m \033[1;33mou\033[m \033[1;34m111\033[m\033[1;33m)\033[m\n")
            try:
                conta = banco.buscar_conta_por_cpf(cpf)
                while (True):
                    menu = int(input("""
\033[1;34mDigite o número da opção desejada:\033[m
\033[1;33m1\033[m  Transferir dinheiro para outra conta
\033[1;33m2\033[m  Conferir financiamentos de um cliente
\033[1;33m3\033[m  Total de valor nas contas do banco
\033[1;33m4\033[m  Total dos financiamentos do cliente
\033[1;33m5\033[m  Listar clientes com alto rendimento
\033[1;33m6\033[m  Logar com outro CPF
\033[1;33m7\033[m  Sair
"""))
                    if menu == 1:
                        cpf = input(
                            "\n\033[1;33mInsira o CPF do destinatário:\033[m\n")
                        try:
                            outra_conta = banco.buscar_conta_por_cpf(cpf)
                            valor = float(
                                input("\n\033[1;33mInsira o valor:\033[m\n"))
                            outra_conta = conta.transferencia(
                                valor, outra_conta)
                            contas = []
                            for c in banco.get_contas():
                                if c.get_cliente().get_cpf() == cpf:
                                    contas.append(outra_conta)
                                else:
                                    contas.append(c)
                            banco.set_contas(contas)
                            print(f"\n\033[1;33mTransferido\033[m \033[1;34mR${valor:.2f}\033[m \033[1;33mcom sucesso\033[m\n".replace(
                                ".", ","))
                            continue
                        except Exception as e:
                            print(e)
                            continue

                    if menu == 2:
                        if len(banco.get_financiamentos()) < 1:
                            print(
                                "\n\033[1;33mEsse cliente não possui financiamentos\033[m\n")
                        for f in banco.get_financiamentos():
                            if f.get_cliente().get_cpf() == conta.get_cliente().get_cpf():
                                print(
                                    f"\n\033[1;33mImóvel do tipo\033[m \033[1;34m{f.get_imovel().get_tipo()}\033[m\033[1;33m no valor de\033[m \033[1;34mR${f.get_imovel().get_valor():.2f}\033[m\n".replace(
                                        ".", ","))
                                continue
                        continue

                    if menu == 3:
                        valor_contas = banco.total_valor_contas()
                        print(
                            f"\n\033[1;33mO valor total das contas neste banco é de\033[m \033[1;34mR${valor_contas:.2f}\033[m\n".replace(
                                ".", ","))
                        continue

                    if menu == 4:
                        total_financiado_cliente = conta.get_cliente().total_financiado()
                        print(f"\n\033[1;33mValor financiado total\033[m \033[1;34mR${total_financiado_cliente:.2f}\033[m\n".replace(
                            ".", ","))

                    if menu == 5:
                        for c in banco.get_contas():
                            if c.get_cliente().get_salario() >= 20000:
                                cliente = c.get_cliente()
                                print(
                                    f"\033[1;33mCliente {cliente.get_nome()}, de CPF {cliente.get_cpf()}, com salário de\033[m \033[1;34mR${cliente.get_salario()}\033[m".replace(
                                        ".", ","))

                    if menu == 6:
                        break

                    if menu == 7:
                        quit()

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
