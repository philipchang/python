#!/usr/bin/env python
#coding=utf-8

import time
import logging
import logging.handlers


def _getFormater():
    format = "%(asctime)s %(levelname)-8s[%(filename)s:%(lineno)d(%(funcName)s)] %(message)s"
    return logging.Formatter(format)

def _getTimeRotatingHandler(log_dir,prefix):
    if len(log_dir) > 0 :
        if log_dir[len(log_dir)-1] != '/':
            log_dir += '/'
        prefix = log_dir + prefix
    hdlr = logging.handlers.TimedRotatingFileHandler(prefix, 'midnight', 1, 0)
    #hdlr = logging.handlers.TimedRotatingFileHandler(prefix, 'M', 1, 0)
    hdlr.setFormatter(_getFormater())
    hdlr.suffix = "%Y-%m-%d.log"
    return hdlr

def getlogger(log_dir,log_level="DEBUG", log_name="master", timeRotating=True):
    logger = logging.getLogger(log_name)

    # 文件日志
    hdlr = _getTimeRotatingHandler(log_dir,log_name)
    logger.addHandler(hdlr)

    if "DEBUG" == log_level.upper():
        logger.setLevel(logging.DEBUG)
        # 屏幕输出
        ch = logging.StreamHandler()
        logger.addHandler(ch)
    elif "INFO" == log_level.upper():
        logger.setLevel(logging.INFO)
    elif "WARNING" == log_level.upper():
        logger.setLevel(logging.WARNING)
    elif "ERROR" == log_level.upper():
        logger.setLevel(logging.ERROR)
    elif "CRITICAL" == log_level.upper():
        logger.setLevel(logging.CRITICAL)
    else:
        logger.setLevel(logging.ERROR)
    return logger


if __name__ == '__main__':    
    
    master_log = getlogger('./',log_name="master.log")
    for i in range(0,10):
        master_log.debug("%d s" % (i,))
        time.sleep(1)
