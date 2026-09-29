 Titanic Data Analysis — Python

 Project Overview

This project analyses passenger data from the Titanic disaster to identify patterns associated with passenger survival.

The analysis was completed using Python, Pandas and Matplotlib, with a focus on data cleaning, exploratory data analysis (EDA), grouping, correlation analysis and data visualization.

The project demonstrates my ability to take a raw dataset, clean the data, analyse important variables and communicate findings using data.



 Business / Analytical Question

The main question explored in this project is:

What passenger characteristics were associated with different survival rates in the Titanic dataset?

The analysis focuses on:

* Gender
* Passenger class
* Age
* Family size
* Fare
* Number of siblings/spouses
* Number of parents/children aboard



 Objectives

The objectives of this project were to:

1. Load and inspect the Titanic dataset.
2. Identify and handle missing values.
3. Perform exploratory data analysis.
4. Calculate the overall survival rate.
5. Compare survival rates by gender.
6. Compare survival rates by passenger class.
7. Analyse the interaction between gender and passenger class.
8. Analyse survival across different age groups.
9. Examine correlations between numerical variables and survival.
10. Investigate survival patterns based on family size.
11. Communicate the findings using visualizations.



 Tools and Technologies

| Tool       | Purpose                                   |
| ---------- | ----------------------------------------- |
| Python     | Data analysis                             |
| Pandas     | Data cleaning and manipulation            |
| Matplotlib | Data visualization                        |
| GitHub     | Project documentation and version control |
| PyCharm    | Development environment                   |



 Dataset

The dataset contains information about passengers aboard the Titanic.

Important variables used in the analysis include:

* Survived — whether the passenger survived
* Pclass — passenger class
* Sex — passenger gender
* Age — passenger age
* SibSp — number of siblings/spouses aboard
* Parch — number of parents/children aboard
* Fare — passenger fare
* Embarked — port of embarkation
* Cabin — cabin information



 Data Cleaning

The dataset was inspected for missing values before analysis.

 Missing-value treatment

Age

Missing Age values were replaced using the median age:

python
df["Age"] = df["Age"].fillna(df["Age"].median())


Embarked

Missing Embarked values were replaced using the most frequent value:

python
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])


Cabin

Instead of attempting to fill the missing cabin numbers, a new binary feature was created:

python
df["CabinKnown"] = df["Cabin"].notna().astype(int)


This records whether cabin information was available.

The original Cabin column was then removed from the analysis.



 Exploratory Data Analysis

 Overall Survival Rate

The overall survival rate was:

38.38%

This means approximately 38 out of every 100 passengers in the dataset survived.



 Survival by Gender

| Gender | Survival Rate |
| ------ | ------------: |
| Female |        74.20% |
| Male   |        18.89% |

The analysis shows a substantial difference in observed survival rates between female and male passengers.

 Visualization

![Survival by Gender](visualizations/survival_by_gender.png)



 Survival by Passenger Class

| Passenger Class | Survival Rate |
| --------------- | ------------: |
| 1st Class       |        62.96% |
| 2nd Class       |        47.28% |
| 3rd Class       |        24.24% |

The observed survival rate decreased from 1st class to 3rd class.

 Visualization

![Survival by Class](visualizations/survival_by_class.png)



 Survival by Gender and Passenger Class

Combining gender and passenger class revealed additional differences.

| Gender | 1st Class | 2nd Class | 3rd Class |
| ------ | --------: | --------: | --------: |
| Female |    96.81% |    92.11% |    50.00% |
| Male   |    36.89% |    15.74% |    13.54% |

The highest observed survival rate was among female 1st-class passengers.

 Visualization

![Survival by Gender and Class](visualizations/survival_gender_class.png)



 Survival by Age Group

| Age Group   | Survival Rate |
| ----------- | ------------: |
| Child       |        57.97% |
| Teenager    |        42.86% |
| Young Adult |        38.27% |
| Adult       |        40.00% |
| Senior      |        22.73% |

Children had a higher observed survival rate than several older groups, while seniors had the lowest observed survival rate.

 Visualization

![Survival by Age Group](visualizations/survival_by_age.png)



 Correlation Analysis

The following correlations with `Survived` were observed:

| Variable | Correlation |
| -------- | ----------: |
| Pclass   |      -0.338 |
| Fare     |       0.257 |
| Age      |      -0.077 |
| Parch    |       0.082 |
| SibSp    |      -0.035 |

Pclass had the strongest correlation with survival among the variables examined.

The negative correlation indicates that higher numerical Pclass values, which represent lower passenger classes, were associated with lower survival rates.

Fare showed a positive correlation with survival.

However, correlation does not establish causation.

Visualization

![Correlation Matrix](visualizations/correlation_matrix.png)



 Family Size Analysis

Family size was calculated using:

python
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1


This was used to explore whether the number of family members travelling with a passenger was associated with survival.

The analysis provides an additional dimension for understanding passenger survival patterns beyond individual characteristics.



Key Findings

The analysis identified several notable patterns:

 1. Gender was strongly associated with observed survival rates

Female passengers had a substantially higher survival rate than male passengers in the dataset.

 2. Passenger class was associated with survival

1st-class passengers had the highest observed survival rate, while 3rd-class passengers had the lowest.

 3. Gender and passenger class together revealed stronger differences

The combination of the two variables showed considerable differences between passenger groups.

 4. Age groups showed different survival patterns

Children had a higher observed survival rate than several older groups, while seniors had the lowest.

 5. Passenger class had the strongest numerical correlation with survival

Among the numerical variables examined, Pclass had the strongest correlation with Survived.

 6. Correlation should not be interpreted as causation

The analysis identifies relationships and patterns within the dataset. It does not prove that a particular characteristic directly caused a passenger to survive or die.



 Business / Analytical Interpretation

Although this is a historical dataset rather than a conventional business dataset, the project demonstrates a transferable analytical workflow.

The same process can be applied to business problems:

Raw Data → Data Cleaning → Exploration → Analysis → Visualization → Insights → Communication

For example, the same approach could be used to analyse:

* Customer churn
* Sales performance
* Customer segmentation
* Employee turnover
* Marketing campaign performance
* Product performance
* Customer satisfaction



 Skills Demonstrated

This project demonstrates practical experience with:

* Python
* Pandas
* Matplotlib
* Data cleaning
* Missing-value treatment
* Feature engineering
* Exploratory data analysis
* GroupBy analysis
* Descriptive statistics
* Correlation analysis
* Data visualization
* Analytical thinking
* Communicating data-driven findings



 How to Run the Project

Clone the repository and install the required libraries:

bash
pip install pandas matplotlib


Then run:

bash
python src/titanic_analysis.py



 Conclusion

This project demonstrates an end-to-end exploratory data analysis workflow using Python.

Starting with a raw dataset, I inspected and cleaned the data, created additional features, analysed survival patterns across multiple passenger characteristics, calculated correlations and produced visualizations to communicate the results.

The project strengthened my practical understanding of Python, Pandas, data cleaning, exploratory data analysis and data storytelling.
