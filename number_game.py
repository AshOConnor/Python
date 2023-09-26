import sys
import random
#creates a prompt that asks you to type a name
name=input("please enter your name: "+ "\n")
#creates a prompt that asks you to write true or false, when false it written it then asks you to write true so you can continue
fact=input("please write true " + "\n")
#i used the while loop because when "if" is used after one wrong answer the system fails
while fact !=("true"):
    sys.stdout.write("id recommend you write true " + "\n" + "\n")
    fact=input("please write true  " +"\n"+"\n")

sys.stdout.write("hello " + name + "!"+"\n"+"\n")
#the following is a simple string used to add some character to the program
message1="please be patient"
sys.stdout.write(str(message1)+"\n"+"\n")
message="thankyou for being patient"
sys.stdout.write(str(message)+"\n"+"\n")
#if != was used so the program knew if the asnwer wasnt yes to display a prompt and continue to run anyway
yes = input("are you ready to play a game? " + "\n")
if yes !=("yes"):
    sys.stdout.write("too bad lets start! "+"\n"+"\n")
#elis here is used so that it doesnt run in a loop with the previous if statment so that typing yes still starts the program
elif yes =="yes":
    sys.stdout.write("okay! lets go"+ "\n"+"\n")
#random.randint will selects a random integer from the marked 1,1000 
n = random.randint(1,1000)
sys.stdout.write("im thinking of a random number between 1 & 1000"+"\n")
# guesses=[] is creating a list so that the program knows later on what to do with the information weve given it 
Guesses= []
#running is at True so that the program will run
gamma = True
while gamma:
#_str is used to display readable information in the program
    guess_str = input("take a guess ")
    #int() is for the turning the number into an integer number
    guess = int(guess_str)
    Guesses.append(guess)
    # == just means equals here
    if guess == n:
        #\n is to add a new line to the text below so its not clumped
        sys.stdout.write("well done, thats correct"+"\n")
        #str(len()) displays the length of the string in question ie Guesses
        sys.stdout.write("you used "+ str(len(Guesses))+ " Guesses\n")
        # if was used at the start but elif was used after to check multiple expressions
        if len(Guesses)<5:
            #ive added a grading system based on the the program listing how many attempts it takes
            sys.stdout.write("you got an A")
        elif len(Guesses)<10:
            sys.stdout.write("you got a B")
        elif len (Guesses)<15:
            sys.stdout.write("you got a C")
        elif len(Guesses)<20:
            sys.stdout.write("you got a D")
        else:
            sys.stdout.write("you got a F")
            #if your guess is smaller than n(the number) the system tells you to guess a bigger number
        gamma = False
    elif guess < n:
        sys.stdout.write("try a bigger number ")
    else:
        sys.stdout.write("try a smaller number ")
