#Chad Johnson 1323504: Final Project
import csv
from datetime import datetime

# Creating output inventory files using the class method.
class OutputInventory:
    def __init__(self, item_list):
        self.item_list = item_list
    def damaged_inventory(self):
        dam_items = self.item_list
        dam_keys = sorted(dam_items.keys(), key=lambda x: dam_items[x]['price'], reverse=True)
        with open('DamagedInventory.csv', 'w') as new_file:
            dam_write = csv.writer(new_file)
            for x in range(0, len(dam_keys)):
                dam_write.writerow(dam_keys[x])
    def full_inventory(self):
        with open('FullInventory.csv', 'w') as new_file:
            full_items = self.item_list
            full_keys = sorted(full_items.keys(), key=lambda x: full_items[x]['manufacturer'])
            full_write = csv.writer(new_file)
            for x in range(0, len(full_keys)):
                full_write.writerow(full_keys[x])
            new_file.close()
    def past_service(self):
        past_items = self.item_list
        past_keys = sorted(past_items.keys(), key=lambda x: datetime.strptime(past_items[x]['service_date'], "%m/%d/%Y").date(),reverse=True)
        with open('PastServiceDateInventory.csv', 'w') as new_file:
            past_write = csv.writer(new_file)
            for x in range(0, len(past_keys)):
                past_write.writerow(past_keys[x])
    def type_inventory(self):
        inv_items = self.item_list
        inv_types = []
        inv_keys = sorted(inv_items.keys())
        for inv_item in inv_items:
            inv_type = inv_items[inv_item]['item_type']
            if inv_type not in inv_types:
                inv_types.append(inv_type)
        for inv_type in inv_types:
            file_name = inv_type.capitalize() + 'Inventory.csv'
            with open('' + file_name, 'w') as new_file:
                inv_write = csv.writer(new_file)
                for x in range(0, len(inv_keys)):
                    inv_write.writerow(inv_keys[x])



#Selecting the csv files to read and orginize the data from
items = {}
csv_files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
for document in csv_files:
    if document == csv_files[0]:
        with open(document, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for column in csv_reader:
                item_id = column[0]
                items[item_id] = {}
                man_label = column[1]
                it_type = column[2]
                item_damaged = column[3]
                items[item_id]['manufacturer'] = man_label.strip()
                items[item_id]['item_type'] = it_type.strip()
                items[item_id]['damaged'] = item_damaged
    elif document == csv_files[1]:
        with open(document, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for column in csv_reader:
                item_id = column[0]
                price = column[1]
                items[item_id]['price'] = price
    elif document == csv_files[2]:
        with open(document, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for column in csv_reader:
                item_id = column[0]
                service_date = column[1]
                items[item_id]['service_date'] = service_date

#Creating the output files to be added in the files directory
output_inventory = OutputInventory(items)
output_inventory.damaged_inventory()
output_inventory.full_inventory()
output_inventory.past_service()
output_inventory.type_inventory()


#Input the data you want to search the inventory
user_input = None
man_name = None
type_item = None
price_remainder = None
diff_types = []
mfl = []
while user_input != 'q':
    user_input = input("Please enter a manufacturer and type or enter 'q' to quit:")
    if user_input =='q':
        break
    else:
        user_input = user_input.split()
        for item in items:
            man_name = items[item]['manufacturer']
            type_item = items[item]['item_type']
            if man_name not in diff_types:
                mfl.append(man_name)
            if type_item not in diff_types:
                diff_types.append(type_item)
        for word in user_input:
            if word in mfl:
                man_name = word
            elif word in diff_types:
                type_item = word
        if not man_name or not type_item:
            print("No such item in inventory")
        else:
            keys = sorted(items.keys(), reverse=True)
            exact_match = []
            matched_item = {}
            for item in keys:
                if items[item]['item_type'] == type_item:
                    service_expiration = datetime.strptime(items[item]['service_date'], "%m/%d/%Y").date()
                    if items[item]['manufacturer'] == man_name:
                        if not service_expiration < datetime.now().date() and not items[item]['damaged']:
                            exact_match.append((item, items[item]))
                    else:
                        if not service_expiration < datetime.now().date() and not items[item]['damaged']:
                            matched_item[item] = items[item]
            if exact_match:
                item = exact_match[0]
                your_list = item[0], item[1]['manufacturer'], item[1]['item_type'], item[1]['price']
                print("\nYour item is: {}\n".format(your_list))
                if matched_item:
                    equal_charge = item[1]['price']
                    for item in matched_item:
                        eq_price = int(equal_charge) - int(matched_item[item]['price'])
                        if eq_price != price_remainder:
                            price_remainder = abs(eq_price)
                            item_id = item
                            your_match = item_id, matched_item[item]['manufacturer'], \
                                         matched_item[item]['item_type'], matched_item[item]['price']
                            print("You may also consider: {}\n".format(your_match))
                else:
                    print("No such item in the inventory")