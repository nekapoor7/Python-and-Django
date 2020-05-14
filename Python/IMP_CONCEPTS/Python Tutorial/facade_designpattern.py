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


class Facade(object):

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
    sensor = int(input())

    if sensor > 60:
        facade.emergency()
    else:
        facade.NotEmergency()


