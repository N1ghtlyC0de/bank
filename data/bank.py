from data.cancelTransaction import CancelTransaction
from data.account import Account
from data.client import Client
from userInterface.ui import UI

ui = UI()


class Bank():

  def __init__(self):
    self._clients = {}
    self._accounts = {}
    self.accountNumber = 1

  def getAccount(self, accountId, password):
    try:
      account = self._accounts[int(accountId)]

      if account.verifyPassword(password):
        return account

    except CancelTransaction as error:
      self._ui.showMessage(error)
      pass

  def getClient(self, clientId):
    try:
      client = self._clients[clientId]
      return client

    except CancelTransaction as error:
      self._ui.showMessage(error)

  def setClientInfo(self, clientId, clientName):
    client = Client(clientId, clientName)
    self._clients[clientId] = client
    return client

  def setAccountInfo(self, initialBalance, password):
    account = Account(self.accountNumber, initialBalance, password)
    self._accounts[self.accountNumber] = account
    self.accountNumber += 1
    return account

  def createAccount(self, clientId, clientName, initialBalance, password):
    setNewClient = self.setClientInfo(clientId, clientName)
    setNewAccount = self.setAccountInfo(initialBalance, password)
    setNewClient.addAccount(setNewAccount.id)

    ui.showMessage('La nueva cuenta es: ' + str(self.accountNumber - 1))
    ui.showMessage('Guardando...')

  def deposit(self, amount, account):
    if amount > 0:
      account.balance += amount
      ui.showMessage('Cantidad consignada: ' + str(amount))
      ui.showMessage('Su nuevo saldo: ' + str(account.balance))

    else:
      ui.showMessageRed('El monto a consignar no es válido')

  def withdraw(self, amount, account):
    minus_balance = account.balance - amount
    if minus_balance >= 0:
      account.balance = minus_balance
      ui.showMessage('Cantidad retirada: ' + str(amount))
      ui.showMessage('Su nuevo saldo: ' + str(account.balance))

    else:
      ui.showMessageRed('Saldo insuficiente')

  def showAccounts(self):
    if not self._accounts:
      ui.showMessage('No hay cuentas que mostrar\n')

    for k, v in self._accounts.items():
      print(v)
