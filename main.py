# Penggunaan "end"

print("A", end=", ")
print("B", end=", ")
print("C", end=", ")
print()
print("X")
print("Y")
print("Z")


# Penggunaan separator

w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=", ")
print(w, x, y, z, sep="")
print(w, x, y, z, sep=":")
print(w, x, y, z, sep=" ---- ")


# Penggunaan string format

print(0, 12**0)
print(1, 12**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

print("{0:>} {1:>16}" .format(0, 10**0))
print("{0:>} {1:>16}" .format(0, 10**1))
print("{0:>} {1:>16}" .format(0, 10**2))
print("{0:>} {1:>16}" .format(0, 10**3))
print("{0:>} {1:>16}" .format(0, 10**4))
print("{0:>} {1:>16}" .format(0, 10**5))
print("{0:>} {1:>16}" .format(0, 10**6))
print("{0:>} {1:>16}" .format(0, 10**7))
print("{0:>} {1:>16}" .format(0, 10**8))
print("{0:>} {1:>16}" .format(0, 10**9))
print("{0:>} {1:>16}" .format(0, 10**10))


# Penggunaan string format dan konversi

a = input("Masukan nilai a : ")
b = input("Masukan nilai b : ")
print("Variable a = ", a)
print("Variable b = ", b)

# # print("hasil penggabungan {0} & {1} = %d".format(a, b) %(a + b))

a = int(a)
b = int(b)
print("hasil penjumlahan {0} + {1} = %d ".format(a, b) %(a + b))
print("hasil penjumlahan {0} // {1} = %d ".format(a, b) %(a // b))


# Latihan 3

print(end="\n")

print("{0:>9}" .format("*"))
print("{0:>10}" .format("***"))
print("{0:>11}" .format("*****"))
print("{0:>12}" .format("*******"))
print("{0:>13}" .format("*********"))
print("{0:>12}" .format("*******"))
print("{0:>11}" .format("*****"))
print("{0:>10}" .format("***"))
print("{0:>9}" .format("*"))

print(end="\n")