import time
#延迟时间
time.sleep()
#时间戳时间
time.time()                         #获取当前时间戳时间，1970年1月1日伦敦时间计算
time.mktime(strruct_time)           #结构化时间转时间戳时间
#格式化时间
time.strftime('%Y-%m-%d %h:%M:%s',strruct_time)     #strrut_time为结构化时间
time.strftime('%Y-%m-%d %h:%M:%s')    #当前时间
                        # % y           两位数的年份表示（00 - 99）
                        # % Y           四位数的年份表示（000 - 9999）
                        # % m           月份（01 - 12）
                        # % d           月内中的一天（0 - 31）
                        # % H           24小时制小时数（0 - 23）
                        # % I           12小时制小时数（01 - 12）
                        # % M           分钟数（00 = 59）
                        # % S           秒（00 - 59）
                        # % a           本地简化星期名称
                        # % A z          本地完整星期名称
                        # % b           本地简化的月份名称
                        # % B           本地完整的月份名称
                        # % c           本地相应的日期表示和时间表示
                        # % j           年内的一天（001 - 366）
                        # % p           本地A.M.或P.M.的等价符
                        # % U           一年中的星期数（00 - 53）星期天为星期的开始
                        # % w           星期（0 - 6），星期天为星期的开始
                        # % W           一年中的星期数（00 - 53）星期一为星期的开始
                        # % x           本地相应的日期表示
                        # % X           本地相应的时间表示
                        # % Z           当前时区的名称
                        # % %           % 号本身
#结构化时间
time.localtime(15000000000)             #转换为北京时间/时间戳转结构化  无参数则当前北京时间
time.gmtime(15000000000)                #转换为伦敦时间/时间戳转结构化  无参数则当前北京时间
time.strptime('2018-8-8','%Y-%m-%d')    #字符串转结构化
                    # 0       tm_year(年)                比如2011
                    # 1       tm_mon(月)                 1 - 12
                    # 2       tm_mday(日)                1 - 31
                    # 3       tm_hour(时)                0 - 23
                    # 4       tm_min(分)                 0 - 59
                    # 5       tm_sec(秒)                 0 - 60
                    # 6       tm_wday(weekday)           0 - 6（0表示周一）
                    # 7       tm_yday(一年中的第几天)     1 - 366
                    # 8       tm_isdst(是否是夏令时)      默认为0
                    #例如：用.tm_year获取值




字符串时间/格式时间<=>元组时间/结构化<=>浮点型时间/时间戳




############计算时间差
# import time
# def timec(f):
#     tuple_time=time.strptime(f,'%Y-%m-%d %H:%M:%S')
#     float_time=time.mktime(tuple_time)
#     float_time_now=time.time()
#     timex=int(float_time_now-float_time)
#     tuple_timex=time.gmtime(timex)
#     str_time=time.strftime('%Y-%m-%d %H:%M:%S',tuple_timex)
#     print('你已经活了{}年{}月{}日{}时{}分{}秒'.format(tuple_timex.tm_year-1970,tuple_timex.tm_mon,tuple_timex.tm_mday,\
#                                            tuple_timex.tm_hour,tuple_timex.tm_min,tuple_timex.tm_sec))
# f=input('请输入你的出生日期(2000-4-28 23:59:59):')
# timec(f)
time.ctime(now_ti)