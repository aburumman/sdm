# Auto generate new documents name from date and random alphabet
# Author: Alayande Mustapha: alayandemustapha@gmail.com
from  datetime import datetime
from random import choice


vowels_s = ['a', 'e', 'i', 'o', 'u']
cons = ['b','c','d','f','g','h','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


def docname(): 
    return str(str(datetime.now())[0:19].replace(':', '-') + '-' + '{}{}{}{}{}{}'.format(choice(cons), \
        choice(vowels_s),choice(cons), choice(vowels_s),choice(cons), choice(vowels_s)))
    

#print(docname())