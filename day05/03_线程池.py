from concurrent.futures import ThreadPoolExecutor


def func(name):  # 下载图片的任务
    for i in range(100):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(20) as t:
        # 10个任务
        # 把任务提交给线程池
        for i in range(10000):
            t.submit(func, f"任务{i}")
