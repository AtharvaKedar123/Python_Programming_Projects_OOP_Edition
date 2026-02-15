class Mineral:
    def __init__(self, mineral_id, name, composition):
        if not all(0 <= value <= 100 for value in composition.values()):
            raise ValueError("Invalid composition: each element must be 0-100")
        if sum(composition.values()) > 100:
            raise ValueError("Invalid composition: sum of percentages cannot exceed 100")
        self.mineral_id = mineral_id
        self.name = name
        self.composition = composition

    def major_element(self):
        if not self.composition:
            return None
        return max(self.composition, key=self.composition.get)

    def is_stable(self):
        return sum(self.composition.values()) == 100

    def get_info(self):
        return {
            "mineral_id": self.mineral_id,
            "name": self.name,
            "composition": self.composition,
            "major_element": self.major_element(),
            "stable": self.is_stable()
        }


class RareMineral(Mineral):
    def __init__(self, mineral_id, name, composition, rarity_level, planet_found):
        super().__init__(mineral_id, name, composition)
        if not (1 <= rarity_level <= 5):
            raise ValueError("Invalid rarity level: must be 1-5")
        self.rarity_level = rarity_level
        self.planet_found = planet_found

    def get_info(self):
        info = super().get_info()
        info["rarity_level"] = self.rarity_level
        info["planet_found"] = self.planet_found
        return info


class MineralLab:
    def __init__(self):
        self.minerals = []

    def add_mineral(self, mineral):
        if not isinstance(mineral, Mineral):
            return -1
        self.minerals.append(mineral)

    def list_minerals(self):
        return [mineral.get_info() for mineral in self.minerals]

    def count_stable(self):
        return sum(1 for mineral in self.minerals if mineral.is_stable())

    def count_rare(self):
        return sum(1 for mineral in self.minerals if isinstance(mineral, RareMineral))





m1 = Mineral("M001", "Olivine", {"Mg": 40, "Fe": 60})
m2 = Mineral("M002", "Quartz", {"Si": 50, "O": 50})
m3 = RareMineral("M003", "Tranquillite", {"Fe": 30, "Ni": 30, "Co": 40}, 4, "Mars")
m4 = RareMineral("M004", "Xenotime", {"Y": 20, "PO4": 80}, 5, "Venus")
m5 = Mineral("M005", "Feldspar", {"Al": 20, "Si": 50, "O": 30})


lab = MineralLab()
lab.add_mineral(m1)
lab.add_mineral(m2)
lab.add_mineral(m3)
lab.add_mineral(m4)
lab.add_mineral(m5)


print("All Minerals:")
for mineral_info in lab.list_minerals():
    print(mineral_info)


print("\nNumber of stable minerals:", lab.count_stable())


print("Number of rare minerals:", lab.count_rare())
