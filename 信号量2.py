import threading
import time
import random

# 超市可可容纳的人数
max = 50

# 缓冲区，有界信号量句柄
s = threading.BoundedSemaphore(max)

# 定义顾客活动
def fun_customer(n):
    global activate_number
    s.acquire()
    activate_number += 1# 顾客尝试进入超市，若有空间则进入，超市可容纳数量减一，否则等待
    t = random.choice([i for i in range(1,30)])
    print(f'》》》第{n}位顾客进入超市，并待{t}秒\n')
    time.sleep(t)                                # 假设每个顾客随机在超市待1-5秒
    s.release()                                  # 顾客进入超市，超市可容纳数量加一
    print(f'《《《第{n}位顾客出超市\n')
    activate_number -= 1

if __name__ == "__main__":

    n = 0
    activate_number = 0
    while True:
        customer_thread = threading.Thread(target=fun_customer,args=(n,))
        customer_thread.start()                   # 不阻塞式调用
        n += 1
        time.sleep(1)
                # 一次允许一人通过，抽象为一秒钟只允许通过一人
        print(f'当前存活{activate_number}个线程')


