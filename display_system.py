import sys

def display_system_v2():
    try:
        import surgery_disaplay1
        sys.stdout.write("We have the following patients in queue Monday, they are seeing the following doctors.\n\n")
        sys.stdout.write("\n")
        sys.stdout.write("Thank you for your patience.")

    except ModuleNotFoundError:
        from surgery_display_2 import display_queue
        sys.stdout.write("We have the following patients in queue Tuesday, they are seeing the following doctors.\n\n")
        display_queue()
        sys.stdout.write("\n")
        sys.stdout.write("Thank you for your patience.")

    finally:
        sys.stdout.write("\n\n")
        sys.stdout.write("Have a nice day!")

display_system_v2()


