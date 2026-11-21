
import psutil
import platform

CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 90

print("===== SERVER HEALTH MONITOR =====")

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent

if platform.system() == "Windows":
    disk = psutil.disk_usage("C:\\").percent
else:
    disk = psutil.disk_usage("/").percent

print("CPU Usage:", cpu, "%")
print("RAM Usage:", ram, "%")
print("Disk Usage:", disk, "%")

if cpu > CPU_LIMIT or ram > RAM_LIMIT or disk > DISK_LIMIT:
    print("Status: WARNING")
else:
    print("Status: HEALTHY")