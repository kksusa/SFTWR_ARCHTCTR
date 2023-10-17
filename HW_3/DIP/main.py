from diesel import Diesel
from petrol import Petrol

if __name__ == '__main__':
    diesel_car = Diesel()
    petrol_car = Petrol()
    diesel_car.start()
    petrol_car.start()
