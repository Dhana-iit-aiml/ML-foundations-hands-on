
#Series

import pandas as pd

pd_series1 = pd.Series([100,90,80], index=['Math', 'science', 'social'])
print(pd_series1['Math'])
#100


pd_df1 = pd.DataFrame({
'student_name' : ['Dhana','Sankar'],
'math' : [75,85],
'science' : [80,90],
'social' : [94,64]

})

print(pd_df1['student_name'][0])