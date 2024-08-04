def solution(sequence, k):
    
    result = []
    sub_sum = 0
    r = len(sequence)-1

    # 비내림차순이기 때문에 뒤에서부터 순회함으로써 시간복잡도를 줄일 수 있음
    for i, v in enumerate(sequence[::-1]):

        sub_sum += v

        if sub_sum < k:
            continue

        elif sub_sum > k:
            sub_sum -= sequence[r]
            r -= 1

            # 값을 빼고 난 후에도 sub_sum 확인 필요
            if sub_sum == k:
                result.append([len(sequence)-1-i, r])

        else:
            result.append([len(sequence)-1-i, r])

    # 길이가 짧은 구간으로 정렬 후, x[0]를 기준으로 다시 오름차순 정렬
    result.sort(key=lambda x: (x[1] - x[0], x[0]))
    answer = result[0]
    
    return answer
