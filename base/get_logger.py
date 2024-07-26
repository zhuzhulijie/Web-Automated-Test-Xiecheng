# 导包
import logging.handlers

class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger()

            # 设置 日志器级别
            cls.logger.setLevel(logging.INFO)

            # 获取 处理器 控制台
            sh = logging.StreamHandler()

            # 获取 处理器 文件-以时间分隔
            th = logging.handlers.TimedRotatingFileHandler(filename='../log/log.log', when='midnight', interval=1, backupCount=30, encoding='utf-8')

            # 设置 格式器
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
            fm = logging.Formatter(fmt)

            # 将格式器 添加到处理器中-控制台
            sh.setFormatter(fm)

            # 将格式器 添加到处理器中-文件
            th.setFormatter(fm)

            # 将处理器 添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger