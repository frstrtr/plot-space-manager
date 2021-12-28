import random
from datetime import datetime

# plot size simulation
### K32 ###
K32_UPPER = 108836365547
K32_LOWER = 108716934884
# from 103 691 000 kBytes to 103 795 999 kBytes
# k32 = random.randint(K32_UPPER, K32_LOWER)

### K33 ###
K33_UPPER = 224315100209
K33_LOWER = 224103462844
# from 213 724 000 kBytes to 213 970 999 kBytes
# k33 = random.randint(K33_UPPER, K33_LOWER)


def pseudo_hash():
    bits = random.getrandbits(256)
    bits_hex = hex(bits)
    return bits_hex[2:]  # get rid of 0x


def time_stamp():
    # datetime object containing current date and time
    now = datetime.now()
    return now.strftime("%Y-%m-%d-%H-%M-")

### GENERATING PLOTS ###


def plot_the_drive(drive):
    # sata18 - 140 x k32 + 12 x k33
    # raid32 - 313 x k32 + 8 x k33
    # plots directories simulation init
    # naming plot-k33-2021-12-24-22-04-88c5dbd12e5536f81f93cd89bdd3617c9276ca5acd8bc32eab64bd68b30d9c60.plot
    plots_dict = dict()
    # plots k32
    if drive == SATA18:
        k32_count, k33_count = 140, 12
    else:
        k32_count, k33_count = 313, 8

    # k32 plots
    for _ in range(0, k32_count):
        file_name = 'plot-k32-' + time_stamp() + pseudo_hash()+'.plot'
        plots_dict[file_name] = random.randint(K32_LOWER, K32_UPPER)

    # k33 plots
    for _ in range(0, k33_count):
        file_name = 'plot-k33-'+time_stamp()+pseudo_hash()+'.plot'
        plots_dict[file_name] = random.randint(K33_LOWER, K33_UPPER)

    return plots_dict

### GENERATING SATA18 and RAID32 drives file sets ###
# TODO dummy drives population as dictionary
# sata18 - 140 x k32 + 12 x k33 - 152 TOTAL
# raid32 - 313 x k32 + 8 x k33 - 321 TOTAL


### GENERATING MOUNT POINTS ###

MOUNT_DIR = "/mnt"
SATA18 = "/sata18-"
RAID32 = "/raid32-"

SATA18_COUNT = 13
RAID32_COUNT = 8


def rack_config(sata18=SATA18_COUNT, raid32=RAID32_COUNT):
    drive_list = list()
    for i in range(1, sata18+1):
        drive_list.append(MOUNT_DIR+SATA18+str(i)+"/")
    for i in range(1, raid32+1):
        drive_list.append(MOUNT_DIR+RAID32+str(i)+"/")

    # Sefver mounted drives configuration
    rack_config = dict.fromkeys(drive_list)

    for k in rack_config.keys():
        if '18' in k:
            rack_config[k] = plot_the_drive(SATA18)
        else:
            rack_config[k] = plot_the_drive(RAID32)
    return rack_config


if __name__ == '__main__':

    print(rack_config())
