#!/usr/bin/env python
# coding: utf-8

# In[20]:


def waterRatioCalculation(ratio,waterAllotment):
    ratioSplit = ratio.split(":")
    corporation_Water_Ratio = int(ratioSplit[0])
    borewell_Water_Ratio = int(ratioSplit[1])
    x = waterAllotment // (corporation_Water_Ratio + borewell_Water_Ratio) 
    corporationWater = x * corporation_Water_Ratio
    borewellWater = x * borewell_Water_Ratio
    return corporationWater, borewellWater

def priceCalculationForGuest(guest_Water_Requirement):
    price = 0
    for i in range(1,1000):
        if i==1:
            if guest_Water_Requirement < 500:
                price = guest_Water_Requirement * 2
                return price
            else:
                price += 500*2
                guest_Water_Requirement = guest_Water_Requirement - 500
                
        elif i == 2:
            if guest_Water_Requirement < 1000:
                price += guest_Water_Requirement * 3
                return price
            else:
                price += 1000*3
                guest_Water_Requirement = guest_Water_Requirement -1000
        
        elif i == 3:
            if guest_Water_Requirement < 1500:
                price += guest_Water_Requirement * 5
                return price
            price += 1500*5
            guest_Water_Requirement = guest_Water_Requirement - 1500
            
        else:
            price += guest_Water_Requirement * 8
            return price
            
    

def calculation(apartment_type,ratio,numberOfguest):
    if apartment_type ==2:                 #total water required for people of flat 
        waterAllotment = 3 * 10 * 30
    else:
        waterAllotment = 5 * 10 * 30
    corporationWater, borewellWater = waterRatioCalculation(ratio,waterAllotment)
    guest_Water_Requirement = numberOfguest * 10 * 30  # total water required for guest
    Total_Water_Requirement = waterAllotment + guest_Water_Requirement #total water required for people + guest
    price_Of_Water_For_People_Of_Flat = ((corporationWater * 1) + (borewellWater * 1.5)) # price of water of flatmates
    price_Of_Water_For_Guest = priceCalculationForGuest(guest_Water_Requirement)# price of water of guest
    Total_Price_Of_Water = price_Of_Water_For_People_Of_Flat + price_Of_Water_For_Guest #  total price of water of flatmates + guest
    
    print("{0} {1}".format(Total_Water_Requirement,int(Total_Price_Of_Water)))

numberOfguest = 0
while(1):
    input1 = input()
    splitInput = input1.split()
    if splitInput[0] == "ALLOT_WATER":
        apartment_type = splitInput[1]
        ratio = splitInput[2]
    if splitInput[0] == "ADD_GUESTS":
        numberOfguest += int(splitInput[1])
    if splitInput[0] == "BILL":
        calculation(int(apartment_type),ratio,int(numberOfguest))
        break


# In[ ]:




