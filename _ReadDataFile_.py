def funcFindHeader(RawData) :

    """
    Find name of data columns and number of start line for rawdata

    :param RawData : [list] str type list of rawdata each line
    :return: number of line column and data
    """

    import numpy as np
    from scipy import stats
    import functools

    regWordDelimiter = [r' ', r'\t', r',']
    regCharacter = {'letter' : r'[a-zA-Z]', 'number' : r'[0-9.]', 'special' : r'[^\sa-zA-Z0-9+-.]'}

    # 문장수로 구분
    indexDelimiter = np.argmax([np.sum(list(map(len, list(RawData[0].str.findall(delimiter)))))
                                for delimiter in regWordDelimiter])
    delimiter = regWordDelimiter[indexDelimiter]
    tmpContinues1 = list(map(len, list(RawData[0].str.findall(delimiter))))
    tmpContinues2 = [[i, k] for i, k in enumerate(tmpContinues1) if (tmpContinues1[i] - tmpContinues1[i - 1]) != 0]
    continuesWord = list(zip(*tmpContinues2))

    # 문자수로 구분
    tmpContinues1 = [list(map(len, list(RawData[0].str.findall(reg)))) for reg in regCharacter.values()]
    tmpContinues2 = [[[i, k] for i, k in enumerate(data) if (data[i] - data[i - 1]) != 0] for data in tmpContinues1]
    continuesChar = [list(zip(*data)) for data in tmpContinues2]

    lineNumLastWordChangeLine = continuesWord[0][-1]
    lineNumLastCharChangeLine = [data[0][-1] for data in continuesChar]

    '''
    각각의 문자들의 형식을 인식하고 문자들의 글자수를 인식한다.
    1. 데이터시작 위치 찾기      
     (1) 구분자에 의해 구분된 단락들의 변화가 없는 위치
     (2) 숫자가 가장 많고, 글자수의 변화가 없는 위치
     (3) 부호 및 소수점을 제외한 특수문자가 없으면서 글자수의 변화가 없는 위치
      - 숫자의 자리수가 변하면서 데이터들이 변하는 경우 있음
     (4) 구분자로 이용 줄을 나눴을때, (1)~(3)와 같은 경우 채택으로 변경
     → 파일에서 사용하는 구분자는 카운트가 가장 많은 특수문자로 구분(문장에서의 구분자와는 다르다)
     (5) 구분자 이용 단어들의 갯수와 (1)~(3) 중에 같은 경우가 없을때는 어떻해 해야 되는지에 대해서 고민해봐야댐
      
    2. 채널이름 위치 찾기
     (1) 영문자가 가장 많은 위치
     (2) 데이터 시작위치와의 거리 차이
      weightedLetter = L X D
       L : 라인에 있는 영문자수
       D : 데이터와의 시작위치(멀어질수록 라인 당 0.1의 Weight 차감 ,10라인 밖에 있는 라인들은 후보군 제외)
    '''
    lineNumStartData = [line for line in lineNumLastCharChangeLine if lineNumLastWordChangeLine == line][0]

    # if lineNumLastChangeLine[0] == lineNumLastChangeLine[1] and \
    #         lineNumLastChangeLine[0] == lineNumLastChangeLine[2] :
    #     lineNumStartData = lineNumLastChangeLine[0]
    # elif continuesChar[0][0][max(np.where([val == 0 for val in continuesChar[0][1]])[0])] == \
    #         continuesChar[1][0][np.argmax(continuesChar[1][0])] :
    #     lineNumStartData = continuesChar[1][0][np.argmax(continuesChar[1][0])]
    # elif continuesChar[2][0][max(np.where([val == 0 for val in continuesChar[2][1]])[0])] == \
    #         continuesChar[1][0][np.argmax(continuesChar[1][0])] :
    #     lineNumStartData = continuesChar[1][0][np.argmax(continuesChar[1][0])]
    # else :
    #     lineNumStartData = continuesChar[1][0][np.argmax(continuesChar[1][0])]

    dist =[1 - 0.1*(lineNumStartData - line) for line in continuesChar[0][0] if lineNumStartData - line > 0]
    lineNumColumn = continuesChar[0][0][np.argmax([continuesChar[0][1][i] * k for i, k in enumerate(dist)])]

    return lineNumColumn, lineNumStartData


def funcMakeDataFrame(RawData, *lineNum : int) :
    """
    :param RawData:
    :param lineNum:
    :return:
    """
    import re
    import numpy as np
    from collections import Counter
    from scipy.stats import rankdata
    from _ListDelimiter_ import funcFindDelimiter

    # 라인에 대한 넘버 정보 하나일때, 즉 데이터 정의나 단위 정보일때
    if len(lineNum) < 2 :
        listLineNum = [lineNum[0], lineNum[0] + 1]
    # 형을 맞춰주기 위함
    # 라인에 대한 넘버 정보가 두개 이상일때, 즉 데이터에 대한 행렬일때
    else :
        listLineNum = [lineNum[0], lineNum[1]]

    lineData = RawData.iloc[listLineNum[0]: listLineNum[1], 0]
    # 형을 맞춰주기 위함
    separator = funcFindDelimiter(lineData)

    if len(separator) > 1 :  # Channel name 및 단위에 대한 행처리
        regx = [f"{separator[0]}", f"{separator[1]}"]
        tmpData = lineData.str.split(regx[1], expand=True)
        tmpData2 = tmpData[tmpData.astype(bool)].dropna(axis=1).copy()
        ResultData = tmpData2.iloc[0].str.split(regx[0], expand=True)

    else :  # Data 대한 행처리
        regx = [f"{separator[0]}"]
        ResultData = lineData.str.split(regx[0], expand=True)
        # ResultData = tmpData.iloc[:, 0].str.split(regx[0], expand=True)

    return ResultData

# def funcMakeData(RawData, NumName, NumData) :
#     import re
#     import numpy as np
#     from collections import Counter
#     from scipy.stats import rankdata
#     from _ListDelimiter_ import funcFindDelimiter
#
#     line = RawData.loc[NumData]
#     separator = funcFindDelimiter(line)
#     a = RawData.loc[8:][0].str.split(separator, expand=True)
