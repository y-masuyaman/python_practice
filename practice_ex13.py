def main():
    a = 0
    b = 1
    lists = []
    while True:
        try:
            num = int(input('好きな数字をいれてね: \n'))
        except:
            print('エラーだよ！')

        print('あなたが入れた数字は', num, 'ですね')
        y_or_n = input('これでよければ[y],だめなら[n]を入力してね\n')
        if y_or_n == 'y':
            break
        else:
            print('もう一度数字をいれてね')

    while len(lists) < num:
        a , b = b , a + b
        lists.append(a)

    for i in lists:
        print(i)

if __name__ == "__main__":
    main()