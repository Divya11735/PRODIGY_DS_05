import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:/Users/Divya varshini/OneDrive/Desktop/Traffic-Accident-Project/data/accidents.csv.csv")


df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
df['Hour'].value_counts().sort_index().plot(kind='bar')
plt.title("Accidents by Hour")
plt.show()



df['Weather_Conditions'].value_counts().head(5).plot(kind='bar')
plt.title("Accidents by Weather")
plt.show()


df['Road_Surface_Conditions'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Road Surface Conditions")
plt.show()


df['Accident_Severity'].value_counts().plot(kind='bar')
plt.title("Accident Severity")
plt.show()
