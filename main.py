from cmath import log
import simulation
# import binpacking

SATA18_SIZE = 17927473950720
RAID32_SIZE = 35856004677632

PLOT_SIZE_THRESHOLD = 200000000000


class Server():

    pass


class Drive():

    # SATA18 17 927 473 950 720 bytes
    SATA18_SIZE = 17927473950720
    # RAID32 35 856 004 677 632 bytes
    RAID32_SIZE = 35856004677632


class Plot():

    SIZE_THRESHOLD = 200000000000
    size = 1

    def __init__(self) -> None:
        """ Init method for the class"""
        pass


def prnf(title, value_to_dec_split):
    """
    Prints decimal with space separators between 1000'th group
    """
    print(title, end='')
    print(format(value_to_dec_split, ',').replace(',', ' ').replace('.', ','))
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


def check_drive_free_space(disk_to_optimize):
    drive_taken_space = sum(list(disk_to_optimize.values()))
    # prnf('Drive space taken:                      ', drive_taken_space)

    # Calculate drive free space depanding on its size
    if len(disk_to_optimize) > 200:  # check number of plots on the disk to determine disk size
        # RAID32
        drive_free_space = RAID32_SIZE - drive_taken_space
    else:
        # SATA18
        drive_free_space = SATA18_SIZE - drive_taken_space
    # prnf('Drive free space:     ', drive_free_space)
    return drive_free_space


