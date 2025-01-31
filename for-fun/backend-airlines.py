import random 
from flask import Flask, jsonify, request
import json 

app = Flask(__name__)

# Static lists of cities
ucities = ["Narpay", "Ko'kcha", "Beshariq", "Xazorasp", "Zangiota", "Beshariq", "Angren", "Chirchiq"]
fcities = ["Buenos Aires", "Lissabon", "Madrid", "Las Vegas", "Istanbul", "Amsterdam", "Brussel"]

# Loading flights data from your json file (initialization)
def load_flights():
    with open('for-fun/uzbekcities.json', 'r') as file:
        data = json.load(file)
        return data['flights']

# Save flights data to json
def save_flights(flights):
    with open('for-fun/uzbekcities.json', 'w') as file:
        json.dump({'flights': flights}, file, indent=4)

# Initial flight list when the app starts
flights = load_flights()


# Flight class
class Flights:
    def __init__(self, flying, landing, flight):
        self.flying = flying
        self.landing = landing
        self.flight = flight

    def __str__(self):
        return f'I want to buy ticket for {self.flight} flight'


# Route to get all flights
@app.route('/flights', methods=['GET'])
def get_all_flights():
    return jsonify({'flights': flights})


# Route to generate random flight
@app.route('/random-flight', methods=['GET'])
def get_random_flight():
    random_ucity = random.choice(ucities)
    random_fcity = random.choice(fcities)
    flight_random = f'{random_ucity} - {random_fcity}'

    # Append the random flight to the flight list
    flights.append({'flying': random_ucity, 'landing': random_fcity, 'flight': flight_random})
    save_flights(flights)

    return jsonify({'flying': random_ucity, 'landing': random_fcity, 'flight': flight_random})


# Route to create a custom flight (from user input)
@app.route('/create-flight', methods=['POST'])
def create_flight():
    data = request.get_json()  # Expecting a JSON body with 'flying' and 'landing'
    flying = data.get('flying')
    landing = data.get('landing')
    your_flight = f'{flying} - {landing}'

    # Append new custom flight to flights list
    flights.append({'flying': flying, 'landing': landing, 'flight': your_flight})
    save_flights(flights)

    return jsonify({'flying': flying, 'landing': landing, 'flight': your_flight})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
