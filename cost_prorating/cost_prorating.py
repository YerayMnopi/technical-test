from math import floor


class CostProrating:
    """
    Implement a function that takes a cost and a set of weights and returns the distribution of the cost
    proportionally to the weights, with the initial cost and all the prorated costs being integers.

    The order of elements in the returned array corresponds of the order of the weights

    The total amount distributed must be exactly the initial cost.
    • For a weight equal to 0, prorated cost must be 0.
    • For a weight > 0, rounded prorated cost must differ from the exact prorated cost by strictly
    less than 1. In that case we define the relative rounding error as Abs(roundedProrata - exactProrata)
    / weight. (So the relative error for a rounding difference of 0.5 on a weight of 1 is 0.5; and the
    relative error for a rounding difference of 0.6 on a weight of 2 is 0.3).

    The algorithm should minimize the deviation, which is the sum of all relative rounding errors.
    The cost is greater than or equal to 0.
    The set of weights is non null and contains at least one non-zero weight.
    Each weight is greater than or equal to 0.

    Abs(roundedProrata - exactProrata) / weight
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

