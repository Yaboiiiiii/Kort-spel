print("Välkommen till mitt spel av russian roulette. Vinn eller dö")

miss = 0

plats = input("välj ett nummer mellan 0 och 5: ")

while miss != 6:

    import random

    kula = [0,1,2,3,4,5]
    live = random.randint(0,5)
    kula[live] = "ded"
    for x in kula:
        print(x)

    if int(plats) == live:  
        print("Du är sämst på det här.")
    else:
        print("Du är inte lika sämst som hen som dog")


