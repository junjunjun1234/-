from threading import Thread

# def func():
#     print(123)
#
#
# if __name__ == '__main__':  # 主线程
#     t = Thread(target=func)  # 创建一个子线程
#     t.start()  # 启动一个线程
#     print(123)


# def func():
#     for i in range(1000):
#         print("子线程", i)
#
#
# if __name__ == '__main__':  # 主线程
#     t = Thread(target=func)  # 创建一个子线程
#     t.start()  # 启动一个线程
#     for i in range(1000):
#         print("主线程", i)


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':  # 主线程
    t1 = Thread(target=func, args=("周润发",))  # 创建一个子线程
    t1.start()  # 启动一个线程

    t2 = Thread(target=func, args=("周杰伦",))  # 创建一个子线程
    t2.start()  # 启动一个线程
