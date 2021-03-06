
#parent class (clouboutin) has attributes share by all the child classes
class CLouboutin:
    industry = 'High-end products'
    website = 'https://us.christianlouboutin.com/'
    items = 'Shoes'
    soles = 'Red'
#each child class (dressup and athletic) inherits from the parent (clouboutin) and has its own attributes    
class Dressup(CLouboutin):
    high_heels = 'Kate Strass'
    price = 4395.00
class Athletic(CLouboutin):
    sneakers = 'Spike sock'
    price = 1295.00

obj1 = Dressup()
print(obj1.industry, obj1.items, obj1.high_heels)

obj2 = Athletic()
print(obj2.industry, obj2.items, obj2.sneakers)
