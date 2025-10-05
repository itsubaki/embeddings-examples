from yasem import SpladeEmbedder

model_name = "hotchpotch/japanese-splade-v2"
embedder = SpladeEmbedder(model_name)

query = "車の燃費を向上させる方法は？"
docs = [
    "急発進や急ブレーキを避け、一定速度で走行することで燃費が良くなります。",
    "車の運転時、急発進や急ブレーキをすると、燃費が悪くなります。",
    "車を長持ちさせるには、消耗品を適切なタイミングで交換することが重要です。",
]

print(embedder.rank(query, docs, return_documents=True))
