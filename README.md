# 🚀📊 ETF Liquidity & Institutional Block Trade Dashboard

## 🎯 Project Overview
This project is designed to monitor and visualize key performance indicators for two specific ETF fund families: Global X and BetaPro. This project replaces manual data entry by integrating Python and Office Scripts to process high-frequency trading data across 36 distinct tickers for the Global X and BetaPro fund families.

---

## 🚀 Key Features

### **🐍 Python-Powered Dashboards**
* Uses Pandas and Matplotlib to generate multi-asset grid visualizations.
* Tracks **AUM trends**, **daily volume**, and **trade frequency** in real-time summary tabs.

### **⚙️ Block Trade Automation**
* Implemented a custom **Office Script (TypeScript)** to scan intraday execution logs.
* Automatically identifies and counts "Block Trades" defined as any single execution **>= 250,000 units**.

### **🧹 Data Engineering & Cleaning**
* Developed custom logic to convert complex Bloomberg financial strings (e.g., converting 1,000,000 into "1M").

### **🏗️ Scalable Architecture**
* Designed to handle 36 distinct tickers across various fund families.
* Built to process detailed intraday timestamps for accurate liquidity tracking.

---

## 🌟 Impact

* **⏱️ Efficiency:** Significantly reduced the time required to generate weekly launch reports for senior management by automating data aggregation.
* **💡 Institutional Insight:** Enhanced market sentiment analysis by isolating high-conviction "Block Trades" from standard retail flow.
* **🎯 Data Integrity:** Eliminated human error in trade counting and manual formatting through standardized scripting.

---

## 🛠️ Technical Stack

* **Languages:** Python (Pandas, Matplotlib), TypeScript (Office Scripts).
* **Tools:** Microsoft Excel (Advanced), Bloomberg Terminal (BDH/BDP Logic).

---

## 🎓 About Me
I am a Financial Analysis and Risk Management student @University of Waterloo. 🇨🇦🐈
