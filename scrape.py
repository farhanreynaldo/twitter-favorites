import twint 
import pandas as pd 

username = "xynx"
c = twint.Config()
c.Username = username
c.Limit = 20
c.Pandas = True
c.Pandas_clean = True
c.Store_json = True
c.Output = 'favorites'

twint.run.Favorites(c)

new_favorites = twint.storage.pandas.Tweets_df
favorites_df = pd.read_csv('favorites/favorites-all.csv')

favorites_df = pd.concat([favorites_df, new_favorites])
favorites_df.to_csv('favorites/favorites-all.csv', sep=';', index=False)