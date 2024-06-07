import multiprocessing

cpu_cores = multiprocessing.cpu_count()
# 查看线程
print(f'CPU cores: {cpu_cores}')
