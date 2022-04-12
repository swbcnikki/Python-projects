

from abc import ABC, abstractmethod #importing abc module
class secretAgentMan(ABC): #abstract class
    def realName(self,name): #method - regular method
        print('Real name of agent: ',name)

    @abstractmethod
    def moniker(self): #method definition
        pass

class Alias(secretAgentMan):
    def moniker(self): #abstract method definition
        print('Your undercover name will be {} for this case '.format('Napoleon'))


obj = Alias()
obj.realName('Chad')
obj.moniker()

