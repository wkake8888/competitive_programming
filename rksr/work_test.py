# 問題1.回文
# 1-a.引数で渡された文字列が回文（例「たけやぶやけた」）かどうかを判定するメソッドを書け。メソッドの引数は文字列、返り値はBoolean型とする
# ※テキストエリアにコードをコピー&ペーストしてご回答ください
def check_palindrome(text: str) -> bool:
    if type(text) != str or len(text) == 0:
        return False
    # [日英対応]特別な記号を取り除く
    special_chars = ". 。！!？?、,’'”\""
    for special_char in special_chars:
        text = text.replace(special_char, '')
    # 英語の場合、大文字小文字を揃える必要あり
    text = text.lower()
    # テキストの両端から等しいかチェック
    for i in range(len(text)//2):
        if text[i] != text[-i - 1]:
            return False
    return True

# 1-b. このメソッドに対する単体テストを書け
# ※テキストエリアにコードをコピー&ペーストしてご回答ください
# 1-c. この実装に於いて、文字列の長さを n とした時の時間計算量を答えよ
# 約 n/2


