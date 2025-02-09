from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        # You'll remove this when you fill out your constructor
        self.inventory = []

    # What methods will you need?
    def make_banner(self):
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

    def print_inventory(self):
        print(self.inventory)

    def buy(self,computer):
        self.inventory.append(computer.computer_info())
        return self.inventory.index(computer.computer_info())

    def sell(self,item_id):
        self.inventory.remove(item_id)

    def raise_price(self,inventory,item_id,computer):
        if inventory[item_id] is not None:
            inventory[item_id]["price"] = computer.raise_price()
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def update_price(item_id: int,inventory):
        if inventory[item_id] is not None:
            computer = inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    def refurbish(self,computer,inventory,item_id):
        if inventory[item_id] is not None:
            i = inventory[item_id]
            i["operating_system"] = computer.refurbish()

def main():
    C1 = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    C1.computer_info()
    C2 = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    C2.computer_info()
    S1 = ResaleShop()
    S1.buy(C1)
    S1.buy(C2)
    print(S1.buy(C1).item_id)
    S1.print_inventory()

main()