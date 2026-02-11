import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Load CSV
# -------------------------------
df = pd.read_csv("Facebook Metrics of Cosmetic Brand.csv")

# -------------------------------
# Dashboard Title
# -------------------------------
st.title("📊 Facebook Metrics Dashboard")
st.write("This dashboard helps you understand which posts perform best and when to post for maximum engagement.")

# -------------------------------
# Dataset Overview
# -------------------------------
st.subheader("Dataset Overview")
st.write(f"✅ The dataset contains **{df.shape[0]} posts** and **{df.shape[1]} columns** of information.")
st.write("Here are the first few rows of data:")
st.dataframe(df.head())

# -------------------------------
# Post Type Performance
# -------------------------------
st.subheader("🔥 Which Post Types Perform Best?")
post_type_perf = df.groupby("Type")["Total Interactions"].mean().sort_values(ascending=False)

fig1, ax1 = plt.subplots()
sns.barplot(x=post_type_perf.index, y=post_type_perf.values, ax=ax1, palette="viridis")
ax1.set_title("Average Interactions by Post Type")
ax1.set_ylabel("Avg Total Interactions")
st.pyplot(fig1)

best_type = post_type_perf.idxmax()
best_value = round(post_type_perf.max(), 1)
st.write(f"👉 On average, **{best_type} posts** perform the best with about **{best_value} interactions**.")

# -------------------------------
# Best Day to Post
# -------------------------------
st.subheader("📅 Best Day of the Week to Post")
weekday_perf = df.groupby("Post Weekday")["Total Interactions"].mean()

fig2, ax2 = plt.subplots()
sns.lineplot(x=weekday_perf.index, y=weekday_perf.values, marker="o", ax=ax2)
ax2.set_title("Average Interactions by Weekday")
ax2.set_xlabel("Weekday (1=Sunday, 7=Saturday)")
ax2.set_ylabel("Avg Total Interactions")
st.pyplot(fig2)

best_day = weekday_perf.idxmax()
best_day_value = round(weekday_perf.max(), 1)
st.write(f"👉 The best day to post is **Day {best_day}** with about **{best_day_value} interactions** on average.")

# -------------------------------
# Best Hour to Post
# -------------------------------
st.subheader("⏰ Best Hour of the Day to Post")
hour_perf = df.groupby("Post Hour")["Total Interactions"].mean()

fig3, ax3 = plt.subplots()
sns.lineplot(x=hour_perf.index, y=hour_perf.values, marker="o", ax=ax3, color="orange")
ax3.set_title("Average Interactions by Hour")
ax3.set_xlabel("Hour of Day (0-23)")
ax3.set_ylabel("Avg Total Interactions")
st.pyplot(fig3)

best_hour = hour_perf.idxmax()
best_hour_value = round(hour_perf.max(), 1)
st.write(f"👉 The best time to post is around **{best_hour}:00** with about **{best_hour_value} interactions**.")

# -------------------------------
# Correlation Heatmap
# -------------------------------
st.subheader("📈 Correlation Between Metrics")
fig4, ax4 = plt.subplots(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", ax=ax4)
ax4.set_title("Correlation Heatmap")
st.pyplot(fig4)

st.write("👉 This shows how metrics are related. For example, posts with more **likes** often also have more **shares and comments**.")