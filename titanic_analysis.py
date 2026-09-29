import pandas as pd
import matplotlib.pyplot as plt


# 1. LOAD DATA


df = pd.read_csv("train.csv")

print("Dataset shape:")
print(df.shape)

print("\nMissing values before cleaning:")
print(df.isnull().sum())



# 2. DATA CLEANING

# Fill missing Age values with the median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with the mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Create a feature showing whether Cabin information is available
df["CabinKnown"] = df["Cabin"].notna().astype(int)

# Remove original Cabin column
df = df.drop(columns=["Cabin"])

print("\nMissing values after cleaning:")
print(df.isnull().sum())



# 3. SUMMARY STATISTICS


print("\nSummary statistics:")
print(df.describe())



# 4. OVERALL SURVIVAL RATE


survival_rate = df["Survived"].mean() * 100

print("\nOverall survival rate:")
print(f"{survival_rate:.2f}%")



# 5. SURVIVAL BY GENDER


survival_by_gender = df.groupby("Sex")["Survived"].mean() * 100

print("\nSurvival rate by gender:")
print(survival_by_gender)

survival_by_gender.plot(kind="bar")

plt.title("Titanic Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# 6. SURVIVAL BY PASSENGER CLASS


survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100

print("\nSurvival rate by passenger class:")
print(survival_by_class)

survival_by_class.plot(kind="bar")

plt.title("Titanic Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# 7. SURVIVAL BY GENDER AND CLASS


survival_by_gender_class = df.groupby(
    ["Sex", "Pclass"]
)["Survived"].mean() * 100

print("\nSurvival rate by gender and passenger class:")
print(survival_by_gender_class)

gender_class_table = survival_by_gender_class.unstack()

gender_class_table.plot(kind="bar")

plt.title("Titanic Survival Rate by Gender and Passenger Class")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.legend(title="Passenger Class")
plt.tight_layout()
plt.show()


# 
# 8. SURVIVAL BY AGE GROUP
# 

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teenager", "Young Adult", "Adult", "Senior"]
)

survival_by_age = df.groupby(
    "AgeGroup",
    observed=True
)["Survived"].mean() * 100

print("\nSurvival rate by age group:")
print(survival_by_age)

survival_by_age.plot(kind="bar")

plt.title("Titanic Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# 9. CORRELATION ANALYSIS


correlation = df[
    ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
].corr()

print("\nCorrelation matrix:")
print(correlation)


# Correlation heatmap
plt.figure(figsize=(8, 6))

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Titanic Correlation Matrix")
plt.tight_layout()
plt.show()



# 10. FAMILY SIZE ANALYSIS


df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

survival_by_family = df.groupby(
    "FamilySize"
)["Survived"].mean() * 100

print("\nSurvival rate by family size:")
print(survival_by_family)


survival_by_family.plot(kind="bar")

plt.title("Titanic Survival Rate by Family Size")
plt.xlabel("Family Size")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# END OF ANALYSIS

print("\nAnalysis complete.")
