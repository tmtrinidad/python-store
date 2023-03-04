# ----------------------------------------------------------------------
# Name:      store
# Author(s): taylor trinidad
# ----------------------------------------------------------------------
"""
This program consists of 4 classes: Product, VideoGame, Book, and Bundle

All of these classes can be used to generate items relating to them with a
description, serial numbers, prices, and stock.
"""


class Product:

    """
    Represents product items
    Arguments:
    description (string): description of the product
    list_price (int)?: manufacturer suggested retail price

    Attributes:
    sales (list): list of actual sales prices
    reviews (tuple): list of user reviews
    id (string): automatically assigned ID which is the category + serial
    number
    """

    category = "GN"
    next_serial_number = 1

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.sales = []
        self.reviews = []
        self.id = self.generate_product_id()
        self.stock = 0

    def __str__(self):
        return f'{self.description}\nProduct ID: ' \
               f'{self.id}\nList Price: ' \
               f'${float(self.list_price):.2f}\nAvailable in stock:' \
               f' {self.stock}'

    def __add__(self, other):
        return Bundle(self, other)

    def restock(self, quantity):
        """
        adds a specified number of items to the stock
        :param quantity: int
        :return: None
        """
        self.stock += quantity


    def review(self, stars, text):
        """
        appends a review into the reviews attribute
        :param stars: int
        :param text: string
        :return: None
        """
        the_review = (text, stars)
        self.reviews.append(the_review)

    def sell(self, quantity, sale_price):
        """
        sells a specified number of items for the stated price
        :param quantity: int
        :param sale_price: float
        :return:
        """
        if quantity <= self.stock:
            for x in range(quantity):
                self.sales += [sale_price]
            self.stock -= quantity
        else:
            for x in range(self.stock):
                self.sales += [sale_price]
            self.stock = 0

    @classmethod
    def generate_product_id(cls):
        """
        creates a formatted product ID string
        :param cls:
        :return:
        """
        id_number = cls.next_serial_number
        cls.next_serial_number += 1
        return f'{cls.category}{id_number:06}'

    @property
    def lowest_price(self):
        """
        calculates the lowest price an item has been sold
        :return: float
        """
        return min(self.sales, default=None)

    @property
    def average_rating(self):
        """
        calculates the average rating of items from the reviews
        :return:
        """
        if len(self.reviews) == 0:
            return "None"
        else:
            total_stars = 0
            for rev in self.reviews:
                total_stars += int(rev[1])
            return total_stars / len(self.reviews)


class VideoGame(Product):

    """
    Represents a Video Game Product
    Inherits from: Product
    """

    category = "VG"
    next_serial_number = 1

    def __init__(self, description, list_price):
        super().__init__(description, list_price)


class Book(Product):

    """
    Represents a Book Product
    Inherits from: Product

    Arguments:
    description (string): description of the book
    author (string): author of the book
    pages (int): number of pages
    list_price (float): cost of the book
    """

    category = "BK"
    next_serial_number = 1

    def __init__(self, description, author, pages, list_price):
        self.pages = pages
        self.author = author
        super().__init__(description, list_price)

    def __lt__(self, other):
        return self.pages < other.pages


class Bundle(Product):

    """
    Represents a Video Game Product
    Inherits from: Product

    Arguments:
    args (Product): product objects to add to a bundle

    Attributes:
    bundle_description (string): items in the bundle
    bundle_price (float): price of the bundle that will be discounted
    """

    category = "BL"
    next_serial_number = 1
    bundle_discount = 20

    def __init__(self, *args):
        self.bundle_description = ''
        self.bundle_price = 0

        count = 0
        for x in args:
            self.bundle_price += x.list_price
            if count < len(args) - 1:
                self.bundle_description += x.description + " & "
            else:
                self.bundle_description += x.description
            count += 1
        self.total_price = self.bundle_price * (1 - self.bundle_discount/100)
        super().__init__(self.bundle_description, self.total_price)

    def __str__(self):
        return f'{self.bundle_description}\n' \
               f'Product ID: {self.id}\n' \
               f'List Price: ${float(self.total_price):.2f}\n' \
               f'Available in Stock: {self.stock}'


def main():
    
    print("Testing Step 1")
    sunglasses = Product('Vans Hip Cat Sunglasses', 14)
    print(Product.category)
    print(Product.next_serial_number)
    print(sunglasses.id)
    print(sunglasses.description)
    print(sunglasses.list_price)
    print(sunglasses.stock)
    print(sunglasses.reviews)
    print(sunglasses.sales)
    headphones = Product('Apple Airpods Pro', 199)
    sunglasses.restock(20)
    headphones.restock(5)
    print(sunglasses)
    print(headphones)
    sunglasses.sell(3, 14)
    sunglasses.sell(1, 10)
    print(sunglasses.sales)
    headphones.sell(8, 170)  # There are only 5 available
    print(headphones.sales)
    print(sunglasses)
    print(headphones)
    sunglasses.restock(10)
    print(sunglasses)
    headphones.restock(20)
    print(headphones)
    sunglasses.review(5, 'Great sunglasses! Love them.')
    sunglasses.review(3, 'Glasses look good but they scratch easily')
    headphones.review(4, 'Good but expensive')
    print(sunglasses.reviews)
    print(headphones.reviews)
    print(Product.category)
    print(Product.next_serial_number)

    print("\nTesting Step 2:")
    print(sunglasses.lowest_price)
    print(sunglasses.average_rating)
    backpack = Product('Nike Explore', 60)
    print(backpack.average_rating)
    print(backpack.lowest_price)

    print("\nTesting Step 3:")
    mario = VideoGame('Mario Tennis Aces', 50)
    mario.restock(10)
    mario.sell(3, 40)
    mario.sell(4, 35)
    print(mario)
    print(mario.lowest_price)
    mario.review(5, 'Fun Game!')
    mario.review(3, 'Too easy')
    mario.review(1, 'Boring')
    print(mario.average_rating)
    lego = VideoGame('LEGO The Incredibles', 30)
    print(lego)
    lego.restock(5)
    lego.sell(10, 20)
    print(lego)
    print(lego.lowest_price)
    print(VideoGame.category)
    print(VideoGame.next_serial_number)

    print("\nTesting Step 4:")
    book1 = Book('The Quick Python Book', 'Naomi Ceder', 472, 39.99)
    print(book1.author)
    print(book1.pages)
    book1.restock(10)
    book1.sell(3, 30)
    book1.sell(1, 32)
    book1.review(5, 'Excellent how to guide')
    print(book1)
    print(book1.average_rating)
    print(book1.lowest_price)
    book2 = Book('Learning Python', 'Mark Lutz', 1648, 74.99 )
    book1.restock(20)
    book1.sell(2, 50)
    print(book2)
    print(book1 > book2)
    print(book1 < book2)
    print(Book.category)
    print(Book.next_serial_number)

    print("\nTesting Step 5:")
    bundle1 = Bundle(sunglasses, backpack, mario)
    print(bundle1)
    print()
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    print()
    bundle1.sell(2, 95)
    print(bundle1)
    print()
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    print()
    bundle1.sell(3, 95)
    print(bundle1)
    print()
    print(bundle1.lowest_price)
    print()
    bundle2 = Bundle(book1, book2)
    bundle2.restock(2)
    print(bundle2)
    print()
    print(Bundle.category)
    print()
    print(Bundle.next_serial_number)
    print()
    print(Bundle.bundle_discount)
    print()

    print("\n Testing Step 6:")
    print()
    back_to_school_bundle = backpack + book1
    print(back_to_school_bundle)


if __name__ == '__main__':
    main()