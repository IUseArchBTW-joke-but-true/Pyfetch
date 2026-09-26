#  Lite-Fastfetch, python edition (personal project)


import os
import socket
import platform
import subprocess
import shutil

def User():
    print(f"\nUser: {os.getlogin()}")

def Hostname():
    print(f"Hostname: {socket.gethostname()}")

def OS():
    print(f"OS: {platform.system()}")

def Distro():
    os_info = platform.freedesktop_os_release()
    print(f"Distro: {os_info["PRETTY_NAME"]}")

def Kernel():
    print(f"Kernel: {platform.release()}")

def CPU():
    with open("/proc/cpuinfo") as file:
        for line in file:
            if line.startswith("model name"):
                cpu_parts = line.split(":", 1)
                print(f"CPU: {cpu_parts[1].strip()}")
                break

def RAM():
    with open("/proc/meminfo") as file:
        for line in file:
            if line.startswith("MemTotal"):
                ram1_parts = line.split(":", 2)
                total_ram = ram1_parts[1].strip().split("kB", 1)[0]
    with open("/proc/meminfo") as file:
        for line in file:
            if line.startswith("MemAvailable"):
                ram2_parts = line.split(":", 1)
                available_ram = ram2_parts[1].strip().split("kB", 1)[0]
    used_ram = float(total_ram) - float(available_ram)  # pyright: ignore[reportPossiblyUnboundVariable]
    used_ram_GiB = used_ram / (1024 ** 2)
    total_ram_GiB = float(total_ram) / (1024 ** 2)  # pyright: ignore[reportPossiblyUnboundVariable]
    ram_percentage = float(used_ram) / float(total_ram) * 100  # pyright: ignore[reportPossiblyUnboundVariable]
    print(f"RAM: {used_ram_GiB:.2f} GiB / {total_ram_GiB:.2f} GiB ({ram_percentage:.2f} %)")

def Uptime():
    with open ("/proc/uptime") as file:
        for line in file:
            time_parts = line.split()
            idle_time_seconds = time_parts[0].strip()
    idle_time_minutes = int(float(idle_time_seconds) / 60)   # pyright: ignore[reportPossiblyUnboundVariable]
    hours = idle_time_minutes // 60
    minutes = idle_time_minutes % 60
    print(f"Uptime: {hours} hour(s), {minutes} minute(s)")

def WM_DE():
    WM_DE = os.environ.get("XDG_CURRENT_DESKTOP") or os.environ.get("XDG_SESSION_DESKTOP") or os.environ.get("DESKTOP_SESSION")
    print(f"DE/WM: {WM_DE}")

def Terminal():
    term = os.environ.get("TERM")
    print(f"Term: {term}")

def Shell():
    Shell = subprocess.check_output(["ps", "-p", str(os.getppid()), "-o", "comm="], text=True) .strip()
    print(f"Shell: {Shell}")

def Disk():
    usage = shutil.disk_usage("/")
    Total_disk_unformatted = usage.total
    Used_disk_unformatted = usage.used
    Free_disk_unformatted = usage.free
    Total_disk_formatted = Total_disk_unformatted / (1024 ** 3)
    Used_disk_formatted = Used_disk_unformatted / (1024 ** 3)
    Free_disk_formatted = Free_disk_unformatted / (1024 ** 3)  # pyright: ignore[reportUnusedVariable]
    Used_disk_percentage = Used_disk_unformatted / Total_disk_unformatted * 100
    print(f"Disk: {Used_disk_formatted:.2f} GiB / {Total_disk_formatted:.2f} GiB  ({Used_disk_percentage:.2f} %)")


print(f"\n")
print(f"                                           \n");
print(f"                                           \n");
print(f"████  █   █ █████ █████ █████  ███  █   █    .");
print(f"█░░░█  █ █ ░█░░░░░█░░░░░ ░█░░░█ ░░░ █░  █░   .");
print(f"████░░  █ ░ ████░░████░░░ █░░░█░ ░░░█████░░  .");
print(f"█░░░░ ░ █░ ░█░░░░ █░░░░   █░░ █░░   █░░░█░░  .");
print(f"█░░░░░  █░░ █░░░░░█████░  █░░  ███  █░░░█░░  .");
print(f"░░      ░░  ░░    ░░░░░   ░░   ░░░  ░░  ░░   .");
print(f"░       ░   ░     ░░░░░   ░    ░░░  ░   ░    .");
print(f"                                           \n");
print(f"                                           \n");
print(f"                                           \n");

print(User())
print(Hostname())
print(OS())
print(Distro())
print(Kernel())
print(CPU())
print(RAM())
print(Uptime())
print(WM_DE())
print (Terminal())
print(Shell())
print(Disk())
