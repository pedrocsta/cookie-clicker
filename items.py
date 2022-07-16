class Item:

    def __init__(self, name: str, cost: int, cps: float, cpc: float):
        self.name = name
        self.cost = cost
        self.cps = cps  # cookies per second
        self.cpc = cpc  # cookies per click

    def update_cost(self) -> tuple:
        self.cost += self.cost // 6

        return self.cps, self.cpc


class Upgrades:

    def __init__(self, items_: list[Item], upgrades: list[int]):
        self.items = items_
        self.upgrades = upgrades

    def load_upgrades(self) -> tuple:
        for item, upgrades in zip(self.items, self.upgrades):
            for upgrade in range(upgrades):
                yield item.update_cost()

    def upgrade(self, item: Item, cookies: float) -> tuple:
        cost = cps = cpc = 0
        if cookies >= item.cost:
            index = self.items.index(item)
            cps, cpc, cost = item.cps, item.cpc, item.cost
            self.upgrades[index] += 1
            self.items[index].update_cost()

        return cost, cps, cpc


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
