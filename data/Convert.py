'''Authors: Anthony , Jacky , Bwalya 
    Date: 2025-28-04'
    Description: l read your dataset's file and write one CSV file for each of the tables in your database design. 
    If you have designed a table named animals, for example, the corresponding CSV file should be named animals.csv,
    and should have the same columns as the table. 
    
    run the script as follows:
    python3 convert.py <accumulated_csv_file>
    The script will create the following CSV files:
    animals.csv
    continents.csv
    countries.csv
    populationTrend.csv
    populationStatus.csv
    animals_continents.csv
    animals_countries.csv
    animals_concern.csv
    '''


import csv
import sys

def main(input_filename):
    animals = [] # List to store animal data
    AnimalDict= {} # Dictionary to store unique animals (still testing something with table linking)
    PlacesDict={} # Dictionary to store unique continents
    CountriesDict={} # Dictionary to store unique countries
    populationTrendDict={} # Dictionary to store unique population trends
    populationStatusDict={} # Dictionary to store unique population status
    LinkTable=[]# List to store linking table data

    with open(input_filename) as f:
        reader = csv.reader(f)
        for csv_row in reader:
            
            AnimalName = csv_row[0]  # Animal name
            Species = csv_row[1]  # Species name
            LifeSpan = csv_row[2] # Life span
            continents = csv_row[3] # Continent
            countries=csv_row[4] # Country
            PopulationTrend = csv_row[5] # Population trend
            PopulationStatus = csv_row[6] # Population status


            name_key = f'{AnimalName}+{Species}+{LifeSpan}' 

           
            if name_key not in AnimalDict: 
                animal_id = len(animals) +1    
                AnimalDict[name_key] = animal_id

            ## Append animal data to the list
            animals.append((animal_id, AnimalName, Species, LifeSpan, continents,  countries, PopulationTrend, PopulationStatus)) # Append animal data to the list
            
            
            if continents not in PlacesDict: # Check if the continent is unique
                place_id = len(PlacesDict) + 1 # Unique ID for the continent
                PlacesDict[continents] = place_id # Add continent to the dictionary

            if countries not in CountriesDict: # Check if the country is unique
                country_id = len(CountriesDict) + 1 # Unique ID for the country
                CountriesDict[countries] = country_id # Add country to the dictionary

            if PopulationTrend not in populationTrendDict: # Check if the population trend is unique
                population_id = len(populationTrendDict) + 1 # Unique ID for the population trend
                populationTrendDict[PopulationTrend] = population_id # Add population trend to the dictionary

            if PopulationStatus not in populationStatusDict: # Check if the population status is unique
                population_id = len(populationStatusDict) + 1 # Unique ID for the population status
                populationStatusDict[PopulationStatus] = population_id # Add population status to the dictionary

            # Append the animal ID and place ID to the linking table
            LinkTable.append((AnimalDict[name_key], PlacesDict[continents], CountriesDict[countries], populationTrendDict[PopulationTrend], populationStatusDict[PopulationStatus])) # Append the animal ID and place ID to the linking table

    

    with open('animals.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for animal in animals:
            writer.writerow([animal[0], animal[1], animal[2], animal[3]])  # Write animal data to CSV file

    # Write continents/Place table
    with open('Continents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for place, place_id in PlacesDict.items():
            writer.writerow([place_id, place]) # Write continent data to CSV file
            
    with open ('countries.csv', 'w') as f:
        writer = csv.writer(f)
        for country, country_id in CountriesDict.items():
            writer.writerow([country_id, country]) # Write country data to CSV file
        
    with open ('populationtTrend.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for trend, trend_id in populationTrendDict.items():
            writer.writerow([trend_id, trend]) # Write population trend data to CSV file

    with open ('populationStatus.csv', 'w') as f:
        writer = csv.writer(f)
        for status, status_id in populationStatusDict.items():
            writer.writerow([status_id, status]) # Write population status data to CSV file
            
  
    with open('animals_continents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for link in LinkTable:
            writer.writerow([link[0], link[1]]) # Write animal ID and continent ID to CSV file

    with open ('animals_countries.csv', 'w') as f: 
        writer = csv.writer(f)
        for link in LinkTable:
            writer.writerow([link[0], link[2]])      # Write animal ID and country ID to CSV file 

    with open ('animals_concern.csv', 'w') as f:
        writer = csv.writer(f)
        for link in LinkTable:
            writer.writerow([link[0], link[3], link[4]])  # Write animal ID and population trend ID to CSV file

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} original_csv_file', file=sys.stderr)
    exit()

main(sys.argv[1])