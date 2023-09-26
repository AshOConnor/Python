import sys
import datetime


# ------------------------------------------------------------------------------------------------------------------
class FinanceRecordError(Exception):
    pass


# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
class FinanceRecordDateError(FinanceRecordError):
    pass


# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
class FinanceRecordNameError(FinanceRecordError):
    pass


# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
class FinanceRecordAmountError(FinanceRecordError):
    pass


# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
class FinanceRecord():
    __date = None  # "YYYY-MM-DD"
    __name = None
    __amount = 0

    def __init__(self, date, name, amount):
        self.date = date
        self.name = name
        self.amount = amount

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        try:
            self.__date = datetime.datetime.strptime(value, "%Y-%m-%d")
        except:
            raise FinanceRecordDateError(value + " must be in the format YYYY-MM-DD")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:
            raise FinanceRecordNameError("Value cannot be None")
        elif not isinstance(value, str):
            raise FinanceRecordNameError("Value cannot be str")
        elif len(value.strip()) <= 0:
            raise FinanceRecordNameError("Value be an empty str")
        self.__name = value.strip()

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value is None:
            raise FinanceRecordAmountError("Value cannot be None")
        elif type(value) != int and type(value) != float:
            raise FinanceRecordAmountError("Value must be an int or a float")
        self.__amount = value


# ------------------------------------------------------------------------------------------------------------------
class Expense(FinanceRecord):
    def __init__(self, date, name, amount):
        if amount > 0:
            amount = -amount
        super().__init__(date, name, amount)


# ------------------------------------------------------------------------------------------------------------------
class Income(FinanceRecord):
    __source = None

    def __init__(self, date, name, amount, source):
        super().__init__(date, name, amount)
        self.source = source

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        self.__source = value.strip()


# ------------------------------------------------------------------------------------------------------------------
class FinanceManager():
    finance_records = []

    def add_record(self, record_date, record_name, record_amount, record_source=""):  #
        record = None
        if record_amount < 0:  #
            record = Expense(record_date, record_name, record_amount)
        else:
            record = Income(record_date, record_name, record_amount, record_source)
        self.finance_records.append(record)

    def get_matching_records(self, record_name_partial):
        record_name_partial = record_name_partial.lower()
        for r in self.finance_records:
            if record_name_partial in r.name.lower():
                yield r  #

    def remove_record(self, record):
        self.finance_records.remove(record)

    def load_data(self, file_name):
        file_object = open(file_name, "r")
        i = 0
        line = file_object.readline()
        while line != "":
            fields = line.split(",")
            record_date = fields[0]
            record_name = fields[1]
            record_amount = float(fields[2])
            if len(fields) <= 3:
                self.add_record(record_date, record_name, record_amount)
            else:  #
                record_source = fields[3]
                self.add_record(record_date, record_name, record_amount, record_source)
            line = file_object.readline()
            i += 1
        file_object.close()
        return i

    def save_data(self, file_name):
        file_object = open(file_name, "w")
        num_records = len(self.finance_records)
        i = 0
        while i < num_records:
            rdate = self.finance_records[i].date
            formatted_date = '{:04d}-{:02d}-{:02d}'.format(rdate.year, rdate.month, rdate.day)
            line = formatted_date + "," + self.finance_records[i].name + "," + str(self.finance_records[i].amount)
            if isinstance(self.finance_records[i], Income):  #
                line += "," + self.finance_records[i].source
            file_object.write(line + "\n")
            i += 1
        file_object.close()
        return i


