import pandas as pd
data=[(1,1,0),(1,1,1),(1,1,2),(1,2,3),(1,2,4),(2,1,5),(2,1,6)]
schema= ['ActorId', 'DirectorId',   'timestamp']

df=pd.DataFrame(data =data,columns =schema)
print(df)

result_df = df.groupBy("ActorId","DirectorId").count()
print(result_df)



df1 = result_df.filter(result_df["count"]>2)
print(df1)
