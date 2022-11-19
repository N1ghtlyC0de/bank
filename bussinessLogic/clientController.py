from data.cancelTransaction import CancelTransaction


class ClientController():

  def __init__(self, ui, bank):
    self._ui = ui
    self._bank = bank

  def controller(self):
    while True:
      self._ui.welcome()
      userID = self._ui.askUserId()
      if not userID:
        self._ui.showMessageRed('Opción no valida. Intente de nuevo.')
        continue
      checkUserID = self._bank.getClient(userID)
      if checkUserID:
        self._ui.showClientMenu()
        option = self._ui.askOption()

        #operaciones cliente
        if not option:
          self._ui.showMessageRed('Opción no valida. Intente de nuevo.')
          continue

        if option[0] != 's' and option[0] != 'c' and option[
            0] != 'r' and option[0] != 't':
          self._ui.showMessageRed('Opción no valida. Intente de nuevo.')
          continue

        if option[0] == 's':  #ver saldo
          self._ui.showMessage('*** Obtener Saldo ***')
          accountId = self._ui.askAccountId()
          password = self._ui.askAccountPassword()

          account = self._bank.getAccount(accountId, password)

          self._ui.showMessage('El saldo es: ' + str(account.balance))

        if option[0] == 'c':  #consignar
          self._ui.showMessage('*** Consignación ***')
          accountId = self._ui.askAccountId()
          password = self._ui.askAccountPassword()

          account = self._bank.getAccount(accountId, password)

          amount = int(self._ui.askDepositAmount())
          self._bank.deposit(amount, account)

        if option[0] == 'r':  #retirar
          self._ui.showMessage('*** Retiro ***')
          accountId = self._ui.askAccountId()
          password = self._ui.askAccountPassword()

          account = self._bank.getAccount(accountId, password)

          amount = int(self._ui.askWithdrawAmount())
          if amount <= 0:
            self._ui.showMessageRed('El monto a retirar no es válido')
          else:
            self._bank.withdraw(amount, account)

        if option[0] == 't':  #terminar
          break

      else:
        self._ui.showMessage(
          'La identificaión ingresada no se encuentra en nuestro sistema.')
        break
