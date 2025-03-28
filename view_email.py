import streamlit as st
import pandas as pd

# Streamlit UI
st.title("📊 Task Viewer")


# Load CSV into DataFrame
df = pd.read_csv("email.csv")

# Hide Index
df.index = [""] * len(df)

# Optional: Filter Columns
selected_columns = st.multiselect("Select columns to display", df.columns)
if selected_columns:
    st.subheader("🔍 Filtered View")
    st.dataframe(df[selected_columns])

# Show raw table
# st.subheader("🔹 Task List")
# st.dataframe(df.style.format(precision=2))  # Show styled DataFrame
st.dataframe(df, use_container_width=True, hide_index=True)

# # Optional: Show Summary Statistics
# if st.checkbox("Show Summary Statistics"):
#     st.subheader("📈 Summary Statistics")
#     st.write(df.describe())


