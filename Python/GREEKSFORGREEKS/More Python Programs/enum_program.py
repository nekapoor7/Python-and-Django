from enum import Enum,unique,auto

@unique
class Sensor(Enum):

    Temparture = 1
    Humidity = 2
    Air = auto()

if __name__ == "__main__":
    print(Sensor)
    print(Sensor.Temparture.name)
    print(Sensor.Temparture.value)

    for item in Sensor:
        print(item.value)