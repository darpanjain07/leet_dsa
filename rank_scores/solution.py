import pandas as pd
import numpy as np

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores.score.rank(ascending = False)
    df = scores[['score', 'rank']].sort_values(by='score', ascending=False)
    # df['rank'] = df['rank'].astype('Int64')
    df['rank'] = df['rank'].apply(np.int64)
    return df

df = order_scores(scores)
print(df)