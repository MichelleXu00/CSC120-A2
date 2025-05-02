class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,description,processor_type,hard_drive_capacity,memory,operating_system,year_made,price):
        # constructor
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def computer_info(self) -> dict:
        """returns a dictionary of a computer's info
        """
        return {'description': self.description,
            'processor_type': self.processor_type,
            'hard_drive_capacity': self.hard_drive_capacity,
            'memory': self.memory,
            'operating_system': self.operating_system,
            'year_made': self.year_made,
            'price': self.price}

    def updateOS(self, new_OS: str) -> str:
        """updates the operating system of a computer
        :param new_OS: (str): the new operating system that will be updated to
        :return: the updated operating system
        """
        self.operating_system = new_OS
        return self.operating_system

    def raise_price(self, new_price: int) -> int:
        """raise the price of a computer to any price
        :param new_price: (int): the price that will be updated to
        :return: the raised price
        """
        self.price = new_price
        return self.price

    def updatePrice(self, computer):
        """raise the price of a computer to any price
        """
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff
