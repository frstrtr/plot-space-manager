import simulation
import binpacking


if __name__ == '__main__':

    two_drives = simulation.rack_config(12, 7)
    # proc = KnapsackGreedy.FractionalKnapsack()
    drives = (two_drives.values())  # list of file dict per drive
    weight_list = list()
    for drive in drives:
        weight_list.extend(list(drive.values()))
        print('Drive: ', sum(list(drive.values())))
    volume_list = weight_list
    max_weight = 18000000000000
    # RAID32     35 856 004 677 632
    #               213 724 000 000
    # SAAT18     17 927 473 950 720
    number_of_items = len(weight_list)
    result = binpacking.to_constant_volume(volume_list, max_weight)
    # result = KnapSackDP_Printing.printknapSack(
    #     weight_list, volume_list, max_weight, number_of_items)
    # print("Max Value:\t", result)

    # print("===== list\n", volume_list, "\n")
    disk = int()

    for i in result:
        disk += 1
        print(i)
        print('Disk ', disk)
        print('Number of plots: ', len(i))
        print('Total disk space taken: ', sum(i), '\n\n\n')
