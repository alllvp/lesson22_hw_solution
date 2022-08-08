# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:

    def __init__(self, room_name=42):
        self._room_name = room_name

    def get_name(self):
        return self._room_name


class Street:

    def __init__(self, room):
        self._room = room

    def get_room(self) -> Room:
        return self._room


class City:

    def __init__(self, street, population=100500):
        self._street = street
        self._population = population

    def get_street(self) -> Street:
        return self.street

    def population(self):
        return self._population


class Country:

    def __init__(self, city):
        self._city = city

    def get_city(self) -> City:
        return self._city


class Planet:

    def __init__(self, country):
        self._country = country

    def get_country(self) -> Country:
        return self._country


class Person:
    def __init__(self, city_population, person_room):
        self._city_population = city_population
        self._person_room = person_room

    def get_person_room(self):
        return self._person_room

    def get_city_population(self):
        return self._city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

room = Room()
street = Street(room)
city = City(street)
country = Country(city)
planet = Planet(country)
person = Person(city.population(), room.get_name())
print(person.get_person_room())
print(person.get_city_population())