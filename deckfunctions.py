def showhand():
    return df.loc[df['Zone']=='Hand']
    
def showboard():
    return df.loc[df['Zone']=='Board']

def showgraveyard():
    return df.loc[df['Zone']=='Graveyard']
    
def showexile():
    return df.loc[df['Zone']=='Exile']

def drawcard(x: int) -> int:
    start = df.loc[df['Zone'] == 'Deck'].iloc[0].name
    df.loc[start:start+x-1, 'Zone'] = 'Hand'
# hand = df.sample(n=7).index
# df.loc[hand,'Zone'] = 'Hand'
def shuffledeck(df):
    df = df.sample(frac=1, ignore_index=True)
    return df

def playcard(x: int) -> int:
    df.loc[x,'Zone'] ='Board'

def discard(x: int) -> int:
    df.loc[x,'Zone'] ='Graveyard'
    
def exile(x: int) -> int:
    df.loc[x,'Zone'] ='Exile'

def text(x: int) -> int:
    print(df.at[x, 'Text'])

def reset():
    df['Zone'] = 'Deck'
