# Week 2 — Creating Financial Forecasts

## Objective
 Compare a 20-day moving average and a linear-regression time trend for daily closing-price forecasting.

## Dataset
 1,258 observations from 2018-05-01 to 2023-04-28.

## Test results
 | Model | MAE | RMSE | MAPE |
 |---|---:|---:|---:|
 | 20-day Moving Average | 848.33 | 1018.12 | 2.64% |
 | Linear Regression | 4072.70 | 4257.51 | 12.68% |

 Best by test RMSE: **20-day Moving Average**.

## Run
 `pip install -r requirements.txt` then `python src/financial_forecasting.py`.

## Files
 - `data/`: source workbook and cleaned data
 - `notebooks/`: step-by-step analysis\n
 - `src/`: Python script
 - `charts/`: five charts
 - `reports/`: DOCX report and CSV results
 - `docs/`: methodology

## Limitations
 Historical closing prices only; excludes news, fundamentals and macroeconomic conditions. Business-day dates are approximate. Not investment advice.
