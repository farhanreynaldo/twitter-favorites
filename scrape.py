import twint 
import pandas as pd 

username = "xynx"
c = twint.Config()
c.Username = username
c.Limit = 100
c.Pandas = True
c.Pandas_clean = True
c.Store_json = True
c.Output = 'favorites'

twint.run.Favorites(c)

new_favorites = twint.storage.panda.Tweets_df
favorites_df = pd.read_csv('favorites/favorites-all.csv', sep='\t')
new_json = pd.read_json('favorites/tweets.json', lines=True)
current_json = pd.read_json('favorites/current-tweets.json')

favorites_df = pd.concat([favorites_df, new_favorites])
current_json = pd.concat([current_json, new_json])

favorites_df.to_csv('favorites/favorites-all.csv', sep='\t', index=False)
current_json.to_json('favorites/current-tweets.json')