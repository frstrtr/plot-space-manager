class KnapsackPackage(object):

    """ Knapsack Package Data Class """

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapsack(object):
    def __init__(self):
        pass

    def knapsackGreProc(self, W, V, M, n):
        packs = []
        for i in range(n):
            packs.append(KnapsackPackage(W[i], V[i]))

        packs.sort(reverse=True)

        remain = M
        result = 0

        i = 0
        stopProc = False

        while (stopProc != True):
            if (packs[i].weight <= remain):
                remain -= packs[i].weight
                result += packs[i].value

            print("Pack ", i, " - Weight ",
                  packs[i].weight, " - Value ", packs[i].value)

            if (packs[i].weight > remain):
                i += 1

            if (i == n):
                stopProc = True
        return result


if __name__ == "__main__":
    # W stands for the weight of the item
    weight_list = [1024, 2048, 3192, 4096]
    # V stands for Value of the item
    # THE BIGGER THE PLOT THE BIGGER THE VALUE
    volume_list = weight_list  # [1, 2, 3, 4]
    # M stands for KnapSack MAX Volume
    max_weight = 36000348766208
    # N stands for a number of items,
    number_of_items = len(weight_list)
    # C stands for Cost of the item.

    proc = FractionalKnapsack()
    proc.knapsackGreProc(weight_list, volume_list, max_weight, number_of_items)
