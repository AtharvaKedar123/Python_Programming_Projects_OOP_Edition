import random


class BehaviorStrategy:
    def act(self, animal, environment):
        pass


class HuntStrategy(BehaviorStrategy):
    def act(self, animal, environment):
        prey_list = [a for a in environment.animals if isinstance(a, Prey) and a.energy > 0]
        if prey_list:
            target = random.choice(prey_list)
            if random.random() < animal.speed:
                animal.energy += target.energy
                target.energy = 0
                print(f"{animal.name} hunted {target.name}")
            else:
                animal.energy -= 2
        else:
            animal.energy -= 1


class EscapeStrategy(BehaviorStrategy):
    def act(self, animal, environment):
        predator_near = any(isinstance(a, Predator) and a.energy > 0 for a in environment.animals)
        if predator_near:
            if random.random() < animal.speed:
                animal.energy -= 1
            else:
                animal.energy -= 3
        else:
            animal.energy += 2


class Animal:
    def __init__(self, name, energy, speed, strategy):
        self.name = name
        self.energy = energy
        self.speed = speed
        self.strategy = strategy

    def act(self, environment):
        if self.energy > 0:
            self.strategy.act(self, environment)

    def is_alive(self):
        return self.energy > 0


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name, energy=20, speed=random.uniform(0.4, 0.9), strategy=HuntStrategy())


class Prey(Animal):
    def __init__(self, name):
        super().__init__(name, energy=15, speed=random.uniform(0.3, 0.8), strategy=EscapeStrategy())


class Environment:
    def __init__(self):
        self.animals = []
        self.generation = 1

    def add_animal(self, animal):
        self.animals.append(animal)

    def simulate_step(self):
        print(f"\n--- Generation {self.generation} ---")
        for animal in self.animals:
            animal.act(self)

        self.animals = [a for a in self.animals if a.is_alive()]

        self.reproduce()
        self.mutate()

        self.generation += 1
        self.show_status()

    def reproduce(self):
        new_animals = []
        for animal in self.animals:
            if animal.energy > 25:
                child = self.create_offspring(animal)
                new_animals.append(child)
                animal.energy -= 10
        self.animals.extend(new_animals)

    def create_offspring(self, parent):
        if isinstance(parent, Predator):
            child = Predator(parent.name + "_child")
        else:
            child = Prey(parent.name + "_child")

        child.speed = parent.speed
        return child

    def mutate(self):
        for animal in self.animals:
            if random.random() < 0.2:
                change = random.uniform(-0.1, 0.1)
                animal.speed = max(0.1, min(1.0, animal.speed + change))

    def show_status(self):
        predators = sum(isinstance(a, Predator) for a in self.animals)
        prey = sum(isinstance(a, Prey) for a in self.animals)
        print(f"Predators: {predators}, Prey: {prey}")


if __name__ == "__main__":
    env = Environment()

    for i in range(3):
        env.add_animal(Predator(f"Predator_{i}"))

    for i in range(6):
        env.add_animal(Prey(f"Prey_{i}"))

    for _ in range(10):
        env.simulate_step()