import time

from loguru import logger
import os

'''
add(sink, *, level='DEBUG', format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> |
 <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', filter=None, 
 colorize=None, serialize=False, backtrace=True, diagnose=True, enqueue=False, catch=True, **kwargs)
'''
local_time = time.strftime("%Y-%m-%d_%H", time.localtime())
# add公用的参数
log_path = os.path.abspath(os.path.join(os.path.dirname(__file__)) + '/../logs/' + '{}.log'.format(local_time))
log_level = 'INFO'
# 保存到日志文件时的格式
log_format = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> |<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>'
log_filter = None
log_colorize = None
log_serialize = False  # True ,将日志输出形式为字典
log_backtrace = True  # 异常追踪
log_diagnose = False  # (异常调试，是否显示具体的值)生产环境，避免数据泄露，设置为False
log_enqueue = True  # 设置成True,解决多进程问题
log_catch = True  # 记录日志是否成功，不成功就打印在屏幕上,但这不影响程序的正常使用;

# 当sink 是文件路径时，这些参数是可以使用的
log_rotation = '1h'  # 指示何时关闭当前日志文件并启动一个新文件的条件。
# int 字节数大小
# str 人类合适的表达 "100 MB", "0.5 GB", "1 month 2 weeks", "4 days", "10h", "monthly", "18:00", "sunday", "w0", "monday at 12:00", …
log_retension = '2 days'  # 日志保留多久
# int 保存日志的数量
# str 人类合适的表达 "100 MB", "0.5 GB", "1 month 2 weeks", "4 days", "10h", "monthly", "18:00", "sunday", "w0", "monday at 12:00", …
log_encoding = 'utf-8'

#

