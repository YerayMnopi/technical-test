import itertools


class WaterJugs:

    def __init__(self):
        self.visited = {}
        self.target_volume = 0
        self.jugs_capacities = []
        self.jugs_status = []
        self.number_of_jugs = 0
        self.steps = []

    def find_sequence(self, target_volume: int, jugs_capacities: []) -> []:
        self.target_volume = target_volume
        self.jugs_capacities = jugs_capacities
        self.number_of_jugs = len(jugs_capacities)
        self.jugs_status = self.number_of_jugs * [0]
        self.resolve(self.jugs_status)
        all_values = list(itertools.chain.from_iterable(self.steps))
        return self.steps if self.target_volume in all_values else None

    def resolve(self, jugs_status: []) -> bool:
        if self.target_volume in jugs_status:
            self.steps.append(jugs_status)
            return True

        if str(jugs_status) in self.visited.keys():
            return False

        self.steps.append(jugs_status)

        self.visited[str(jugs_status)] = True

        return (
            self.all_fills_combinations(jugs_status) or
            self.all_pour_in_sink_combinations(jugs_status) or
            self.all_pour_in_another_jug_combinations(jugs_status)
        )

    def all_fills_combinations(self, jugs_status) -> bool:
        for index in range(self.number_of_jugs):
            result = self.fill_jug(index, jugs_status)

            if result:
                return True
        return False

    def all_pour_in_sink_combinations(self, jugs_status) -> bool:
        for index in range(self.number_of_jugs):
            result = self.pour_jug_in_sink(index, jugs_status)

            if result:
                return True

        return False

    def all_pour_in_another_jug_combinations(self, jugs_status) -> bool:
        combinations = itertools.combinations(range(self.number_of_jugs), 2)

        for combination in combinations:
            result = self.pour_jug_in_another_jug(combination[0], combination[1], jugs_status)

            if result:
                return True

            result = self.pour_jug_in_another_jug(combination[1], combination[0], jugs_status)

            if result:
                return True

        return False

    def fill_jug(self, jug_index: int, jugs_status: []) -> []:
        copy = jugs_status.copy()
        copy[jug_index] = self.jugs_capacities[jug_index]
        return self.resolve(copy)

    def pour_jug_in_sink(self, jug_index: int, jugs_status: []) -> []:
        copy = jugs_status.copy()
        copy[jug_index] = 0
        return self.resolve(copy)

    def pour_jug_in_another_jug(self, jug_source_index: int, jug_destination_index: int, jugs_status: []) -> []:
        copy = jugs_status.copy()
        destination_empty_capacity = self.jugs_capacities[jug_destination_index] - copy[jug_destination_index]
        source_capacity = copy[jug_source_index]
        transferred_water = min(source_capacity, destination_empty_capacity)

        copy[jug_destination_index] = copy[jug_destination_index] + transferred_water
        copy[jug_source_index] = copy[jug_source_index] - transferred_water
        return self.resolve(copy)


if __name__ == '__main__':
    WaterJugs().find_sequence(2, [4, 3])
