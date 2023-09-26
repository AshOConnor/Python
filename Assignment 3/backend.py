class BackEnd:

    def __init__(self, bookmarks_filename):
        """This function is used to initialise the front end menu."""

        # The list name bookmarks was best used for this program as the program
        # is related to bookmarks. This list is used to store the added inputs from the user
        # on the front end and is stored in this list. The list is empty because we want to program to start fresh
        # as not everyone's bookmarks are the same. When the information is saved into the list the list gets
        # returned.
        self.__bookmarks = []
        self.__bookmarks_filename = bookmarks_filename

        # This code block uses the try and except method. When the program is loaded it will try and load
        # a csv file that is stored on the users computer. If the user does not have this file on their computer
        # it will raise the FileNotFoundError but it will also create the file for the user at the same time.
        # The file is then saved to the users computer. If a file has been loaded from the users computer
        # it will import all saved information if there is any on there. It will skip over the headings
        # so that the user doesn't get confused with how many bookmarks are stored.
        file = None
        try:
            file = open(self.__bookmarks_filename)
        except:
            self.save_bookmarks()
            raise FileNotFoundError(
                "File not found. A bookmark data.csv file has been created. Please restart the program.")

        if file != None:
            line = file.readline()
            line = file.readline()
            while line != "":
                fields = line.strip().split(",")
                self.add_bookmark(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6])
                line = file.readline()
            file.close()

    def add_bookmark(self, bookmark_name, bookmark_nickname, bookmark_address, bookmark_password,
                     bookmark_channel, bookmark_channel_password, number):
        """This function is used to collect all the information that has been input from the user on the front end
            and adds them to their correct variables."""

        # This code adds the inputs from the user on the front end on the variables used and it allows the user
        # to continuously add more and more bookmarks if required.
        self.__bookmarks.append(
            Bookmark(bookmark_name, bookmark_nickname, bookmark_address, bookmark_password, bookmark_channel,
                     bookmark_channel_password, number))

    def remove_bookmark(self, bookmark_name, bookmark_nickname, bookmark_address, bookmark_password, bookmark_channel,
                        bookmark_channel_password, number):
        """This function allows the user to remove bookmarks from the program."""

        # This code block gathers the stored bookmark information from the list
        # it then uses a while loop to gather the correct information that is stored.
        # When the user has input the correct names of stored information it
        # will then remove the bookmark from the program.
        len_bookmarks = self.bookmark_amount()

        i = 0
        while i < len_bookmarks and self.__bookmarks[i].matches(bookmark_name, bookmark_nickname, bookmark_address,
                                                                bookmark_password, bookmark_channel,
                                                                bookmark_channel_password, number) == False:
            i += 1

        if i < len_bookmarks:
            del self.__bookmarks[i]

    def bookmark_amount(self):
        """This function counts all bookmarks that have been loaded from a file and
            uses this information to be displayed in the frontend."""

        # This code counts the length of bookmarks and is displayed in the front end
        # when the code is called.
        return len(self.__bookmarks)

    def __str__(self):
        """This function gathers all the strings that have been input into the program"""

        # This code block is used to count how many bookmarks have been stored in
        # the program and returns the overview of the amount. The variable "overview" could of
        # alternatively been called "summary".
        len_bookmarks = self.bookmark_amount()
        overview = ""
        i = 0
        while i < len_bookmarks:
            overview += self.__bookmarks[i].__str__() + "\n"
            i += 1
        return overview

    def save_bookmarks(self):
        """This function is used to save a csv file to the users computer"""

        # The code below takes into account all the information that the user has input into the program
        # it is then written into a CSV and saved on the users computer. When the data is saved
        # the headings of each variable will appear on the first line followed by the input of the user underneath.
        # Once the file has been saved the file will close and doing so will save resources.
        file_obj = open(self.__bookmarks_filename, "w")
        file_obj.write("Name, Nickname, Address, Password, Channel, Password, Number\n")
        file_obj.write(self.__str__())
        file_obj.close()


class Bookmark:

    def __init__(self, bookmark_name, bookmark_nickname, bookmark_address, bookmark_password, bookmark_channel,
                 bookmark_channel_password, number):
        """This init function stores all the inputs from the front end and adds them to the variables"""

        # This code block is the list of all variables in the program and the self. statement
        # is used to initiate them in the front end. The variable names can be refered to in the front end.
        self.__bookmark_name = bookmark_name
        self.__bookmark_nickname = bookmark_nickname
        self.__bookmark_address = bookmark_address
        self.__bookmark_password = bookmark_password
        self.__bookmark_channel = bookmark_channel
        self.__bookmark_channel_password = bookmark_channel_password
        self.__number = number

    # Accessor method for the bookmark_name attribute
    @property
    def bookmark_name(self):
        """This function is an accessor method for this variable."""

        return self.__bookmark_name

    # Accessor method for the bookmark_nickname attribute
    @property
    def bookmark_nickname(self):
        """This function is an accessor method for this variable."""

        return self.__bookmark_nickname

    # Accessor method for the bookmark_address attribute
    @property
    def bookmark_address(self):
        """This function is an accessor method for this variable."""

        return self.__bookmark_address

    # Accessor method for the bookmark_password attribute
    @property
    def bookmark_password(self):
        """This function is an accessor method for this variable."""

        return self.__bookmark_password

    # Mutator method for the bookmark_password attribute
    @bookmark_password.setter
    def bookmark_password(self, bookmark_password):
        """This function is an mutator method for this variable."""

        self.__bookmark_password = bookmark_password

    # Accessor method for the bookmark_channel attribute
    @property
    def bookmark_channel(self):
        """This function is an accessor method for this variable."""

        return self.__bookmark_channel

    # Accessor method for the bookmark_channel_password attribute
    @property
    def bookmark_channel_password(self):
        """This function is an accessor method for this variable."""

        return self.__bookmark_channel_password

    # Mutator method for the bookmark_channel_password attribute
    @bookmark_channel_password.setter
    def bookmark_channel_password(self, bookmark_channel_password):
        """This function is an mutator method for this variable."""

        self.__bookmark_channel_password = bookmark_channel_password

    # Accessor method for the number attribute
    @property
    def number(self):
        """This function is an accessor method for this variable."""

        return self.__number

    def matches(self, bookmark_name, bookmark_nickname, bookmark_address, bookmark_password, bookmark_channel,
                bookmark_channel_password, number):
        """This function is used in collaboration to the remove passwords function."""

        # This code below is used in the remove password function, it makes sure
        # that the information that has been input matches the information stored
        # when removing the password.
        outcome = False
        if self.__bookmark_name == bookmark_name and self.__bookmark_nickname == bookmark_nickname \
                and self.__bookmark_address == bookmark_address and self.__bookmark_password == bookmark_password \
                and self.__bookmark_channel == bookmark_channel \
                and self.__bookmark_channel_password == bookmark_channel_password and str(self.__number == number):
            outcome = True
        return outcome

    def __str__(self):
        """This function gathers all the strings that have been input into the program"""

        # This code block is used to count how many passwords have been stored in
        # the program and returns the overview of the amount. The variable "overview" could of
        # alternatively been called "summary".
        overview = self.__bookmark_name + ","
        overview += self.__bookmark_nickname + ","
        overview += self.__bookmark_address + ","
        overview += self.__bookmark_password + ","
        overview += self.__bookmark_channel + ","
        overview += self.__bookmark_channel_password + ","
        overview += str(self.__number)
        return overview
