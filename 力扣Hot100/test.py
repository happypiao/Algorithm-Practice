import threading


def single(cls):
    instance = {}
    lock = threading.Lock()

    def wrapper(*args, **kwargs):
        # 第一重检查：快速判断实例是否已存在
        if cls not in instance:
            # 第二重检查：加锁确保只有一个线程创建实例
            with lock:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
                    return instance[cls]
        return instance[cls]

    return wrapper
