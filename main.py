import simulation
import KnapsackGreedy


if __name__ == '__main__':

    two_drives = simulation.rack_config(1, 1)
    proc = KnapsackGreedy.FractionalKnapsack()
    drives = (two_drives.values())  # list of file dict per drive
    weight_list = list()
    for drive in drives:
        weight_list.extend(list(drive.values()))
    volume_list = weight_list
    max_weight = 17927473950720
    #            35 856 004 677 632
    #               213 724 000 000
    #            17 927 473 950 720
    number_of_items = len(weight_list)
    result = proc.knapsackGreProc(
        weight_list, volume_list, max_weight, number_of_items)
    print("Max Value:\t", result)
