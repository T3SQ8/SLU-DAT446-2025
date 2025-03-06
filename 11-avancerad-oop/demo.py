"""
- Namn
- Genus
- Art
- Habitat
- Föda
- Ålder 
"""

class Djur():

    antal_djur = 0

    def __init__(self, namn: str, genus: str, art: str, habitat: str, föda: str, ålder: int):
        self.namn = namn
        self.genus = genus
        self.art = art
        self.habitat = habitat
        self.föda = föda
        self.ålder = ålder


"""
  - Vingspann
  - Näbbfärg
  - Simmhastighet
"""

class Anka(Djur):
    def __init__(self, namn, genus, art, habitat, föda, ålder, vingspann, näbbfärg, simmhastighet):
        super().__init__(namn, genus, art, habitat, föda, ålder)
        self.vingspann = vingspann
        self.näbbfärg = näbbfärg
        self.simmhastighet = simmhastighet