# ------------------------------------------------------------------------------------------------------------------
class FinanceManagerUI():
    finance_manager = FinanceManager()

    def run_finance_manager(self):
        data_file_name = "finance_records.csv"

        try:  #
            self.finance_manager.load_data(data_file_name)
        except Exception as e:
            self.output_error(str(e) + ". Could not load from file " + data_file_name)

        choice = self.get_menu_choice()
        while choice != "e":
            sys.stdout.write("\n")
            if choice == "a":
                self.add_record_via_menu()
            elif choice == "r":
                self.remove_records_via_menu()
            elif choice == "f":
                self.find_records_via_menu()
            choice = self.get_menu_choice()

        try:
            self.finance_manager.save_data(data_file_name)
        except Exception as e:
            self.output_error(str(e) + ". Could not save to file " + data_file_name)

    def get_menu_choice(self):
        menu = "\n====================\n"
        menu += "Finance Manager v2.0\n"
        menu += "====================\n"
        menu += "[A]dd a record\n"
        menu += "[R]emove a record\n"
        menu += "[F]ind records\n"
        menu += "[E]xit\n"

        sys.stdout.write(menu)

        menu = menu.lower()
        choice = self.get_str("Enter choice: ").lower()
        while not "[" + choice + "]" in menu:
            choice = self.get_str(choice + " was an invalid choice! Re-enter: ").lower()

        return choice

    def get_str(self, prompt):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        value = sys.stdin.readline().strip()
        while len(value) == 0:
            sys.stdout.write("input cannot be blank. Re-enter: ")
            sys.stdout.flush()
            value = sys.stdin.readline().strip()

        return value

    def get_float(self, prompt):
        value = None
        while value == None:
            try:
                value = float(self.get_str(prompt))
            except:
                prompt = "That wasn't right. Re-enter: "
            return value

    def get_positive_float(self, prompt):
        value = self.get_float(prompt)
        while value < 0:
            value = self.get_float("Input must be positive. Re-enter: ")
        return value

    def output_error(self, message):
        sys.stderr.write("Problem! " + message + "\n")

    def add_record_via_menu(self):
        sys.stdout.write("------------\n")
        sys.stdout.write("Add a record\n")
        sys.stdout.write("------------\n")

        record_date = self.get_str("Enter record date (YYYY-MM-DD): ")
        sys.stdout.write("\n")
        record_name = self.get_str("Enter record name: ")
        sys.stdout.write("\n")
        record_amount = self.get_float("Enter amount (negative: expense | positive: income): ")
        sys.stdout.write("\n:")

        if record_amount < 0:
            self.finance_manager.add_record(record_date, record_name, record_amount)
        else:
            record_source = self.get_str("Enter income source: ")
            sys.stdout.write("\n")

            try:
                self.finance_manager.add_record(record_date, record_name, record_amount, record_source)
            except Exception as e:
                self.output_error(str(e))

    def find_records_via_menu(self):
        sys.stdout.write("------------\n")
        sys.stdout.write("Find records\n")
        sys.stdout.write("------------\n")
        sys.stdout.write("Enter partial record name to find: ")  #
        search_target = sys.stdin.readline().strip()

        self.search_and_display_matching_records(search_target)

    def remove_records_via_menu(self):
        sys.stdout.write("---------------\n")
        sys.stdout.write("Remove a record\n")
        sys.stdout.write("---------------\n")

        sys.stdout.write("Enter partial record name to find: ")  #
        sys.stdout.flush()
        search_target = sys.stdin.readline().strip()
        self.search_and_display_matching_records(search_target)
        for r in self.finance_manager.get_matching_records(search_target):
            self.finance_manager.remove_record(r)
        sys.stdout.write("Above matches were removed.\n")

    def search_and_display_matching_records(self, search_target):
        sys.stdout.write("\n")
        dates_width = 11
        names_width = 20
        amounts_width = 10
        source_width = 20
        column_format = "{:<" + str(dates_width) + "} {:<" + str(names_width) + "} {:>" + str(
            amounts_width) + "} {:>" + str(source_width) + "}\n"

        row_text = column_format.format("----", "----", "--------", "------")
        sys.stdout.write(row_text)
        row_text = column_format.format("Date", "Name", "Amount $", "Source")
        sys.stdout.write(row_text)
        row_text = column_format.format("----", "----", "--------", "------")
        sys.stdout.write(row_text)

        total_amount = 0
        num_matching_records = 0
        for r in self.finance_manager.get_matching_records(search_target):  #
            formatted_date = '{:04d}-{:02d}-{:02d}'.format(r.date.year, r.date.month, r.date.day)
            if isinstance(r, Income) and r.source != None:
                row_text = column_format.format(formatted_date, r.name, r.amount, r.source)
            else:
                row_text = column_format.format(formatted_date, r.name, r.amount, "")
            total_amount += r.amount
            num_matching_records += 1
            sys.stdout.write(row_text)

        sys.stdout.write("\nNet position is $" + str(total_amount) + " for " + str(num_matching_records) +
                         " matches.\n")


home_finance_manager = FinanceManagerUI()
home_finance_manager.run_finance_manager()
