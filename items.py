class Item:

    def __init__(self, name: str, cost: int, cps: float, cpc: float):
        self.name = name
        self.cost = cost
        self.cps = cps  # cookies per second
        self.cpc = cpc  # cookies per click

    def __str__(self):
        return self.name

    def update_cost(self):
        self.cost += self.cost // 6

        return self.cps, self.cpc

    def upgrade(self, cookies: float, cps: float, cpc: float):
        if cookies < self.cost:
            return cookies, cps, cpc
        cost = self.cost
        self.update_cost()

        return cookies - cost, cps + self.cps, cpc + self.cpc


class Upgrade:

    def __init__(self, items_: list, upgrades: list):
        self.items = items_
        self.upgrades = upgrades

    def load_upgrades(self):
        for item, upgrades in zip(self.items, self.upgrades):
            for upgrade in range(upgrades):
                yield item.update_cost()


def _get_items():
    yield Item('Cursor', 15, 0.1, 0)
    yield Item('Grandma', 100, 1, 0)
    yield Item('Fingers', 400, 1, 1)
    yield Item('Farm', 1100, 8, 1)
    yield Item('Mine', 12000, 47, 1)
    yield Item('Factory', 130000, 260, 2)
    yield Item('Bank', 1400000, 1400, 0)
    yield Item('Temple', 2000000, 7800, 1)
    yield Item('Wizard Tower', 330000000, 44000, 4)
    yield Item('Shipment', 5100000000, 260000, 0)
    yield Item('Alchemy Lab', 75000000000, 1600000, 3)
    yield Item('Portal', 1000000000000, 10000000, 6)
    yield Item('Time Machine', 14000000000000, 65000000, 6)
    yield Item('Cookie Monster', 180000, 350, 70)
    yield Item('Blaster', 20000000, 0, 3500)
    yield Item('Hacker', 200000000000000, 6000000000000, 1000000000)


items = list(_get_items())
