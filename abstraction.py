

from abc import ABC, abstractmethod
class secretAgentMan(ABC):
    def realName(self, name):
        print('Real name of agent: ', name)

    @abstractmethod
    def moniker(self, name):
        pass

class Alias(secretAgentMan):
    def moniker(self, name):
        print('Your undercover name will be {} for this case '.format('Napoleon'))


obj = Alias()
obj.realName('Chad')
obj.Alias('Napoleon')
obj.Alias()
