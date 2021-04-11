#Chad Johnson 1323504: Final Project Part 1
import csv
from operator import itemgetter

# Gathering the list of csv files
ManufacturerList = []
PriceList = []
ServiceDatesList = []

# Adding the content of the svc files
with open("ManufacturerList.csv") as manlist:
    ml = csv.reader(manlist)
    for line in ml:
        ManufacturerList.append(line)

with open("PriceList.csv") as pricelist:
    pl = csv.reader(pricelist)
    for line in pl:
        PriceList.append(line)

with open("ServiceDatesList.csv") as sdlist:
    sl = csv.reader(sdlist)
    for line in sl:
        ServiceDatesList.append(line)

# Sorting the lists in order
new_ManufacturerList = (sorted(ManufacturerList, key=itemgetter(0)))
new_PriceList = (sorted(PriceList, key=itemgetter(0)))
new_ServiceDatesList = (sorted(ServiceDatesList, key=itemgetter(0)))

# adding to the missing prices and dates
for x in range(0, len(new_ManufacturerList)):
    new_ManufacturerList[x].append(PriceList[x][1])

for x in range(0, len(new_ManufacturerList)):
    new_ManufacturerList[x].append(ServiceDatesList[x][1])

final_list = new_ManufacturerList

full_inventory = (sorted(final_list, key=itemgetter(1)))

# Creating the inventory file with the lists.
with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)

    for x in range(0, len(full_inventory)):
        fiwrite.writerow(full_inventory[x])

# Creating the list for the different types
item_type = final_list
tower_list = []
laptop_list = []
phone_list = []

# Checking the lists for the item type and adding to their lists
for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower_list.append(item_type[x])
    elif item_type[x][2] == "phone":
        phone_list.append(item_type[x])
    elif item_type[x][2] == "laptop":
        laptop_list.append(item_type[x])

# Writing files for the item type
with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)

    for x in range(0, len(laptop_list)):
        liwrite.writerow(laptop_list[x])

with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)

    for x in range(0, len(phone_list)):
        piwrite.writerow(phone_list[x])

with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)

    for x in range(0, len(tower_list)):
        tiwrite.writerow(tower_list[x])

# Damage products lists
damagedlist = []

for x in range(0, len(item_type)):
    if item_type[x][3] == "damaged":
        damagedlist.append(item_type[x])

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

# Damage product file
with open('DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)

    for x in range(0, len(damagedlist)):
        diwrite.writerow(damagedlist[x])

# Manufacture input request
user_manuf = str(input("Enter your manufacturer: "))
user_type = str(input("Please enter your item type: "))

your_item = []

# Quit "Q" vs "q"
while (user_manuf != "q"):
    for x in range(0, len(final_list)):
        if user_manuf in final_list[x] and user_type in final_list[x]:
            your_item.append(final_list[x])

# Product does not exist
    if len(your_item) != 0:
        your_item = sorted(your_item, key=itemgetter(4), reverse=True)
        print("Your Item is: ", your_item[0])
    else:
        print("No such item in Inventory")

    user_manuf = str(input("Enter your manufacturer, or q to exit query:"))
    user_type = str(input("Please enter your item type: "))