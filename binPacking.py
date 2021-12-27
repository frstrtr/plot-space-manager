import binpacking

b = { 'a': 10, 'b': 10, 'c':11, 'd':1, 'e': 2,'f':7 }
bins = binpacking.to_constant_bin_number(b,4)
print("===== dict\n",b,"\n",bins)

b = list(b.values())
bins = binpacking.to_constant_volume(b,11)
print("===== list\n",b,"\n",bins)