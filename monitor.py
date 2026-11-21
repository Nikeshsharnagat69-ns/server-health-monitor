
import psutil

print("===== SERVER HEALTH MONITOR =====")

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("C:\\").percent

print("CPU Usage:", cpu, "%")
print("RAM Usage:", ram, "%")
print("Disk Usage:", disk, "%")

if cpu > 80 or ram > 80 or disk > 90:
    print("Status: WARNING")
else:
    print("Status: HEALTHY")
