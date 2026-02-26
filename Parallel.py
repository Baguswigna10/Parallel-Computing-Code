#Parallel

import time
import random
from multiprocessing import Pool, cpu_count

# Fungsi untuk menghitung subtotal
def partial_sum(sub_array):
    total = 0
    for num in sub_array:
        total += num
    return total

if __name__ == "__main__":
    N = 10_000_000
    data = [random.randint(1, 10) for _ in range(N)]

    jumlah_core = cpu_count()
    print("Jumlah core:", jumlah_core)

    # Membagi data sesuai jumlah core
    chunk_size = len(data) // jumlah_core
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    start = time.time()

    with Pool(jumlah_core) as p:
        results = p.map(partial_sum, chunks)

    total = sum(results)

    end = time.time()

    print("Total:", total)
    print("Waktu eksekusi (Parallel):", end - start, "detik")