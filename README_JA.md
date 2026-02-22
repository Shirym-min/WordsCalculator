# WordsCalculator
日本語テキストをベクトルに変換し、単語間の加算・減算などの演算を可能にします。
# 情報
- トレーニングデータ: Wikipedia (https://dumps.wikimedia.org/jawiki/20260201/)
- ライブラリ: gensim, MeCab
- 技術: Word2Vec
- パラメータ:
```Python
epochs=1,
vector_size=200,
min_count=20,
window=15,
sg=1
```
# 使用方法
## 事前準備
- Python 3.12以上
- インストールが必要: gensim, PyQt6, logging
- ```bash
  pip install gensim PyQt6 logging
  ```
## 準備
こちらからダウンロードしてください（最初はUI Calculatorのみダウンロードすれば十分です）
 | バージョン | ダウンロード | ソースコード |
 |------------------|--------------|--------------|
 | UI Calculator(推奨) v1.0.0 Stable | [WordCalculatorUI](https://github.com/Shirym-min/WordsCalculator/releases/download/Stable/WordCalculatorUI) | [ソースコード](https://github.com/Shirym-min/WordsCalculator/blob/main/code/wordcalcui.py) |
 | Text2Vec Trainer v1.0.0 Stable | [Trainer](https://github.com/Shirym-min/WordsCalculator/releases/download/Stable/Trainer) |[ソースコード](https://github.com/Shirym-min/WordsCalculator/blob/main/code/wordcalcui.py) |
 | Command Calculator v1.0.0 | [WordCalculatorCommand](https://github.com/Shirym-min/WordsCalculator/releases/download/Stable/WordCalculatorCommand) | [ソースコード](https://github.com/Shirym-min/WordsCalculator/blob/main/code/wordcalc.py)|

 モデルをダウンロードしてください。（モデルをさらに訓練したい場合は、.text8fileもダウンロードしてください）
| バージョン | モデルダウンロード | .text8fileダウンロード |
|-------------|-------------|----------------|
 | v1.0.0　| [モデル](https://github.com/Shirym-min/WordsCalculator/releases/download/Stable/Models) | [テキストデータ](https://drive.google.com/file/d/1WoO2YA9k0aP-XKLJNdxw9A5slEGSPV2m/view?usp=share_link)|

このファイルを解凍し、フォルダ名を変更して、Pythonファイルをこのフォルダに移動してください。

## 実行方法
- 全てのファイルを単一のディレクトリに配置し、wordcalcui.pyを実行してください。UIが表示され、使用可能になります。
- Command Calculatorをダウンロードした場合は、ターミナルで実行してください。
  
