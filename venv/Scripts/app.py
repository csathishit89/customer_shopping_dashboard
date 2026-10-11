import streamlit as st
import pandas as pd
from pathlib import Path
import datetime
import calendar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Customer Shopping Dashboard",
    page_icon="",
    layout="wide"
)

csv_path = BASE_DIR / "Data_Science.xlsx"

st.title("Customer Shopping Dashboard 🚀")

customer_df = pd.read_excel(csv_path)

# Custom CSS for modern card UI styling
st.markdown("""
<style>
    .block-container {
        padding-top: 3rem; /* Adjusts spacing above the main header */
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 20px 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        font-size: 14px;
        font-weight: 600;
        color: #6c757d;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: 700;
        color: #1e293b;
    }
    .text-profit {
        color: #10b981; /* Soft Green for Profit */
    }
    .text-expense {
        color: #ef4444; /* Soft Red for Expense */
    }
</style>
""", unsafe_allow_html=True)

total_customers = customer_df['Transaction_ID'].count()
total_revenue = customer_df['Revenue'].sum()
total_expense = customer_df['Expense'].sum()
total_profit = customer_df['Profit'].sum()

# Render cards in 4 columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Customers</div>
        <div class="metric-value">{total_customers:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💰 Total Revenue</div>
        <div class="metric-value">₹{total_revenue:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📉 Total Expense</div>
        <div class="metric-value text-expense">₹{total_expense:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📈 Total Profit</div>
        <div class="metric-value text-profit">₹{total_profit:,.0f}</div>
    </div>
    <br/>
    """, unsafe_allow_html=True)
    
col1, col2 = st.columns(2)

# Revenue Distribution
with col1:
    fig1, ax1 = plt.subplots(figsize=(8, 5))

    customer_df["Revenue"].hist(
        bins=15,
        ax=ax1,
        edgecolor="black",
        color='#3b82f6',
    )

    ax1.set_title("Revenue Distribution")
    ax1.set_xlabel("Revenue")
    ax1.set_ylabel("Frequency")

    fig1.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)


# Expense Distribution
with col2:
    fig2, ax2 = plt.subplots(figsize=(8, 5))

    customer_df["Expense"].hist(
        bins=15,
        ax=ax2,
        edgecolor="black",
        color="#f56363",
    )

    ax2.set_title("Expense Distribution")
    ax2.set_xlabel("Expense")
    ax2.set_ylabel("Frequency")

    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

col1, col2 = st.columns(2)

# Unit_Price Distribution
with col1:
    fig1, ax1 = plt.subplots(figsize=(8, 5))

    customer_df["Unit_Price"].hist(
        bins=15,
        ax=ax1,
        edgecolor="black",
        color="#d7f33a",
    )

    ax1.set_title("Unit_Price Distribution")
    ax1.set_xlabel("Unit_Price")
    ax1.set_ylabel("Frequency")

    fig1.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)


# Profit Distribution
with col2:
    fig2, ax2 = plt.subplots(figsize=(8, 5))

    customer_df["Profit"].hist(
        bins=15,
        ax=ax2,
        edgecolor="black",
        color="#31eb50",
    )

    ax2.set_title("Profit Distribution")
    ax2.set_xlabel("Profit")
    ax2.set_ylabel("Frequency")

    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)
    
col1, col2 = st.columns(2)

# Quantity Distribution
with col1:
    fig1, ax1 = plt.subplots(figsize=(8, 5))

    customer_df["Quantity"].hist(
        bins=15,
        ax=ax1,
        edgecolor="black",
        color="#f3c327",
    )

    ax1.set_title("Quantity Distribution")
    ax1.set_xlabel("Quantity")
    ax1.set_ylabel("Frequency")

    fig1.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)


# Customer_Rating Distribution
with col2:
    fig2, ax2 = plt.subplots(figsize=(8, 5))

    customer_df["Customer_Rating"].hist(
        bins=15,
        ax=ax2,
        edgecolor="black",
        color="#3cd5f0",
    )

    ax2.set_title("Customer Rating Performance Score Distribution")
    ax2.set_xlabel("Customer Rating Performance Score Distribution")
    ax2.set_ylabel("Frequency")

    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)
    
st.divider()

st.subheader("Profit Margin (%) by Department")

dept_margin = (
    customer_df.groupby('Department')[['Revenue', 'Profit']]
    .sum()
    .reset_index()
)

dept_margin['Profit_Margin_%'] = (dept_margin['Profit'] / dept_margin['Revenue']) * 100

dept_margin = dept_margin.sort_values(by='Profit_Margin_%', ascending=False)

plt.figure(figsize=(10, 4))
sns.set_theme(style="whitegrid")

ax = sns.barplot(
    data=dept_margin,
    x='Profit_Margin_%',
    y='Department',
    hue='Department',
    legend=False,
)

plt.xlabel('Profit Margin (%)', fontsize=12, fontweight='bold')
plt.ylabel('Department', fontsize=12, fontweight='bold')
plt.xlim(0, dept_margin['Profit_Margin_%'].max() * 1.18)

for p in ax.patches:
    width = p.get_width()
    ax.annotate(
        f'{width:.2f}%',
        (width, p.get_y() + p.get_height() / 2.),
        ha='left', va='center',
        fontsize=10, fontweight='bold', color='#333333'
    )

plt.tight_layout()
st.pyplot(plt)

st.divider()

st.subheader("Profit Margin (%) by Product")

prod_margin = (
    customer_df.groupby('Product')[['Revenue', 'Profit']]
    .sum()
    .reset_index()
)

prod_margin['Profit_Margin_%'] = (prod_margin['Profit'] / prod_margin['Revenue']) * 100

prod_margin = prod_margin.sort_values(by='Profit_Margin_%', ascending=False)


plt.figure(figsize=(10, 4))
sns.set_theme(style="whitegrid")

ax = sns.barplot(
    data=prod_margin,
    x='Profit_Margin_%',
    y='Product',
    hue='Product',
    legend=False,
)

plt.xlabel('Profit Margin (%)', fontsize=12, fontweight='bold')
plt.ylabel('Product', fontsize=12, fontweight='bold')
plt.xlim(0, prod_margin['Profit_Margin_%'].max() * 1.18)

for p in ax.patches:
    width = p.get_width()
    ax.annotate(
        f'{width:.2f}%',
        (width + 0.8, p.get_y() + p.get_height() / 2.),
        ha='left', va='center',
        fontsize=10, fontweight='bold', color='#333333'
    )

plt.tight_layout()
st.pyplot(plt)

st.divider()

st.subheader("Profit Margin (%) by City")

city_margin = (
    customer_df.groupby('City')[['Revenue', 'Profit']]
    .sum()
    .reset_index()
)

city_margin['Profit_Margin_%'] = (city_margin['Profit'] / city_margin['Revenue']) * 100

city_margin = city_margin.sort_values(by='Profit_Margin_%', ascending=False)

plt.figure(figsize=(10, 4))
sns.set_theme(style="whitegrid")

ax = sns.barplot(
    data=city_margin,
    x='Profit_Margin_%',
    y='City',
    hue='City',
    legend=False,
)

plt.xlabel('Profit Margin (%)', fontsize=12, fontweight='bold')
plt.ylabel('City', fontsize=12, fontweight='bold')
plt.xlim(0, city_margin['Profit_Margin_%'].max() * 1.18)

for p in ax.patches:
    width = p.get_width()
    ax.annotate(
        f'{width:.2f}%',
        (width + 0.8, p.get_y() + p.get_height() / 2.),
        ha='left', va='center',
        fontsize=10, fontweight='bold', color='#333333'
    )

plt.tight_layout()
st.pyplot(plt)

st.divider()

col1, col2 = st.columns(2)

numeric_cols = [
    'Quantity',
    'Unit_Price',
    'Revenue',
    'Expense',
    'Profit',
    'Customer_Rating',
    'Employee_Performance_Score'
]

corr = customer_df[numeric_cols].corr()

with col1:
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(
        'Correlation Heatmap',
        fontsize=20,
        fontweight='bold',
        pad=15
    )
    plt.xticks(rotation=45)
    st.pyplot(plt)
    
with col2:
    plt.figure(figsize=(6, 5))
    sns.boxplot(
        data=customer_df[numeric_cols]
    )
    plt.xticks(rotation=45)
    plt.title("Outlier Detection Using Boxplot", fontsize=16,
            fontweight='bold')
    st.pyplot(plt)
    
st.divider()

col1, col2 = st.columns(2)

with col1:
    current_year = datetime.datetime.now().year-1
    years_list = ["Select Year"] + list(range(current_year, current_year - 2, -1))

    selected_year = st.selectbox("Select Year", options=years_list)
    
with col2:
    months_list = ["Select Month"] + list(calendar.month_name)[1:]

    selected_month = st.selectbox("Select Month", options=months_list)

customer_df['Purchase_Date'] = pd.to_datetime(customer_df['Purchase_Date'])

filtered_df = customer_df.copy()

if selected_year != "Select Year":
    filtered_df = filtered_df[filtered_df['Purchase_Date'].dt.year == int(selected_year)]

if selected_month != "Select Month":
    month_num = list(calendar.month_name).index(selected_month)
    filtered_df = filtered_df[filtered_df['Purchase_Date'].dt.month == month_num]

col1, col2 = st.columns(2)

filtered_df['Purchase_Date'] = pd.to_datetime(
    filtered_df['Purchase_Date'],
    errors='coerce'
)

filtered_df = filtered_df.dropna(subset=['Purchase_Date'])

with col1:
    if not filtered_df.empty:

        monthly_df = (
            filtered_df
            .set_index('Purchase_Date')
            .resample('MS')[['Revenue', 'Profit']]
            .sum()
            .reset_index()
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            monthly_df['Purchase_Date'],
            monthly_df['Revenue'],
            color='#1f77b4',
            label='Total Revenue',
            linewidth=2.5,
            marker='o'
        )

        ax.fill_between(
            monthly_df['Purchase_Date'],
            monthly_df['Revenue'],
            color='#1f77b4',
            alpha=0.15
        )

        ax.plot(
            monthly_df['Purchase_Date'],
            monthly_df['Profit'],
            color='#2ca02c',
            label='Total Profit',
            linewidth=2.5,
            marker='s'
        )

        ax.fill_between(
            monthly_df['Purchase_Date'],
            monthly_df['Profit'],
            color='#2ca02c',
            alpha=0.15
        )

        ax.set_title(
            'Monthly Revenue & Profit',
            fontsize=14,
            fontweight='bold',
            pad=15
        )
        ax.set_xlabel('Month')
        ax.set_ylabel('Amount')
        ax.legend(loc='upper left')
        ax.grid(True, linestyle=':', alpha=0.6)

        fig.autofmt_xdate(rotation=30)
        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    else:
        st.warning("No data available for the selected Year/Month.")

with col2:
    if not filtered_df.empty:
        monthly_df = (
            filtered_df
            .set_index('Purchase_Date')
            .resample('MS')[['Revenue', 'Profit']]
            .sum()
            .reset_index()
        )

        # Running totals across the selected period
        monthly_df['Cumulative_Revenue'] = (
            monthly_df['Revenue'].cumsum()
        )

        monthly_df['Cumulative_Profit'] = (
            monthly_df['Profit'].cumsum()
        )

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            monthly_df['Purchase_Date'],
            monthly_df['Cumulative_Revenue'],
            color='#9467bd',
            label='Cumulative Revenue',
            linewidth=2.5,
            marker='o'
        )

        ax.plot(
            monthly_df['Purchase_Date'],
            monthly_df['Cumulative_Profit'],
            color='#ff7f0e',
            label='Cumulative Profit',
            linewidth=2.5,
            marker='s'
        )

        ax.set_title(
            'Cumulative Revenue & Profit',
            fontsize=14,
            fontweight='bold',
            pad=15
        )
        ax.set_xlabel('Month')
        ax.set_ylabel('Cumulative Amount')
        ax.legend(loc='upper left')
        ax.grid(True, linestyle=':', alpha=0.6)

        fig.autofmt_xdate(rotation=30)
        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    else:
        st.warning("No data available for the selected Year/Month.")

st.divider()

if not filtered_df.empty:
    monthly_df = (
        filtered_df.set_index('Purchase_Date')
        .resample('W')[['Revenue', 'Profit']]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        monthly_df['Purchase_Date'],
        monthly_df['Revenue'],
        color='#1f77b4',
        label='Total Revenue',
        linewidth=2.5,
        marker='o'
    )
    plt.fill_between(
        monthly_df['Purchase_Date'],
        monthly_df['Revenue'],
        color='#1f77b4',
        alpha=0.15
    )

    plt.plot(
        monthly_df['Purchase_Date'],
        monthly_df['Profit'],
        color='#2ca02c',
        label='Total Profit',
        linewidth=2.5,
        marker='s'
    )
    plt.fill_between(
        monthly_df['Purchase_Date'],
        monthly_df['Profit'],
        color='#2ca02c',
        alpha=0.25
    )

    plt.title('Weekly Revenue & Profit Time Trends', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Purchase Date', fontsize=12, fontweight='bold')
    plt.ylabel('Amount', fontsize=12, fontweight='bold')
    plt.xticks(rotation=30)
    plt.legend(loc='upper left', frameon=True, facecolor='white', framealpha=0.9)
    plt.grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    st.pyplot(plt)
    
st.divider()
