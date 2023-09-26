import sys
import time

def main ():
        '''This is an interactive story of a Go Kart adventure that allows the user to answer different
        questions and displays the answers back to them during the adventure story. Throughout the
        story when answer different questions the story will change or ask the user to input another answer.'''

#This section of codes explains what the story is and how to interact with it.
#This is printed out at the start of the story when the program is ran.
sys.stdout.write("This is a story of a Go Kart adventure through a rainforest.\n")
sys.stdout.write("You get to choose the character names and a number to get started.\n")
sys.stdout.write("Throughout the story, you have to answer certain questions.\n")
sys.stdout.write("This will give you the chance to choose your own path!\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(2)

#This section asks the user to enter a name for a variable.
#This variable is input and saved for later use in the program.
#The variable name snake is the most appropriate for this code.
sys.stdout.write("\n")
sys.stdout.write("Please enter a name for a snake: ")
snake=sys.stdin.readline().strip()
sys.stdout.write("You have chosen the name "+snake+".\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(1)

#This section asks the user to enter a name for a variable.
#This variable is input by the user and saved for later use in the program.
#The variable name crocodile is the most appropriate for this code.
sys.stdout.write("\n")
sys.stdout.write("Please enter a name for a crocodile: ")
crocodile=sys.stdin.readline().strip()
sys.stdout.write("You have chosen the name "+crocodile+".\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(1)

#This section asks the user to enter a name for a variable.
#This variable is input by the user and saved for later use in the program.
#The variable name mermaid is the most appropriate for this code.
sys.stdout.write("\n")
sys.stdout.write("Please enter a name for a mermaid: ")
mermaid=sys.stdin.readline().strip()
sys.stdout.write("You have chosen the name "+mermaid+".\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(1)

#This section asks the user to enter an integer in words used as a variable.
#The variable is input by the user and saved for later use in the program.
#The variable word_nam could of been alternately written as wordnum
#but is easier to see as it is written in the code.
#This makes it the most appropriate.
sys.stdout.write("\n")
sys.stdout.write("Please enter a number in words: ")
word_num=sys.stdin.readline().strip()
sys.stdout.write("You have chosen the number "+word_num+".\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(1)

#This section asks the user to input a name for the varaible
#The variable is input by the user and save for use in the start of the story.
#The variable name is the most appropriate for this section as it covers the users name.
sys.stdout.write("\n")
sys.stdout.write("Please enter your name: ")
name=sys.stdin.readline().strip()

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep (1)

#This section prints out a sentence with the variable that the user input into
#the "name" section variable.
#This section also ask's you a question that must be answered correctly to proceed in the story.
#The variable "adventuring" could of been called "advneture" but is best
#suited for this code.
sys.stdout.write("\n")
sys.stdout.write("Hello "+name+". Would you like to go adventuring?\n")
sys.stdout.write("Yes/No: ")
adventuring=sys.stdin.readline().strip()

#This if statement makes sure that the user inputs the correct answer to the question.
#If the question isn't input correctly the program responds making the user continue anyway.
#The answer can be anything as the code makes you continue even if you answer wrong.
#The variable name "adventuring" could alternativley be "adventure" but is best suited for this code.
#The if and elif statements could be swapped around and the code will still work.
if adventuring =="Yes":
        sys.stdout.write("\n")
        sys.stdout.write("Welcome aboard the Go Kart adventure "+name+".\n")
        
elif adventuring =="No":
        sys.stdout.write("\n")
        sys.stdout.write("You party pooper "+name+"! Well we're going to go anyway!\n")
        
else: sys.stdout.write("I told you to answer Yes or No "+name+". Bad luck, you're coming anyway!\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate..
time.sleep(1)

#This section also asks the user to answer a specific question using an integer.
#The variable "number" could of been named differently such as "num" but is most appropriate for this section,
#as the question needs an answer to it that is a number.
sys.stdout.write("\n")
sys.stdout.write("You head off on a journey into a mystical rainforest in a GoKart.\n")
sys.stdout.write("While driving around the rainforest in your Go Kart you come to a sign with a large gate.\n")
sys.stdout.write("The sign says to enter a number either 1 or 2 to continue.\n")
sys.stdout.write("Please enter number: ")
number=int(sys.stdin.readline().strip())

#This if statement makes sure that the user enters the correct answer to the question.
#If the question isn't input correctly the program responds making the user input again.
#The answer must be in a int form to correctly move on in the story.
#The variable name "number" could alternativley be "num" but is best suited for this code.
if number !=1:
        sys.stdout.write("\n")
        sys.stdout.write("YOU SHALL NOT PASS. The gate starts to get angry!\n")
        sys.stdout.write("Please answer again: ")
        number = (sys.stdin.readline().strip())
    
else: sys.stdout.write("\n")
sys.stdout.write("YOU HAVE CHOSEN CORRECTLY. YOU SHALL PASS.\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(2)

#This section asks the user to input a word to continue the story on which way they want to go.
#The variable "torch" could of been an alternative name like "light" but was most appropriate for this section,
#as it relates to the question in the story.
sys.stdout.write("\n")
sys.stdout.write("The gates creak as they slowly open allowing you to view what's behind.\n")
sys.stdout.write("As you get a better look, you can see that the rainforest is very dense and there is a bend up ahead.\n")
sys.stdout.write("You continue on around the bend then a palm tree and into a dark tunnel.\n")
sys.stdout.write("You come to a stop in the middle of the tunnel.\n")
sys.stdout.write("You find a torch on the floor of the GoKart.\n")
sys.stdout.write("Do you turn it on or leave it off?\n")
sys.stdout.write("On/Off: ")
torch=sys.stdin.readline().strip()

#The while loop was most appropriate here as it prompts the user to answer with
#the correct input and if not the program displays back how to answer.
#The if and elif statements can be swapped around if needed. The way it was written
#is the way the question was asked keeping it in order.
#The variable "torch" could of been an alternative name such as light,
#but was most appropriate for this section as it relates to the question in the story.
while torch !="On" and torch !="Off":
        sys.stdout.write("Please answer with On or Off: ")
        torch = (sys.stdin.readline().strip())
        
if torch == "Off":
        sys.stdout.write("\n")
        sys.stdout.write("You hear the sound of "+snake+" the snake. The snake hisses at you as you scream for help.\n")
        sys.stdout.write("You fiddle around with the torch trying to find the switch to turn it on.\n")
        sys.stdout.write("You turn it on just in time and "+snake+" slithers away. Phew!\n")

elif torch == "On":
        sys.stdout.write("\n")
        sys.stdout.write("You hear something in the darkness slithering around, you shine the torch over.\n")
        sys.stdout.write("To your horror you find "+snake+" hissing at the light. You yell at "+snake+" to getaway.\n")
        sys.stdout.write(""+snake+" turns around and slithers away.\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.        
time.sleep(3)

#This section continues the story and could of been written in one long sentence.
#Usuing different lines to write the code helps with readability and looks better
#when being written and when it's produced.
#This section asks the user to input a word to continue the story on which way they want to go.
#The variable "path" could of been an alternative name but was most appropriate for this section,
#as it relates to the which way to go in the story.
sys.stdout.write("\n")
sys.stdout.write("You continue driving down the tunnel in your Go Kart and finally can start to see the light at the end of the tunnel.\n")
sys.stdout.write("As you start heading out of the tunnel, you see a magical lake down the bottom of a valley on your left-hand side.\n")
sys.stdout.write("You can see that the road winds down the rainforest mountains and eventually meets the lake.\n")
sys.stdout.write("You also see that there could be a shortcut through the foliage of the rainforest to the left.\n")
sys.stdout.write("Which path do you take, the shortcut or the road?\n")
sys.stdout.write("Shortcut/Road: ")
path=sys.stdin.readline().strip()

#The while loop was most appropriate here as it prompts the user to answer with
#the correct input and if not the program displays back how to answer.
#The if and elif statements can be swapped around if needed. The way it was written
#is the way the question was asked keeping it in order.
#The variable "path" could of been an alternative name but was most appropriate for this section,
#as it relates to the which way to go in the story.
while path !="Shortcut" and path !="Road":
        sys.stdout.write("Please answer with Shortcut or Road: ")
        path = (sys.stdin.readline().strip())
        
if path == "Shortcut":
        sys.stdout.write("\n")
        sys.stdout.write("You turn off the road and start heading down a very old dirt road.\n")
        sys.stdout.write("As you go further and further into the unknown, you start to pick up speed.\n")
        sys.stdout.write("You start flying down the hill, trying to stay on the road as much as you can.\n")
        sys.stdout.write("The Go Kart starts losing traction as you come up to a large jump. You hit the jump and do a 360 in the air.\n")
        sys.stdout.write("You stick the landing and start slowing down as you get closer and closer to the bottom.\n")
        sys.stdout.write("As you get to the bottom you can see the road coming up and you turn just in time to safely rejoin the road.\n")
        
elif path == "Road":
        sys.stdout.write("\n")
        sys.stdout.write("You continue down the windy road around the mountain ranges.\n")
        sys.stdout.write("The view is breathtaking as you start winding down the mountain.\n")
        sys.stdout.write("About halfway down the mountain, you start to lose a little bit of traction and drift around the corner.\n")
        sys.stdout.write("As you start to straighten up and almost reach the bottom your Go Kart cuts out.\n")
        sys.stdout.write("Just as you reach the bottom your Go Kart decides to turn back on and you can see the exit of the shortcut that you didn't take.\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(3)

#This section continues the story and could of been written in one long sentence.
#Usuing different lines to write the code helps with readability and looks better
#when being written and when it's produced.
#This part of the story uses a variable to validate different aspects.
#The variables crocodile could be different but is best suited for this story.
#This section also asks the user to answer a specific question using an integer.
#The variable "answer" could of been named differently but is most appropriate for this section,
#as the question needs an answer to it.
sys.stdout.write("\n")
sys.stdout.write("You continue along the last 100 meters of the road and finally arrive at the magical lake.\n")
sys.stdout.write("As you pull into the parking area to view the lake you see a large green figure in the water.\n")
sys.stdout.write("The green figure appears to be getting closer and closer to the lookout area.\n")
sys.stdout.write("You realise that it's "+crocodile+" the crocodile.\n")
sys.stdout.write(""+crocodile+" comes to the edge of the lookout and asks you to answer a question correctly to continue.\n")
sys.stdout.write("You politely accept and await the question.\n")
sys.stdout.write("The question is.. Which number will let you pass, 1.5 or 1.4?: ")
answer=float(sys.stdin.readline().strip())

#This if statement makes sure that the user enters the correct answer to the question.
#If the question isn't input correctly the program responds making the user input again.
#The answer must be in a float form to correctly move on in the story.
#THe variable name "answer" could alternativley be "decmial".
#The variable "crocodile" is used in the this section to add to additional story line.
if answer !=1.5:
        sys.stdout.write("\n")
        sys.stdout.write("You answered incorrectly and "+crocodile+" the crocodile tries to eat you.\n")
        sys.stdout.write("You quickly move out of the way and dodge the bite.\n")
        sys.stdout.write("Please answer again: ")
        answer = sys.stdin.readline().strip()
        
else: sys.stdout.write("\n")
sys.stdout.write("CONGRATULATIONS YOU MAY PASS!\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(2)

#This section continues the story and could of been written in one long sentence.
#Usuing different lines to write the code helps with readability and looks better
#when being written and when it's produced.
#This part of the story uses variable to validate different aspects.
#The variable name crocodile could be different but is best suit for this story.
#This section also asks the user to answer a specific question and inputs the answer.
#This helps the story continue. The variable "action" could of differently but is most appropriate for this section,
#as it relates to the action of going fast or slow.
sys.stdout.write("\n")
sys.stdout.write("You wave goodbye to "+crocodile+" and start heading down the road on your part of the journey.\n")
sys.stdout.write("As "+crocodile+" fades out in the distance you keep driving and can see that the rainforest is getting less dense as you go.\n")
sys.stdout.write("You soon come out of the dense jungle and the landscape has turned into sandy dunes with the sound of waves crashing not too far away.\n")
sys.stdout.write("The sound of the waves gets closer and closer and closer! You see a strange figure in the distance.\n")
sys.stdout.write("As you get closer you can't tell if the figure is a fish or a human....\n")
sys.stdout.write("You cannot believe what you're seeing.... IT'S A MERMAID!\n")
sys.stdout.write("As you get closer you start to freak out. You're not sure if you should speed up or slow down.\n")
sys.stdout.write("Which action do you take, speed up or slow down?\n")
sys.stdout.write("Speed/Slow: ")
action=sys.stdin.readline().strip()

#This creates a list of items that are used later on in the story.
#I have prefilled the list with information as how it reflects later in the story.
#There could of been alternative names for the lists, but this was the most appropriate.
repair_kit =["Wheel", "Jack", "Lug Wrench"]
repair_kit_amount =["1", "1", "1"]

#The while loop was most appropriate here as it prompts the user to answer with
#the correct input and if not the program displays back how to answer.
#The if and elif statements can be swapped around if needed but for this code
#it is easier to do as the first word in the question is Speed and the second is Slow.
#The variable action could of been an alternative name but was most appropriate for this section,
#as it relates to the action of going fast or slow.
while action !="Speed" and action !="Slow":
        sys.stdout.write("Please answer wth Speed or Slow: ")
        action = (sys.stdin.readline().strip())

if action =="Speed":
        sys.stdout.write("\n")
        sys.stdout.write("You speed up, almost losing control of your Go Kart, you slide around the road hitting the kerb and buckling a wheel.\n")
        sys.stdout.write("You stop your vehicle and look around in the footwell and luckily you find a repair kit that has the following inside -\n")
#The while i  loop produces a list outcome in the story.
#This shows the user what items are in the list and how many of the items there are.
#This is the most appropriate way to do this.
#You can alternativley use a for loop but this is the best method.
#The other alternative is to also print each list side by side but is not worth it.
#Printing this outcome is clean and neat. The amount and name could be the other way around if need be.
        i = 0
        while i < len(repair_kit):
                print("-", repair_kit[i], "x", repair_kit_amount[i])
                i = i + 1
        sys.stdout.write("You get out of your car trembling from the fright you received from almost crashing and almost injuring yourself.\n")
        sys.stdout.write("You take a few minutes to repair the Go Kart.\n")
        sys.stdout.write("Once you finish the repair you jump back in the GoKart and continue driving closer to the mermaid.\n")
        sys.stdout.write("You arrive at the strange-looking creature.\n")

elif action =="Slow":
        sys.stdout.write("\n")
        sys.stdout.write("You slow down to try and gain some confidence about arriving at the destination where the mermaid is.\n")
        sys.stdout.write("The closer you get the more nervous you feel.\n")
        sys.stdout.write("You start to sweat...\n")
        sys.stdout.write("You start to shake...\n")
        sys.stdout.write("You take a deep breath and edge closer and closer to the creature..\n")
        sys.stdout.write("You realise once you get there you should never have been scared all along.\n")

#Sleep stops the program for the time specified to allow the user to read
#the story at an easier rate.
time.sleep(3)

#This section continues the story and could of been written in one long sentence.
#Usuing different lines to write the code helps with readability and looks better
#when being written and when it's produced.
#This section of code uses variables taken at the start of the story and inputs them
#into the sentence as the story goes on. The variable names could of been called anything
#but using the name of the specific creature is best suited for this program.
#The variable "word_num" was used in this last section to finish the story.
sys.stdout.write("\n")
sys.stdout.write("The strange creature all along was a very friendly mermaid called "+mermaid+".\n")
sys.stdout.write("Then all of a sudden two figures appear from behind "+mermaid+"...\n")
sys.stdout.write("It's "+snake+" the snake and "+str(crocodile)+" the crocodile.\n")
sys.stdout.write("They appear friendlier than when you first met them!.\n")
sys.stdout.write("All of them ask you to answer the next question to be able to finish your journey.\n")
sys.stdout.write("How many stars are there in the sky?\n")
sys.stdout.write("You look up and count as many as you can... "+word_num+" you shout!\n")
sys.stdout.write("They all smile and tell you to start your Go Kart back up and you may leave.\n")
sys.stdout.write("You look back as you drive off into the sunset waving goodbye, with a tear in your eye.\n")
sys.stdout.write("Your drive into the distance, over the horizon and never return.\n")
sys.stdout.write("\n")
sys.stdout.write("THE END.")


main()
