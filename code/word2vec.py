import logging
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# 1️⃣ ログ設定（学習進捗を INFO で出力）
logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s",
    level=logging.INFO
)

# 2️⃣ 分かち書きテキストを逐次読み込み
sentences = LineSentence("jawiki_text.text8")  # Text8Corpus でもOK

# 3️⃣ Word2Vec モデル学習
model = Word2Vec(
    sentences,
    vector_size=200,  # 埋め込みベクトルの次元（旧: size）
    window=15,        # 文脈ウィンドウサイズ
    min_count=20,     # 出現回数が少ない単語は無視
    sg=1,             # Skip-gram
    workers=7,        # 並列処理コア数
    epochs=1,         # 学習回数
    compute_loss=True # 損失を計算して進捗確認可能
)

# 4️⃣ モデル保存
model.save("jawiki_word2vec.model")
model.wv.save_word2vec_format("jawiki_word2vec.vec", binary=False)

# 5️⃣ 最終損失確認
print("Final training loss:", model.get_latest_training_loss())
