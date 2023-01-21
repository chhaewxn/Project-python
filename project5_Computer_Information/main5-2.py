import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f"cpu속도: {cpu_current_ghz}GHz")

cpu_core = psutil.cpu_count(logical=False)
print(f"코어: {cpu_core} 개")

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print(f'메모리: {memory_total}GB')

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f'디스크크기: {disk_total}GB')
    # 디스크는 하나가 아닌 여러 개가 있을 수 있으므로 찾은 수 만큼 출력한다.

net = psutil.net_io_counters()
sent = round(net.bytes_sent/1024**2, 1)
recv = round(net.bytes_recv/1024**2, 1)
print(f'보내기: {sent}MB   받기: {recv}MB')
# 네트워크를 통해 보내고 받은 데이터를 크기를 MB단위로 출력한다. 보내고 받은 데이터는 누적데이터의 값이다.
