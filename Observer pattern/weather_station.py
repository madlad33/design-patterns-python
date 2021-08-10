from abc import ABC, abstractmethod


class IObserver(ABC):

    @abstractmethod
    def update(self):
        pass


class IObservable(ABC):
    subscribers = set()

    @abstractmethod
    def add(self, observer: IObserver):
        pass

    @abstractmethod
    def remove(self, observer: IObserver):
        pass

    def notify(self):
        pass


class WeatherStation(IObservable):
    current_temperature = None

    def add(self, observer):
        return self.subscribers.add(observer)

    def remove(self, observer):
        return self.subscribers.remove(observer)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def get_temperature(self):
        return self.current_temperature

    def set_temperature(self, temp):
        self.current_temperature = temp
        return


class IDisplay(ABC):
    @abstractmethod
    def display(self):
        pass


class MobileDisplay(IObserver, IDisplay):
    def __init__(self, observable: WeatherStation):
        self.observable = observable

    def update(self):
        print(f'Updating weather status, now temprature {self.observable.get_temperature()}')

    def display(self):
        print('The current temprature is ...')


class LCDDisplay(IObserver, IDisplay):
    def __init__(self, observable: WeatherStation):
        self.observable = observable

    def update(self):
        print(f'Updating weather status, now temprature {self.observable.get_temperature()}')

    def display(self):
        print('Displaying temperature on the LCD PANEL...')


weather_station = WeatherStation()
mobile = MobileDisplay(weather_station)
lcd = LCDDisplay(weather_station)

weather_station.add(mobile)
weather_station.add(lcd)
weather_station.set_temperature('100 c')
mobile.display()
lcd.display()
weather_station.notify()
weather_station.set_temperature('90 c')
weather_station.notify()
