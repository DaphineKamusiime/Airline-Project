from cs50 import SQL 
import csv 

open("Airline.db","w").close()

db=SQL("sqlite:///Airline.db")

db.execute("CREATE TABLE airline(ID INTEGER PRIMARY KEY,Airline_code TEXT, Airline_name TEXT, Number_of_planes INTEGER)")
db.execute("CREATE TABLE Route(Route_id INTEGER,Destinations INTEGER)")
db.execute("CREATE TABLE Airport(Airport_id INTEGER, Airport_names TEXT, city TEXT, country TEXT ,PRIMARY KEY(Airport_id))")
db.execute("CREATE TABLE Aeroplane(ID INTEGER PRIMARY KEY,Airline_code TEXT,capacity INT, Route_id INTEGER, number_of_flights INTEGER,FOREIGN KEY(ID) REFERENCES airline(ID))")
with open("Airline csv.csv","r") as file:
    reader=csv.DictReader(file)
    
    for row in reader:
        airlines=row["Airline_names"]
        airline_code=row["Airline_code"]
        number_of_planes=row["Number_of_planes"]
        route=row["Route_id"]
        destinations=row["Destinations"]
        airline_code=row["Airline_code"]
        airport_name=row["Airport_name"]
        country=row["Country"]
        city_name=row["city"]
        capacity=row["Average_capacity"]
        number_of_flights=row["Number of flights"]
        
        db.execute("INSERT INTO airline(Airline_code,Airline_name,Number_of_planes) VALUES(?,?,?)",airline_code,airlines,number_of_planes)
        db.execute("INSERT INTO Route(Route_id,Destinations) VALUES(?,?)",route,destinations)
        db.execute("INSERT INTO Airport(Airport_names,city, Country) VALUES(?,?,?)",airport_name,city_name,country)
        db.execute("INSERT INTO Aeroplane(Airline_code,Number_of_flights, Route_id,Capacity) VALUES(?,?,?,?)",airline_code,number_of_flights,route,capacity)
        
