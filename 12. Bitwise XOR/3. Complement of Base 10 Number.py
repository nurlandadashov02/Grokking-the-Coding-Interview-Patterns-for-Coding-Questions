num = 8

bit_count, n = 0, num

while n > 0:
    bit_count += 1
    n = n >> 1

all_bits_set = pow(2, bit_count) - 1

print(num ^ all_bits_set)

