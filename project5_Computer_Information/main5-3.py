import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    # cpu의 사용량을 1초동의 평균값을 구한다. interval의 시간을 조절하여 평균 구하는 시간을 조절한다.
    print(f'CPU사용량: {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3, 1)
    print(f'사용가능한 메모리: {memory_avail}GB')

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    # 현재의 값에서 이전의 값을 빼면 1초동안 보내는 데이터를 구할 수 있다.
    sent = round(curr_sent-prev_sent, 1)
    recv = round(curr_recv-prev_recv, 1)

    print(f'보내기: {sent}MB   받기: {recv}MB')

    # 이전의 값에 현재 값을 바인딩한다. 이전의 값을 가지고 있어야 현재값과 비교하여 1초 동안 얼마를 보내고 받았는지 계산 가능.
    prev_sent = curr_sent
    prev_recv = curr_recv
