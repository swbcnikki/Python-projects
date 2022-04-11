

class Password:
    def __init__(self):
        self.passwordVar = 'qwerty1' #This is a non protected password
                
        self._passwordVar = 'qwerty123' #This is a protected password because of the _ before the word password
                
        self.__passwordVar = 'qwerty123!@#' #This is a private password because of the __ before the word password

    def getPassword(self):
        print(self.__passwordVar)

    def setPassword(self):
        self.__passwordVar = password
        

obj = Password()

print(obj.passwordVar)

print(obj._passwordVar)

obj.getPassword()
obj.setPassword()
print(obj.password)

