def init():
    """This function is used to initialise the front end menu."""

    # The list name bookmarks was best used for this program as the program
    # is related to bookmarks. This list is used to store the added inputs from the user
    # on the front end and is stored in this list. The list is empty because we want to program to start fresh
    # as not everyone's bookmarks are the same. When the information is saved into the list the list gets
    # returned.
    bookmarks = []
    return bookmarks


def add_bookmark(bookmarks, bookmark_name, bookmark_nickname, bookmark_address, bookmark_password,
                 bookmark_channel, bookmark_channel_password, number):
    """This function is used to collect all the information that has been input from the user on the front end
        and adds them to their correct variables."""

    # This code adds the inputs from the user on the front end on the variables used and it allows the user
    # to continuously add more and more bookmarks if required.
    bookmarks.append([bookmark_name, bookmark_nickname, bookmark_address, bookmark_password, bookmark_channel,
                      bookmark_channel_password, number])


def get_overview(bookmarks):
    """This function gets the overview from the front end of information input into the program."""

    # This code below collects the information stored from the variables that were input in the frontend
    # of the program and when called it displays the information stored in the variables back to the user
    # as I skipped the headings in the loading of the bookmark it will show the headings along with the
    # user input information when called.
    overview = ""
    i = 0
    while i < len(bookmarks):
        overview += bookmarks[i][0] + "\t"
        overview += (bookmarks[i][1]) + "\t"
        overview += (bookmarks[i][2]) + "\t"
        overview += (bookmarks[i][3]) + "\t"
        overview += (bookmarks[i][4]) + "\t"
        overview += (bookmarks[i][5]) + "\t"
        overview += str(bookmarks[i][6]) + "\n"
        i += 1
    return overview


def load_bookmarks(bookmarks, filename):
    """This function is used to load a file either csv or txt that is already stored
        on the users computer."""

    # The code below imports the saved information on a CSV or txt file that the user already
    # has on their computer, it will skip the first line which is usually the headings and then
    # it will import that data and when the user decides to display it in the front end the stored
    # information will appear. Once the file has been read it will close the file so it is not left open
    # and use up resources.
    file_obj = open(filename, "r")
    line = file_obj.readline()

    line = file_obj.readline()
    while line != "":
        fields = line.strip().split(",")
        bookmarks.append(fields)
        line = file_obj.readline()

    file_obj.close()


def save_bookmarks(bookmarks, filename):
    """This function is used to save a file either csv or txt to the users computer"""

    # The code below takes into account all the information that the user has input into the program
    # it is then written into a CSV or txt file and saved on the users computer. When the data is saved
    # the headings of each variable will appear on the first line followed by the input of the user underneath.
    # It replaces the /t with , so that it looks a lot nice and more practical. Once the file has been saved
    # the file will close and doing so will save resources.
    file_obj = open(filename, "w")
    overview = get_overview(bookmarks)
    file_obj.write("Name, Nickname, Address, Password, Channel, Password, Number\n")
    file_obj.write(overview.replace("\t", ","))
    file_obj.close()
