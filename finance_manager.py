import sys


class FinanceRecord():
    __date = "YYYY-MM-DD"
    __name = None
    __amount = 0

    def __init__(self, date, name, amount):
        self.__date = date
        self.__name = name
        self.__amount = amount


class Expense(FinanceRecord):
    __category = None


class Income(FinanceRecord):
    __source = None

    def __init__(self, date, name, amount, source):
        super().__init__(date, name, amount)
        self.__source = source


class FinanceManager():
    __finance_record = []
