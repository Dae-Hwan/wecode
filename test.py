# 1부터 50의 자연수 중 짝수를 구하는 함수

def even(start = 1, end = 50):
    even_list = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            continue

    return even_list
            
