import os
import sys

# assign directory
# directory = '/mnt/sata18-1'

# iterate over files in
# that directory
plot_dir_data = dict()

# s = os.statvfs(directory)
s = os.statvfs(sys.argv[0])
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
print('Total disk space: ', total+dir_space_left)