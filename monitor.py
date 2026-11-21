
import psutil
import platform
import logging

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)
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

    if cpu > CPU_LIMIT:
        print("ALERT: CPU usage is too high!")

    if ram > RAM_LIMIT:
        print("ALERT: RAM usage is too high!")

    if disk > DISK_LIMIT:
        print("ALERT: Disk usage is too high!")

    logging.warning("Server health is WARNING")

else:
    print("Status: HEALTHY")
    logging.info("Server health is HEALTHY")