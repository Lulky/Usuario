from User import User


john = User("jhon")
mary = User("Mary")



john.hacer_deposito(1500)
john.hacer_retiro(100)

mary.hacer_deposito(100)

john.transfer_dinero(mary, 100)

john.mostrar_balance_usuario()

print(john.pesos)
print(mary.pesos)