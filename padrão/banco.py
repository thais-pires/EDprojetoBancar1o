class Cliente:
    def __init__(
        self,
        nome,
        cpf,
        salario,
        financiamentos=[]
    ):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.financiamentos = financiamentos

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def get_financiamentos(self):
        return self.financiamentos

    def set_financiamentos(self, financiamentos):
        self.financiamentos = financiamentos

    def total_financiado(self):
        return sum(self.financiamentos)


class Conta:
    def __init__(
        self,
        id,
        saldo,
        cliente
    ):
        self.id = id
        self.saldo = saldo
        self.cliente = cliente

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor
        raise Exception("Quantia indisponível para saque.")

    def transferencia(self, valor, outra_conta):
        if(self.saldo >= valor):
            self.saldo -= valor
            outra_conta.creditar(valor)
            return outra_conta
        raise Exception("Saldo indisponível para transferência.")


class Banco:
    def __init__(
        self,
        nome_do_banco,
        contas=[],
        financiamentos=[]
    ):
        self.nome_do_banco = nome_do_banco
        self.contas = contas
        self.financiamentos = financiamentos

    def get_nome_do_banco(self):
        return self.nome_do_banco

    def set_nome_do_banco(self, nome_do_banco):
        self.nome_do_banco = nome_do_banco

    def get_contas(self):
        return self.contas

    def set_contas(self, contas):
        self.contas = contas

    def get_financiamentos(self):
        return self.financiamentos

    def set_financiamentos(self, financiamentos):
        self.financiamentos = financiamentos

    def total_valor_contas(self):
        total_valor = 0
        for c in self.contas:
            total_valor += c.saldo
        return total_valor

    def financiamentos_cliente(self, cpf):
        for c in self.contas:
            if (c.get_cliente().get_cpf() == cpf):
                return c.get_financiamentos()

    def buscar_conta_por_cpf(self, cpf):
        for c in self.contas:
            if (c.get_cliente().get_cpf() == cpf):
                return c
        raise Exception(f"Não existe conta com esse CPF ({cpf})")


class Imovel:
    def __init__(
        self,
        codigo,
        tipo,
        valor
    ):
        self.codigo = codigo
        self.tipo = tipo
        self.valor = valor

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor


class Financiamento:
    def __init__(
        self,
        cliente,
        imovel,
        banco,
        valor_financiamento,
        num_aportes
    ):
        self.cliente = cliente
        self.imovel = imovel
        self.banco = banco
        self.valor_financiamento = valor_financiamento
        self.num_aportes = num_aportes

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_imovel(self):
        return self.imovel

    def set_imovel(self, imovel):
        self.imovel = imovel

    def get_banco(self):
        return self.banco

    def set_banco(self, banco):
        self.banco = banco

    def get_valor_financiamento(self):
        return self.valor_financiamento

    def set_valor_financiamento(self, valor_financiamento):
        self.valor_financiamento = valor_financiamento

    def get_num_aportes(self):
        return self.num_aportes

    def set_num_aportes(self, num_aportes):
        self.num_aportes = num_aportes

    def receber_aporte(self, valor):
        self.valor_financiamento -= valor
        self.num_aportes += 1
