import simulation
# import binpacking

SATA18_SIZE = 17927473950720
RAID32_SIZE = 35856004677632


def prnf(string_in):
    """
    Prints decimal with space separators between 1000'th group
    """
    print(format(string_in, ',').replace(',', ' ').replace('.', ','))
    return 0


def update_whole_plots_set(all_drives):
    plot_sizes_list = list()
    # all_drives_list = list()
    for drive in all_drives:
        # list of all plot sizes
        plot_sizes_list.extend(list(drive.values()))
        # list of dictionaries of all drives with k:v plot_name:plot_size
        # all_drives_list.append(drive)
    return plot_sizes_list


if __name__ == '__main__':

    two_drives = simulation.rack_config(12, 0)  # 12 SATA18 and 0 RAID32
    # proc = KnapsackGreedy.FractionalKnapsack()
    # list of file dict per drive
    server_drives_list = list(two_drives.values())

    # list of all plot sizes
    # weight_list = list()
    # server_drives_list = list()
    # disk = 0

    # for drive in drives:
    #     weight_list.extend(list(drive.values()))
    # all_drives_list.append(drive)
    #     print('Drive: ', sum(list(drive.values())))
    # print('\n\n\n')

    server_all_plots_size_list = update_whole_plots_set(server_drives_list)

    # RAID32     35 856 004 677 632
    #               213 724 000 000
    # SAAT18     17 927 473 950 720

    total_number_of_plots = len(server_all_plots_size_list)

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
    temp_plot_set = dict()  # temporary storage for plots moved from drive

    # create two lists with all plots, splitted by 100Tb and 200Tb sizes
    server_k32_plot_size_100_list = list()  # all sizes of 100Gb
    server_k33_plot_size_200_list = list()  # all sizes of 200Gb
    for plot_size_to_split in server_all_plots_size_list:
        if plot_size_to_split > 200000000000:
            server_k33_plot_size_200_list.append(plot_size_to_split)
        else:
            server_k32_plot_size_100_list.append(plot_size_to_split)

    for disk_to_optimize in server_drives_list:  # Iterate over all disks in server

        # split disk dict in to two dictioanry
        # with different plot sizes
        plots_100tb = dict()
        plots_200tb = dict()

        for plot_to_distribute in disk_to_optimize:
            if disk_to_optimize[plot_to_distribute] > 200000000000:
                plots_200tb[plot_to_distribute] = disk_to_optimize[plot_to_distribute]
            else:
                plots_100tb[plot_to_distribute] = disk_to_optimize[plot_to_distribute]

        # optimizing 18TB allocation
        while (drive_free_space > 0):
            # print (disk_to_optimize)
            __ += 1
            smallest_plot = min(_ for _ in list(plots_100tb.values()))
            biggest_plot = max(_ for _ in list(plots_100tb.values()))

            # Drive number
            print('Drive Bay: ', __)

            # Smallest plot
            print('Smallest 100Tb plot on the drive: ', end='')
            prnf(smallest_plot)

            # Biggest plot
            print('Biggest 100Tb plot on the drive: ', end='')
            prnf(biggest_plot)

            # Calcualate free space on the selected drive
            drive_taken_space = sum(list(disk_to_optimize.values()))

            # Calculate drive free space depanding on its size
            if len(disk_to_optimize) > 200:  # check number of plots on disk to determine disk size
                # RAID32
                drive_free_space = RAID32_SIZE - drive_taken_space
            else:
                # SATA18
                drive_free_space = SATA18_SIZE - drive_taken_space

            print('Drive free space: ',  format(drive_free_space,
                                                ',').replace(',', ' ').replace('.', ','))

            # Biggest plot in set
            biggest_100tb_plot_on_disk = max(plots_100tb.values())
            print('Biggest 100Tb plot in set: ', end='')
            prnf(biggest_100tb_plot_on_disk)

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
                    # remove found plot from list of 100Tb plots for this drive
                    plots_100tb.__delitem__(k)
                    # add removed plot to origin disk of the biggest plot?
                    #
                    temp_plot_set[k] = smallest_plot

                    # remove biggest 100Tb plot from all_drives_list
                    for drive in server_drives_list:
                        for k1 in drive.keys():
                            if drive[k1] == biggest_100tb_plot_on_disk:
                                biggest_plot_to_remove_name = k1
                                # remove found biggest plot from source drive
                                drive.__delitem__(k1)
                                # add found biggest plot to the current drive
                                disk_to_optimize[k1] = biggest_100tb_plot_on_disk
                                # remove found biggest plot from the 100Tb plots dict of SERVER
                                server_k32_plot_size_100_list.remove(
                                    biggest_100tb_plot_on_disk)
                                plots_100tb[k1] = biggest_100tb_plot_on_disk

                                # TODO: update whole_set_of_plots
                                server_all_plots_size_list = update_whole_plots_set(
                                    server_drives_list)

                                break  # TODO check if plots with same size persists on the other drives

                    # print(temp_plot_set)
                    print('.', end='')

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
