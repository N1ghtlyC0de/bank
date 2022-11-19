class Client():

  def __init__(self, id, name):
    self._id = id
    self._name = name
    self._accountIds = set()

  def addAccount(self, newId):
    self._accountIds.add(newId)
