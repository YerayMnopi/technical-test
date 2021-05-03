from math import floor


class CostProrating:
    """
    Prorates the cost across a list of weights.
    """

    def prorate(self, cost: int, weights: []) -> []:
        total_weight = sum(weights)
        prorates = []

        for weight in weights:
            fraction = cost * (weight / total_weight)
            rounded = floor(fraction)

            prorates.append((rounded, fraction))

        rounded_sum = sum([pair[0] for pair in prorates])

        while rounded_sum < cost:
            error_list = [pair[1] - pair[0] for pair in prorates]
            max_error = max(error_list)
            element_to_compensate = error_list.index(max_error)
            prorates[element_to_compensate] = (prorates[element_to_compensate][0] + 1, prorates[element_to_compensate][1])
            rounded_sum = sum([pair[0] for pair in prorates])

        return [tuple[0] for tuple in prorates]

