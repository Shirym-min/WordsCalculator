import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from gensim.models import Word2Vec

# 学習済みモデルロード
model_path = "jawiki_word2vec.model"
model = Word2Vec.load(model_path)

class Word2VecGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word2Vec 類似語検索")
        self.resize(600, 400)

        layout = QVBoxLayout()

        # Positive 単語入力
        layout.addWidget(QLabel("Positive 単語（スペース区切り）:"))
        self.positive_input = QLineEdit()
        layout.addWidget(self.positive_input)

        # Negative 単語入力
        layout.addWidget(QLabel("Negative 単語（スペース区切り、任意）:"))
        self.negative_input = QLineEdit()
        layout.addWidget(self.negative_input)

        # topn 入力
        layout.addWidget(QLabel("上位何件表示:"))
        self.topn_input = QLineEdit()
        self.topn_input.setText("10")  # デフォルト 10
        layout.addWidget(self.topn_input)

        # 検索ボタン
        self.search_btn = QPushButton("検索")
        self.search_btn.clicked.connect(self.search_similar)
        layout.addWidget(self.search_btn)

        # 結果表示
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def search_similar(self):
        positive_words = self.positive_input.text().split()
        negative_words = self.negative_input.text().split()
        try:
            topn = int(self.topn_input.text())
        except ValueError:
            topn = 10

        # 存在チェック
        positive_words = [w for w in positive_words if w in model.wv]
        negative_words = [w for w in negative_words if w in model.wv]

        if not positive_words:
            self.result_text.setText("Positive 単語がモデルに存在しません")
            return

        results = model.wv.most_similar(positive=positive_words, negative=negative_words, topn=topn)
        output = "\n".join([f"{w} : {s:.4f}" for w, s in results])
        self.result_text.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Word2VecGUI()
    window.show()
    sys.exit(app.exec())