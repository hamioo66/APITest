from .log_config import *
from loguru import logger

log = logger

log.add(sink=log_path, level=log_level, format=log_format, filter=log_filter, colorize=log_colorize,
        serialize=log_serialize, backtrace=log_backtrace, diagnose=log_diagnose, enqueue=log_enqueue,
        catch=log_catch, rotation=log_rotation, retention=log_retension, encoding=log_encoding)
