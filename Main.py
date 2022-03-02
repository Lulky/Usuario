from User import User


john = User("jhon")
mary = User("Mary")
luciano = User("Luciano")



john.hacer_deposito(1500)
john.hacer_deposito(300)
john.hacer_deposito(200)
john.hacer_retiro(600)

john.mostrar_balance_usuario()

mary.hacer_deposito(400)
mary.hacer_deposito(500)

mary.mostrar_balance_usuario()

luciano.hacer_deposito(400)
luciano.hacer_retiro(50)
luciano.hacer_retiro(150)
luciano.hacer_retiro(199)

luciano.mostrar_balance_usuario()

#Bonus

john.transfer_dinero(luciano, 400)

john.mostrar_balance_usuario()
luciano.mostrar_balance_usuario()




