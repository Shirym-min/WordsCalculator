from gensim.models import Word2Vec, KeyedVectors

# 学習済みモデルの読み込み
# バイナリ形式なら binary=True、テキスト形式なら False
model_path = "jawiki_word2vec.model"  # または .vec
model = Word2Vec.load(model_path)

# 類似単語を取得
positive = list(map(str,input().split()))
negative = list(map(str,input().split()))
topn = int(input("outputint"))  # 上位10件
print(positive)
print(negative)
similar_words = model.wv.most_similar(positive=positive, negative=negative, topn=topn)
print(f"結果:")
for word, score in similar_words:
  print(f"{word} : {score:.4f}")
