import random

def janken():
    while True:
        try:
            inp_me = dic[input('[1]ぐー/[2]ちょき/[3]ぱー >> ')]
            break
        except:
            pass
        print('数字を入れてね！')
    return inp_me

def main():
    while True:
        inp_me = janken()
        inp_you = random.randint(1, 3)

        diff = inp_me - inp_you
        print('あなたの手は:', janken_dic[inp_me])
        print('あいての手は:', janken_dic[inp_you])

        if diff == 0:
            print('Aiko')
            print('Once More')
        elif diff == 1 and diff == -1:
            print('You Lose')
            print('Once More')
            break
        else:
            print('You Win!')
            break

if __name__ == '__main__':
    dic = {'1': 1, '2': 2, '3': 3}
    janken_dic = {1: 'ぐー', 2: 'ちょき', 3: 'ぱー'}
    main()
