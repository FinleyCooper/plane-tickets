import sqlite3
import json

from flask import Flask, request

import App.seats.seat_manager as seat_manager

app = Flask(__name__)

connection = sqlite3.connect("seats/seats.db", check_same_thread=False)

@app.route('/api/<string:plane_name>/seat', methods=['POST', 'DELETE'])
def seat(plane_name):
    if request.method == 'POST':
        seat = seat_manager.get_seat(plane_name, request.json["seat"], connection)

        if not seat:
            return {
                "successful": False,
                "msg": "That is not a valid seat number."
            }, 404

        elif seat.passenger_information:
            return {
                "successful": False,
                "msg": "Seat has already been booked."
            }, 204
        
        elif not request.json["passengerInformation"] or len(request.json["passengerInformation"]) != 5:
            return {
                "successful": False,
                "msg": "Passenger information not provided"
            }, 400

        seat.passenger_information = json.dumps(request.json["passengerInformation"])

        passenger_id = seat_manager.book_seat(seat, connection)

        return {
            "successful": True,
            "passengerID": passenger_id
        }, 200


    elif request.method == 'DELETE':
        seat = seat_manager.get_seat(plane_name, request.json["seat"], connection)

        if not seat:
            return {
                "successful": False,
                "msg": "That is not a valid seat number."
            }, 404
        
        elif not seat.passenger_information:
            return {
                "successful": False,
                "msg": "That seat has not been booked yet."
            }, 400

        elif seat.passenger_id != request.json["passengerID"]:
            return {
                "successful": False,
                "msg": "You are not authorized to modify this seat"
            }, 403
        
        seat_manager.unbook_seat(seat, connection)
        
        return {
            "successful": True,
        }, 200



@app.route('/api/<string:plane_name>/seats', methods=['GET'])
def seats(plane_name):
    seats = seat_manager.get_all_seats_from(plane_name, connection)

    return {
            seat._id: seat.toJSON() for seat in seats
        }, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
