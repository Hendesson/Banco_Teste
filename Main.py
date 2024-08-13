class Main:
    pass

print("Testando")

from Cliente import Cliente
from Conta import Conta

c1= Cliente("João", "11444-2222")
conta=Conta(c1.nome,6565,0)


print(conta.titular, "Numero: ",conta.numero, "Seu Saldo: ", conta.saldo)