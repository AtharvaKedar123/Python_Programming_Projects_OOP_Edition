class Crystal:
    def __init__(self, name, size, purity):
        if size <= 0 or purity < 0 or purity > 100:
            raise ValueError("Invalid size or purity")
        self.name = name
        self.size = size
        self.purity = purity

    def is_stable(self):
        return self.size >= 5 and self.purity >= 90

    def grow(self, growth_rate):
        if growth_rate <= 0:
            return -1
        self.size += growth_rate

    def get_info(self):
        return {
            "name": self.name,
            "size": self.size,
            "purity": self.purity,
            "stable": self.is_stable()
        }


class ColoredCrystal(Crystal):
    def __init__(self, name, size, purity, color):
        super().__init__(name, size, purity)
        self.color = color

    def get_info(self):
        info = super().get_info()
        info["color"] = self.color
        return info


class CrystalLab:
    def __init__(self):
        self.crystals = []

    def add_crystal(self, crystal):
        if not isinstance(crystal, Crystal):
            return -1
        self.crystals.append(crystal)

    def list_crystals(self):
        return [crystal.get_info() for crystal in self.crystals]

    def count_stable(self):
        return sum(1 for crystal in self.crystals if crystal.is_stable())


# -------------------- Sample Usage --------------------

# Create crystals
c1 = Crystal("Quartz", 6, 95)
c2 = ColoredCrystal("Amethyst", 4.5, 92, "Purple")
c3 = ColoredCrystal("Ruby", 5.5, 97, "Red")

# Create lab and add crystals
lab = CrystalLab()
lab.add_crystal(c1)
lab.add_crystal(c2)
lab.add_crystal(c3)

# Grow crystals
c2.grow(1)  # Now Amethyst will be stable

# List all crystals
print("All Crystals:")
for crystal_info in lab.list_crystals():
    print(crystal_info)

# Count stable crystals
print("\nNumber of stable crystals:", lab.count_stable())
