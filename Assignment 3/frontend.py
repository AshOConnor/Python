import sys
import backend


class FrontEnd:

    def get_str(prompt):
        """This function collects all inputs from the user that has been input
        and stores them in their appropriate variables."""

        # The variable "added_str" was used because it is most appropriate
        # in the program. There could of been an alternative used such as "input_str"
        # but "added_str" was used. The while loop was used here so that if the user
        # doesn't need to add anything to a string that they can just press enter
        # if the user inputs a space then presses enter then the program will advise
        # that the input that was entered is incorrect and will make the user enter
        # the input again. This then returns the added strings.
        sys.stdout.write(prompt)
        added_str = sys.stdin.readline().strip()
        while added_str == " ":
            sys.stdout.write("Error! You must enter a valid input: ")
            added_str = sys.stdin.readline().strip()

        return added_str

    def __init__(self, __backend):
        """This program allows a user to store all bookmarks associated with their TeamSpeak3
            application. It provides a menu to load, add, display and save their bookmarks.
            Throughout the code there are different variables used and the users input is
            stored allowing display or saving of inputs."""

        # This code is implemented from the backend and collects the list "bookmarks" so it can be used
        # with the menu options and variables below. It also imports the csv file that is required.
        # If the csv file isn't the same name or isn't located on the computer the program will create one.
        # This is intended as the filename should never be played with.
        self.__backend = backend

        # This section is provided to the user as soon as the program has been ran it takes
        # into account that the user has loaded the program and has chosen to select the
        # bookmarks menu as they want to add or view bookmarks.
        # This was the most appropriate as there wasn't any need to choose to go to the
        # bookmark section from a main menu.
        sys.stdout.write("======================\n")
        sys.stdout.write("LOADING PROGRAM.......\n")
        sys.stdout.write("======================\n\n")
        sys.stdout.write("======================\n")
        sys.stdout.write("WELCOME TO TEAMSPEAK3!\n")
        sys.stdout.write("======================\n\n")
        sys.stdout.write("Please enter your TeamSpeak security code to continue..\n")

        # This section asks the user to input a security code to be able to access the bookmarks
        # menu. The variable teamspeak_password was most appropriate in this instance although
        # it could of been called "teamspeak_code". It uses a try and except here and raises and exception
        # if the user hasn't put the correct input in. The exception "ValueError" is most appropriate for this
        # code block.
        sys.stdout.write("Enter code: ")
        teamspeak_password = sys.stdin.readline().strip()
        try:
            ts_password = int(teamspeak_password)
            input_correct = True
        except:
            raise ValueError("Incorrect input entered. Must be an integer. Please restart program.\n")
        sys.stdout.write("\n\n")
        sys.stdout.write("======================\n")
        sys.stdout.write("LOADING BOOKMARK MENU.\n")
        sys.stdout.write("======================\n")
        sys.stdout.write("\n\n")
        sys.stdout.write(str(self.__backend.bookmark_amount()) + " bookmarks loaded from file...\n\n")

        # This menu is provided to the user and was the most appropriate name to be used.
        # The menu options could have been arranged in any order when being created
        # but this will suffice.
        menu = "\n"
        menu += "~~~~~~~~~~~~~~~~~~~~~~~~\n"
        menu += "TeamSpeak3 Bookmark Menu\n"
        menu += "~~~~~~~~~~~~~~~~~~~~~~~~\n"
        menu += "[A]dd Bookmark\n"
        menu += "[R]emove a Bookmark\n"
        menu += "[D]isplay Bookmarks\n"
        menu += "[S]ave Bookmarks\n"
        menu += "[E][X]it\n"
        menu += "Enter Option: "
        option = FrontEnd.get_str(menu).lower()

        # I used the while loop here to be able to recall the menu and to also
        # recall the menu if the user has input the correct information.
        # This option allows the user to exit the program if needed.
        # The option "e" and "x" were the most appropriate for this option
        # as they are most commonly used for exiting a program menu. The alternative
        # that could of been used here are "e" and "Exit".
        while option != "e" and option != "x":
            sys.stdout.write("\n")

            # This option allows the user to add a bookmark to the program and this
            # option can be selected multiple times to add multiple bookmarks.
            # The option "a" was most appropriate for this option although alternatively
            # the word "add" could have been used. The variables that have been assigned
            # were the most appropriate for this program and don't need any other justification.
            # The while loop is used for bookmark_number as the user must enter an integer.
            # If the input isn't correct it will ask the user to input again. After the bookmark data has been
            # input a message will display to the user advising that the bookmark has been added.
            if option == "a":
                sys.stdout.write("You have selected to add a bookmark...\n")
                bookmark_name = FrontEnd.get_str("Enter bookmark name: ")
                bookmark_nickname = FrontEnd.get_str("Enter nickname for "+bookmark_name+": ")
                bookmark_address = FrontEnd.get_str("Enter server address for "+bookmark_name+": ")
                bookmark_password = FrontEnd.get_str("Enter bookmark password (if required) for "+bookmark_name+": ")
                bookmark_channel = FrontEnd.get_str("Enter bookmark default channel (if required) for "+bookmark_name+": ")
                bookmark_channel_password = FrontEnd.get_str(
                    "Enter bookmark default channel password (if required) for "+bookmark_name+": ")

                input_correct = False
                while input_correct == False:
                    bookmark_number = FrontEnd.get_str("Enter bookmark number: ")
                    try:
                        number = int(bookmark_number)
                        input_correct = True
                    except:
                        number = 0
                        sys.stdout.write("Invalid Number!\n")

                self.__backend.add_bookmark(bookmark_name, bookmark_nickname,
                                            bookmark_address, bookmark_password, bookmark_channel,
                                            bookmark_channel_password, number)

                sys.stdout.write("\n")
                sys.stdout.write("Adding bookmark...\n\n")
                sys.stdout.write("Your bookmark has successfully been added!\n")

            # This option allows the user to remove a bookmark from the program and this
            # option can be selected multiple times to remove multiple bookmarks.
            # The option "r" was most appropriate for this option although alternatively
            # the word "remove" could have been used. The variables that have been assigned
            # were the most appropriate for this program and don't need any other justification.
            # The user must enter the correct stored information. Once the correct information has been input
            # the message will appear back to the user advising of removal. The user will still need to check
            # if it has been removed by displaying bookmarks. If the user input incorrect information
            # the bookmark will not have been deleted.
            elif option == "r":
                sys.stdout.write("Removing bookmark...\n")
                bookmark_name = FrontEnd.get_str("Enter bookmark name: ")
                bookmark_nickname = FrontEnd.get_str("Enter nickname: ")
                bookmark_address = FrontEnd.get_str("Enter server address: ")
                bookmark_password = FrontEnd.get_str("Enter bookmark password (if required): ")
                bookmark_channel = FrontEnd.get_str("Enter bookmark default channel (if required): ")
                bookmark_channel_password = FrontEnd.get_str(
                    "Enter bookmark default channel password (if required): ")
                number = FrontEnd.get_str("Enter bookmark Number: ")
                self.__backend.remove_bookmark(bookmark_name, bookmark_nickname, bookmark_address, bookmark_password,
                                               bookmark_channel, bookmark_channel_password, number)
                sys.stdout.write("Bookmark has been found and removed if entry was correct...\n")

            # This option displays the loaded information or the added information
            # back to the user. The data is collected from the backend and input
            # into the front end. The option "d" was most appropriate for this section
            # although the option "display" could of been alternately used. The display back
            # to the user could have been formatted better but I was unsure of how to do this.
            elif option == "d":
                sys.stdout.write("Displaying bookmarks...\n\n")
                sys.stdout.write("Name, Nickname, Address, Password, Channel, Password, Number\n")
                sys.stdout.write(self.__backend.__str__())

            # This option allows the user to save a csv or txt file from the information that
            # was added during the program. The option "s" was best suit for this although the alternative
            # could have been "save" but "s" was most appropriate.
            elif option == "s":
                sys.stdout.write("You have selected to save bookmarks....\n")
                self.__backend.save_bookmarks()
                sys.stdout.write("You have successfully saved bookmarks to data.csv")

            # This statement is displayed back to the user if the user did not put in the
            # correct input at the menu entry. It will then display the menu back to the user
            # and the user must choose a correct option.
            else:
                sys.stdout.write("Invalid menu option!\n")

            option = FrontEnd.get_str(menu).lower()
        # This is displayed to the user when they have chosen to close the program.
        sys.stdout.write("TeamSpeak3 now closing...\n")
