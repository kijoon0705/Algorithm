data = [12, 123, 14, 515, 51, 54, 12, 87, 2, 5]

def quicksort(data, left, right):
    pivot = left
    while 1:
        if data[left] > data[pivot]:

            while (data[right] >= data[pivot]):
                right = right - 1
                #right -= 1
                if left > right:
                    break
                pass #end

            if left > right:

                break

            data[left], data[right] = data[right], data[left]

        else:
            left = left + 1

            if left > right:
                break

        data[pivot], data[right] = data[right], data[pivot]

        return right
        pass

data_left = 0
data_right = len(data) - 1
data_pivot = 0
epoch_counter = 0 #몇번의 에포크를 샐행헀는지 카운트

check = []

print("data: ", data)
print("=" * 40)

#check list에 초기 data 처음과 끝 index 삽입
check.append(data_left) 
check.append(data_right)

while(len(check)!= 0):
    data_right = check.pop()
    data_left = check.pop()
    data_pivot = quicksort(data, data_left, data_right)

    epoch_counter += 1 # 몇번의 에포크가 실행됐는지 count
    print("%s epoch: " % (epoch_counter))
    print(data)
    print("=" * 40)

    #epoch 수행 후 더 정렬할 index가 있는지 확인
    #index사 남아있다면 check 리스트에 시작 및 끝 index 삽입

    if(data_pivot - 1 > data_left): #pivot 기준 왼쪽으로 더 정렬할 데이터가 있는지 확인
        check.append(data_left)
        check.append(data_pivot - 1)
        pass # end of it

    if(data_pivot + 1 < data_right):
        check.append(data_pivot + 1)
        check.append(data_right)
        pass 
    pass

