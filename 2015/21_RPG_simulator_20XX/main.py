from itertools import combinations


class Player(object):
    def __init__(
        self, items=tuple(), name="player", hit_points=100, damage=0, armor=0
    ):  # tuple[Item]
        self.name = name
        self.spent = 0
        self.armor = armor
        self.damage = damage
        self.hit_points = hit_points
        self.equipment = []

        for item in items:
            self.spent += item.cost
            self.armor += item.armor
            self.damage += item.damage
            self.equipment.append(item)

    def __repr__(self):
        return f"Name: {self.name}, Damage: {self.damage}, Armor: {self.armor}, Spent: {self.spent}, HP: {self.hit_points}"

    def __lt__(self, other):
        return self.spent < other.spent

    def __le__(self, other):
        return self.spent <= other.spent

    def __gt__(self, other):
        return self.spent > other.spent

    def __ge__(self, other):
        return self.spent >= other.spent

    def __eq__(self, other):
        return self.spent == other.spent

    def __ne__(self, other):
        return self.spent != other.spent


class Item(object):
    def __init__(self, name, cost, damage, armor, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.type = type

    def __repr__(self):
        return f"{self.name} {self.type}"


def get_all_store_combinations():
    weapons = [
        Item("Dagger", 8, 4, 0, "w"),
        Item("Shortsword", 10, 5, 0, "w"),
        Item("Warhammer", 25, 6, 0, "w"),
        Item("Longsword", 40, 7, 0, "w"),
        Item("Greataxe", 74, 8, 0, "w"),
    ]

    armor = [
        Item("Leather", 13, 0, 1, "a"),
        Item("Chainmail", 31, 0, 2, "a"),
        Item("Splintmail", 53, 0, 3, "a"),
        Item("Bandedmail", 75, 0, 4, "a"),
        Item("Platemail", 102, 0, 5, "a"),
    ]

    rings = [
        Item("Damage + 1", 25, 1, 0, "r"),
        Item("Damage + 2", 50, 2, 0, "r"),
        Item("Damage + 3", 100, 3, 0, "r"),
        Item("Defense + 1", 20, 0, 1, "r"),
        Item("Defense + 2", 40, 0, 2, "r"),
        Item("Defense + 3", 80, 0, 3, "r"),
    ]

    store = weapons + armor + rings + rings
    four_items = list(combinations(store, 4))
    three_items = list(combinations(store, 3))
    two_items = list(combinations(store, 2))
    one_item = list(combinations(weapons, 1))
    all_comb = one_item + two_items + three_items + four_items

    return list(filter(conditions, all_comb))


def conditions(equipment):
    R, W, A = 0, 0, 0
    for item in equipment:
        if item.type == "r":
            R += 1

        if item.type == "a":
            A += 1

        if item.type == "w":
            W += 1

    return all([W == 1, R <= 2, A <= 1])


def run_sim(p1, p2, verbose=False):
    turns = 0

    while p1.hit_points > 0 and p2.hit_points > 0:
        turns += 1
        dealt = p1.damage - p2.armor
        p2.hit_points -= dealt

        if verbose:
            print(
                f"{p1.name} deals {p1.damage}-{p2.armor}={dealt} damage; {p2.name} goes down to {p2.hit_points}."
            )

        p1, p2 = p2, p1

    return (p1 if p1.hit_points > 0 else p2, turns)


def win(player, boss, winner_name="player"):
    winner, _ = run_sim(player, boss)
    return winner.name == winner_name


def solve(hp, dmg, armor):
    players = [Player(x) for x in get_all_store_combinations()]

    winner_players = []
    looser_players = []

    for player in players:
        # Resets the boss stats
        boss = Player(name="Boss", hit_points=hp, damage=dmg, armor=armor)

        if win(player, boss):
            winner_players.append(player)

        else:
            looser_players.append(player)

    ans1 = min(winner_players).spent
    ans2 = max(looser_players).spent

    return (ans1, ans2)


ans = solve(hp=100, dmg=8, armor=2)
print(ans)
