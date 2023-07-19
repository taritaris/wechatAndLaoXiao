import datetime
# 获取日期和倒计时
def get_time():
    a = datetime.datetime.now()  # 实施时间
    y = str(a.year)
    m = str(a.month)
    d = str(a.day)  # 转换为字符串，便于打印
    time = y + '年' + m + '月' + d + '日' + '\n'
    b = datetime.datetime(2023, 12, 23)  # 自己设置的研究生考试时间
    count_down = (b - a).days  # 考研倒计时
    return  count_down

if __name__ == '__main__':
    print(get_time())