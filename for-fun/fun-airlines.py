import random 
from flask import Flask, jsonify, request
import json 

app = Flask(__name__)

ucities = ["Narpay", "Ko'kcha", "Beshariq", "Xazorasp", "Zangiota", "Beshariq", "Angren", "Chirchiq"]
random_ucity = random.choice(ucities)

fcities = ["Buenos Aires", "Lissabon", "Madrid", "Las Vegas", "Istanbul", "Amsterdam", "Brussel"]
random_fcity = random.choice(fcities)

with open('for-fun/uzbekcities.json', 'r') as file:
      data = json.load(file)
      flights = data['flights']

class Flights:
      def __init__(self, flying, landing, flight):
            self.flying = flying
            self.landing = landing
            self.flight = flight
            
      def __str__(self):
            return f'I want to buy ticket for {self.flight} flight'



def main():
      flight_choice = input('Do you want to get random flight? Yes/No ').lower().strip()

      if flight_choice == 'yes':
            randomed_flight = random_flight()
            print(randomed_flight)
      elif flight_choice == 'no':
           created_flight = create_flight() 
           print(created_flight)
      else:
            return None
      

def random_flight():
      flight_random = f'{random_ucity} - {random_fcity}'

      flights.append({'flying': random_ucity, 'landing': random_fcity, 'flight': flight_random})

      with open('for-fun/uzbekcities.json', 'w') as file:
            json.dump({'flights': flights}, file, indent=4)

      return Flights(random_ucity, random_fcity, flight_random)

def create_flight():
      flying = input('Enter Uzbek city: ')
      landing = input('Enter landing city: ')
      your_flight = f'{flying} - {landing}'
      
      flights.append({'flying': flying, 'landing': landing, 'flight': your_flight})
      with open('for-fun/uzbekcities.json', 'w') as file:
            json.dump({'flights': flights}, file, indent=4)

      return Flights(flying, landing, your_flight)


@app.route('/random-flight', methods=['GET'])
def get_random_flight():
    flight = random_flight()
    return jsonify({'flying': flight.flying, 'landing': flight.landing, 'flight': flight.flight})

# Route to get list of all flights
@app.route('/flights', methods=['GET'])
def get_all_flights():
    return jsonify({'flights': flights})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)