# Network Traffic Analysis

A data analytics project analyzing network intrusion patterns to identify which protocols and services are most associated with malicious traffic, using Python (Pandas) and SQL.

## Dataset

- Source: [Network Intrusion Detection dataset](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection) (Kaggle)
- 25,192 rows, 42 columns
- No missing values
- Target column: `class` (normal / anomaly)

## Tools Used

- Python (Pandas, Matplotlib)
- SQL (SQLite, via `sqlite3`)

## Key Findings

1. **Overall traffic split** — 53.4% normal, 46.6% anomaly. The dataset is well-balanced for analysis.

2. **Protocol-wise risk** — ICMP traffic has an 84% attack rate, far higher than TCP (48%) or UDP (17%). ICMP is disproportionately associated with malicious activity (e.g. ping floods, smurf attacks).

3. **Service-wise risk** — The `private` service has a 95.4% attack rate, and `ecr_i`/`eco_i` are above 89%. In contrast, `http` — despite carrying the most traffic (8,003 connections) — has only a 5.5% attack rate, making it one of the safest services in the dataset. High traffic volume does not correlate with high risk.

4. **SQL validation** — Re-ran the protocol-wise analysis as a SQL query (`GROUP BY` on a SQLite database) and confirmed identical results to the Pandas analysis, validating the findings across both approaches.

## Visualizations

| Chart | Insight |
|---|---|
| `class_distribution.png` | Overall normal vs anomaly split |
| `protocol_attacks.png` | Attack distribution by protocol type |
| `service_attack_rate.png` | Attack rate % by service (top 10 by traffic) |

## How to Run

```bash
pip install pandas matplotlib
python explore.py
```

## Files

- `explore.py` — main analysis script
- `*.png` — generated charts
- Dataset CSVs excluded via `.gitignore` (download from Kaggle link above to reproduce)
