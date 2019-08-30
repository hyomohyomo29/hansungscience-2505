list = ['미소등','복장','출입','지각','불참','음식','노트북','취침','외출','귀가','불이행','전자기기','입실시각','소란','정리', '봉사']
burlist = [1,1,2,2,4,3,4,3,4,6,1,4,1,1,-1,-1]
namelist = ['미소등','용의 복장 규정 위반','기숙사 출입 규정 위반','아침 점호 지각','아침 점호 불참','생활관 내 음식물 반입','기숙사 내 노트북 무단반입','취침 규정 위반','무단 외출','무단 귀가','지시 불이행','학업목적 외 전자기기 사용','자습실 입실시각 미준수','방 정리 양호','자습실 청소 및 간식시간 봉사','자습실 내 소란 행위']
messenger = input('벌점 문자를 모두 넣어주세요')
messenger = messenger.split('.')
score = int(0)
bur,num,name = {},{},{}

for i in list:
    bur[i] = 0
    num[i] = 0
    name[i] = namelist[list.index(i)]
for i in messenger : 
    for j in list:
        if j in i:
            num[j]+=1
            bur[j]+=burlist[list.index(j)]
for i in bur.values() :
    score += i
for i in num :  # 가장 많은 횟수로 걸린 벌점 항목 찾기
    if num[i] == max(num.values()) :
        most = i
for i in bur :  #가장 많은 벌점이 쌓인 벌점 항목 찾기
    if bur[i] == max(bur.values()) :
        most2 = i
print('당신의 벌점은',score,'점 입니다')
print('당신은 ',name[most],' 에 가장 많이 걸렸고 ',name[most2],' 에 가장 많은 벌점을 받았습니다')
a = input('당신이 알고싶은 벌점항목을 입력해주세요')
print('당신이 ',name[a],' 로 걸린 횟수는 ',num[a],'점 , 받은 벌점은 ',bur[a],' 점 입니다')
