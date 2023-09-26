import sys

# ---------------------------------------------------
class Expense():
    date = "YYYY-MM-DD"
    name = None
    amount = 0

    def __init__(self,date,name,amount):
        self.date=date
        self.name=name
        self.amount=amount
# ---------------------------------------------------

#----------------------------------------------------
class ExpenseManager():
    expenses = []

    def add_expense(self, expense_date, expense_name, expense_amount):
        expense = Expense(expense_date,expense_name,expense_amount)
        self.expenses.append(expense)

    def get_matching_expenses(self, expense_name_partial):
        matching_expenses = []
        for e in self.expenses:
            if expense_name_partial in e.name:
                matching_expenses.append(e)
        return matching_expenses

    def remove_expense(self, expense):
        self.expenses.remove(expense)

    def load_data(self, file_name):
        try:
            file_object = open(file_name, "r")
            i = 0
            line = file_object.readline()
            while (line != ""):
                fields = line.split(",")
                expense_date = fields[0]
                expense_name = fields[1]
                expense_amount = float(fields[2])
                self.add_expense(expense_date, expense_name, expense_amount)
                line = file_object.readline()
                i += 1
            file_object.close()
            return i
        except:
            pass

    def save_data(self, file_name):
        try:
            file_object = open(file_name, "w")
            num_expenses = len(self.expenses)
            i = 0
            while (i < num_expenses):
                file_object.write(
                    self.expenses[i].date + "," + self.expenses[i].name + "," + str(self.expenses[i].amount) + "\n")
                i += 1
            file_object.close()
            return i
        except:
            pass


# -------------------------------------------------------------

class ExpenseManagerUI():
    expense_manager = ExpenseManager()

    def run_expenses_manager(self):
        data_file_name = "expenses.csv"
        if (self.expense_manager.load_data(data_file_name) == None):
            sys.stdout.write("Could not load file " + data_file_name)
        choice = self.get_menu_choice()
        while (choice != "x"):
            sys.stdout.write("\n")
            if choice == "a":
                self.add_expense_via_menu()
            elif choice == "r":
                self.remove_expense_via_menu()
            elif choice == "f":
                self.find_expenses_via_menu()
            choice = self.get_menu_choice()
        if (self.expense_manager.load_data(data_file_name) == None):
            sys.stdout.write("Could not save file " + data_file_name)

    def get_menu_choice(self):
        menu = "\n====================\n"
        menu += "Expenses Manager v1.0\n"
        menu += "====================\n"
        menu += "[A]dd an expense\n"
        menu += "[R]emove an expense\n"
        menu += "[F]ind expenses\n"
        menu += "E[x]it\n"

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
        while (len(value) == 0):
            sys.stdout.write("Input cannot be blank. Re-enter: ")
            sys.stdout.flush()
            value = sys.stdin.readline().strip()

        return value

    def get_float(self, prompt):
        value = None
        while (value == None):
            try:
                value = float(self.get_str(prompt))
            except:
                self.prompt = "That wasn't right. Re-enter: "
            return value

    def get_positive_float(self, prompt):
        value = self.get_float(prompt)
        while (value < 0):
            value = self.get_float("Input must be positive. Re-enter: ")
        return value

    def add_expense_via_menu(self):
        sys.stdout.write("--------------\n")
        sys.stdout.write("Add an expense\n")
        sys.stdout.write("--------------\n")

        expense_date = self.get_str("Enter expense date as YYYY-MM-DD: ")
        sys.stdout.write("\n")
        expense_name = self.get_str("Enter expense name: ")
        sys.stdout.write("\n")
        expense_amount = self.get_positive_float("Enter expense amount: ")
        sys.stdout.write("\n")

        self.expense_manager.add_expense(expense_date, expense_name, expense_amount)

    def find_expenses_via_menu(self):
        sys.stdout.write("-------------\n")
        sys.stdout.write("Find expenses\n")
        sys.stdout.write("-------------\n")

        self.matching_expenses = self.search_and_display_matching_expenses()

    def remove_expense_via_menu(self):
        sys.stdout.write("-----------------\n")
        sys.stdout.write("Remove an expense\n")
        sys.stdout.write("-----------------\n")

        matching_expenses = self.search_and_display_matching_expenses()
        if (matching_expenses == None):
            return

        num_matching_expenses = len(matching_expenses)
        i = 0
        while (i < num_matching_expenses):
            self.expense_manager.remove_expense(matching_expenses[i])
            i += 1
        sys.stdout.write("Above matches were removed.\n")

    def search_and_display_matching_expenses(self):
        if (len(self.expense_manager.expenses) <= 0):
            sys.stdout.write("No expenses added. Trying adding expenses first....");
            return

        sys.stdout.write("Enter partial expense name to find: ")
        sys.stdout.flush()
        search_target = sys.stdin.readline().strip()

        matching_expenses = self.expense_manager.get_matching_expenses(search_target)
        num_matching_expenses = len(matching_expenses)
        if (num_matching_expenses <= 0):
            sys.stdout.write("There were not expenses that matched: " + search_target + "\n")
            return

        sys.stdout.write("\n")
        dates_width = 11
        names_width = 20
        amounts_width = 10
        column_format = "{:<" + str(dates_width) + "} {:<" + str(names_width) + "} {:>" + str(amounts_width) + "}\n"

        row_text = column_format.format("----", "----", "--------")
        sys.stdout.write(row_text)
        row_text = column_format.format("Date", "Name", "Amount $")
        sys.stdout.write(row_text)
        row_text = column_format.format("----", "----", "--------")
        sys.stdout.write(row_text)

        total_amount = 0
        i = 0
        while (i < num_matching_expenses):
            row_text = column_format.format(matching_expenses[i].date, matching_expenses[i].name,
                                            matching_expenses[i].amount)
            total_amount += matching_expenses[i].amount
            sys.stdout.write(row_text)
            i += 1

        sys.stdout.write("\nYou've spent $" + str(total_amount) + " on " + str(num_matching_expenses) + " matches.\n")

        return matching_expenses


home_expense_manager = ExpenseManagerUI()
home_expense_manager.run_expenses_manager()
