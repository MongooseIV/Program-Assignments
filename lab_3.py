import random
foods={"chicken":1.59,"beef":1.99,"cheese":1.00,"milk":2.50} #provided dict
meatNames={"chicken":"chicken","cow":"beef","pig":"pork"} #my own dict
#access foods
chickenPrice=foods["chicken"]
beefPrice=foods["beef"]
cheesePrice=foods["cheese"]
milkPrice=foods["milk"]
print(f"Chicken: ${chickenPrice}, Beef: ${beefPrice}, Cheese: ${cheesePrice}, Milk: ${milkPrice}")
#accesss meatNames
for i in meatNames:
    print(f"{i}: {meatNames[i]}")
#update a dict
def discount(dcItem,dcAmount):
    foods[dcItem]-=dcAmount
    return foods[dcItem]
print(discount("chicken",0.50))
#new dict about shoes
bShoes={"Jordan 13":1,"Yeezy":8,"Foamposite":10,"Air Max":5,"SB Dunk":20}
print(f"Basketball shoe stocks: {bShoes}")
#a customer buys shoes:
bShoes["SB Dunk"]-=2
bShoes["Yeezy"]+=1
for j in bShoes:
    bShoes[j]+=7
for k in bShoes:
    bShoes[k]-=3
#add 3 new values
foods["apples"]=0.50
foods["ham"]=4.00
foods["flour"]=5.05
meatNames["sheep"]="mutton"
meatNames["deer"]="venison"
meatNames["lamb"]="lamb"
bShoes["Nike"]=13
bShoes["Adidas"]=3
bShoes["Underarmour"]=6
del(foods["cheese"])
del(foods["milk"])
del(meatNames["cow"])
del(meatNames["lamb"])
del (bShoes["Nike"])
del (bShoes["SB Dunk"])
print(meatNames,foods,bShoes)



