import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Facebook Metrics Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Sidebar - Developed by Rabia Muneeb
# -------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>📱 DASHBOARD</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h3 style='text-align: center;'>📊 Navigation</h3>", unsafe_allow_html=True)
    option = st.radio(
        "Go to",
        ["🏠 Home", "📈 Post Analysis", "⏰ Timing Analysis", "🔗 Correlation"]
    )
    
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>📂 Dataset Info</h3>", unsafe_allow_html=True)
    
    # Load CSV
    df = pd.read_csv("Facebook Metrics of Cosmetic Brand.csv")
    
    st.write(f"**Total Posts:** {df.shape[0]}")
    st.write(f"**Total Columns:** {df.shape[1]}")
    st.write(f"**Post Types:** {df['Type'].nunique()}")
    
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: #4ECDC4;'>👩‍💻 Developed by</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #FFD93D;'>Rabia Muneeb</h2>", unsafe_allow_html=True)
   
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #888;'>© 2024 All Rights Reserved</p>", unsafe_allow_html=True)

# -------------------------------
# Main Content Area
# -------------------------------

# ============= HEADER SECTION =============
st.markdown("<h1 style='text-align: center; color: #2E86AB;'>📊 FACEBOOK METRICS DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666;'>Cosmetic Brand Social Media Performance Analysis</h4>", unsafe_allow_html=True)
st.markdown("---")

# Load data if not already loaded in sidebar
if 'df' not in locals():
    df = pd.read_csv("Facebook Metrics of Cosmetic Brand.csv")

# ============= HOME SECTION =============
if option == "🏠 Home":
    # ---------- MAIN HEADING ----------
    st.markdown("<h2 style='color: #2E86AB;'>📋 DASHBOARD OVERVIEW</h2>", unsafe_allow_html=True)
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>📌 Dataset Summary</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Total Posts", df.shape[0])
    with col2:
        st.metric("📏 Total Features", df.shape[1])
    with col3:
        st.metric("🎯 Post Types", df['Type'].nunique())
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>🔍 Data Preview</h3>", unsafe_allow_html=True)
    st.dataframe(df.head(10), use_container_width=True)
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>📋 Column Information</h3>", unsafe_allow_html=True)
    col_info = pd.DataFrame({
        'Column Name': df.columns,
        'Data Type': df.dtypes.values,
        'Non-Null Count': df.count().values
    })
    st.dataframe(col_info, use_container_width=True)

# ============= POST ANALYSIS SECTION =============
elif option == "📈 Post Analysis":
    # ---------- MAIN HEADING ----------
    st.markdown("<h2 style='color: #2E86AB;'>🔥 POST TYPE PERFORMANCE ANALYSIS</h2>", unsafe_allow_html=True)
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>📊 Average Interactions by Post Type</h3>", unsafe_allow_html=True)
    
    post_type_perf = df.groupby("Type")["Total Interactions"].mean().sort_values(ascending=False)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        colors = ['#FF6B6B', '#4ECDC4', '#FFD93D', '#6C5B7B', '#F08A5D']
        bars = sns.barplot(x=post_type_perf.index, y=post_type_perf.values, ax=ax1, palette=colors[:len(post_type_perf)])
        ax1.set_title("Average Interactions by Post Type", fontsize=14, fontweight='bold')
        ax1.set_ylabel("Avg Total Interactions", fontsize=12)
        ax1.set_xlabel("Post Type", fontsize=12)
        
        # Add value labels on bars
        for i, v in enumerate(post_type_perf.values):
            ax1.text(i, v + 0.5, str(round(v, 1)), ha='center', fontweight='bold')
        
        st.pyplot(fig1)
    
    with col2:
        st.markdown("<h4 style='color: #2E86AB;'>📈 Key Insights</h4>", unsafe_allow_html=True)
        best_type = post_type_perf.idxmax()
        best_value = round(post_type_perf.max(), 1)
        
        st.info(f"🏆 **Best Performing:** {best_type}")
        st.success(f"⭐ **Avg Interactions:** {best_value}")
        st.write("---")
        
        # Show all types performance
        st.markdown("<h4 style='color: #2E86AB;'>📊 Performance Ranking</h4>", unsafe_allow_html=True)
        for idx, (post_type, value) in enumerate(post_type_perf.items(), 1):
            st.write(f"{idx}. **{post_type}**: {round(value, 1)} interactions")
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>📌 Recommendation</h3>", unsafe_allow_html=True)
    st.success(f"👉 **OPTIMAL STRATEGY:** Focus on creating more **{best_type} posts** as they generate the highest average engagement of **{best_value} interactions**.")

