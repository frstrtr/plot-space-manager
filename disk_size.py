import shutil

total, used, free = shutil.disk_usage("/")

print("Total: %d B" % (total))  # // (2**30)))
print("Used: %d B" % (used))  # // (2**30)))
print("Free: %d B" % (free))  # // (2**30)))

# TODO Get drives mount points from /mnt folder

DRIVE = "/mnt"

# 18TB Drive ext4 with journal
# SIZE 17 999 671 066 624B
# 12 x k33
# the rest for k32
# TODO check shutil.disk_usage for // total, used, free = shutil.disk_usage("/")
total, used, free = shutil.disk_usage(DRIVE)
SATA18_VOLUME = total
#               17999671066624 B DELL parted
#               18000174383104 B DELL smartctl
#                    503316480 B DELTA
#               17926972764160 B DELL shutil.disk_usage
#               17927473950720 B HP shutil.disk_usage

# 32TB RAID0 2x18 Drive ext4 with journal
# SIZE 36 000 348 766 208B
# 8 x k33
# the rest for k32
# TODO check shutil.disk_usage for // total, used, free = shutil.disk_usage("/")
total, used, free = shutil.disk_usage(DRIVE)
RAID32_VOLUME = total
#               36000348766208