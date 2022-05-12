# 반복문 공부
a=0
while True:
    a+=1
    print('안녕하세요')
    if a==15:
        break

# 우주선발사
import time
c=11
while True:
    time.sleep(1)
    c-=1
    print('%d초 남았습니다'%c)
    if c==0:
        break
print('발사')

# 음료 자판기
coffee=10
while True:
    money=int(input('돈을 넣어 주세요:'))
    if 300<=money<=599:
        print('거스름돈을 %d원 만큼 주고 커피를 1개 줍니다.'%int(money-300))
        coffee-=1
        print('커피는 %d개 남았습니다.\n'%coffee)
    elif money>599:
        get=int(input("커피 몇 잔을 원하십니까?:"))
        while get*300>money:
            print('돈이 모자랍니다.')
            get=int(input("커피 몇 잔을 원하십니까?:"))
        if coffee-get>=0:
            print('거스름돈 %d원을 주고 커피를 %s개 줍니다.'%(int(money-300*get),str(get)))
            coffee-=get
            print('커피는 %d개 남았습니다\n'%coffee)
        else:
            print("남은 커피가 %s개 밖에 없습니다. 전부 드리겠습니다."%coffee)
            print("거스름돈 %d원을 주고 커피를 %s개 줍니다.\n"%(int(money-300*coffee),str(coffee)))
            coffee=0
    else:
        print('돈을 더 넣어주세요.')
        print('커피는 %d개 남았습니다\n.'%coffee)
    if coffee==0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.\n')
        break