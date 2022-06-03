import openai
import csv
import numpy as np
import sentence_transformers.util
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

import transformers

from scipy.spatial.distance import cosine

openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    f_in = open("../data/processed/test.csv")
    with open("../data/processed/test.csv") as csvfile:
        cosine_similarity_score = 0
        reader = csv.reader(csvfile)
        next(reader)
        for entry in reader:
            prompt = entry[0] + ' ->'
            true_completion = entry[1]

            # fine tuning result
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n"]
            )

            predict = response['choices'][0]['text']
            if len(predict) > 0:
                resp = openai.Embedding.create(
                    input=[true_completion, predict],
                    engine="text-similarity-davinci-001"
                )

                embedding_a_gpt3 = [resp['data'][0]['embedding']]
                embedding_b_gpt3 = [resp['data'][1]['embedding']]

                cosine_similarity_score += cosine_similarity(embedding_a_gpt3, embedding_b_gpt3)[0][0]

        print("Cosine similarity Score: ")
        print(cosine_similarity_score / 50)

