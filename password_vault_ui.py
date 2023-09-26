import sys
import password_vault_backend


class PasswordVaultUI:
    """This class has all information of code that will be displayed to the user
        that is running the program."""

    def get_str(prompt):
        """This function collects the inputs from the user and stores them as a string."""

        # The while loop for this code block makes sure that there is no question left
        # unanswered. If the user hits enter without any information they will be asked to enter it
        # again. The variable added_str was most appropriate in this case but could of been called
        # an alternative name such as "input_str".
        sys.stdout.write(prompt)
        added_str = sys.stdin.readline().strip()
        while added_str == "":
            sys.stdout.write("Incorrect input!")
            added_str = sys.stdin.readline().strip()

        return added_str

    def __init__(self):
        """The __init__ function is the main function for all of the code
         it initialises all the attributes of classes and is the constructor
         of this program."""

        # This code block below introduces the program to the user and also loads a file
        # that may or may not be already stored on the user computer. It then will display
        # if there are any passwords in the file and indicate that back to the user.
        self.__backend = password_vault_backend.PasswordVault("passwords.csv")
        sys.stdout.write("Attempting to load a file...\n\n")
        sys.stdout.write("If file found password count will not include headings...\n\n")
        sys.stdout.write(str(self.__backend.get_password_amount()) + " passwords loaded...\n\n")
        sys.stdout.write("------------------------------\n")
        sys.stdout.write("----LOADING PASSWORD VAULT----\n")
        sys.stdout.write("------------------------------\n")
        sys.stdout.write("\n\n")
        # This while loop asks the user to enter a input to continue. The input
        # must be an integer and can be any number. The variable m_password/master password
        # was most appropriate for this section as it relates to a master password
        # to access the vault. If the user does not enter the correct information
        # the program will continue asking until the correct information has been input.
        sys.stdout.write("Please enter the master password to continue..\n")
        input_correct = False
        while not input_correct:
            sys.stdout.write("Enter master password: ")
            master_password = sys.stdin.readline().strip()
            try:
                m_password = int(master_password)
                input_correct = True
            except:
                m_password = ""
                sys.stdout.write("Invalid Master Password!\n")

        sys.stdout.write("\n\n")
        sys.stdout.write("------------------------------\n")
        sys.stdout.write("LOADING PASSWORD VAULT MANAGER\n")
        sys.stdout.write("------------------------------\n")
        sys.stdout.write("\n\n")

        # This menu is provided to the user and was the most appropriate name to be used.
        # The menu options could have been arranged in any order when being created
        # but this will suffice.
        menu = "\n"
        menu += "------------------------------\n"
        menu += "----PASSWORD VAULT MANAGER----\n"
        menu += "------------------------------\n"
        menu += "[A] Add Password\n"
        menu += "[E] Edit Password\n"
        menu += "[D] Display Passwords\n"
        menu += "[R] Remove Password\n"
        menu += "[S] Save File\n"
        menu += "[X] Exit\n"
        menu += "Enter option: "
        option = PasswordVaultUI.get_str(menu).lower()

        # This option allows the user to exit the program if needed.
        # The option "e" is the most appropriate for this option
        # as they it is most commonly used for exiting a program menu. The alternative
        # that could of been used here is "Exit"
        while option != "x":
            # This option allows the user to add a password. The variables used to collect this information
            # were the most appropriate as they reflect on the information that needs to be stored.
            # The variable "website" alternatively could of been called "site" and "email" could of been
            # alternatively called "username" but the chosen will suffice.
            # The option "a" was most appropriate as it indicates that we are adding a password. Alternatively
            # the option could of been called "add". The second if statement in this code block,
            # takes into account errors raised in the back end. This is to make sure the correct
            # number of letters/numbers have been added for the variables.
            if option == "a":
                sys.stdout.write("Adding a new password...\n")
                website = PasswordVaultUI.get_str("Enter website: ")
                email = PasswordVaultUI.get_str("Enter email for " + website + ": ")
                password = PasswordVaultUI.get_str("Enter password for " + email + ": ")
                self.__backend.add_password(website, email, password)

            # This option allows the user to edit a password. The variables used to collect this information
            # were the most appropriate as they reflect on the information that needs to be stored.
            # The variable "website" alternatively could of been called "site" and "email" could of been
            # alternatively called "username" but the chosen will suffice.
            # The option "e" was most appropriate as it indicates that we are editing a password. Alternatively
            # the option could of been called "edit".
            elif option == "e":
                sys.stdout.write("Edit a password...\n")
                website = PasswordVaultUI.get_str("Enter name website: ")
                email = PasswordVaultUI.get_str("Enter email for " + website + ": ")
                password = PasswordVaultUI.get_str("Enter password for " + email + ": ")
                new_password = PasswordVaultUI.get_str("Enter new password for " + email + ": ")

                # In this code block, to check if the password value exists the get_password method
                # will return a boolean value. The boolean value is referenced by placing the
                # method in an if statement; if True it will add the new password object and
                # inform the user, else it will only inform the user the password cannot be changed.
                # In addition, the change_password method runs simultaneously while referenced in
                # the if statement.
                if self.__backend.change_password(website, email, password, new_password):
                    sys.stdout.write("Password changed.\n")
                else:
                    sys.stdout.write("Could not change password. Wrong details.\n")
            # This option allows the user to display all passwords in the system.
            # The option "d" was most appropriate as it indicates that we are displaying passwords.
            # Alternatively the option could of been called "find".
            elif option == "d":
                sys.stdout.write("Displaying passwords...\n")
                sys.stdout.write(self.__backend.__str__())
            # This option allows the user to remove a password by inputting the correct information
            # from the questions asked. The option "r" was most appropriate as
            # it indicates that we are removing a password. Alternatively
            # the option could of been called "remove".
            elif option == "r":
                sys.stdout.write("Removing password...\n")
                website = PasswordVaultUI.get_str("Enter website: ")
                email = PasswordVaultUI.get_str("Enter email for " + website + ": ")
                password = PasswordVaultUI.get_str("Enter password for " + email + ": ")
                self.__backend.remove_password(website, email, password)
                sys.stdout.write("Password has been found and removed...\n")
            # This option allows the user to save the passwords that have been stored into the program.
            # The file automatically saves to a csv file called passwords.csv. This is the most efficient way
            # in this code although it could have an added feature which allows the user to name their
            # own file and file type. The option "s" was most appropriate as it indicates that we are
            # saving passwords. Alternatively this option could of been called "save".
            elif option == "s":
                sys.stdout.write("Saving passwords to file...\n")
                self.__backend.save_passwords()
                sys.stdout.write("Saved to passwords.csv\n")

            else:
                sys.stdout.write("Invalid Menu Option!\n")

            option = PasswordVaultUI.get_str(menu).lower()

        sys.stdout.write("Password Vault now closing...")


pv = PasswordVaultUI()
