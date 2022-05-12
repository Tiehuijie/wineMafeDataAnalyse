import pandas as pd


def countryNameList():
    # (1)输入'国家名列表'，统计文件中出现的葡萄酒生产国家，输出不重复的国家名列表，按字母表升序排序,若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素
    with open('templateFiles/wineData.csv', "r") as csv_file:
        df = pd.read_csv(csv_file)
        result = df['country'].drop_duplicates().values.tolist()
        print(sorted(result))
        csv_file.close()


def calAverageScore():
    # （2）输入'平均分'，计算每个国家的葡萄酒的平均得分( 保留最多2位小数)，返回值为国家名和得分的列表
    result = []
    with open('templateFiles/wineData.csv', "r") as csv_file:
        df = pd.read_csv(csv_file)
        df_mean = df.groupby('country')['points']
        for key, value in df_mean:
            result.append([key, value.mean().round(2)])
        print(result)
        csv_file.close()


def calAverageScoreWithSort():
    # （3）输入'平均分排序'，计算每个国家的葡萄酒的平均得分，返回值为国家名和得分的列表，按评分由高到低降序排列
    result = []
    with open('templateFiles/wineData.csv', "r") as csv_file:
        df = pd.read_csv(csv_file)
        df_mean = df.groupby('country')['points']
        for key, value in df_mean:
            result.append([key, value.mean().round(2)])
        print(sorted(result, key=lambda x: x[1], reverse=True))
        csv_file.close()


def getMaxScore():
    # （4）输入'评分最高'，输出评分最高的十款葡萄酒的编号、出产国、评分和价格，按评分降序输出
    with open('templateFiles/wineData.csv', "r") as csv_file:
        df = pd.read_csv(csv_file, usecols=['number', 'country', 'points', 'price'])
        df_sorted_with_point = df.sort_values(by=['points'], ascending=False)[:10]
        print(df_sorted_with_point.values.tolist())
        csv_file.close()


def getMaxPrice():
    # （5）输入'价格最高'，输出价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价格降序输出
    with open('templateFiles/wineData.csv', "r") as csv_file:
        df = pd.read_csv(csv_file, usecols=['number', 'country', 'points', 'price'])
        df_sorted_with_point = df.sort_values(by=['price'], ascending=False)[:20]
        print(df_sorted_with_point.values.tolist())
        csv_file.close()


def getWineScore():
    # （6）输入'葡萄酒评分'，统计各个评分的葡萄酒数量是多少，输出包含评分和数量的列表
    print('getWineScore')


def getMaxSize():
    # （7）输出拥有葡萄酒数量最多的评分和数量
    print('getMaxSize')


def getMaxSizeAverageScore():
    # （8）输出拥有葡萄酒数量最多的评分的葡萄酒的平均价格
    print('getMaxSizeAverageScore')
