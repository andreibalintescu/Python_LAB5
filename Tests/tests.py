from Modelle.IDS.ID import Identifiable
from Modelle.DISHES.FOOD_DRINK import *
from Modelle.CUSTOMERS_AND_ORDERS.CUSTOMERS_ORDERS import *
from Repository.DATA.DATA_REPOS import *

# Am creat un repository pentru bauturi cu fisierul DrinksData
drink_repo = DrinkRepo('DrinksData')

# Am numit doua obiecte de tip drink
drink1 = Drink("1", "Vodka", "300ml", "50lei", "80%")
drink2 = Drink("2","Wasser","1L","15lei","0%")

# Am facut o lista cu aceste obiecte
drinks1 = [drink1,drink2]

# Am salvat lista ca binary in DrinksData
drink_repo.save(drinks1)

#Am afisat continutul binar al fisierului


#Am asignat lista unei variabile
list_of_drinks = drink_repo.load()

#Am convertit continutul intr-o lista de tuplete ce reprezinta atributele fiecarui obiect
conv_content = drink_repo.convert_to_string(list_of_drinks)

#Am salvat continutul convertit in fisier, (continutul din fisier are tipul None)
drink_repo.write_to_file(str(conv_content))

#Am convertit lista de tuplete intr-o lista de obiecte noi
rev_conv_content = drink_repo.read_file()

list_of_drinkies = drink_repo.convert_from_string(rev_conv_content)



