# WordsCalculator
Japanese text can be converted into vectors, enabling operations such as addition and subtraction between words.
# Information
- TrainingData: Wikipedia (https://dumps.wikimedia.org/jawiki/20260201/)
- Library: gensim, MeCab
- Tech: Word2Vec
- Parameters:
```Python
epochs=1,
vector_size=200,
min_count=20,
window=15,
sg=1
```
# How To Use
## Prerequisites
- Python 3.12+
- Need to install: gensim, PyQt6, logging
- ```bash
  pip install gensim PyQt6 logging
  ```
## Prepare
Download from this. (At first, you only need to download UI Calculator)
 | Version | Download | Source code |
 |------------------|--------------|--------------|
 | UI Calculator(recommended) v1.0.0 Stable | [WordCalculatorUI](https://github.com/Shirym-min/WordsCalculator/releases/download/Stable/WordCalculatorUI) | [source code](https://github.com/Shirym-min/WordsCalculator/blob/main/code/wordcalcui.py)|
 | Text2Vec Trainer v1.0.0 Stable| [Trainer](https://github.com/Shirym-min/WordsCalculator/releases/download/Stable/Trainer)|[source code]()|
 | Command Calculator v1.0.0 Stable | [WordCalculatorCommand](https://github.com/Shirym-min/WordsCalculator/releases/download/Stable/WordCalculatorCommand) | [source code](https://github.com/Shirym-min/WordsCalculator/blob/main/code/wordcalc.py)|

 And download model.
 | Version | Download |
 |-------------|-------------|
 | v1.0.0　| [Model](https://drive.google.com/file/d/11TZYpJFyQR9kAcRAZZnw08LJLg-VceQs/view?usp=share_link) |

Unzip this file and rename folder, and move python file to this.
