
from data.bank import Bank
from userInterface.ui import UI

from data.login import LogIn

from bussinessLogic.clientController import ClientController
from bussinessLogic.adminController import AdminController

bank = Bank()
ui = UI()
login = LogIn()

adminCon = AdminController(ui, bank, login,)
clientCon = ClientController(ui, bank)

while True:
  ui.welcome()
  ui.showMainMenu()
  option = ui.askOption()

  if not option:
    ui.showMessageRed('Opción no valida. Intente de nuevo.')
    continue

  if option[0] != 'a' and option[0] != 'c':
    ui.showMessageRed('Opción no valida. Intente de nuevo.')

  if option[0] == 'a':
    ui.clearConsole()
    adminCon.controller()
    ui.clearConsole()

  if option[0] == 'c':
    ui.clearConsole()
    clientCon.controller()
    ui.clearConsole()
  continue
