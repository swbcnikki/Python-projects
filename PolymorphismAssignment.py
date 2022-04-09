
#Parent Class StarTrek TOS
class StarTrekBlue:
    creator = 'Gene Roddenberry'
    TOS_setting = 'Starship'
    TOS_captain = 'James T Kirk'
    TOS_vessel = 'USS Enterprise'

    def getTickets(self):
        enter_creator = input('Name of creator: ')
        enter_TOS_setting = input('TOS Environment: ')
        enter_TOS_captain = input('Name of TOS captain: ')
        enter_TOS_vessel = input('Name of TOS vessel: ')
        if (enter_creator == self.creator and enter_TOS_setting == self.TOS_setting and
            enter_TOS_captain == self.TOS_captain and enter_TOS_vessel == self.TOS_vessel):
            print('\nYou win tickets to TrekkieCon level 1!\n')
        else:
            print('\nNo entry! Review your answers and try again!\n')

            
#Child Class StarTrek TNG
class StarTrekRed:
    TNG_captain = 'Jean-Luc Picard'
    TNG_vessel = 'USS Enterprise D'
    TNG_security_chief = 'Worf son of Mogh'

    def getTickets(self):
        enter_TNG_captain = input('Name of TNG captain: ')
        enter_TNG_vessel = input('Name of TNG vessel: ')
        enter_TNG_security_chief = ('Full name of TNG Chief of Security: ')
        if (enter_TNG_captain == self.TNG_captain and enter_TNG_vessel == self.TNG_vessel and enter_TNG_security_chief == self.TNG_security_chief):
            print('\nYou win tickets to TrekkieCon level 2!\n')
        else:
            print('\nNo entry! Review your answers and try again!\n')


#Child Class StarTrek DS9
class StarTrekYellow:
    DS9_captain = 'Benjamin Sisko'
    DS9_vessel = 'USS Defiant'
    DS9_setting = 'Space Station'

    def getTickets(self):
        enter_DS9_captain = input('Name of DS9 captain: ')
        enter_DS9_vessel = input('Name of DS9 vessel: ')
        enter_DS9_setting = input('DS9 Environment: ')
        if (enter_DS9_captain == self.DS9_captain and enter_DS9_vessel == self.DS9_vessel and enter_DS9_setting == self.DS9_setting):
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
