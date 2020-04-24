class Sensor(object):
    def __init__(self):
        pass

    def sensorON(self):
        print("Sensor is ON")

    def sensorOFF(self):
        print("Sensor is OFF")


class Smoke(object):
    def __init__(self):
        pass

    def smokeON(self):
        print("Smoke is ON")

    def smokeOFF(self):
        print("Smoke is OFF")


class Lights(object):
    def __init__(self):
        pass

    def lightsON(self):
        print("Light is ON")

    def lightsOFF(self):
        print("Light is OFF")

class Meta(type):

    """ Singleton Design Pattern"""

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Meta,cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class Facade(metaclass=Meta):

    def __init__(self):
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Lights()

    def emergency(self):
        self._sensor.sensorON()
        self._light.lightsON()
        self._smoke.smokeON()

    def NotEmergency(self):
        self._sensor.sensorOFF()
        self._light.lightsOFF()
        self._smoke.smokeOFF()


if __name__ == "__main__":
    facade = Facade()
    print(facade)
    facade1 = Facade()
    print(facade1)


