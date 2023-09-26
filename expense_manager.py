import sys
expense_dates=[]
expense_names=[]
expense_amounts=[]

def run_expenses_manager():
    '''This function returns a program that is used to add data
        to a spreadsheet by using a csv file. It produces a menu
        with which the user can interact with. It takes into account
        what data the file already has and returns that information to the
        user when prompted. This program allows you to remove items,
        add items and find items on the spreadsheet by using the program.'''
    
    load_data()
    choice=get_menu_choice()
    while(choice!="x"):
        sys.stdout.write("\n")
        if choice=="a":
            add_expense_via_menu()
        elif choice=="r":
                remove_expense()
        elif choice=="f":
                find_expenses()
        choice=get_menu_choice()
    save_data()

def get_str(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    value=sys.stdin.readline().strip()
    while( len(value)==0 ):
        sys.stdout.write("Input cannot be blank. Re-enter: ")
        sys.stdout.flush()
        value=sys.stdin.readline().strip()

    return value

def get_float(prompt):
    value=None
    while( value==None ):
        try:
            value=float(get_str(prompt))
        except:
            prompt="That wasn't right. Re-enter: "
        return value

def get_positive_float(prompt):
    value=get_float(prompt)
    while(value<0):
        value=get_float("Input must be positive. Re-enter: ")
    return value

def get_menu_choice():
    '''get_menu_choice shows a menu to the user and in brackets
        shows the character that should be used when interacting.
        If the choice was invalid it will ask the user to re-enter
        their choice. There choice will take them to another section
        to input data'''
    
    menu="\n====================\n"
    menu+="Expenses Manager v1.0\n"
    menu+="\n====================\n"
    menu+="[A]dd an expense\n"
    menu+="[R]emove an expense\n"
    menu+="[F]ind expenses\n"
    menu+="E[x]it\n"

    sys.stdout.write(menu)

    menu=menu.lower()
    choice=get_str("Enter choice: ").lower()
    while not "["+choice+"]" in menu:
        choice=get_str(choice+" was an invalid choice! Re-enter: ").lower()

    return choice

def load_data():
    '''This function loads the data from the csv file and inputs it into
        the program depending on which lines of the file are chosen.'''
    
    with open("expenses.csv","r") as file_object:
        for line in file_object:
            fields=line.split(",")
            expense_date=fields[0]
            expense_name=fields[1]
            expense_amount=float( fields[2] )
            add_expense(expense_date,expense_name,expense_amount)

def add_expense(expense_date,expense_name,expense_amount):
    '''This function adds the expense name, date and amount to
        the csv file from inside the program.'''
    
    expense_dates.append(expense_date)
    expense_names.append(expense_name)
    expense_amounts.append(expense_amount)

def add_expense_via_menu():
    '''This function shows the add expense menu to the user. It asks
        for the date, expense name and how much is cost. This
        is then added to the csv file.'''
    
    sys.stdout.write("--------------\n")
    sys.stdout.write("Add an expense\n")
    sys.stdout.write("--------------\n")

    expense_date=get_str("Enter expense date as YYYY-MM-DD: ")
    sys.stdout.write("\n")
    expense_name=get_str("Enter expense name: ")
    sys.stdout.write("\n")
    expense_amount=get_positive_float("Enter expense amount: ")
    sys.stdout.write("\n")

    add_expense(expense_date,expense_name,expense_amount)

def remove_expense():
    '''This function shows the remove expense menu to the user.
        It asks the user which expense they would like to remove
        by asking the expense date follow by the expense name.
        This then removes it from the csv file.'''
    sys.stdout.write("--------------\n")
    sys.stdout.write("Remove an expense\n")
    sys.stdout.write("--------------\n")
    if ( len(expense_names)<=0 ):
        sys.stdout.write("No expenses to remove. Try adding expenses first...\n");
        return

    search_target_date=get_str("Enter expense date: ")
    search_target_name=get_str("Enter expense name: ")

    sys.stdout.write("Attempting to remove...\n")

    dates_width=11
    names_width=len(max(expense_names, key=len))+4
    amounts_width=10
    column_format="{:<"+str(dates_width)+"} {:<"+str(names_width)+"} {:>"+str(amounts_width)+"}\n"

    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)
    row_text=column_format.format("Date","Name","Amount $")
    sys.stdout.write(row_text)
    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)

    matches=0
    num_expenses=len(expense_names)
    i=0
    while(i< num_expenses):
        if (search_target_date==expense_dates[i] and search_target_name==expense_names[i]):
            row_text=column_format.format(expense_dates[i],expense_names[i],expense_amounts[i])
            sys.stdout.write(row_text)
            del(expense_dates[i])
            del(expense_names[i])
            del(expense_amounts[i])
            matches+=1
        i+=1
    sys.stdout.write("Removed "+str(matches)+" matches.\n")

def find_expenses():
    '''This function shows a menu to the user to finding an expense
        the user must enter a partial expense name and it will show
        a list of expenses starting with the partal name and how
        much the expense cost. This information is pulled from the csv file.'''
    sys.stdout.write("--------------\n")
    sys.stdout.write("Find expenses\n")
    sys.stdout.write("--------------\n")
    if ( len(expense_names)<=0 ):
        sys.stdout.write("No expenses to find. Trying adding expenses first...\n");
        return

    sys.stdout.write("Enter partial expense name to find: ")
    sys.stdout.flush()
    search_target=sys.stdin.readline().strip()
    sys.stdout.write("\n")

    dates_width=11
    names_width=len(max(expense_names, key=len))+4
    amounts_width=10

    column_format="{:<"+str(dates_width)+"} {:<"+str(names_width)+"} {:>"+str(amounts_width)+"}\n"

    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)
    row_text=column_format.format("Date","Name","Amount $")
    sys.stdout.write(row_text)
    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)

    matches=0
    total_amount=0
    num_expenses=len(expense_names)
    i=0
    while( i<num_expenses ):
        if ( search_target in expense_names[i] ):
            row_text=column_format.format(expense_dates[i],expense_names[i],expense_amounts[i])
            total_amount+=expense_amounts[i]
            matches+=1;
            sys.stdout.write(row_text)
        i+=1

    sys.stdout.write("\nYou've spent $"+str(total_amount)+" on "+str(matches)+" matches\n")

def save_data():
    '''This function saves the data to the csv file that the user
        has inputed or removed. It saves it in the correct columns
        in the csv file.'''
    try:
        file_object=open("dealership_stock.csv","w")
        num_expenses=len(expense_names)
        i=0
        while(i<num_expenses):
            file_object.write(expense_dates[i]+","+expense_names[i]+","+str(expense_amounts[i])+"\n")
            i+=1
        file_object.close()
    except:
        sys.stdout.write("Could not save to file")

run_expenses_manager()
