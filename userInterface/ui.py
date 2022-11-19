from userInterface.colors import Colors
import os

colors = Colors()


class UI():

  def welcome(self):
    print(colors.AMARILLO, '\n','-' * 7, 'BANCO NACIONAL', '-' * 7, colors.DEFAULT)

  def askUserId(self):
    userId = input('¿Cuál es el número de identificación del cuentahabiente? ')
    return userId

  def askUserName(self):
    userName = input('¿Cuál es el nombre del cuentahabiente? ')
    return userName

  def askAccountId(self):
    accId = input('¿Cuál es el número de la cuenta? ')
    return accId

  def askAccountPassword(self):
    accPassword = input('¿Cuál es la contraseña de la cuenta? ')
    return accPassword

  def askDepositAmount(self):
    depositAmount = input('Ingrese el monto de la consignación: ')
    return depositAmount

  def askWithdrawAmount(self):
    withdrawAmount = input('Ingrese el monto del retiro: ')
    return withdrawAmount

  def askAccountBalance(self):
    initialBalance = input('¿Cuál es el saldo inicial para esta cuenta? ')
    return initialBalance

  def askOption(self):
    option = input('\n¿Qué operación quiere hacer?\n').casefold()
    return option

  def askInfo(self):
    info = input()
    return info

  def showMainMenu(self):
    print('Para ingresar como Administrador, digite a')
    print('Para ingresar como Cliente, digite c')

  def showAdminMenu(self):
    print('Para abrir una nueva cuenta, digite a')
    print('Para mostrar todas las cuentas, digite m')
    print('Para terminar, digite t')

  def showClientMenu(self):
    print('Para obtener el saldo, digite s')
    print('Para consignar, digite c')
    print('Para retirar, digite r')
    print('Para terminar, digite t')

  def showMessage(self, msg):
    print()
    print(colors.AMARILLO, msg, colors.DEFAULT)

  def showMessageRed(self, msg):
    print()
    print(colors.ROJO, msg, colors.DEFAULT)

  def clearConsole(self):
    os.system("clear")