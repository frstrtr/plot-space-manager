import os
import sys

if __name__ == '__main__':
    # assign directory
    if len(sys.argv) == 1: # check for arguments and if there is no arguments - exit
        print ('Please provide path to check first!')
        exit()

    directory = sys.argv[1]
    directory2 = sys.argv[2]

    # iterate over files in
    # that directory
    plot_dir_data = dict()
    s = os.statvfs(directory)
    dir_space_left = (s.f_bavail * s.f_frsize) / 1024

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):

            # print(f, end='::')
            file_size = os.path.getsize(f)
            # print(file_size)

            plot_dir_data[f]=file_size

    values = plot_dir_data.values()
    #Return values of a dictionary

    total = sum(values)

    print(plot_dir_data)
    print('All files summary size: ',total)
    print('Space left: ', dir_space_left)