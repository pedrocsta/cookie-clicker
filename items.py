class Item:
    def __init__(self, name, cost, cps, cpc):
        self.name = name

        self.cost = cost

        self.cps = cps  # cookies per second
        self.cpc = cpc  # cookies per click

    def __str__(self):
        return self.name

    def update_cost(self):
        self.cost += self.cost // 6


Cursor = Item('Cursor', 15, 0.1, 0)
Grandma = Item('Grandma', 100, 1, 0)
Fingers = Item('Fingers', 400, 1, 1)
Farm = Item('Farm', 1100, 8, 1)
Mine = Item('Mine', 12000, 47, 1)
Factory = Item('Factory', 130000, 260, 2)
Bank = Item('Bank', 1400000, 1400, 0)
Temple = Item('Temple', 2000000, 7800, 1)
Wizard_Tower = Item('Wizard Tower', 330000000, 44000, 4)
Shipment = Item('Shipment', 5100000000, 260000, 0)
Alchemy_Lab = Item('Alchemy Lab', 75000000000, 1600000, 3)
Portal = Item('Portal', 1000000000000, 10000000, 6)
Time_Machine = Item('Time Machine', 14000000000000, 65000000, 6)
Cookie_Monster = Item('Cookie Monster', 180000, 350, 70)
Blaster = Item('Blaster', 20000000, 0, 3500)
Hacker = Item('Hacker', 200000000000000, 6000000000000, 1000000000)