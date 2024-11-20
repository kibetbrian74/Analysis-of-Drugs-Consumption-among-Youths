# Creation of an interactive dashboard for visualizations and insights
# Name: Interactive_dashboard.py

# necessary libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set title
st.title("Youth Smoking and Drug Experimentation Dashboard")

# Load the dataset
enhanced_data=pd.read_csv("Enhanced_dataset.csv")

# Customizations of filters on the sidebar
age_group= st.sidebar.selectbox("Select Age Group", enhanced_data['Age_Group'].unique())
gender= st.sidebar.selectbox("Select Gender", enhanced_data['Gender'].unique())

# Filter dataset based on selection
filtered_data= enhanced_data[(enhanced_data['Age_Group'] == age_group) & (enhanced_data['Gender']==gender)]

# show filtered data
st.write("Filtered Data:", filtered_data)

# A plot of Smoking Prevalence vs Drug Experimentation
st.subheader("Smoking Prevalence vs Drug Experimentation")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='Smoking_Prevalence', y='Drug_Experimentation', hue='Risk_Score', palette='coolwarm', ax=ax)
st.pyplot(fig)

# A plot of Risk Score Distribution
st.subheader("Risk Score Distribution")
fig, ax = plt.subplots()
sns.histplot(data=enhanced_data['Risk_Score'], kde=True, ax=ax)
st.pyplot(fig)

# A plot showing Impacts of School Programs
st.subheader("Impact of School Programs on Smoking Prevalence")
fig,ax=plt.subplots()
sns.boxplot(data=enhanced_data,x='School_Programs', y='Smoking_Prevalence', palette='Set2', ax=ax)
st.pyplot(fig)
