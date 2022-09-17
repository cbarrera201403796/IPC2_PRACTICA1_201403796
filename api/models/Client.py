
class Client:

    def __init__(self, name=None, phone=None, orders=None):
        self.__name = name
        self.__phone = phone
        self.__orders = orders

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @phone.deleter
    def phone(self):
        self.__phone = None

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, value):
        self.__orders = value

    @orders.deleter
    def orders(self):
        self.__orders = None
