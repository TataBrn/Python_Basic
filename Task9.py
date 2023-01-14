"""
Необходимо создать два параллельных потока,
каждый из которых выводил бы на экран числа от 10 до 1 в обратном порядке с интервалом в одну секунду.
В выводе должно быть понятно какая нить выполняется,
 и когда каждая из них начинает и заканчивает своё выполнение.
"""
import threading
import time


class MyTread(threading.Thread):
    def __init__(self, font, interval):
        super().__init__()
        self.daemon = True
        self.font = font
        self.interval = interval

    def run(self):
        print(f'{self.font}{self.name} started at {time.ctime()}\033[0m')
        for num in range(10, 0, -1):
            text = f'{self.name}: {num} '
            print(f"{self.font}{text}\033[0m")
            time.sleep(self.interval)
        print(f'{str(self.font)}{self.name} finished at {time.ctime()}\033[0m')


class MyNewTread(threading.Thread):
    def __init__(self, font, interval):
        super().__init__()
        self.daemon = True
        self.font = font
        self.interval = interval

    def run(self):
        print(f'{self.font}{self.name} started at {time.ctime()}\033[0m')
        s = 0
        for num in range(1, 11):
            s += num
            time.sleep(self.interval)
        text = f'{self.name}: S = {s} '
        print(f"{self.font}{text}\033[0m")
        print(f'{str(self.font)}{self.name} finished at {time.ctime()}\033[0m')


green_thread = MyTread("\033[32m", 1)
green_thread.start()

blue_thread = MyTread("\033[34m", 0.3)
blue_thread.start()

sum_thread = MyNewTread("\033[33m", 0.7)
sum_thread.start()

green_thread.join()
blue_thread.join()
sum_thread.join()
