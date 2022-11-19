class LogIn():

  def extractInfo(self):
    with open('.//resources//adminInfo.txt', 'r',
              encoding='utf-8') as loginFile:
      for line in loginFile:
        line = line.split(', ')
        return line
