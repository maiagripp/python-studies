class Cliente:
    def __init__(self, nome, cpf, idade, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        print("Saldo insuficiente")
        return False
    
    def extrato(self):
        return self.saldo
    

cliente1 = Cliente('João', '11111111111', 25, 1000)
cliente2 = Cliente('Maria', '22222222222', 30, 500)
cliente3 = Cliente('Jose', '33333333333', 35, 1500)

cliente1.depositar(100)
cliente1.sacar(50)
# cliente2.depositar(200)
cliente2.sacar(600) 
cliente3.depositar(300)
cliente3.sacar(150)

print(cliente1.extrato())
print(cliente2.extrato())
print(cliente3.extrato())
