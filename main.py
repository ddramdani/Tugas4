sisi = 10
# 4.Ganjil saja
print("awal while")
spasi = int(sisi/2)
count = 1
while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1 
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break
while True:
    if(count%2):
        spasi += 1
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0: 
        break
print("akhir dari while")