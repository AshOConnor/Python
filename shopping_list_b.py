import sys

def main():
    from collections import deque
sys.stdout.write("Welcome to the Shopping List application...\n")
    

sys.stdout.write("Please enter your name: ")
name = sys.stdin.readline().strip()
sys.stdout.write("Hello "+name+". Lets add some items to the shopping list.\n")

shopping_list=[]
shopping_list_amount=[]
deque1 = shopping_list
deque2 = shopping_list_amount
    
menu="\n\n"
menu+="Shopping List Menu\n"
menu+="------------------\n"
menu+="[A]dd item to list\n"
menu+="[D]isplay items in list\n"
menu+="E[x]it\n"
menu+="\n"
menu+="Enter option: "

sys.stdout.write(menu)
option=sys.stdin.readline().strip().lower()
while (option!="x"):
        sys.stdout.write("\n\n")
        if (option=="a"):
            sys.stdout.write("Add item: ")
            shopping_list_name=sys.stdin.readline().strip()

            sys.stdout.write("Add amount of "+shopping_list_name+": ")
            shopping_list_amounts=int(sys.stdin.readline())
            while(shopping_list_amounts<1):
                sys.stdout.write("Error! Please enter a number above 0: ")
                shopping_list_amounts=int(sys.stdin.readline())

            shopping_list.append(shopping_list_name)
            shopping_list_amount.append(shopping_list_amounts)
            
        elif (option=="d"):
            sys.stdout.write("Shopping List\n")
            sys.stdout.write("-------------\n")
            index=0
            while( index<len(shopping_list) ):
                sys.stdout.write(shopping_list[index]+": ")
                sys.stdout.write(str(shopping_list_amount[index])+"\n")
                index+=1
        else:
            sys.stdout.write("Invalid option!\n")
        sys.stdout.write(menu)
        option=sys.stdin.readline().strip().lower()

sys.stdout.write("\n")
sys.stdout.write("Would you like to remove the first item from the list? Please enter Y or N.\n")
sys.stdout.write("Please answer with y or n: ")
remove = sys.stdin.readline().strip().lower()
while remove != "y" and remove !="n":
    sys.stdout.write("Please answer y or n.")
    remove = (sys.stdin.readline().strip())
if remove == "y":
    sys.stdout.write("Okay now you have the following left on the list.\n")
    shopping_list.pop(0)
    shopping_list_amount.pop(0)
else: sys.stdout.write("Okay here is your list.\n")

for i in range (len(shopping_list)) :
            print(i + 1, "-", shopping_list[i], "x", shopping_list_amount[i])

itemPrice = lambda x: x + 1
sys.stdout.write("\n")
sys.stdout.write("The price of each item is $"+str(itemPrice(2))+".")

main()
