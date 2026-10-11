# Customer Shopping Dashboard & Exploratory Data Analysis (EDA)

An interactive Streamlit-based analytical application for tracking business metrics, financial performance, profit margins across departments, and statistical distributions of retail order data.

---

## 📈 Key Metrics & KPI Summary

Based on the dataset analyzed in the application ($N = 8,000$ customers):

| Metric | Recorded Value | Description |
| :--- | :--- | :--- |
| **Total Customers** | `8,000` | Total unique customer transaction profiles analyzed |
| **Total Revenue** | `₹1,764,637,370` | Gross overall revenue generated across all transactions |
| **Total Expense** | `₹1,148,824,129` | Aggregate cost associated with fulfilling orders |
| **Total Profit** | `₹615,813,241` | Net profit generated across the overall period |
| **Overall Profit Margin** | `~34.89%` | Aggregate gross margin across operations |

---

## 📊 Detailed Exploratory Data Analysis Insights

### 1. Financial & Order Distribution Analytics
* **Revenue & Expense Distribution:** Right-skewed distributions indicating a higher concentration of standard-value orders, with a long tail of high-value transactions.
* **Unit Price:** Uniform distribution ranging across price tiers up to **₹80,000**, showing balanced inventory distribution across price points.
* **Order Quantity:** Uniformly distributed across order quantities from **1 to 10 items** per purchase, indicating diverse customer purchasing needs.
* **Customer Rating:** Scores are evenly spread across discrete rating levels (**1.0 through 5.0**), maintaining a balanced distribution without rating skew.

### 2. Departmental Profit Margin Analysis
Profitability margins remain tightly clustered across all business departments, demonstrating consistent operational efficiency:

| Department | Profit Margin (%) |
| :--- | :--- |
| **Marketing** | **35.55%** (Highest Margin) |
| **HR** | **34.94%** |
| **IT** | **34.93%** |
| **Operations** | **34.87%** |
| **Sales** | **34.83%** |
| **Finance** | **34.27%** |

### 3. Correlation & Outlier Analysis
* **Primary Revenue Drivers:** 
  * Strong positive correlation between **Unit Price and Revenue ($r = 0.68$)** and **Quantity and Revenue ($r = 0.65$)**.
  * **Revenue and Expense ($r = 0.94$)** share a strong linear relationship, driving a corresponding high correlation between **Revenue and Profit ($r = 0.84$)**.
* **Independence Metrics:** **Customer Rating** ($r \approx -0.001$) and **Employee Performance Score** ($r \approx 0.003$) show virtually zero correlation with financial metrics like Revenue or Profit.
* **Boxplot Outliers:** Significant upper-bound outliers exist in **Revenue** (peaking around ₹800,000), **Expense** (peaking ~₹700,000), and **Profit** (peaking ~₹480,000).

### 4. Time Series & Trend Analysis (2024 – 2025)
* **Monthly & Cumulative Revenue/Profit:** Stable month-over-month growth from early 2024 through mid-2025, reflected in a constant linear rise in cumulative revenue ($\sim ₹1.75\text{B}$) and profit ($\sim ₹0.615\text{B}$).
* **Weekly Volatility:** Weekly time series analysis highlights short-term revenue spikes peaking near **₹30M** per week, with corresponding profit peaks reaching **₹10M–₹12M**.

---

## 🛠️ Tech Stack & Dependencies

* **Frontend / Dashboard Framework:** [Streamlit](https://streamlit.io/)
* **Data Processing:** Python, Pandas, NumPy
* **Data Visualizations:** Seaborn, Matplotlib, Plotly (Heatmaps, Distribution Histograms, Boxplots, Horizontal Bar Charts, Time Series Line Charts)

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/customer-shopping-dashboard.git
   cd customer-shopping-dashboard
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   *The application will launch in your browser at `http://localhost:8501`.*

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.