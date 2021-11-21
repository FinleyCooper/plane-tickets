# Documented Design

The project will be run on a Flask App using Python.  
The Flask app will be run on Heroku using the environment created by this GitHub repository.  

## Endpoints
There will be 2 endpoints for the API  

`POST /api/<string:plane_name>/seat` - To books a seat  
`DELETE /api/<string:plane_name>/seat` - To unbook a seat  
`GET /api/<string:plane_name>/seats` - To get all seats on the plane

## Data Structures
The main data structure is the Seat class. The class will be a python dataclass and contain 5 attributes and 1 method.  
 - id_ - The id of the seat. Example: A3, B3, C9  
 - passenger_id - The unique hex value that identifies the passenger's requests  
 - passenger_information - A JSON string which contains the passenger's name, age, and if they are vegetarian, pregnant, or disabled.  
 - _class - The class of the seat, First Class, Economy.  
 - plane_name - The name of the plane of which the seat is associated with.  
 - toJSON - A method to return a JSON string of the Seat object, taking one parameter which will change if sensitive data is to be returned.  

## File Structure
Procfile, requirements.txt, and runtime.txt are used by Heroku to build the app.  
In the App folder, there is the main.py folder which contains the routes for all of the endpoints and methods. It also connected to the database.  
In the seats folder, there is seat_manager.py which contains functions to interact with the database.  
The seat.py folder contains the Seat class talked about previously.  
The seats.db folder is the database.  
Back into the App folder there is the aircraft folder which contains functions for creating an aircraft table in the database.  

## The Database
The database is a SQLite database which contains tables for each aircraft. Each table contains columns with the same attributes as the Seat object.  
A new table is initialized through the admin_manager.py function create_plane. The function takes in the name of the new aircraft, along with the length of seats down the plane, and the length of seats widthwise along the plane.  
The seat_manager folder is responsable for editing the database contents. 

### Queries
The admin_manager.py function create_plane executes the SQL command.   
`INSERT INTO {name} (id, passengerID, passengerInformation, class) VALUES {",".join(seat_values)}`  
The algorithm for creating the seat_values list is show here.  
```python
    seat_values = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    for i in range(seat_width):
        for j in range(seat_length):
            seat_values.append(f"('{alphabet[i] + str(j+1)}', NULL, NULL, 'economy')")

```
The algorithm iterates through the seat width and seat length appending new values for the id which is created by indexing the alphabet list by the current seat width and adding on the curent seat length plus one, as there is no seat A0 on an aircraft.  

The query for getting the seat by its id is  
`SELECT * FROM {plane_name} WHERE id="{seat_id}"`  
And the query is the same for getting all the seats but the WHERE condition is removed.   

The query for booking a seat is
`UPDATE {seat.plane_name} SET passengerInformation='{seat.passenger_information}', passengerID='{passenger_id}' WHERE id='{seat._id}'`  
which replaces the passengerInformation and ID with the currently created passengerID and information given by the request.   

The passenger_id is created through the algorithm here  
```python
    passenger_id = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
```
which calls the OS module for random bytes and then the  binascii module hexes the bytes. It is then decoded into utf-8 for storage and for the customer to read.  

The query for unbooking a seat is similar but the passenger values are nulled  
`UPDATE {seat.plane_name} SET passengerInformation=NULL, passengerID=NULL WHERE id="{seat._id}"`

### Handling data from the Database
The Pandas module is used execute SQL querys onto the connection when a return value is needed.  
The read_sql_query() function provided by Pandas returns a Pandas DataFrame.  
Here is an algorithm that returns the Seat from the dataframe  
```python
Seat(*df.iloc[0], plane_name)
```
The asterisk is used to unpack the first row in the dataframe which is a Pandas Series. The plane_name is then also added to the constructor of the Seat.   

This algorithm returns all rows as seats in the DataFrame   
```python
df.apply(lambda seat: Seat(*seat, plane_name), axis=1)
```
The lambda function is used to unpack the values on the current row (the axis kwarg determines this) and the seats are returned.  

This goes into a dictionary comprehension shown below to covert the Pandas Series into a dictionary using the toJSON method on the seats.  
```python
    return {
            seat._id: seat.toJSON() for seat in seats
        }, 200
```