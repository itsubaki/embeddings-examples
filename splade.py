from yasem import SpladeEmbedder
import time

model_name = "hotchpotch/japanese-splade-v2"
embedder = SpladeEmbedder(model_name)

query = "車の燃費を向上させる方法は？"
sentences = [
    "急発進や急ブレーキを避け、一定速度で走行することで燃費が良くなります。",
    "車の運転時、急発進や急ブレーキをすると、燃費が悪くなります。",
    "車を長持ちさせるには、消耗品を適切なタイミングで交換することが重要です。",
]

start = time.perf_counter()
embeddings = embedder.encode(sentences)
print(f"encode: {time.perf_counter() - start:.4f} sec")
print()

for i, emb in enumerate(embeddings):
    print(sentences[i])
    
    token_values = embedder.get_token_values(emb)
    for token, score in token_values.items():
        print(f"{token:<15}: {score:.4f}")
    
    print()
