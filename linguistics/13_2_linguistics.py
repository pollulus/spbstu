!pip install yake

import pandas as pd
import yake

def find_keywords(file_name):
    df = pd.read_csv(file_name, encoding='utf-8')

    kw_extractor = yake.KeywordExtractor(lan='ru', n=2, top=5)

    key_words_list = []
    for text in df['normalized_text']:
        keywords = kw_extractor.extract_keywords(text)
        key_words_list.append(keywords)

    df['key_words'] = key_words_list
    df.to_csv('cafe_reviews_with_keywords.csv', index=False, encoding='utf-8')
    return df

find_keywords('cafe_reviews.csv')
