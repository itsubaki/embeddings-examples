import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

resp = client.embeddings.create(
    model="text-embedding-3-small",
    dimensions=1536,
    input=[
        "車の燃費を向上させる方法は？",
        "急発進や急ブレーキを避け、一定速度で走行することで燃費が良くなります。",
        "車の運転時、急発進や急ブレーキをすると、燃費が悪くなります。",
        "車を長持ちさせるには、消耗品を適切なタイミングで交換することが重要です。",
    ],
)

embeddings = resp.data[0].embedding
print(len(embeddings), embeddings[:5])
