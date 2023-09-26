import sys
import time


def main():
    """This is an interactive story of a GoKart adventure that allows the user to answer different
            questions and displays the answers back to them during the adventure story."""


sys.stdout.write("This is a story of a GoKart adventure through a rainforest.\n")
sys.stdout.write("You get to choose the character names and numbers as we go along.\n")
sys.stdout.write("This will give you the chance to choose your own path!\n")

sys.stdout.write("\nPlease enter a name for a snake: ")
snake = sys.stdin.readline().strip()
sys.stdout.write("You have chosen the name " + snake + ".\n")

time.sleep(1)

sys.stdout.write("\nPlease enter a name for a crocodile: ")
crocodile = sys.stdin.readline().strip()
sys.stdout.write("You have chosen the name " + crocodile + ".\n")

time.sleep(1)

sys.stdout.write("\nPlease enter a name for a mermaid: ")
mermaid = sys.stdin.readline().strip()
sys.stdout.write("You have chosen the name " + mermaid + ".\n")

time.sleep(1)

sys.stdout.write("\nPlease enter your name: ")
name = sys.stdin.readline().strip()

time.sleep(1)

sys.stdout.write("\nHello " + name + ". Would you like to go adventuring? Yes/No: ")
adventuring = sys.stdin.readline().strip()

if adventuring == "Yes":
    sys.stdout.write("\nWelcome aboard the GoKart adventure " + name + ".\n")

elif adventuring == "No":
    sys.stdout.write("\nYou party pooper " + name + "! Well we're going to go anyway!\n")

else:
    sys.stdout.write("\nI told you to answer Yes or No " + name + ". Bad luck, you're coming anyway!\n")

time.sleep(1)

sys.stdout.write("You head off on a journey into a mystical rainforest in a GoKart.\n")
sys.stdout.write("While driving around the rainforest in your GoKart you come to a sign with a large gate.\n")
sys.stdout.write("The sign says to enter a number between 1 and 3 to continue.\n")
sys.stdout.write("Please enter number: ")
number = int(sys.stdin.readline().strip())

if number != 1:
    sys.stdout.write("YOU SHALL NOT PASS. The GoKart blows up.\n")
    sys.stdout.write("Please restart the program to start again.")
    number = (sys.stdin.readline().strip())
    time.sleep(36000)

else:
    sys.stdout.write("\nYOU HAVE CHOSEN CORRECTLY. YOU SHALL PASS.\n")

time.sleep(2)

sys.stdout.write("The gates creak as they slowly open allowing you to view whats behind.\n")
sys.stdout.write(
    "As you get a better look, you can see that the rainforest is very dense and there is a bend up ahead.\n")
sys.stdout.write("You continue on around the bend then a palm tree and into a dark tunnel.\n")
sys.stdout.write("You come to a stop in the middle of the tunnel.\n")
sys.stdout.write("You find a torch on the floor of the GoKart.\n")
sys.stdout.write("Do you turn it on or leave it off? On/Off: ")
torch = sys.stdin.readline().strip()

while torch != "On" and torch != "Off":
    sys.stdout.write("Please answer with On or Off:")
    torch = (sys.stdin.readline().strip())

if torch == "Off":
    sys.stdout.write(
        "\nYou hear the sound of " + snake + " the snake. The snake hiss's at you as you scream for help.\n")
    sys.stdout.write("You fiddle around with the torch trying to find the switch to turn it on.\n")
    sys.stdout.write("You turn it on just in time and " + snake + " slithers away. Phew!\n")

elif torch == "On":
    sys.stdout.write("\nYou hear something in the darkness slithering around, you shine the torch over.\n")
    sys.stdout.write(
        "To your horror you find " + snake + " hissing at the light. You yell at " + snake + " to get away.\n")
    sys.stdout.write("" + snake + " turns around and slithers away.\n")

time.sleep(3)

sys.stdout.write(
    "\nYou continue driving down the tunnel in your GoKart and finally can start to see the light at the end of the "
    "tunnel.\n")
sys.stdout.write(
    "As you start heading out of the tunnel, you see a magical lake down the bottom of a valley on your left hand "
    "side.\n")
