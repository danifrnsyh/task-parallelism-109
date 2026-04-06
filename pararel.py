import threading
import time

def fetch_info_109():
    for i in range(1, 4):
        print(f"[NRP 109 - FETCH] Mengambil data ke-{i}")
        time.sleep(1)

def compute_info_109():
    for i in range(1, 4):
        print(f"[NRP 109 - COMPUTE] Memproses data ke-{i}")
        time.sleep(1)

def save_info_109():
    for i in range(1, 4):
        print(f"[NRP 109 - SAVE] Menyimpan data ke-{i}")
        time.sleep(1)

print("PROGRAM TASK PARALLELISM NRP 109 DIMULAI")

t1 = threading.Thread(target=fetch_info_109)
t2 = threading.Thread(target=compute_info_109)
t3 = threading.Thread(target=save_info_109)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("SEMUA PROSES SELESAI")

