
import psutil
import platform

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

if cpu > 80 or ram > 80 or disk > 90:
    print("Status: WARNING")
else:
    print("Status: HEALTHY")
