import threading
import time

# 新建事件对象，默认_flag为False
signal = threading.Event()

def f1():

    time.sleep(2)
    # 将_flag设置为True
    signal.set()
    print(f"this is {f1.__name__}")

def f2():

    # 虽然f1()主动阻塞了两秒，但是因为f1()足赛期间，_flag为False,所以f2()一直等待，知道f1()将_flag设置为True
    # 如果_flag为Ture,程序继续向下运行，否则，等待，直到_flag为False
    signal.wait()
    print(f"this is {f2.__name__}")

    # 重新将_flag设置为False
    signal.clear()

if __name__ == "__main__":

    t1 = threading.Thread(target=f1,args=())
    t2 = threading.Thread(target=f2,args=())
    t2.start()
    t1.start()
