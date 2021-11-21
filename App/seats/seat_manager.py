import binascii
import os
from typing import Optional
from sqlite3 import Connection
import pandas as pd

from App.seats.seat import Seat


def get_seat(plane_name: str, seat_id: str, connection: Connection) -> Optional[Seat]:
    """Prompts the Database to get seats on a given plane, returns None if the seat isn't found"""
    
    df = pd.DataFrame()

    plane_name = plane_name.upper()
    seat_id = seat_id.upper()

    try:
        df = pd.read_sql_query(f'SELECT * FROM {plane_name} WHERE id="{seat_id}"', connection)
    except pd.io.sql.DatabaseError:
        return None

    if df.empty:
        return None
    

    return Seat(*df.iloc[0], plane_name)


def get_all_seats_from(plane_name: str, connection: Connection) -> Optional[pd.Series[Seat]]:
    """Prompts the Database to get all seats on a given plane"""
    
    df = pd.DataFrame()

    plane_name = plane_name.upper()

    try:
        df = pd.read_sql_query(f'SELECT * FROM {plane_name}', connection)
    except pd.io.sql.DatabaseError:
        return None

    return (df.apply(lambda seat: Seat(*seat, plane_name), axis=1))
    


def book_seat(seat: Seat, connection: Connection) -> str:
    """Queries the Database to reserve the given seat, on the given plane and returns the passenger's ID"""

    passenger_id = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    connection.execute(f"UPDATE {seat.plane_name} SET passengerInformation='{seat.passenger_information}', passengerID='{passenger_id}' WHERE id='{seat._id}'")
    connection.commit()

    return passenger_id


def unbook_seat(seat: Seat, connection: Connection) -> None:
    """Queries the Datebase to mark the given seat as untaken, removing the passenger identifier"""

    connection.execute(f'UPDATE {seat.plane_name} SET passengerInformation=NULL, passengerID=NULL WHERE id="{seat._id}"')
    connection.commit()
