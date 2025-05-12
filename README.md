# 🚀 CRM LEADS DATA PROJECT

A full-stack data exploration and interactive visualization project analyzing CRM lead data for Trelleborg using **Python**, **Pandas**, and **Streamlit**.

> 📊 From raw data → to insight → to dashboard → to deployment.

---

## 📁 Project Overview
https://ha11yeon-crm-leads-data-trlleborg.streamlit.app/

This project aims to visualize and explore lead-related CRM data, helping business stakeholders better understand:

- Lead status & lifecycle
- Marketing & sales channel efficiency
- Lead engagement scores & expected revenue
- Survey-based customer satisfaction

---
## 📂 Directory Structure

```
CRM_LEADS/
├── code/
│   ├── 01leads_data.ipynb
│   ├── 02Feature_importance.ipynb
│   ├── 03~06Data_Flow.ipynb
│   └── crm_full_dashboard.ipynb
│
├── CRM/
│   └── crm.py                  # ✅ Streamlit 메인 앱
│   └── df_sample.csv           # ✅ Streamlit 첨부데이터
│
├── data/
│   ├── lead_columns_list.csv
│   ├── lead_notes.csv          # ⚠️ 약 57MB
│   ├── leads_df_cleaned.csv    # ⚠️ 약 65MB
│   └── notes_only.csv
```

> 📝 핵심 파일:
> - `crm.py`: Streamlit 대시보드 실행 파일
> - `df_sample.csv`: 테스트용 CSV 파일
> - `code/`: Jupyter 기반 분석 기록
> - `data/`: 실제 CRM 리드 및 메모 데이터

---

## 🧰 Tech Stack

- **Python 3.11**
- **Pandas** for data manipulation
- **Seaborn & Matplotlib** for plotting
- **Streamlit** for web dashboard
- **GitHub + Streamlit Cloud** for deployment

---

## 📊 Dashboard Features

✅ Upload `.csv` CRM lead dataset  
✅ Interactive visualizations:
- Lead status (`Status_Text`) distribution
- Engagement / score / revenue by category
- Channel comparison
- Owner-based performance ranking
✅ Auto-adapts to any uploaded CSV (as long as `Status_Text` exists)

---

## 🚀 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run Streamlit app
streamlit run CRM/crm.py
