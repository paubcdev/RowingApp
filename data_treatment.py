from dataframe_creator import df

fastest = df[df['2000m time'] == df['2000m time'].min()]
slowest = df[df['2000m time'] == df['2000m time'].max()]

heaviest = df[df['weight'] == df['weight'].max()]
lightest = df[df['weight'] == df['weight'].min()]

oldest = df[df['age'] == df['age'].max()]
youngest = df[df['age'] == df['age'].min()]
