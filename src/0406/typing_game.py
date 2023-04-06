import random
import time

# ランダムな単語のリスト
words = ['apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']

# ゲームの開始を促す
input('Press Enter to start the typing game...')

# ゲームの開始時刻を取得
start_time = time.time()

# ランダムな単語を選んで表示
target_word = random.choice(words)
print('Type the word: {}'.format(target_word))

# ユーザーが入力した文字列を取得
input_word = input('> ')

# ゲームの終了時刻を取得
end_time = time.time()

# 入力した文字列が正しいかどうかをチェック
if input_word == target_word:
    # 経過時間と入力速度を計算して表示
    elapsed_time = end_time - start_time
    input_speed = len(target_word) / elapsed_time
    print('You typed the word in {:.2f} seconds with an input speed of {:.2f} characters per second!'.format(elapsed_time, input_speed))
else:
    print('You typed the wrong word!')
