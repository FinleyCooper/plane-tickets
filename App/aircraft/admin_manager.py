from sqlite3 import OperationalError

def create_plane(name, seat_length, seat_width, connection):
    try:
        connection.execute(f"CREATE TABLE {name}(id VARCHAR(3), passengerID VARCHAR(30), passengerInformation VARCHAR(255), class VARCHAR(10))")
    
    except OperationalError:
        print(f"The table {name} already exists")
        return None

    seat_values = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    for i in range(seat_width):
        for j in range(seat_length):
            seat_values.append(f"('{alphabet[i] + str(j+1)}', NULL, NULL, 'economy')")
    

        connection.execute(f'INSERT INTO {name} (id, passengerID, passengerInformation, class) VALUES {",".join(seat_values)}')
        connection.commit()

        