if __name__ == '__main__':

    two_drives = simulation.rack_config(12, 0)  # 12 SATA18 and 0 RAID32

    server_drives_list = list(two_drives.values())

    # RAID32     35 856 004 677 632
    #               213 724 000 000
    # SAAT18     17 927 473 950 720

    ### HUMAN SORTING ALGORHYTHM WITH INTERRUPTABLE OPTIMIZATION ###

    # pre algo: determine optimal count of different-sized plots for coarse optimization for plot splitting
    # for example N x Raid32 + NN x SATA18 per drive

    # ALGORHYTHM DESCRIPTION PSEUDOCODE
    # 01 Take first disk
    # 02 calculate free space
    # 03 find largest file in whole set to replace smallest one on choosen drive
    # 04 replace the file
    # 05 repeat starting step 2 until it is possible to replace files on disk
    # 06 when the next plot is oversize drive space, seek for the last one plot size
    #    to max fill the rest of space on the drive
    # 07 FINISHED optimization of DRIVE 1
    # 08 RESTART for the NEXT drive until there is no optimized drives on the disk.

    __ = int()
    drive_free_space = 1

    # remember how many drives left unoptimized
    server_drives_list_left = server_drives_list.copy()

    for disk_to_optimize in server_drives_list:  # Iterate over all disks in server

        # remove current drive from unoptimized drives list
        server_drives_list_left.remove(disk_to_optimize)

        # Create list of all plots left on unoptimized drives
        server_all_plots_left_size_list = update_whole_plots_set(
            server_drives_list_left)

        # create two lists with all plots, splitted by 100Tb and 200Tb sizes
        server_k32_plot_size_100_list = list()  # all sizes of 100Gb
        server_k33_plot_size_200_list = list()  # all sizes of 200Gb
        for plot_size_to_split in server_all_plots_left_size_list:
            if plot_size_to_split > PLOT_SIZE_THRESHOLD:
                server_k33_plot_size_200_list.append(plot_size_to_split)
            else:
                server_k32_plot_size_100_list.append(plot_size_to_split)
        __ += 1
        # Drive number
        print('Drive Bay:   ', __)

        # split disk dict in to two dictioanry
        # with different plot sizes
        plots_100tb = dict()
        plots_200tb = dict()

        for plot_to_distribute in disk_to_optimize:
            if disk_to_optimize[plot_to_distribute] > PLOT_SIZE_THRESHOLD:
                plots_200tb[plot_to_distribute] = disk_to_optimize[plot_to_distribute]
            else:
                plots_100tb[plot_to_distribute] = disk_to_optimize[plot_to_distribute]

        drive_free_space = check_drive_free_space(disk_to_optimize)
        print('K32 (100Tb) plots: ', len(plots_100tb))
        print('K33 (200Tb) plots: ', len(plots_200tb), '\n')
        prnf('Used drive space: ', sum(disk_to_optimize.values()))
        prnf('Drive free space:      ', drive_free_space)
        print('\n')

        biggest_k32_plot_size_100Gb_on_the_server = 1
        smallest_plot = 0
        # optimizing 100Gb plots allocation
        while ((drive_free_space > 0) and (biggest_k32_plot_size_100Gb_on_the_server > smallest_plot)):
            # print (disk_to_optimize)

            # Smallest plot
            smallest_plot = min(_ for _ in list(plots_100tb.values()))
            # prnf('Smallest k32 plot on the DRIVE:            ', smallest_plot)

            # TODO: remove 200Gb check
            biggest_k32_plot_size_100Gb_on_the_server = max(
                _ for _ in server_k32_plot_size_100_list if _ < PLOT_SIZE_THRESHOLD)
            # prnf('Biggest k32 plot size 100Gb on the SERVER: ',
            #  biggest_k32_plot_size_100Gb_on_the_server)

            # Calcualate free space on the selected drive
            drive_taken_space = sum(list(disk_to_optimize.values()))
            # prnf('Drive space taken:                      ', drive_taken_space)

            # Calculate drive free space depanding on its size
            drive_free_space = check_drive_free_space(disk_to_optimize)

            # Remove smallest plot
            # From disk to optimize
            # From 100Tb plots list
            for plot_to_remove in disk_to_optimize.keys():
                if disk_to_optimize[plot_to_remove] == smallest_plot:
                    # prnf('Removing smallest plot from the DRIVE: ', smallest_plot)
                    disk_to_optimize.__delitem__(plot_to_remove)
                    # remove found plot from list of 100Tb plots for this drive
                    # print(
                    # 'Removing found plot from the list of 100Tb plots on this drive')
                    plots_100tb.__delitem__(plot_to_remove)
                    # TODO: add removed plot to origin disk of the biggest plot?

                    # remove biggest 100Tb plot from all_drives_list
                    # print('Removing biggest 100Tb plot from SERVER list...')
                    break
            for drive in server_drives_list_left:
                if biggest_k32_plot_size_100Gb_on_the_server in drive.values():
                    for k1 in drive.keys():
                        if drive[k1] == biggest_k32_plot_size_100Gb_on_the_server:
                            biggest_plot_to_remove_name = k1
                            # print(
                            # 'Biggest k32 plot on the SERVER to remove: ', k1)
                            # remove found biggest plot from source drive
                            # print(
                            # 'Removing found biggest plot from the source drive')
                            drive.__delitem__(k1)
                            # Adding smallest plot from optimized drive
                            drive[plot_to_remove] = smallest_plot
                            # remove found biggest plot from the 100Tb plots dict of SERVER
                            # print(
                            # 'Removing found biggest k32 plot from the 100Tb plots dict of SERVER')
                            server_k32_plot_size_100_list.remove(
                                biggest_k32_plot_size_100Gb_on_the_server)
                            # TODO: update server drives list with new drive state!
                            # add found biggest plot to the current drive
                            # print(
                            # 'Adding found biggest plot to the current drive')
                            disk_to_optimize[k1] = biggest_k32_plot_size_100Gb_on_the_server
                            # print(
                            # 'Adding found biggest plot to the drive 100Tb list')
                            plots_100tb[k1] = biggest_k32_plot_size_100Gb_on_the_server

                            # prnf('Before biggest plot added: ',
                            #  sum(plots_100tb.values())+smallest_plot)

                            plots_100tb[k1] = biggest_k32_plot_size_100Gb_on_the_server

                            # prnf('After biggest plot added: ',
                            #  sum(plots_100tb.values()))

                            total_disk_space_taken = sum(
                                plots_100tb.values())+sum(plots_200tb.values())
                            prnf(
                                'Total disk space taken after plot replacement: ', total_disk_space_taken)
                            # TODO: update whole_set_of_plots
                            # print('Updating all plots list')
                            server_all_plots_left_size_list = update_whole_plots_set(
                                server_drives_list_left)

                            break  # TODO check if plots with same size persists on the other drives
                    drive_free_space = check_drive_free_space(
                        disk_to_optimize)

                    break

            # prnf('Drive free space: ', drive_free_space)
            # print('\n')

        with open(str(__)+'.txt', 'w') as f:
            print(disk_to_optimize, file=f)
            print('Drive free space: ', drive_free_space, file=f)
