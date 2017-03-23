# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:50:39 2017

@author: steierjo
"""

import uuid

########################
###   USER CLASSES   ###
########################
class User(object):
    def __init__(self):
        username = ""
        password = ""

    # Setters
    def setUsername(self, newName):
        self.username = newName

    def setPassword(self, newPass):
        self.password = newPass

    # Getters
    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password


class Customer(User):
    def __init__(self):
        self.username = ''
        self.password = ''
        self.balance = 0
        self.address = ''
        self.email = ''
        self.cart = []

    # Setters
    def addBalance(self, amount):
        self.balance += amount

    def subBalance(self, amount):
        self.balance -= amount

    def setAddress(self, newAddress):
        self.address = newAddress

    def setEmail(self, newEmail):
        self.email = newEmail

    def addCart(self, prod):
        self.cart.append(prod)

    def voidCart(self):
        self.cart = []

    # Getters
    def getBalance(self):
        return self.balance

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def getCart(self):
        return self.cart

class Admin(User):
    def __init__(self):
        self.username = "admin"
        self.password = "admin"

####################################################################################
###########################
###   PRODUCT CLASSES   ###
###########################

class Product(object):
    def __init__(self):
        self.name = ""
        self.description = []
        self.price = 0.00
        self.quantity = 0
        self.category = ""
        self.delivery = ""
        self.reviews = []
        self.promotion = ""

    def __str__(self):
        string = str(str(self.name)
                     + " \n  " + str(self.getPrice())
                     + "\n  " + str(self.description)
                     + "\n  " + str(self.getQuantity())
                     + "\n  " + str(self.getReview())
                     )
        return string

    # Setters && Getters
    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setDescription(self, newDes):
        self.description = newDes

    def getDescription(self):
        return self.description

    def setPrice(self, newPrice):
        self.price = newPrice

    def getPrice(self):
        return '$' + str(self.price)

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

    def remOne(self):
        self.quantity -= 1

    def getQuantity(self):
        if self.quantity == 0:
            return "There is no more"
        else:
            return "In stock: " + str(self.quantity)

    def setReview(self, newReview):
        self.reviews.append(newReview)

    def getReview(self):
        return self.reviews

    def setCategory(self, newCat):
        self.category = newCat

    def getCategory(self):
        return self.category

    def setDelivery(self, newDelivery):
        self.delivery = newDelivery

    def getDelivery(self):
        return self.delivery

    def setPromotion(self, newPromotion):
        self.promotion = newPromotion

    def getPromotion(self):
        return self.promotion

class DigitalProduct(Product):
    def __init__(self):
        cd = self.genCode()
        self.name = ""
        self.description = []
        self.price = 0.00
        self.quantity = 0
        self.category = ""
        self.delivery = ""
        self.reviews = []
        self.code = cd
        # self.promotion = promotion

    # Setter and Getter for code
    def genCode(self):
        cd = uuid.uuid4()
        return cd

    def getCode(self):
        return self.code

class PhysicalProduct(Product):
    def __init__(self):
        self.name = ""
        self.description = []
        self.price = 0.00
        self.quantity = 0
        self.category = ""
        self.delivery = ""
        self.reviews = []
        self.promotion = ""

class SubProduct(Product):
    def __init__(self):
        self.name = ""
        self.description = []
        self.price = 0.00
        self.quantity = 0
        self.category = ""
        self.delivery = ""
        self.reviews = []
        self.promotion = ""

###############################################################################
###############################################################################
###############################################################################
dude = Customer()
dude.setUsername("jon")
dude.setPassword("hi")


users = {"admin": Admin(), "jon": dude}
products = {"Hats":[], "Shoes":[], "Toys":[]}
currentUser = None


class Store():
    #Log in Menu
    def __init__(self):
        self.users = users
        self.products = products
        self.currentUser = currentUser

        new = input("New user? (y/n)")
        if new == "y":
            self.newUser()
        elif new != "n":
            print("Answer should be y/n")
            self.__init__()

        nm = input("Enter username: ")
        pw = input("Enter password: ")

        if self.users.__contains__(nm):
            if nm == "admin":
                if self.users.__getitem__(nm).getPassword() == pw:
                    print("you got to the admin page")
                    self.adminInterface()
            elif self.users.__getitem__(nm).getPassword() == pw:
                self.currentUser = self.users.__getitem__(nm)
                print("Welcome!")
                self.customerInterface()
            else:
                print("User does not exist.")

    def adminInterface(self):
        print("""
                            1. Add Category
                            2. Remove Category
                            3. Add Product
                            4. Remove Product
                            5. Set Price of Product
                            6. Restock Product
                            7. Log Out
                            """)
        ans = input("Choice: ")
        if ans == "1":
            self.addCategory()
        elif ans == "2":
            self.removeCategory()
        elif ans == "3":
            self.addProduct()
        elif ans == "4":
            self.removeProduct()
        elif ans == "5":
            self.setPOP()
        elif ans == "6":
            self.restockProduct()
        elif ans == "7":
            self.logOut()
        else:
            print("\n Invalid Choice, Try Again")

    ####### Admin Methods ##########
    def addCategory(self):
        nm = input("Name of category: ")
        self.products[nm] = []
        print("Category added.")
        print(self.products)
        self.adminInterface()
    def removeCategory(self):
        nm = input("Name of category: ")
        if self.products.__contains__(nm):
            del self.products[nm]
            print("Category removed.")
            print(self.products)
        else:
            print("Category does not exist.")
            self.adminInterface()
        self.adminInterface()
    def addProduct(self):
        cat = input("Category the product is in: ")
        if cat in self.products:
            nm = input("Name of product: ")
            tpe = input("Type of product (physical, digital, or subscription): ")
            if tpe == "physical":
                prod = PhysicalProduct()
                prod.setCategory(cat)
                prod.setName(nm)

                self.products[cat].append(prod)
            elif tpe == "digital":
                prod = DigitalProduct()
                prod.setCategory(cat)
                prod.setName(nm)

                self.products[cat].append(prod)
            elif tpe == "subscription":
                prod = SubProduct()
                prod.setCategory(cat)
                prod.setName(nm)

                self.products[cat].append(prod)
            print(self.products.get(cat))
        else:
            print("Category does not exist.")
            self.adminInterface()
        self.adminInterface()
    def removeProduct(self):
        cat = input("Category the product is in: ")
        if cat in self.products:
            nm = input("Name of product: ")
            for x in self.products[cat]:
                if nm == x.getName():
                    self.products[cat].remove(x)
                    print("Product removed.")
            print(self.products.get(cat))
        else:
            print("Category does not exist.")
            self.adminInterface()
        self.adminInterface()
    def setPOP(self):
        cat = input("Category the product is in: ")
        if cat in self.products:
            nm = input("Name of product: ")
            for x in self.products[cat]:
                if nm == x.getName():
                    newPrice = float(input("Price of the product you are changing: "))
                    x.setPrice(newPrice)
                    print("Price set.")
                    print(x.getPrice())
                    self.adminInterface()
                else:
                    print("Product does not exist.")
                    self.adminInterface()
        else:
            print("Category does not exist.")
            self.adminInterface()
        self.adminInterface()
    def restockProduct(self):
        cat = input("Category the product is in: ")
        if cat in self.products:
            nm = input("Name of product: ")
            for x in self.products[cat]:
                if nm == x.getName():
                    newStock = int(input("Quantity of the product you are changing: "))
                    x.setQuantity(newStock)
                    print("Quantity set.")
                    print(x.getQuantity())
                    self.adminInterface()
                else:
                    print("Product does not exist.")
                    self.adminInterface()
        else:
            print("Category does not exist.")
            self.adminInterface()
        self.adminInterface()

    #Customer Interface
    def customerInterface(self):
        print("""
                    1. Add Funds
                    2. Categories
                    3. Check Out
                    4. Log Out
                    """)
        ans = input("Choice: ")
        if ans == "1":
            self.addBalance()
        elif ans == "2":
         self.categoryInterface()
        elif ans == "3":
         self.checkOut()
        elif ans == "4":
            self.logOut()
        else:
            print("\n Invalid Choice, Try Again")
            self.customerInterface()


####### Customer Methods ##########

    def newUser(self):
        # get login info
        nm = input("Enter login name: ")
        if nm in users:
            print("Login name already exists.")
            self.newUser()
        pw = input("Enter login password: ")

        # creating a new Customer
        user = Customer()
        user.setUsername(nm)
        user.setPassword(pw)

        # adding customer to users dict
        self.users[nm] = user
        print("User added.")

    def addBalance(self):
        print(self.currentUser.getBalance())

        amount = int(input("Amount you would like to add: "))
        if amount < 0:
            print("Cannot add negative funds.")
        else:
            self.currentUser.addBalance(amount)
        print("Funds added to account.")
        print(self.currentUser.getBalance())
        self.customerInterface()

    def logOut(self):
        self.currentUser = None
        self.__init__()

    def checkOut(self):
        print("this is check out")
        """print(self.currentUser.getBalance())
        if self.currentUser.getBalance() <= 0:
            return print("Insufficient Funds.")
        elif len(self.currentUser.getCart()) <= 0:
            return print("Cannot check out without any products in cart.")
        elif len(self.currentUser.getCart()) > 0:
            totalPrice = 0
            currentCart = self.currentUser.getCart()
            for prod in currentCart:
                totalPrice += currentCart[prod].getPrice()
                curr = self.products[prod.getCategory()]
                curr[prod].remOne()

                self.currentUser.subBalance(totalPrice)
                self.currentUser.voidCart()
                print(self.products)"""

    def categoryInterface(self):
        print("\n1. Check Out\n2. Log Out")

        i = 3
        for x in self.products:
            print(str(i) + ". " + x)
            i = i+1
        ans = int(input("Choice: "))

        if ans == "1":
            self.checkOut()
        elif ans == "2":
            self.logOut()

        j = 0
        for x in self.products:
            if j == (ans - 2):
                print(x)


        """while j <= i:
            if ans == j:
                print(self.products[i])
                #productInterface(self.products[i])
                j = j+1
        else:
            print("\n Invalid Choice.")
            self.customerInterface()"""


Store()