class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        points = []
        max_num = len(arr)
        answer = sorted(arr)

        while True:
            print(points)
            if arr == answer:
                return points

            reverse_point = arr.index(max_num)  # 전체길이가 가장 큰 수 이므로 가장 큰 값이 있는 곳을 찾고

            points.append(reverse_point + 1)
            points.append(max_num)

            arr = (
                arr[reverse_point::-1] + arr[reverse_point + 1 :]
            )  # 그 곳에서 뒤집고 안뒤집은건 뒤에 붙여놓고 일단
            arr = arr[max_num - 1 :: -1] + arr[max_num:]  # 다시 그 큰 수를 맨뒤로 보내기 위해 뒤집음

            max_num -= 1
