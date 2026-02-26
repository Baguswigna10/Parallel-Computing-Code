#Single

import time
import random

# Membuat data besar
N = 10_000_000
data = [random.randint(1, 10) for _ in range(N)]

start = time.time()

total = 0
for i in range(len(data)):
    total += data[i]

end = time.time()

print("Total:", total)
print("Waktu eksekusi (Single):", end - start, "detik")