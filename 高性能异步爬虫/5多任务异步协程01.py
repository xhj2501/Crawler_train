import asyncio
import time


async def request(url):
    print("正在下载", url)
    # 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    # time.sleep(2)
    await asyncio.sleep(2)  # 当在asyncio中遇到阻塞操作必须进行手动挂起，即使用await关键字
    print("下周完毕", url)


start = time.time()
urls = [
    "www.baidu.com",
    "www.sogou,com",
    "www.uestc.edu.cn"
]

# 任务列表：存放多个任务对象
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))  # 不能直接传递列表，需要将任务列表封装到wait中

print(time.time() - start)
