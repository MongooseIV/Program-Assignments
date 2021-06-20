def x_to_y(x,m,b):
    y=m*x+b
    return y
foods={"chicken":1.59,"beef":1.99,"cheese":1.00,"milk":2.50}
#print(x_to_y(3,5,1))
def total_price(food1,food2):
    food_price="The total price of "+str(food1)+" and "+str(food2)+" is "+str(foods[food1]+foods[food2])
    return food_price
#print(total_price('chicken','milk'))

def price_dif(food1,food2):
    if foods[food1]>foods[food2]:
        print(f"The difference in price between {food1} and {food2} is {(foods[food1] - foods[food2]):.2}")
    elif foods[food2]>foods[food1]:
        print(f"The difference in price between {food2} and {food1} is {(foods[food2] - foods[food1]):.2}")
    else:
        print("The difference in price between " + str(food1) + " and " + str(food2) + " is 0")
#price_dif("beef","chicken")
bShoes={"Jordan 13":1,"Yeezy":8,"Foamposite":10,"Air Max":5,"SB Dunk":20}
def restock(shoeBrand,rsMultiplier):
    bShoes[shoeBrand]*=rsMultiplier
    return bShoes
#print(restock("Yeezy",3))
def restockAll(rsMultiplier):
    for i in bShoes:
        bShoes[i]*=rsMultiplier
    return bShoes
#print(restockAll(3))

def sale(shoe,num):
    bShoes[shoe]=int(bShoes[shoe]/num)
    return bShoes
#print(sale("Foamposite",4))

meatNames={"chicken":"chicken","cow":"beef","pig":"pork"}
def meatMixer(meat1,meat2):
    tempMeat=meatNames[meat2]
    meatNames[meat2]=meatNames[meat1]
    meatNames[meat1]=tempMeat
    return  meatNames
#print(meatMixer("chicken","cow"))
cities=["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver","New Orleans"]
def listPrinter(l):
    try:
        l.reverse()
    except:
        print("Please enter a valid data type.")
        return
    for i in l:
        print(i)


#listPrinter(cities)
def listSorter(l):
    try: l.reverse()
    except:
        print("Please enter a valid data type.")
        return
    tempLen=len(l)

    for i in range(tempLen):
        lastVal = False
        try: temp=l[i+1]
        except: lastVal=True
        if not lastVal:
            if len(l[i])<len(l[i+1]):
                l.append(l[i])
                l.pop(i)
    return l
print(listSorter(cities))


