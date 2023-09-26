import sys
import TeamSpeak3_backend


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


def main():
    """This program allows a user to store all bookmarks associated with their TeamSpeak3
        application. It provides a menu to load, add, display and save their bookmarks.
        Throughout the code there are different variables used and the users input is
        stored allowing display or saving of inputs."""

    # This code is implemented from the backend and collects the list "bookmarks" so it can be used
    # with the menu options and variables below.
    bookmarks = TeamSpeak3_backend.init()

    # This section is provided to the user as soon as the program has been ran it takes
    # into account that the user has loaded the program and has chosen to select the
    # bookmarks menu as they want to add or view bookmarks.
    # This was the most appropriate as there wasn't any need to choose to go to the
    # bookmark section from a main menu.
    sys.stdout.write("LOADING PROGRAM.......\n")
    sys.stdout.write("WELCOME TO TEAMSPEAK3!\n")
    sys.stdout.write("LOADING...............\n")
    sys.stdout.write("Teamspeak3 has now loaded.\n")
    sys.stdout.write("You have chosen to go to the bookmark menu!\n")
    sys.stdout.write("LOADING BOOKMARK MENU.....\n")

    # This menu is provided to the user and was the most appropriate name to be used.
    # The menu options could have been arranged in any order when being created
    # but this will suffice.
    menu = "\n"
    menu += "~~~~~~~~~~~~~~~~~~~~~~~~\n"
    menu += "TeamSpeak3 Bookmark Menu\n"
    menu += "~~~~~~~~~~~~~~~~~~~~~~~~\n"
    menu += "[L]oad Bookmarks\n"
    menu += "[A]dd Bookmark\n"
    menu += "[D]isplay Bookmarks\n"
    menu += "[S]ave Bookmarks\n"
    menu += "[E][X]it\n"
    menu += "Enter Option: "

    sys.stdout.write(menu)
    option = sys.stdin.readline().strip().lower()

    # This option allows the user to exit the program if needed.
    # The option "e" and "x" were the most appropriate for this option
    # as they are most commonly used for exiting a program menu. The alternative
    # that could of been used here are "e" and "Exit".
    while option != "e" and option != "x":
        sys.stdout.write("\n")

        # This option allows the user to load a csv or txt file that has already been created at
        # an earlier time. The option "l" was best suit for this although the alternative
        # could have been "load" but "l" was most appropriate. It also asks the user for the filename
        # which then a function from the backend will import the file entered. If the incorrect format has been
        # entered it will boot the user back into the main menu.
        if option == "l":
            sys.stdout.write("You have selected to load bookmarks from file...\n")
            try:
                filename = get_str("Enter filename:")
                TeamSpeak3_backend.load_bookmarks(bookmarks, filename)
            except:
                sys.stdout.write("Invalid Filename... Going back to Main Menu...")
        # This option allows the user to add a bookmark to the program and this
        # option can be selected multiple times to add multiple bookmarks.
        # The option "a" was most appropriate for this option although alternatively
        # the word "add" could have been used. The variables that have been assigned
        # were the most appropriate for this program and don't need any other justification.
        # The while loop is used for bookmark_number as the user must input and integer and
        # if the integer isn't 0 or above the program will ask the user to input the information
        # again until the user inputs the correct format. After the bookmark data has been
        # input a message will display to the user advising that the bookmark has been added.
        elif option == "a":
            sys.stdout.write("You have selected to add a bookmark...\n")
            bookmark_name = get_str("Enter bookmark name: ")
            bookmark_nickname = get_str("Enter nickname: ")
            bookmark_address = get_str("Enter server address: ")
            bookmark_password = get_str("Enter bookmark password (if required): ")
            bookmark_channel = get_str("Enter bookmark default channel (if required): ")
            bookmark_channel_password = get_str("Enter bookmark default channel password (if required): ")

            input_correct = False
            while input_correct == False:
                bookmark_number = get_str("Enter bookmark number: ")
                try:
                    number = int(bookmark_number)
                    input_correct = True
                except:
                    number = 0
                    sys.stdout.write("Invalid Number!\n")

            TeamSpeak3_backend.add_bookmark(bookmarks, bookmark_name, bookmark_nickname,
                                            bookmark_address, bookmark_password, bookmark_channel,
                                            bookmark_channel_password, number)

            sys.stdout.write("\n")
            sys.stdout.write("Adding bookmark...\n\n")
            sys.stdout.write("Your bookmark has successfully been added!\n")

        # This option displays the loaded information or the added information
        # back to the user. The data is collected from the backend and input
        # into the front end. The option "d" was most appropriate for this section
        # although the option "display" could of been alternately used. The display back
        # to the user could have been formatted better but I was unsure of how to do this.
        elif option == "d":
            sys.stdout.write("Displaying bookmarks...\n\n")
            overview = TeamSpeak3_backend.get_overview(bookmarks)
            sys.stdout.write("Name\tNickname\tAddress\tPassword\tChannel\tPassword\tNumber\n")
            sys.stdout.write(overview)

        # This option allows the user to save a csv or txt file from the information that
        # was added during the program. The option "s" was best suit for this although the alternative
        # could have been "save" but "s" was most appropriate.
        elif option == "s":
            sys.stdout.write("You have selected to save bookmarks to a file...\n")
            filename = get_str("Enter filename: ")
            TeamSpeak3_backend.save_bookmarks(bookmarks, filename)

        # This statement is displayed back to the user if the user did not put in the
        # correct input at the menu entry. It will then display the menu back to the user
        # and the user must choose a correct option.
        else:
            sys.stdout.write("Invalid menu option!\n\n")

        sys.stdout.write(menu)
        option = sys.stdin.readline().strip().lower()
    # This is displayed to the user when they have chosen to close the program.
    sys.stdout.write("Program closing...\n")


main()
