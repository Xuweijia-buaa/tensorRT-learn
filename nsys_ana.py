
import pandas as pd


#df=pd.read_excel('./nsys-nvtx.xlsx')
#df=pd.read_excel('./cudagraph.xlsx')
# filepath='./nsys-nvtx.xlsx'
# df1 = pd.read_excel(filepath, engine='openpyxl')
# filepath='./cudagraph.xlsx'
# df2 = pd.read_excel(filepath, engine='openpyxl')


#filepath='./cudagraph.xlsx'
filepath='clip_fp16.xlsx'
df1 = pd.read_excel(filepath, engine='openpyxl')
filepath='./batch2+all_cudagraph.xlsx'
df2 = pd.read_excel(filepath, engine='openpyxl')

def f(x):
    if x.endswith(" μs"):
        return float(x.replace(" μs",""))*0.001
    elif x.endswith(" ms"):
        return float(x.replace(" ms",""))
    elif x.endswith(" s"):
        return float(x.replace(" s",""))*1000
df1['Duration']=df1['Duration'].apply(lambda x:f(x))
df2['Duration']=df2['Duration'].apply(lambda x:f(x))


print('-------------------原来---------------')
print(df1.groupby("Name")['Duration'].sum())
print(df1.groupby("Name")['Duration'].mean())
print('-------------------后来---------------')
print(df2.groupby("Name")['Duration'].sum())
print(df2.groupby("Name")['Duration'].mean())


print('ok')



# 单次
# Name
#  clip Inference                  29.114850
# control inference                13.479530
# unet inference                   16.433779
# vea inference                   141.388100
# Name: Duration, dtype: float64
# -------------------cudagraph后---------------
# Name
#  clip Inference                 89.638825     **  单次很大  40次
# control inference                9.824020      单次小了4ms, 400次，总的小了6000多s
# unet inference                  21.182395      单次和之前差不多。400次
# vea inference                   31.365150    * 20次。  顺手做，不必管他
# Name: Duration, dtype: float64


# 总的
# Name
#  clip Inference                  1164.594000
# control inference               10783.624000
# unet inference                  13147.023000
# vea inference                    2827.762000
# Name: Duration, dtype: float64
# -------------------cudagraph后---------------
# Name
#  clip Inference                 3585.553000
# control inference               3929.608000
# unet inference                  8472.958000    **
# vea inference                    627.303000
# Name: Duration, dtype: float64
