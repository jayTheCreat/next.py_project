class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    # המחזירה ערך בוליאני המתאר האם החיה רעבה או לא, חיה רעבה היא חיה שערך מידת הרעב שלה גדול מאפס
    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('woof woof')

    def __str__(self):
        return f"Type: {'Dog'}, Name: {super().get_name()}"

    # special method	
    def fetch_stick(self):
        print('There you go, sir!')


class Cat(Animal):
    def talk(self):
        print('meow')

    def __str__(self):
        return f"Type: {'Cat'}, Name: {super().get_name()}"

    # special method
    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal):
    def __init__(self, name, hunger=0, count=6):
        super().__init__(name, hunger)
        self._stink_count = count

    def talk(self):
        print('tsssss')

    def __str__(self):
        return f"Type: {'Skunk'}, Name: {super().get_name()}"

    # special method
    def stink(self):
        print('Dear lord!')


class Unicorn(Animal):
    def talk(self):
        print('Good day, darling')

    def __str__(self):
        return f"Type: {'Unicorn'}, Name: {super().get_name()}"

    # special method
    def sing(self):
        print('I’m not your toy...')


class Dragon(Animal):
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print('Raaaawr')

    def __str__(self):
        return f"Type: {'Dragon'}, Name: {super().get_name()}"

    # special method
    def breath_fire(self):
        print('$@#$#@$')


def main():
    dog = Dog('Brownie', 10)
    cat = Cat('Zelda', 3)
    skunk = Skunk('Stinky')
    unicorn = Unicorn('Keith', 7)
    dragon = Dragon('Lizzy', 1450)
    zoo_lst = [dog, cat, skunk, unicorn, dragon]

    dog = Dog('Doggo', 80)
    cat = Cat('Kitty', 80)
    skunk = Skunk('Stinky Jr.', 80)
    unicorn = Unicorn('Clair', 80)
    dragon = Dragon('McFly', 80)
    zoo_lst += [dog, cat, skunk, unicorn, dragon]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal)
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
