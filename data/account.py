class Account():

  def __init__(self, id, balance, password):
    self._id = id
    self._balance = int(balance)
    self._password = password

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, newId):
    pass

  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, newBalance):
    if newBalance >= 0:
      self._balance = newBalance

  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, newPassword):
    self._password = newPassword

  def verifyPassword(self, password):
    return self._password == password

  def __str__(self):
    return 'Número: ' + str(self._id) + '\nSaldo: ' + str(
      self._balance) + '\nContraseña: ' + str(self._password) + '\n'