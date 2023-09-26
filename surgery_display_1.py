patients = ["Jack".ljust(15), "Ash".ljust(15), "Gemma".ljust(15), "Daniel".ljust(15)]
doctors = ["Dr Neil".rjust(20), "Dr Radford".rjust(20), "Dr O'Connor".rjust(20), "Dr Stevens".rjust(20)]
for x, y in zip(patients, doctors):
    print('{0} will see {1}.' .format(x, y))
