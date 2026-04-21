# IPL Data Pipeline

End-to-end data pipeline analysing IPL match data (2008-2019).

## Versions
- v1: Python + Pandas + SQLite (local)
- v2: PySpark + Databricks (cloud, distributed)

## Architecture
CSV → Python/PySpark → SQLite/Databricks → SQL Analytics → JSON Output

## Key Insights
- Mumbai Indians — most wins (109)
- Fielding first wins 55.94% of matches
- CH Gayle — most Player of Match awards (21)

## Tech Stack
Python, Pandas, SQL, SQLite, PySpark, Databricks

## How to run
Local: python ipl_analysis.py
Cloud: Run IPL_PySpark_Pipeline.ipynb on Databricks
