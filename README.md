# 📈 Growth Marketing CLI: Funnel Analyzer

A custom-built Python Command Line Interface (CLI) to automate and streamline core growth marketing tasks, starting with in-depth funnel analysis.

---

## 🔬 Project 1: Funnel Analyzer

### 🤯 Problem
It's difficult and time-consuming to quantitatively identify the biggest point of friction and user drop-off in a raw user event dataset, slowing down investigation into key business metrics.

### ✅ Solution
I built a Python-based **Funnel Analyzer** that processes raw event data (CSV), calculates step-to-step and overall conversion rates, and outputs the results in a clear, actionable table.

### ⚙️ Technical Implementation
* **Language:** Python
* **CLI Library:** The core tool is built using the `argparse` library for a robust command-line interface.
* **Data Analysis:** The `pandas` library is used for efficient data manipulation and cohort analysis.
* **Key Metrics:** Step-to-step conversion, overall conversion, and total drop-offs.

### 💡 Hypothesis & Insight (Simulated Example)
* **Hypothesis:** The analysis of our simulated data revealed that **40% of users drop off at the email verification step**.
* **Insight:** This suggests a major point of friction. We should immediately investigate our email delivery service's latency and the clarity of the verification UI/UX.

### 🚀 How to Run (Local Machine)
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Growth-Marketing-CLI.git](https://github.com/YOUR_USERNAME/Growth-Marketing-CLI.git)
    cd Growth-Marketing-CLI
    ```
2.  **Install dependencies:**
    ```bash
    pip install pandas
    ```
3.  **Run the analysis:** (The `user_events.csv` would be a file you add later)
    ```bash
    python growth_cli.py funnel-analyze --file data/user_events.csv
    ```
---
