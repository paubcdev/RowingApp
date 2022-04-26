from dataframe_creator import df

slowest = df.loc[:, ['2000m time']].min()
fastest = df.loc[:, ['2000m time']].max()
