# penguins.py
# This program performs data science on a data set of real-world penguin
# measurements collected by biologists on different islands off the coast
# of Antarctica. The goal of the program is to compare the bill lengths and 
# body masses of penguins of different species to see how the three species 
# differ from one another.

# This function reads in all of the penguin data and returns a list of
# penguins, where each penguin is represented as a list of measurements
def read_data():
    # read in the contents of the file
    file = open("penguins_data.csv", "r")
    lines = file.readlines()
    file.close()

    # create a new list to store the penguins
    penguins = list()

    # convert the lines in the file into penguins
    for line in lines[1:]:
        # remove the newline character from the end
        line = line.strip()

        # turn the line into a list of strings
        line = line.split(",")

        # create a new list for this penguin
        penguin = list()

        # save the species and island of the penguin
        penguin.append(line[0]) #the species string
        penguin.append(line[1]) #the island string

        # convert the measurements to floats and save them in the penguin
        penguin.append(float(line[2])) #the bill length
        penguin.append(float(line[3])) #the bill depth
        penguin.append(float(line[4])) #the flipper length
        penguin.append(float(line[5])) #the body mass

        # save this penguin to our list of penguins
        penguins.append(penguin)

    return penguins

def find_species(penguins, species):
    filtered = []
    for penguin in penguins:
        if species == penguin[0]:
            filtered.append(penguin)
    return filtered
    
def find_measurents(filtered, index):
    measurements = []
    for penguin in filtered:
        measurements.append(penguin[index])
    return measurements



def type_measurement(measure_type):
    index = 0
    if measure_type == 1:
        index = 2
    if measure_type == 2:
        index =  3
    if measure_type == 3:
        index =  4
    if measure_type == 4:
        index =  5

    return index

def find_average(measurement):
    total = 0
    length = len(measurement)
    for number in measurement:
        total = total + number
    average = total/length
    return round(average,4)

def find_max(measurement):
    bigest = 0
    for num in measurement:
        if num > bigest:
            bigest = num
    return round(bigest,1)

def find_min(measurement,bigest):

    for num in measurement:
        if num < bigest:
            bigest = num
            lowest = bigest
    return round(lowest,1)
def name_measurement(index):
    if index == 2:
        return "Bill length"
    if index ==3 :
        return "Bill depth"
    if index == 4:
        return "Flipper length"
    if index == 5:
        return "Body mass"





def main():
    print("Welcome to the world of Data Science")
    print("""
          Adelie
          Chinstrap
          Gentoo

""")
    
    e = 1
    while e != 0:
        try:
            species = input("Name of Species: ")
            if species.upper() != "ADELIE" and species.upper() != "GENTOO" and species.upper() != "CHINSTRAP":
                0/0
    
        except Exception:
            print("Invalid Option! Try again!")
        else:
            e = 0
    e = 1
    while e != 0:
        try:
         measure_type = int(input("""
        What type of measurement do you want to see?
        1. Bill length
        2. Bill depth
        3. Flipper length
        4. Body mass
        """))
         if measure_type != 1 and measure_type != 2 and measure_type != 3 and measure_type != 4:
             0/0
        except Exception:
            print("Invalid Option! Try again!")
        else:
            e = 0


  
 
    penguins = read_data()
    filtered = find_species(penguins,species )
    index = type_measurement(measure_type)
    namemeasurement= name_measurement(index)

    measurement = (find_measurents(filtered, index))
    average = find_average(measurement)
    bigest = find_max(measurement)
    lowest = find_min(measurement,bigest)

    
    data = { 'Species': species, 'Measurement':namemeasurement, 'Min':lowest,}
    print("Species")
    print(f"""  
    Species: {species}    
    Measurement type: {namemeasurement}      
    Min: {lowest}    
    Average: {average}    
    Max: {bigest}
   """) 
    

    


    
main()
