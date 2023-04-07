# new-employee-training
これらのコードは[ChatGPT](https://openai.com/blog/chatgpt)を用いて実装しています．
## 提供するもの
### HTML/JavaScript
- [計算機](./src/0405/calculator.html) \
2つの数字を入力し，四則演算を選んで計算結果を算出する．

- [クリッカーゲーム](./src/0405/clicker.html) \
制限時間内にランダムな場所に出現するボタンを何回押せたかを争うゲーム．

- [単語当てゲーム](./src/0407/word.html) \
ランダムに選ばれた単語を当てるゲーム．

- [数当てゲーム](./src/0407/guess-number-between-1-and-100.html) \
1~100の数字を当てるゲーム．

- [暗算ゲーム](./src/0407/mental-arithmentic.html) \
表示された2つの数字を暗算するゲーム．

- [クイズゲーム](./src/0407/quiz.html) \
クイズゲーム．

### Python
- [日報作成プログラム](./src/0405/daily_report_creation.py) \
氏名，報告日，作業内容，反省点を登録し，Excelに出力する．

※ プログラム実行前に`out`ディレクトリを以下のように作成してください．
```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── out
├── requirements.txt
└── src
```
- [デジタル時計CUI](./src/0406/digital_clock_cui.py) \
`Japan`, `UK`, `US`から選択した国の時刻を表示す．1分タイマー機能付き．

- [デジタル時計GUI](./src/0406/digital_clock_gui.py) \
`Japan`, `UK`, `US`から選択した国の時刻を表示する．

- [オセロCUI](./src/0406/othello_cui.py) \
CUIで遊べるオセロ．

- [オセロGUI](./src/0406/othello_gui.py) \
GUIで遊べるオセロ．

- [タイピングゲーム](./src/0406/typing_game.py) \
表示された文字を入力すると，単語を入力するのにかかった時間と，1語あたりの入力速度が表示される．

## Python環境について
Pythonのバージョンは[.python-version](./.python-version)を参考 \
必要ライブラリは[requirements.txt](./requirements.txt)を参考