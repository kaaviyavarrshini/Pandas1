import pandas as pd

#Soln 1: Using Merge
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=customers.merge(orders,
                left_on ='id',
                right_on='customerId',
                how='left')
    df=df[df['id_y'].isnull()]
    print(df[['name']])
    return pd.DataFrame(df[['name']]).rename(columns={'name':'Customers'})

#Soln 2: Using isin()
    df=customers[~customers['id'].isin(orders['customerId'])]
    return pd.DataFrame(df[['name']]).rename(columns={'name':'Customers'})