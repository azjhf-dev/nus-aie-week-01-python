"""Tabular data profiling with explicit validation, no external inputs by default."""
from io import StringIO
import pandas as pd
import numpy as np
from labcore import activity_data


def audit_csv(text, policy='median'):
    # Check the raw header before pandas can silently rename duplicate columns.
    import csv
    raw=list(csv.reader(StringIO(text)))
    if not raw or not raw[0]: raise ValueError('Empty CSV')
    if len(raw[0])!=len(set(raw[0])): raise ValueError('Duplicate column names')
    expected={'hours','practice','score','group'}
    if set(raw[0])!=expected: raise ValueError('Unexpected columns')
    df=pd.read_csv(StringIO(text))
    if df.empty: raise ValueError('No records')
    for col in ['hours','practice','score']:
        df[col]=pd.to_numeric(df[col],errors='raise')
    if df['score'].isna().any() or not df['score'].between(0,100).all(): raise ValueError('Bad score')
    if df['practice'].isna().any() or not df['practice'].between(0,100).all(): raise ValueError('Bad practice count')
    if df.hours.notna().any() and not df.hours.dropna().between(0,24).all(): raise ValueError('Bad hours')
    before=int(df.hours.isna().sum())
    if policy=='drop': df=df.dropna(subset=['hours'])
    elif policy=='median':
        if df.hours.isna().all(): raise ValueError('Cannot learn an imputation value from an all-missing column')
        df['hours']=df.hours.fillna(df.hours.median())
    else: raise ValueError('Unknown missing-data policy')
    if df.empty: raise ValueError('No records after cleaning')
    return df, {'rows':len(df),'missing_before':before,'policy':policy,'hours_mean':float(df.hours.mean())}


if __name__=='__main__':
    frame,report=audit_csv(pd.DataFrame(activity_data()).to_csv(index=False))
    print(report)
