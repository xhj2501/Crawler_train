import requests
import asyncio
import time
import aiohttp  # 使用该模块中的Clientsession

start = time.time()
urls = [
    "http://127.0.0.1:5000/xhj",
    "http://127.0.0.1:5000//Xhj",
    "http://127.0.0.1:5000/jxh"
]


async def get_page(url):
    # print("正在下载", url)
    #  requsets.get是基于同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    #  response = requests.get(url=url)
    # print("下载完毕", response.text)
    async with aiohttp.ClientSession() as session:
        # with前都要添加async关键字且需要添加await关键字进行手动挂起
        # get(),post()
        # headers,params(get)/data(post),proxy='http://ip:port'
        async with await session.get(url) as response:
            # text()方法返回字符串形式的响应数据
            # read()方法返回二进制形式的响应数据
            # json()方法返回的就是json对象
            page_text = await response.text()  # 获取响应数据操作之前一定要使用await进行手动挂起
            print(page_text)


tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print("总耗时：", end - start)
