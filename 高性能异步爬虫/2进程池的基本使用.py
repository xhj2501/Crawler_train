import time
from multiprocessing.dummy import Pool  # 导入进程池模块对应的类


# # 使用单线程串行方式执行
# def get_page(str):
#     print("正在下载：", str)
#     time.sleep(2)
#     print("下载成功：", str)
#
#
# name_list = ['aa', 'bb', 'cc', 'dd']
#
# start_time = time.time()
#
# for name in name_list:
#     get_page(name)
#
# end_time = time.time()
# print('%d second' % (end_time - start_time))

# 使用进程池的方式进行
def get_page(str):
    print("正在下载：", str)
    time.sleep(2)
    print("下载成功：", str)


name_list = ['aa', 'bb', 'cc', 'dd']

start_time = time.time()

# 实例化一个进程池对象
pool = Pool(4)
pool.map(get_page, name_list)  # 将列表中每一个列表元素传递给函数get_page处理

end_time = time.time()
print('%d second' % (end_time - start_time))
