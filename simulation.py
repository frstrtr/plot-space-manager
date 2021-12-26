import random

# chars a..z
CHAR_START = 97
CHAR_END = 122

# plot size simulation
### K32 ###
K32_UPPER = 103691000
K32_LOWER = 103795999
# from 103 691 000 kBytes to 103 795 999 kBytes
k32 = random.randint(K32_UPPER, K32_LOWER)

### K33 ###
K33_UPPER = 213724000
K33_LOWER = 213970999
# from 213 724 000 kBytes to 213 970 999 kBytes
k33 = random.randint(K33_UPPER, K33_LOWER)

# print(k32, 'k32')
# print(k33, 'k33')

### GENERATING PLOTS ###


def plot_the_drive(drive):
    # sata18 - 140 x k32 + 12 x k33
    # raid32 - 313 x k32 + 8 x k33
    # plots directories simulation init
    plots_dict = dict()
    # plots k32
    if drive == 'sata18':
        k32_count, k33_count = 140, 12
    else:
        k32_count, k33_count = 313, 8

    for i in range(0, k32_count):
        file_name = chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END)) + \
            chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END)) + \
            chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END)) + \
            chr(random.randint(CHAR_START, CHAR_END))

        plots_dict['\\'+file_name +
                   '.plot'] = random.randint(K32_UPPER, K32_LOWER)

    # 12 plots k33
    for i in range(0, k33_count):
        file_name = chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END)) + \
            chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END)) + \
            chr(random.randint(CHAR_START, CHAR_END))+chr(random.randint(CHAR_START, CHAR_END)) + \
            chr(random.randint(CHAR_START, CHAR_END))

        plots_dict['\\'+file_name +
                   '.plot'] = random.randint(K33_UPPER, K33_LOWER)

    print(len(plots_dict))

### GENERATING SATA18 and RAID32 drives file sets ###
# TODO dummy drives population as dictionary
# sata18 - 140 x k32 + 12 x k33
# raid32 - 313 x k32 + 8 x k33


### GENERATING MOUNT POINTS ###

MOUNT_DIR = "/mnt"
SATA18 = "/sata18-"
RAID32 = "/raid32-"

SATA18_COUNT = 13
RAID32_COUNT = 8

drive_list = list()
for i in range(1, SATA18_COUNT):
    drive_list.append(MOUNT_DIR+SATA18+str(i)+"/")
for i in range(1, RAID32_COUNT):
    drive_list.append(MOUNT_DIR+RAID32+str(i)+"/")

# Sefver mounted drives configuration
# rack_config = dict.fromkeys(drive_list)

# for k, v in rack_config:
#     if '18' in k:
#         rack_config[k

plot_the_drive('sata18')

print()