# ============= TIMING ANALYSIS SECTION =============
elif option == "⏰ Timing Analysis":
    # ---------- MAIN HEADING ----------
    st.markdown("<h2 style='color: #2E86AB;'>⏰ OPTIMAL POSTING TIME ANALYSIS</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # ---------- SUBHEADING ----------
        st.markdown("<h3 style='color: #4ECDC4;'>📅 Best Day of Week</h3>", unsafe_allow_html=True)
        weekday_perf = df.groupby("Post Weekday")["Total Interactions"].mean()
        
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.lineplot(x=weekday_perf.index, y=weekday_perf.values, marker="o", ax=ax2, 
                    color='#FF6B6B', linewidth=3, markersize=10)
        ax2.set_title("Average Interactions by Weekday", fontsize=14, fontweight='bold')
        ax2.set_xlabel("Weekday (1=Sunday, 7=Saturday)", fontsize=12)
        ax2.set_ylabel("Avg Total Interactions", fontsize=12)
        ax2.grid(True, alpha=0.3)
        st.pyplot(fig2)
        
        best_day = weekday_perf.idxmax()
        best_day_value = round(weekday_perf.max(), 1)
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        st.success(f"📆 **Best Day:** {days[best_day-1]} (Day {best_day}) with **{best_day_value}** avg interactions")
    
    with col2:
        # ---------- SUBHEADING ----------
        st.markdown("<h3 style='color: #4ECDC4;'>⏱️ Best Hour of Day</h3>", unsafe_allow_html=True)
        hour_perf = df.groupby("Post Hour")["Total Interactions"].mean()
        
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        sns.lineplot(x=hour_perf.index, y=hour_perf.values, marker="o", ax=ax3, 
                    color='#4ECDC4', linewidth=3, markersize=10)
        ax3.set_title("Average Interactions by Hour", fontsize=14, fontweight='bold')
        ax3.set_xlabel("Hour of Day (0-23)", fontsize=12)
        ax3.set_ylabel("Avg Total Interactions", fontsize=12)
        ax3.grid(True, alpha=0.3)
        st.pyplot(fig3)
        
        best_hour = hour_perf.idxmax()
        best_hour_value = round(hour_perf.max(), 1)
        st.success(f"⏰ **Best Time:** {best_hour}:00 with **{best_hour_value}** avg interactions")
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>🎯 Combined Timing Recommendation</h3>", unsafe_allow_html=True)
    st.info(f"📌 **OPTIMAL POSTING SCHEDULE:** Post on **{days[best_day-1]} at {best_hour}:00** for maximum engagement (avg {best_hour_value} interactions)")

# ============= CORRELATION SECTION =============
elif option == "🔗 Correlation":
    # ---------- MAIN HEADING ----------
    st.markdown("<h2 style='color: #2E86AB;'>🔗 METRICS CORRELATION ANALYSIS</h2>", unsafe_allow_html=True)
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>📊 Correlation Heatmap</h3>", unsafe_allow_html=True)
    
    fig4, ax4 = plt.subplots(figsize=(12, 8))
    corr_matrix = df.corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", 
                linewidths=0.5, ax=ax4, square=True, cbar_kws={"shrink": 0.8})
    ax4.set_title("Correlation Matrix of Facebook Metrics", fontsize=16, fontweight='bold', pad=20)
    st.pyplot(fig4)
    
    # ---------- SUBHEADING ----------
    st.markdown("<h3 style='color: #4ECDC4;'>📌 Key Correlations</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h4 style='color: #2E86AB;'>✅ Strong Positive Correlations</h4>", unsafe_allow_html=True)
        strong_pairs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > 0.7:
                    strong_pairs.append(f"• **{corr_matrix.columns[i]}** ↔ **{corr_matrix.columns[j]}**: {corr_matrix.iloc[i, j]:.2f}")
        
        for pair in strong_pairs[:5]:
            st.write(pair)
    
    with col2:
        st.markdown("<h4 style='color: #2E86AB;'>📝 Insights</h4>", unsafe_allow_html=True)
        st.info("""
        **What this means:**
        - High correlation between **Likes** and **Total Interactions** indicates likes drive overall engagement
        - **Shares** strongly correlate with **Comments**, suggesting viral content generates discussion
        - Focus on creating content that encourages both **Likes** and **Shares**
        """)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>📊 Dashboard designed with ❤️ by Rabia Muneeb </p>", unsafe_allow_html=True)
