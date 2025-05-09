CREATE TABLE animals (
	id integer NOT NULL,
	animal_name text, 
	animal_species text, 
	animal_lifespan text
);

CREATE TABLE continents (
        id integer NOT NULL, 
        continent_name text
);

CREATE TABLE countries (
        id integer NOT NULL,
        country_name text
); 

CREATE TABLE populationtTrend (
        id integer NOT NULL,
        trend text
);

CREATE TABLE populationStatus (
        id integer NOT NULL,
        status text
);

CREATE TABLE animals_continents (
        animal_id integer,
	continent_id integer
);

CREATE TABLE animals_countries (
        animal_id integer,
        country_id integer
);

CREATE TABLE animals_concern (
        animal_id integer,
        trend_id integer,
	status_id integer
);


