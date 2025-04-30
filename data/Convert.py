'''Authors: Anthony , Jacky , Bwalya 
    Date: 2023-10-01'
    Description: l read your dataset's file and write one CSV file for each of the tables in your database design. 
    If you have designed a table named animals, for example, the corresponding CSV file should be named animals.csv,
    and should have the same columns as the table. '''


import csv
import sys

def main(input_filename):
    animals = [] # List to store animal data
    AnimalDict= {} # Dictionary to store unique animals (still testing something with table linking)

    with open(input_filename) as f:
        reader = csv.reader(f)
        for csv_row in reader:
           AnimalName = csv_row[0]  # Animal name
           Species = csv_row[1] 
           LifeSpan = csv_row[2] 
           Place = csv_row[3]
           PopulationTrend = csv_row[4]
           PopulationStatus = csv_row[5]
           name_key = f'{AnimalName}+{Species}+{LifeSpan}' #( still testing something with table linking)

           
           if name_key not in AnimalDict: # (Check if the animal is unique still testing table linking)
            animal_id = len(animals) # Unique ID for the animal           
            animals.append((animal_id, AnimalName, Species, LifeSpan, Place, PopulationTrend, PopulationStatus)) # Append animal data to the list
            
            # AnimalDict[name_key] = True  (dont worry about this still testing stuff)


    with open('animals.csv', 'w') as f:
            writer = csv.writer(f)
            for animal in animals:
                row = (animal[0], animal[1], animal[2], animal[3])  # Animal ID, Name, Species, LifeSpan
                writer.writerow(row) 

    # with open('continents.csv', 'w') as f:

    # with open ('countries.csv', 'w') as f:

    with open ('populationtTrend.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for animal in animals:
            row =  animal[0], [animal[5]]
            writer.writerow(row)
    

    with open ('populationStatus.csv', 'w') as f:
        writer = csv.writer(f)
        for animal in animals:
            row =  animal[0] ,[animal[6]] # Animals ID and PopulationStatus
            writer.writerow(row)


    # with open ('continents_countries.csv', 'w') as f:

    # with open ('animals_continents.csv', 'w') as f:

    # with open ('animals_countries.csv', 'w') as f:

    with open ('animals_concern.csv', 'w') as f:
        writer = csv.writer(f)
        for animal in animals:
            row =  animal[0] ,[animal[5]], animal[6] # Animals ID and PopulationTrend, and PopulationStatus
            writer.writerow(row)



         

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} original_csv_file', file=sys.stderr)
    exit()

main(sys.argv[1])