from data.cancelTransaction import CancelTransaction


class AdminController():

  def __init__(self, ui, bank, login):
    self._ui = ui
    self._bank = bank
    self._login = login

  def controller(self):
    accessKeys = self._login.extractInfo()
    while True:
      loginList = []
      #Username
      self._ui.showMessage('Digite el Usuario (Si desea cancelar el ingreso, presione Enter)')
      adminUsername = self._ui.askInfo()
      if not adminUsername:
        break

      #Password
      self._ui.showMessage('Digite la Contraseña (Si desea cancelar el ingreso, presione Enter)')
      adminPassword = self._ui.askInfo()
      if not adminPassword:
        break

      loginList.append(adminUsername)
      loginList.append(adminPassword)

      if loginList == accessKeys:
        loginList.clear()
        self._ui.clearConsole()
        #Menú Admin
        while True:
          self._ui.welcome()
          self._ui.showAdminMenu()
          option = self._ui.askOption()

          #operaciones administrador
          if not option:
            self._ui.showMessageRed('Opción no valida. Intente de nuevo.')
            continue

          if option[0] != 'a' and option[0] != 'm' and option[0] != 't':
            self._ui.showMessageRed('Opción no valida. Intente de nuevo.')
            continue

          if option[0] == 'a':  #abrir cuenta
            self._ui.showMessage('*** Abrir Cuenta ***')
            clientId = self._ui.askUserId()
            clientName = self._ui.askUserName()
            startingBalance = self._ui.askAccountBalance()
            accountPassword = self._ui.askAccountPassword()

            try:
              self._bank.createAccount(clientId, clientName, startingBalance, accountPassword)

            except CancelTransaction:
              self._ui.showMessageRed('error')
              continue

          if option[0] == 'm':  #mostrar cuentas
            self._ui.showMessage('*** Mostrar Cuentas ***')
            self._bank.showAccounts()
            continue

          if option[0] == 't':  #terminar
            print()
            self._ui.clearConsole()
            break

      else:
        self._ui.showMessageRed('Por favor, verifique los datos.')
        loginList.clear()
        continue
