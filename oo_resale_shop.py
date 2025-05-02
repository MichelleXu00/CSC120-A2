from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        # constructor
        self.inventory = []

    # What methods will you need?
    def make_banner(self):
        """makes a banner for the resale shop
        """
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)

    def print_inventory(self):
        """prints the list of computers in the inventory
        """
        print("Checking inventory...")
        print(self.inventory)
        print("Done.\n")

    def buy(self, computer):
        """adds a computer to the inventory, default adds to the last
        :param computer: (computer): a computer object
        """
        print("Buying")
        print("Adding to inventory...")
        self.inventory.append(computer.computer_info())
        print("Done.\n")

    def sell(self, item_id: int, computer):
        """removes a specific computer from the inventory
        :param item_id: (int): the order of the computer in the inventory
        :param computer: (computer): a computer object
        """
        print("Selling Computer ID:", item_id)
        if computer in self.inventory:
            self.inventory.remove(item_id)
        else: 
            print("Computer", item_id, "is not in the inventory.")

    def raise_price(self, item_id: int, computer, new_price: int):
        """raise the price of a computer in the inventory to any price
        :param items_id: (int): the order of the computer in the inventory
        :param computer: (computer): a computer object
        :param new_price: (int): the price that will be updated to
        """
        if computer in self.inventory:
            self.inventory[item_id]["price"] = computer.raise_price(new_price)
        else:
            print("Computer", item_id, "is not found. Cannot update price.")

    def update_price(self, item_id: int, computer):
        """updates the price of a computer in the inventory based on its age
        :param items_id: (int): the order of the computer in the inventory
        :param computer: (computer): a computer object
        """
        if computer in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff
        else:
            print("Computer", item_id, "is not found. Please select another computer to refurbish.")

    def refurbish(self, item_id: int, computer, new_OS: str):
        """updates the operating system of a computer in the inventory
        :param items_id: (int): the order of the computer in the inventory
        :param computer: (computer): a computer object
        :param new_OS: (str): the new operating system that will be updated to
        """
        print("Refurbishing Computer ID:", item_id, ", updating OS to", new_OS)
        print("Updating inventory...")
        if computer in self.inventory:
            self.inventory[item_id]["operating_system"] = computer.updateOS(new_OS)
        else:
            print("Computer", item_id, "is not found. Please select another computer to refurbish.")
        print("Done.\n")

def main():
    C1 = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    C2 = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    C3 = Computer("blablabla","type","capacity","xxx","OS",2015,2000)
    S1 = ResaleShop()
    S1.buy(C1)
    S1.buy(C2)
    S1.print_inventory()
    S1.raise_price(1, C2, 1800)
    S1.print_inventory()
    S1.update_price(1, C2)
    S1.print_inventory()
    S1.refurbish(C1, 1, "ios 16")
    S1.print_inventory()
    S1.sell(3, C3)


main()