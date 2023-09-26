class PasswordVault:
    """This class contains all of the backend code for the passwordvaultUI.
        and is the main code to store information and run the program."""

    def __init__(self, password_filename):
        """The __init__ function is responsible for initialising the front end data
            and back end data."""

        # This section stores all the passwords that have been added to the program
        # and also opens the password file from the computer if there is one. The while loop
        # loads the file and imports all the information in the file. If there is no file
        # to begin with there will be no file opened.
        self.__passwords = []
        self.__password_filename = password_filename
        fp = None
        try:
            fp = open(self.password_filename)
        except:
            self.save_passwords()

        if fp != None:
            line = fp.readline()
            line = fp.readline()
            while line != "":
                fields = line.strip().split(",")
                self.add_password(fields[0], fields[1], fields[2])
                line = fp.readline()
            fp.close()

    # Accessor added so the variable cannot be altered.
    @property
    def passwords(self):
        return self.__passwords

    # Accessor added so the variable cannot be altered.
    @property
    def password_filename(self):
        return self.__password_filename

    def get_password_amount(self):
        """This function counts all passwords that have been loaded from a file and
            uses this information to be displayed in the frontend."""

        # This code counts the length of passwords and is displayed in the front end
        # when the code is called.
        return len(self.__passwords)

    def add_password(self, website, email, password):
        """This function allows the user to add passwords to the program."""

        # This code gathers the information from the user that has been input when adding
        # a password and it then appends the information on a list. The try and except method
        # is used to find out the information in regards to the raised errors in the password class.
        password_pass = False
        try:
            self.__passwords.append(Password(website, email, password))
            password_pass = True
        except:
            password_pass = False

    def get_password(self, website, email, password):
        """This function collects the length value of the passwords list"""

        # This code block gathers the stored password information from the list
        # it then uses a while loop to gather the correct information that is stored.
        # When the user has input the correct names of stored information it
        # will then find the password from the program. This method is used for change_password function.
        found_password = None
        len_passwords = self.get_password_amount()
        i = 0
        while i < len_passwords and self.__passwords[i].equal_to(website, email, password) == False:
            i += 1

        if i < len_passwords:
            found_password = self.__passwords[i]

        return found_password

    def change_password(self, website, email, password, new_password):
        """This function is used to change a password that is stored in the program."""

        # This code block is used to change a password that is stored in the program.
        # It uses the "if" statement to gather information that has been input
        # and if the information adds up, it'll change the password. If not the password will not change.
        successful = False
        password_change = self.get_password(website, email, password)

        if password_change != None:
            password_change.password = new_password
            successful = True
        else:
            successful = False

        return successful

    def remove_password(self, website, email, password):
        """This function allows the user to remove passwords from the program."""

        # This code block gathers the stored password information from the list
        # it then uses a while loop to gather the correct information that is stored.
        # When the user has input the correct names of stored information it
        # will then remove the password from the program.
        len_passwords = self.get_password_amount()

        i = 0
        while i < len_passwords and self.__passwords[i].equal_to(website, email, password) == False:
            i += 1

        if i < len_passwords:
            del self.__passwords[i]

    def save_passwords(self):
        """This function is used to save passwords to a file."""

        # This code opens the file passwords.csv and writes the information
        # the has been input into the program along with the relevant headings.
        # Once it has finished writing the information into the file it will
        # then close the file.
        fp = open(self.password_filename, "w")
        fp.write("Website, Email, Password\n")
        fp.write(self.__str__())
        fp.close()

    def __str__(self):
        """This function gathers all the strings that have been input into the program"""

        # This code block is used to count how many passwords have been stored in
        # the program and returns the overview of the amount. The variable "overview" could of
        # alternatively been called "summary".
        len_passwords = self.get_password_amount()
        overview = ""
        i = 0
        while i < len_passwords:
            overview += self.__passwords[i].__str__() + "\n"
            i += 1
        return overview


class Password:
    """This class contains all the information that is needed for the
        password list."""

    def __init__(self, website, email, password):
        """This function initialises the password class to the main program"""

        # This code section stores all strings that have been input from the user
        # in the front end of the program. The "if" statements below are incorporated in the
        # front end when the input information doesn't have enough letters/numbers.
        # The try and except method has been added to the add_password function.
        self.__website = None
        if len(website) > 5:
            self.__website = website
        else:
            raise ValueError("Website name must be 5 letters long or more.")

        self.__email = None
        if len(email) > 10:
            self.__email = email
        else:
            raise ValueError("Email must be 10 letters long or more.")

        self.__password = None
        if len(password) > 3:
            self.__password = password
        else:
            raise ValueError("Password must be 3 letters long or more.")

    # Accessor added so the variable cannot be altered.
    @property
    def website(self):
        return self.__website

    # Accessor added so the variable cannot be altered.
    @property
    def email(self):
        return self.__email

    # Accessor added so the variable cannot be altered.
    @property
    def password(self):
        return self.__password

    # Mutator added allowing the password to be updated.
    @password.setter
    def password(self, password):
        self.__password = password

    def equal_to(self, website, email, password):
        """This function is used in collaboration to the remove passwords function."""

        # This code below is used in the remove password function, it makes sure
        # that the information that has been input matches the information stored
        # when removing the password.
        outcome = False
        if self.__website == website and self.__email == email and self.__password == password:
            outcome = True
        return outcome

    def __str__(self):
        """This function gathers all the strings that have been input into the program"""

        # This code block is used to count how many passwords have been stored in
        # the program and returns the overview of the amount. The variable "overview" could of
        # alternatively been called "summary".
        overview = self.__website + ","
        overview += self.__email + ","
        overview += self.__password
        return overview
