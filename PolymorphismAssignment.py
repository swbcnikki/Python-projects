



#Parent Class StarTrek TOS
class StarTrekBlue:
    creator = 'Gene Roddenberry' # attributes
    setting = 'Starship'
    captain = 'James T Kirk'
    vessel = 'USS Enterprise'

    def getTickets(self): # method for parent class indented under it
        enter_creator = input('Name of creator: ')
        enter_setting = input('TOS Environment: ')
        enter_captain = input('Name of TOS captain: ')
        enter_vessel = input('Name of TOS vessel: ')
        if (enter_creator == self.creator and enter_setting == self.setting and
            enter_captain == self.captain and enter_vessel == self.vessel):
            print('\nYou win tickets to TrekkieCon level 1!\n')
        else:
            print('\nNo entry! Review your answers and try again!\n')

            
#Child Class StarTrek TNG
class StarTrekRed(StarTrekBlue): #connects parent and this child class
    captain = 'Jean-Luc Picard' # captain name override
    vessel = 'USS Enterprise D' # vessel name override
    security_chief = 'Worf son of Mogh' # new attribute for this child

    def getTickets(self): # method for this child class indented under it
        enter_captain = input('Name of TNG captain: ')
        enter_vessel = input('Name of TNG vessel: ')
        enter_security_chief = input('Full name of TNG Chief of Security: ')
        if (enter_captain == self.captain and enter_vessel == self.vessel and enter_security_chief == self.security_chief):
            print('\nYou win tickets to TrekkieCon level 2!\n')
        else:
            print('\nNo entry! Review your answers and try again!\n')


#Child Class StarTrek DS9
class StarTrekYellow(StarTrekBlue): # connects parent and this child class
    captain = 'Benjamin Sisko' # captain name override
    vessel = 'USS Defiant' # vessel name override
    setting = 'Space Station' # setting override

    def getTickets(self): # method for this child class indented under it
        enter_captain = input('Name of DS9 captain: ')
        enter_vessel = input('Name of DS9 vessel: ')
        enter_setting = input('DS9 Environment: ')
        if (enter_captain == self.captain and enter_vessel == self.vessel and enter_setting == self.setting):
            print('\nYou win tickets to TrekkieCon level 3!\n')
        else:
            print('\nNo entry! Review your answers and try again!\n')            


if __name__ == "__main__":

    fan = StarTrekBlue()
    fan.getTickets()
    
    superfan =  StarTrekRed()
    superfan.getTickets()
   
    uberfan = StarTrekYellow()
    uberfan.getTickets()

