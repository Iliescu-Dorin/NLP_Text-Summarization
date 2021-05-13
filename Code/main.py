import pandas as pd
from gensim.summarization import summarize
from rouge import Rouge

from cosine_similarity import cosine
from formatting import gen_serie, columns
from kmean import kmean
from scraper import get_article
from text_rank import text_rank
from tokenizer import tokenize


def compute(topic):
    raw, ref = get_article(topic)

    sent = tokenize(raw)

    df = pd.DataFrame()

    ratio = len(ref) / len(raw) #the proportion of the number of sentences of the original text to be chosen for the summary.

    # TextRank
    result = text_rank(raw, sent, ref)

    r = Rouge()
    rouge = r.get_scores(result, ref)

    df = df.append(gen_serie('TextRank', rouge, result), ignore_index=True)

    # Gensim --- based on ranks of text sentences using a variation of the TextRank algorithm
    ret = summarize(raw, ratio)
    r = Rouge()
    rouge = r.get_scores(ret, ref)
    df = df.append(gen_serie('Gensim', rouge, ret), ignore_index=True)

    # KMean
    df = df.append(kmean(sent, ret))

    # Cosine
    df = df.append(cosine(sent, ref), ignore_index=True)

    # Rearrange columns
    df = df[columns]

    df.to_csv('out/' + topic + '.csv')

    return df.to_json(orient='records')

#compute("Algorithm")
