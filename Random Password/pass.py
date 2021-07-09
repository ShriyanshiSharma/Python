# Ramdom password generator
import random
 
wordlist =[]
sc = ['@','#','#','$','*','&','!']

with open("para.txt","r") as f:
    data = f.readlines()

    for line in data:
        words = line.split()
        
        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())
                
word = random.choice(wordlist)
sch = random.choice(sc)
nm = str(random.randint(10,99))

pas = word + sch + nm

print(pas)
