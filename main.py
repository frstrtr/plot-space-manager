import simulation
import binpacking


def prnf(string_in):
    print(format(string_in, ',').replace(',', ' ').replace('.', ','))
    return 0

def update_whole_plots_set(all_drives):
    weight_list = list()
    all_drives_list = list()
    for drive in all_drives:
        # list of all plot sizes
        weight_list.extend(list(drive.values()))
        # list of dictionaries of all drives with k:v plot_name:plot_size
        all_drives_list.append(drive)
    return weight_list, all_drives_list

if __name__ == '__main__':

    two_drives = simulation.rack_config(12, 0)  # 12 SATA18 and 0 RAID32
    # proc = KnapsackGreedy.FractionalKnapsack()
    drives = list(two_drives.values())  # list of file dict per drive

    # list of all plot sizes
    # weight_list = list()
    all_drives_list = list()
    # disk = 0

    # for drive in drives:
    #     weight_list.extend(list(drive.values()))
        # all_drives_list.append(drive)
    #     print('Drive: ', sum(list(drive.values())))
    # print('\n\n\n')

    weight_list, all_drives_list = update_whole_plots_set(drives)

    # volume_list = weight_list # for knapSack packing algo
    # max_weight = 18000000000000
    # RAID32     35 856 004 677 632
    #               213 724 000 000
    # SAAT18     17 927 473 950 720

    number_of_items = len(weight_list)

    ### HUMAN SORTING ALGORHYTHM WITH INTERRUPTABLE OPTIMIZATION ###

    # pre algo: determine optimal count of different-sized plots for coarse optimization for plot splitting
    # for example N x Raid32 + NN x SATA18 per drive

    # 01 Take first disk
    # 02 calculate free space
    # 03 find largest file in whole set to replace smallest one on choosen drive
    # 04 replace the file
    # 05 repeat starting step 2 until it is possible to replace files on disk
    __ = int()
    drive_free_space = 1
    temp_plot_set = dict() # temporary storage for plots moved from drive

    for disk_to_optimize in drives:  # Iterate over all disks in server
        while (drive_free_space > 0):
            # print (disk_to_optimize)
            __ += 1
            smallest_plot = min(_ for _ in list(disk_to_optimize.values()))
            biggest_plot = max(_ for _ in list(disk_to_optimize.values()))

            # Drive number
            print('Drive Bay: ', __)

            # Smallest plot among all drives
            print('Smallest plot on the drive: ', end='')
            prnf(smallest_plot)

            # Biggest plot among all drives
            print('Biggest plot on the drive: ', end='')
            prnf(biggest_plot)

            # Calcualate free space on the selected drive
            drive_taken_space = sum(list(disk_to_optimize.values()))
            if len(disk_to_optimize) > 200:  # check number of plots on disk to determine disk size
                # RAID32
                drive_free_space = 35856004677632 - drive_taken_space
            else:
                # SATA18
                drive_free_space = 17927473950720 - drive_taken_space

            print('Drive free space: ',  format(drive_free_space,
                                                ',').replace(',', ' ').replace('.', ','))
            
            # Biggest plot in set
            biggest_plot_in_set = max(weight_list)
            print ('Biggest plot in set: ', end='')
            prnf(biggest_plot_in_set)

            # move plot from disk plot list to the whole set plot
            # disk_to_optimize.plot <-> weight_list.plot
            # check for plot duplicates
            # disk_to_optimize
            # weight_list
            # check for biggest 100Gb plot and 200Gb plot
            # remember this plot by removing it from the set

            # disk_to_optimize.remove(smallest_plot) # dictionary
            for k in disk_to_optimize.keys():
                if disk_to_optimize[k] == smallest_plot:
                    plot_to_remove_name = k
                    disk_to_optimize.__delitem__(k)
                    temp_plot_set[k]=smallest_plot
                    # remove this plot from all_drives_list
                    for drive in all_drives_list:
                        for k1 in drive.keys():
                            if drive[k1] == biggest_plot_in_set:
                                biggest_plot_to_remove_name = k1
                                drive.__delitem__(k1)
                                disk_to_optimize[k1] = biggest_plot_in_set
                                # TODO: update whole_set_of_plots
                                weight_list,all_drives_list = update_whole_plots_set(drives)

                                break # TODO check if plots with same size persists on the other drives

                    # print(temp_plot_set)
                    print('.',end='')
                    
                    break
            
            """
            disk_to_optimize.remove(smallest_plot)
            temp_plot_set.append(smallest_plot)
            disk_to_optimize.append(biggest_plot_in_set) # we need to get same class sized plot
            weight_list.remove(biggest_plot_in_set) # we need to get same class sized plot
            print('\n')
            """

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
