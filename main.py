import simulation
import binpacking


if __name__ == '__main__':

    two_drives = simulation.rack_config(12, 7)  # 12 SATA18 and 7 RAID32
    # proc = KnapsackGreedy.FractionalKnapsack()
    drives = (two_drives.values())  # list of file dict per drive
    weight_list = list()
    for drive in drives:
        weight_list.extend(list(drive.values()))
        print('Drive: ', sum(list(drive.values())))
    print('\n\n\n')
    # volume_list = weight_list # for knapSack packing algo
    max_weight = 18000000000000
    # RAID32     35 856 004 677 632
    #               213 724 000 000
    # SAAT18     17 927 473 950 720
    number_of_items = len(weight_list)

    ### HUMAN SORTING ALGORHYTHM WITH INTERRUPTABLE OPTIMIZATION ###
    # 01 Take first disk
    # 02 calculate free space
    # 03 find largest file in whole set to replace smallest one on choosen drive
    # 04 replace the file
    # 05 repeat starting step 2 until it is possible to replace files on disk

    for disk_to_optimize in drives:  # Iterate over all disks in server
        # print (disk_to_optimize)
        smallest_plot = min(_ for _ in list(disk_to_optimize.values()))
        print('Smallest plot on the drive: ', smallest_plot)
        # Calcualate free space on the selected drive
        drive_taken_space = sum(list(disk_to_optimize.values()))
        if len(disk_to_optimize) > 200:  # check number of plots on disk to determine disk size
            # RAID32
            drive_free_space = 35856004677632 - drive_taken_space
        else:
            # SATA18
            drive_free_space = 17927473950720 - drive_taken_space
        print('Drive free space: ',  format(drive_free_space, ',').replace(',', ' ').replace('.', ','))


    # ### BIN PACKING SOLUTION ###
    # result = binpacking.to_constant_volume(volume_list, max_weight)
    # # result = KnapSackDP_Printing.printknapSack(
    # #     weight_list, volume_list, max_weight, number_of_items)
    # # print("Max Value:\t", result)

    # # print("===== list\n", volume_list, "\n")
    # disk = int()

    # for i in result:
    #     disk += 1
    #     print(i)
    #     print('Disk ', disk)
    #     # print disk space in bytes separated decimals
    #     # print('Total files allocation size ', format(
    #     #     sum(i), ',').replace(',', ' ').replace('.', ','))
    #     print('Number of plots: ', len(i))
    #     print('Total disk space taken: ', format(sum(i), ',').replace(
    #         ',', ' ').replace('.', ','), '\n\n\n')
