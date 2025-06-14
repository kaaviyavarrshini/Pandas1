import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df=world[(world['area']>=3000000) | (world['population']>=25000000)]
    return pd.DataFrame(df[['name','population','area']])