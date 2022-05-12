from templateFiles.inputTypeConstant import INPUT_TYPE

if __name__ == "__main__":
    inputString = input('输入: ')
    if inputString in INPUT_TYPE.keys():
        method = INPUT_TYPE.get(inputString, 'countryName')
        if method:
            method()
    else:
        print("请输入合法的输入！")
        print("例如:", INPUT_TYPE.keys())

