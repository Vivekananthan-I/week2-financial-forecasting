from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"; OUT=ROOT/"reports"; CH=ROOT/"charts"
OUT.mkdir(exist_ok=True); CH.mkdir(exist_ok=True)
files=list(DATA.glob("*.xlsx")); raw=pd.read_excel(files[0]) if files else pd.read_csv(DATA/"cleaned_financial_dataset.csv")
raw.columns=[str(c).strip() for c in raw.columns]
ren={}
for c in raw.columns:
 k=c.lower().replace(" ","")
 if k=="date": ren[c]="Date"
 elif k.startswith("close"): ren[c]="Close"
df=raw.rename(columns=ren); df["Date"]=pd.to_datetime(df["Date"],errors="coerce"); df["Close"]=pd.to_numeric(df["Close"],errors="coerce")
df=df.dropna(subset=["Date","Close"]).sort_values("Date").drop_duplicates("Date").reset_index(drop=True)
n=len(df); split=int(n*.8); tr=df.iloc[:split]; te=df.iloc[split:]; close=df.Close.to_numpy(float)
ma=np.array([close[max(0,i-20):i].mean() for i in range(split,n)])
slope,intercept=np.polyfit(np.arange(split),tr.Close.to_numpy(float),1); lr=intercept+slope*np.arange(split,n); y=te.Close.to_numpy(float)
def metrics(y,p):
 e=y-p; return {"MAE":np.mean(abs(e)),"RMSE":np.sqrt(np.mean(e**2)),"MAPE_%":np.mean(abs(e/y))*100}
pd.DataFrame([{"Model":"20-day Moving Average",**metrics(y,ma)},{"Model":"Linear Regression",**metrics(y,lr)}]).to_csv(OUT/"model_performance.csv",index=False)
pd.DataFrame({"Date":te.Date,"Actual":y,"MA_Predicted":ma,"LR_Predicted":lr}).to_csv(OUT/"test_predictions.csv",index=False)
hist=list(close[-20:]); maf=[]
for _ in range(30):
 v=float(np.mean(hist[-20:])); maf.append(v); hist.append(v)
lrf=intercept+slope*np.arange(n,n+30); dates=pd.bdate_range(df.Date.iloc[-1]+pd.offsets.BDay(1),periods=30)
fc=pd.DataFrame({"Forecast_Date":dates,"Moving_Average_Forecast":maf,"Linear_Regression_Forecast":lrf}); fc["Model_Average_Forecast"]=fc.iloc[:,1:3].mean(axis=1); fc.to_csv(OUT/"30_day_forecast.csv",index=False)
print("Model evaluation and 30-day forecast saved in reports/.")
