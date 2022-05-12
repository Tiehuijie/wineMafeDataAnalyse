from templateFiles.analyseWineDataOnOneType import countryNameList, calAverageScore, calAverageScoreWithSort, \
    getMaxScore, getMaxPrice, getWineScore, getMaxSize, getMaxSizeAverageScore

INPUT_TYPE = {
    '国家名列表': countryNameList,
    '平均分': calAverageScore,
    '平均分排序': calAverageScoreWithSort,
    '评分最高': getMaxScore,
    '价格最高': getMaxPrice,
    '葡萄酒评分': getWineScore,
    '葡萄酒数量最多': getMaxSize,
    '葡萄酒数量最多的平均分': getMaxSizeAverageScore,
}