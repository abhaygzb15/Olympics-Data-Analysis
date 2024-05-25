import pandas as pd
def preprocess(df,regions):
    # filtering for summer
    df=df[df['Season']=='Summer']
    # merging with regions
    df=df.merge(regions,on='NOC',how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding (other is Label)
    df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df