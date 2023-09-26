import sys
PatientDoctor = {'Jack'.ljust(15): 'Dr Neil'.rjust(20), 'Ash'.ljust(15): 'Dr Radford'.rjust(20), 'Gemma'.ljust(15): "Dr O'Connor".rjust(20), 'Daniel'.ljust(15): 'Dr Stevens'.rjust(20)}
def display_queue():
    for x, y in PatientDoctor.items():
        print(f'{x:10} will see {y}')
def suprise():
    sys.stdout.write("I invented a new word can you guess what it is?\n")
    sys.stdout.write("Please enter your guess: ")
    sys.stdin.readline().strip()
    sys.stdout.write("Good guess, but it's Plagarism :P\n")
    
