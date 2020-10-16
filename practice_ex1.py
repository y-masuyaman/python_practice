from datetime import datetime

def main():
    name = input("あなたの名前は？: \n")
    age = int(input("あなたの年齢は？: \n"))
    now_year = datetime.now().year
    age_100 = 100 - age

    print(name, "さんが", age, "歳から100歳になるのは")
    print(now_year + age_100, "年です")


if __name__ == '__main__':
    main()
