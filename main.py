import psutil


# CPU usage in %
def main():
    if __name__ == "__main__":
        main()


def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.5)


print("Le CPU est à {} %".format(get_cpu_usage_pct()))


# RAM usage in %
def get_ram_usage_pct():
    return psutil.virtual_memory().percent


print("La RAM est à {} %".format(get_ram_usage_pct()))

# HD usage in %
print("-" * 40, "Info du disque", "-" * 40)


def get_disk_usage_pct():
    return psutil.disk_usage('/')


print("Le disque est à {} ".format(get_disk_usage_pct()))


def get_disk_usage():
    return int(psutil.swap_memory().used)


print("Usage du disque est à {} MB".format(int(get_disk_usage() / 1024 / 1024)))


def get_disk_total():
    return int(psutil.swap_memory().total)


print("Total du disque {} MB".format(int(get_disk_total() / 1024 / 1024)))


def get_disk_usage_pct():
    return psutil.swap_memory().percent


print("Espace utilisé du sique {} %".format(get_disk_usage_pct()))
