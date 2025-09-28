def is_leap_year(year):
    """判断给定的年份是否为闰年"""
    # 闰年条件：能被4整除但不能被100整除，或者能被400整除
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    try:
        # 获取用户输入并转换为整数
        year_input = input().strip()  # 直接读取输入，不显示提示信息
        year = int(year_input)
        
        # 判断是否为闰年并输出结果
        if is_leap_year(year):
            print(f"{year}年是闰年")
        else:
            print(f"{year}年不是闰年")
            
    except ValueError:
        # 处理非数字输入的异常情况
        print("输入错误")

if __name__ == "__main__":
    main()
