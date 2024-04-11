class ContaBancaria: 
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self,valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")  
        

    def exibir_detalhes(self):
        print("Número da conta:" , self.numero)
        print("Titular:" , self.titular)
        print("Saldo:",round(self.saldo,2))



#aqui é criado uma instancia com do objeto "ContaBancaria"
#com o nome conta_do_vitor
numero_conta = input("Digite o numero da conta:")
titular_conta = input("Digite o titular da conta:")
saldo_inicial = float(input("Digite o saldo inicial da conta:").replace(",","."))



conta_do_vitor = ContaBancaria(numero_conta , titular_conta , saldo_inicial)

#Usando os metodos do objeto ContaBancaria
valor_deposito = float(input("Digite o valor a ser depositado:").replace(",","."))
valor_saque = float(input("Digite o valor a ser sacado:") .replace(",","."))

conta_do_vitor.depositar(valor_deposito)
conta_do_vitor.sacar(valor_saque)
conta_do_vitor.exibir_detalhes()

