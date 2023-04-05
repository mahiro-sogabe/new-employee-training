# new-employee-training
これらのコードは[ChatGPT](https://openai.com/blog/chatgpt)を用いて実装しています．
## 提供するもの
### HTML/JavaScript
- [計算機](./src/calculator.html) \
2つの数字を入力し，四則演算を選んで計算結果を算出する．
- [クリッカーゲーム](./src/clicker.html) \
制限時間内にランダムな場所に出現するボタンを何回押せたかを争うゲーム．
### Python
- [日報作成プログラム](./src/daily_report_creation.py) \
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
    ├── calculator.html
    ├── clicker.html
    └── daily_report_creation.py
```
## Python環境について
Pythonのバージョンは[.python-version](./.python-version)を参考 \
必要ライブラリは[requirements.txt](./requirements.txt)を参考