sys.stdout.write("You can see that the road winds down the rainforest mountains and eventually meets the lake.\n")
sys.stdout.write("You also see that there could be a shortcut through the foliage of the rainforest to the left.\n")
sys.stdout.write("Which path do you take, the shortcut or the road? Shortcut/Road: ")
path = sys.stdin.readline().strip()

while path != "Shortcut" and path != "Road":
    sys.stdout.write("Please answer with Shortcut or Road:")
    path = (sys.stdin.readline().strip())

if path == "Shortcut":
    sys.stdout.write("\nYou turn off the road and start heading down a very old dirt road.\n")
    sys.stdout.write("As you go further and further into the unknown, you start to pick up speed.\n")
    sys.stdout.write("You start flying down the hill, trying to stay on the road as much as you can.\n")
    sys.stdout.write(
        "The GoKart starts loosing traction as you come up to a large jump. You hit the jump and do a 360 in the air.\n")
    sys.stdout.write("You stick the landing and start slowing down as you get closer and closer to the bottom.\n")
    sys.stdout.write(
        "As you get to the bottom you can see the road coming up and you turn just in time to safely rejoin the road.\n")

elif path == "Road":
    sys.stdout.write("\nYou continue down the windy road around the mountain ranges.\n")
    sys.stdout.write("The view is breath taking as you start winding down the mountain.\n")
    sys.stdout.write(
        "About halfway down the mountain you start to lose a little bit of traction and drift around the corner.\n")
    sys.stdout.write("As you start to straighten up and almost reach the bottom your GoKart cuts out.\n")
    sys.stdout.write(
        "Just as you reach the bottom your GoKart decides to turn back on and you can see the exit of the shortcut "
        "that you didn't take.\n")

time.sleep(3)

sys.stdout.write("\nYou continue along the last 100 meters of the road and finally arrive at the magical lake.\n")
sys.stdout.write("As you pull into the parking area to view the lake you see a large green figure in the water.\n")
sys.stdout.write("The green figure appears to be getting closer and closer to the lookout area.\n")
sys.stdout.write("You realise that it's " + crocodile + " the crocodile.\n")
sys.stdout.write(
    "" + crocodile + " comes to the edge of the lookout and asks you to answer a question correctly to continue.\n")
sys.stdout.write("You politely accept and await for the question.\n")
sys.stdout.write("The question is what is the exact number between 1 and 2?: ")
answer = float(sys.stdin.readline().strip())

if answer != 1.5:
    sys.stdout.write("\nYou answered incorrectly and " + crocodile + " the crocodile eats you.\n")
    sys.stdout.write("Please restart the program to start again.")
    answer = (sys.stdin.readline().strip())
    time.sleep(36000)

else:
    sys.stdout.write("\nCongratulations you may pass!\n")

time.sleep(2)

sys.stdout.write("You wave goodbye to " + crocodile + " and start heading down the road on your part of the journey.\n")
sys.stdout.write(
    "As " + crocodile + "fades out in the distance you keep driving and can see that the rainforest is getting less "
                        "dense as you go.\n")
sys.stdout.write(
    "You soon come out of the dense jungle and the landscape has turned into sandy dunes with the sound of waves "
    "crashing not to far away.\n")
sys.stdout.write("The sound of the waves get closer and closer and closer! You see a strange figure in the distance.\n")
sys.stdout.write("As you get closer you can't tell if the figure is a fish or a human....\n")
sys.stdout.write("You cannot believe what you're seeing.... IT'S A MERMAID!\n")
sys.stdout.write("As you get closer you start to freak out. You're not sure if you should speed up or slow down.\n")
sys.stdout.write("Which action do you take, speed up or slow down? Speed/Slow: ")
action = sys.stdin.readline().strip()

while action != "Speed" and action != "Slow":
    sys.stdout.write("Please answer wth Speed or Slow: ")
    action = (sys.stdin.readline().strip())

if action == "Speed":
    sys.stdout.write("\nYou speed up.\n")

elif action == "Slow":
    sys.stdout.write("\nYou slow down.\n")

time.sleep(3)

sys.stdout.write("" + mermaid + " Says hello.")

main()
