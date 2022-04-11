

class Password:
    def __init__(self):
        self.passwordVar = 'qwerty1' #This is a non protected password
                
        self._passwordsVar = 'qwerty123' #This is a protected password because of the _ before the word password
                
        self.__passwordssVar = 'qwerty123!@#' #This is a private password because of the __ before the word password

    def getPassword(self):
        print(self.__passwordssVar)

    def setPassword(self, password):
        self.__passwordssVar = password
        

obj = Password()

print(obj.passwordVar)

print(obj._passwordsVar)

obj.getPassword()
obj.setPassword('zxcvb')
obj.getPassword()

