class Order:
    def __init__(self, quantity=None, has_salchicha=None, has_chorizo=None, has_salami=None, has_longaniza=None,
                 has_costilla=None):
        self.__quantity = quantity
        self.__has_salchicha = has_salchicha
        self.__has_chorizo = has_chorizo
        self.__has_salami = has_salami
        self.__has_longaniza = has_longaniza
        self.__has_costilla = has_costilla

    def calculate_time(self):
        return_value: float = 0
        if self.__has_salchicha == 1:
            return_value += 2
        if self.__has_chorizo == 1:
            return_value += 3
        if self.__has_salami == 1:
            return_value += 1.5
        if self.__has_longaniza == 1:
            return_value += 4
        if self.__has_costilla == 1:
            return_value += 6
        return return_value
