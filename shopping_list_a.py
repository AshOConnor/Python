import sys
from collections import deque

def main():
    '''This is what the program is about and what we will use it for'''
sys.stdout.write("welcome to the shopping List application...\n")
#This asks the user to input their name
sys.stdout.write("Please enter your name: ")
name = sys.stdin.readline().strip()

#This produces the users name and explains what is going to happen
sys.stdout.write("Hello "+name+". Leta add an item to a shopping list.\n")

#This asks the user to add anything to the list
sys.stdout.write("Please enter your addition to the list: ")
item = str(sys.stdin.readline().strip())

#This line defines the items and adds it to the list later in the next section
def display():
    '''This line adds an item to the list and displays what they chose'''
    sys.stdout.write("You have added "+str(item)+".\n")
display()

#This produces the list so far with the additional item in the place it has been chosen to attach
sys.stdout.write("Here is your list so far.\n")
shoppingList = deque (['Milk', 'Pet Food', 'Juice', 'Coke'])
shoppingList.insert(0, item)
print(shoppingList)

sys.stdout.write("Would you like to remove milk from the list? Please enter Y or N.\n")
#This line askes the user to answer the above question
sys.stdout.write("Please answer with Y or N: ")
sys.stdin.readline().strip()

#This creates a loop so the user has to answer correctly
remove = sys.stdin.readline().strip()
while remove != "Y" and remove !="N":
    sys.stdout.write("Please answer Y or N.")
    remove = (sys.stdin.readline().strip())
if remove == "Y":
    sys.stdout.write("Okay now you have the following left on the list")
    shoppingList.remove('Milk')
else: sys.stdout.write("Okay here is your list.")

sys.stdout.write("\n")


print(shoppingList)
#This uses the lambda and calculates how much each item is.
itemPrice = lambda x: x + 1
sys.stdout.write("The price of each item is $"+str(itemPrice(2))+".")

main()
