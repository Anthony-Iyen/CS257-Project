SELECT animals.animal_name 
FROM animals 
WHERE animals.animal_species LIKE 'A%';

SELECT animals.animal_name, countries.country_name 
FROM animals, countries, animals_countries
WHERE animals.id = animals_countries.animal_id                                                                    
AND countries.id = animals_countries.country_id;

SELECT animals.animal_name, continents.continent_name 
FROM animals, continents, animals_continents
WHERE animals.id = animals_continents.animal_id                                                                    
AND continents.id = animals_continents.continent_id;

SELECT animals.animal_name, animals.animal_species
FROM animals, populationttrend, animals_concern
WHERE animals.id = animals_concern.animal_id
AND populationttrend.id = animals_concern.trend_id
AND populationttrend.id = 1;
