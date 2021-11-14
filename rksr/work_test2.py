# 問題2. 二次元配列の回転
# 2-a. n x n の二次元配列を左向きに90°回転させるメソッドのテストを書け
# ※テキストエリアにコードをコピー&ペーストしてご回答ください
# 2-b. メソッドの実装を書け
def check_arr_length(arr: list) -> bool:
    correct_len = len(arr)
    for i in range(len(arr)):
        if len(arr[i]) != correct_len:
            return False
    return True

def rotate_2darr_90_to_left(arr: list):
    if check_arr_length(arr) == True:
        t_arr = list(map(list, zip(*arr)))
        return t_arr[::-1]
    else:
        print("\nError: array must be n x n.")
        return
    # return
arr = [[1, 2, 3], [4, 5, 6]]
emp = [[]]
# → arr = [[3, 6], [2, 5], [1, 4]]
# ※テキストエリアにコードをコピー&ペーストしてご回答ください
# print(emp)
# print(rotate_2darr_90_to_left(arr))
print(rotate_2darr_90_to_left(emp))