#!-coding=utf-8

import pandas as pd
import numpy as np

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
'B' : ['A', 'B', 'C'] * 4,'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
'D' : np.random.randn(12),'E' : np.random.randn(12)})

print 'df is\n', df


pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])