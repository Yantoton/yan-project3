class Sahiwal_Bull:
    def diet(self):
        return "Sahiwal:Green Fodder: 15 to 20 kg/Dry Fodder:4 to 6 kg/concentrate mixture: (3–5 kg)"
class Holstein_Bull:
    def diet(self):
        return "Holstein:Green Fodder: 20 to 25 kg/Dry Fodder:5 to 7 kg/concentrate mixture: (5-7 kg)"

diet_info = [Sahiwal_Bull(),Holstein_Bull()]

for cattle in diet_info:
    print(cattle.diet())
