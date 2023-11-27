Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> import scipy.stats
>>> import sqlalchemy
>>> from sqlalchemy import create_engine
>>> database_url='postgresql://postgres:7554@localhost:5432/postgres'
>>> engine=create_engine(database_url)
>>> table_name='medical_malpractice'
>>> medical_malpractice=pd.read_sql(table_name,con=engine)
>>> print(medical_malpractice)
       amount  severity  age  ...  gender date_of_case     id
0       48010         3   23  ...    Male   2022-10-01  16386
1      107944         3   58  ...  Female   2022-10-01  16845
2      396035         5   35  ...  Female   2022-10-01  17391
3       96331         3   13  ...  Female   2022-10-01  17943
4       75996         7   65  ...    Male   2021-10-01  50914
...       ...       ...  ...  ...     ...          ...    ...
79205  161908         2   38  ...  Female   2019-10-01  79205
79206   25305         4   64  ...    Male   2019-10-01  79206
79207   43098         3   87  ...    Male   2019-10-01  79207
79208   35398         3   81  ...    Male   2019-10-01  79208
79209  154228         9   19  ...  Female   2019-10-01  79209

[79210 rows x 10 columns]
>>> medical_malpractice['Gender_Binary']=medical_malpractice['gender'].map({'Male': 1, 'Female': 0})
>>> severity_male = medical_malpractice.loc[medical_malpractice['Gender_Binary'] == 1, 'severity']
>>> severity_female = medical_malpractice.loc[medical_malpractice['Gender_Binary'] == 0, 'severity']
>>> print(severity_male,severity_female)
0        3
4        7
5        5
6        3
20       3
        ..
79203    3
79204    4
79206    4
79207    3
79208    3
Name: severity, Length: 31440, dtype: int64 1        3
2        5
3        3
7        3
8        4
        ..
79200    9
79201    4
79202    3
79205    2
79209    9
Name: severity, Length: 47770, dtype: int64
gender_male_severity_sample=severity_male.sample(n=1000,random_state=20)
gender_female_severity=severity_female.sample(n=1000,random_state=20)
print(gender_male_severity_sample,gender_female_severity)
20823    3
10914    3
78018    3
57989    7
76952    7
        ..
46451    3
51616    4
59370    7
54626    9
9395     4
Name: severity, Length: 1000, dtype: int64 69154    5
56324    2
61683    7
50593    3
27880    3
        ..
62098    4
78389    4
6927     9
26605    3
10061    3
Name: severity, Length: 1000, dtype: int64
import scipy.stats as stats
from scipy.stats import mannwhitneyu
stat,p_value=stats.mannwhitneyu(gender_male_severity_sample,gender_female_severity)
print(stat,p_value)
514923.5 0.23282655842652666
alpha=0.05
if p_value > alpha:
	print('There is not a significant difference between the severity levels between males and females in medical malpractice cases')
else:
    	print('There is a significant difference between the severity levels between males and females in medical malpractice cases')

    	
There is not a significant difference between the severity levels between males and females in medical malpractice cases
n1=1000
n2=1000
_, critical_value = mannwhitneyu([1000], [1000], alternative='two-sided')
print("Critical Value:", critical_value)
Critical Value: 1.0
_, critical_value = mannwhitneyu([severity_male],[severity_female], alternative='two-sided')

plt.bar(x=medical_malpractice['age'], height=medical_malpractice['severity'])

plt.xlabel('Age')

plt.xlabel('Age')
Text(0.5, 0, 'Age')
plt.ylabel('Severity')
Text(0, 0.5, 'Severity')
plt.title('Relationship between age and severity')
Text(0.5, 1.0, 'Relationship between age and severity')
plt.show()
medical_malpractice['severity']=medical_malpractice['severity'].astype('category')
print(medical_malpractice)
       amount severity  age  ...  date_of_case     id Gender_Binary
0       48010        3   23  ...    2022-10-01  16386             1
1      107944        3   58  ...    2022-10-01  16845             0
2      396035        5   35  ...    2022-10-01  17391             0
3       96331        3   13  ...    2022-10-01  17943             0
4       75996        7   65  ...    2021-10-01  50914             1
...       ...      ...  ...  ...           ...    ...           ...
79205  161908        2   38  ...    2019-10-01  79205             0
79206   25305        4   64  ...    2019-10-01  79206             1
79207   43098        3   87  ...    2019-10-01  79207             1
79208   35398        3   81  ...    2019-10-01  79208             1
79209  154228        9   19  ...    2019-10-01  79209             0

[79210 rows x 11 columns]
severity_sample=medical_malpractice['severity'].sample(n=1000,random_state=20)
age_sample=medical_malpractice['age'].sample(n=1000,random_state=20)
correlation_coefficient,p_value=stats.kendalltau(severity_sample,age_sample)
print(correlation_coefficient,p_value)
-0.03689895647491782 0.11230638559871647
print(medical_malpractice.info)
<bound method DataFrame.info of        amount severity  age  ...  date_of_case     id Gender_Binary
0       48010        3   23  ...    2022-10-01  16386             1
1      107944        3   58  ...    2022-10-01  16845             0
2      396035        5   35  ...    2022-10-01  17391             0
3       96331        3   13  ...    2022-10-01  17943             0
4       75996        7   65  ...    2021-10-01  50914             1
...       ...      ...  ...  ...           ...    ...           ...
79205  161908        2   38  ...    2019-10-01  79205             0
79206   25305        4   64  ...    2019-10-01  79206             1
79207   43098        3   87  ...    2019-10-01  79207             1
79208   35398        3   81  ...    2019-10-01  79208             1
79209  154228        9   19  ...    2019-10-01  79209             0

[79210 rows x 11 columns]>
print(medical_malpractice.columns)
Index(['amount', 'severity', 'age', 'private_attorney', 'marital_status',
       'specialty', 'insurance', 'gender', 'date_of_case', 'id',
       'Gender_Binary'],
      dtype='object')
private_attorney_yes=medical_malpractice.loc[medical_malpractice['private_attorney']==1,'amount']
private_attorney_no=medical_malpractice.loc[medical_malpractice['private_attorney']==0,'amount']
sample_private_attorney_yes=private_attorney_yes.sample(n=1000,random_state=20)
sample_private_attorney_no=private_attorney_no.sample(n=1000,random_state=20)
alpha=0.05
stat,p_value=stats.mannwhitneyu(sample_private_attorney_yes,sample_private_attorney_no)
print(stat,p_value)
706217.0 2.0855183198196458e-57
sample_severity_widowed=(medical_malpractice.loc[medical_malpractice['marital_status']==3]['severity']).sample(n=100,random_state=20)

sample_severity_widowed=medical_malpractice.loc[medical_malpractice['marital_status']==3]['severity'].sample(n=100,random_state=20)

sample_severity_widowed=(medical_malpractice.loc[medical_malpractice['marital_status']==3]['severity'])
  
print(sample_severity_widowed)
  
Series([], Name: severity, dtype: category
Categories (9, int64): [1, 2, 3, 4, ..., 6, 7, 8, 9])
medical_malpractice['severity']=medical_malpractice['severity'].astype('integer']
  

medical_malpractice['severity']=medical_malpractice['severity'].astype('integer')
  

medical_malpractice['severity'] = medical_malpractice['severity'].astype('int

                                                                         

medical_malpractice['severity'] = medical_malpractice['severity'].astype('int')
                                                                         

sample_severity_widowed=(medical_malpractice.loc[medical_malpractice['marital_status']==3]['severity']).sample(n=100,random_state=20)
                                                                         

print(medical_malpractice.loc[medical_malpractice['marital_status']==3]['severity'])
  
Series([], Name: severity, dtype: int32)
print(medical_malpractice.loc[medical_malpractice['marital_status']==3,'severity'])
  
Series([], Name: severity, dtype: int32)
filepath=r'C:\Users\Beatrice\Documents\medical_malpractice.csv'
  
df=pd.DataFrame(filepath)
  

df=pd.read_csv(filepath)
medical_malpractice=pd.DataFrame(df)
print(medical_malpractice)
       Amount  Severity  Age  ...           Specialty          Insurance  Gender
0       57041         7   62  ...     Family Practice            Private    Male
1      324976         6   38  ...               OBGYN       No Insurance  Female
2      135383         4   34  ...          Cardiology            Unknown    Male
3      829742         7   42  ...          Pediatrics       No Insurance  Female
4      197675         3   60  ...               OBGYN  Medicare/Medicaid  Female
...       ...       ...  ...  ...                 ...                ...     ...
79205   25305         4   64  ...     General Surgery            Unknown    Male
79206   43098         3   87  ...  Orthopedic Surgery            Unknown    Male
79207   35398         3   81  ...      Anesthesiology            Unknown    Male
79208  154228         9   19  ...         Dermatology            Unknown  Female
79209  168298         7    4  ...     Family Practice            Private  Female

[79210 rows x 8 columns]
sample_severity_widowed=(medical_malpractice.loc[medical_malpractice['Marital_Status']==3]['Severity']).sample(n=100,random_state=20)
                                                                         
sample_severity_unknown=(medical_malpractice.loc[medical_malpractice['Marital_Status']==4]['Severity']).sample(n=100,random_state=20)
                                                                         
sample_severity_divorced=(medical_malpractice.loc[medical_malpractice['Marital_Status']==0]['Severity']).sample(n=100,random_state=20)
                                                                         
sample_severity_Single=(medical_malpractice.loc[medical_malpractice['Marital_Status']==1]['Severity']).sample(n=100,random_state=20)
                                                                         
sample_severity_married=(medical_malpractice.loc[medical_malpractice['Marital_Status']==2]['Severity']).sample(n=100,random_state=20)
                                                                         
stat,p_value=stats.kruskal(sample_severity_divorced,sample_severity_Single,sample_severity_married,sample_severity_widowed,sample_severity_unknown)
                                                                         
print(stat,p_value)
                                                                         
43.37249146493516 8.66055605810938e-09
insurance_types=medical_malpractice['Insurance'].unique()
                                                                         
print(insurance_types)
                                                                         
['Private' 'No Insurance' 'Unknown' 'Medicare/Medicaid'
 'Workers Compensation']
medical_malpractice['Insurance_nominal']=medical_malpractice['Insurance'].map({'Private':1,'No Insurance':2,'Unknown':3,'Medicare/Medicaid':4,'Workers Compensation':5})
                                                                         
sample_private_insurance=(medical_malpractice.loc[medical_malpractice['Insurance_nominal']==1]['Amount']).sample(n=100,random_state=20)
                                                                         
sample_no_insurance=(medical_malpractice.loc[medical_malpractice['Insurance_nominal']==2]['Amount']).sample(n=100,random_state=20)
                                                                         
sample_unknown_insurance=(medical_malpractice.loc[medical_malpractice['Insurance_nominal']==3]['Amount']).sample(n=100,random_state=20)
                                                                         
sample_medicaremedicaid_insurance=(medical_malpractice.loc[medical_malpractice['Insurance_nominal']==4]['Amount']).sample(n=100,random_state=20)
                                                                         
sample_workers_compensation=(medical_malpractice.loc[medical_malpractice['Insurance_nominal']==5]['Amount']).sample(n=100,random_state=20)
                                                                         
stat,p_value=stats.kruskal(sample_private_insurance,sample_no_insurance,sample_unknown_insurance,sample_medicaremedicaid_insurance,sample_workers_compensation)
                                                                         
print(stat,p_value)
                                                                         
28.909963113772392 8.153606814806151e-06
sns.histplot(x='Amount',data=medical_malpractice)
                                                                         
<Axes: xlabel='Amount', ylabel='Count'>
plt.title('Distribution of Claim Amounts')
                                                                         
Text(0.5, 1.0, 'Distribution of Claim Amounts')
plt.show()
                                                                         
bins = [0, 30, 60, 91]
                                                                         
labels=['young adults','middle-aged','elderly']
                                                                         
age_group = pd.cut(medical_malpractice['Age'], bins=bins, labels=labels, right=True)
                                                                         
print(age_group)
                                                                         
0             elderly
1         middle-aged
2         middle-aged
3         middle-aged
4         middle-aged
             ...     
79205         elderly
79206         elderly
79207         elderly
79208    young adults
79209    young adults
Name: Age, Length: 79210, dtype: category
Categories (3, object): ['young adults' < 'middle-aged' < 'elderly']
sns.histplot(x=age_group,data=medical_malpractice)
                                                                         
<Axes: xlabel='Age', ylabel='Count'>
plt.xlabel('age_group')
                                                                         
Text(0.5, 0, 'age_group')
plt.show()
                                                                         
medical_malpractice['Age_Groups']=pd.cut(medical_malpractice['Age'], bins=bins, labels=labels, right=True)
                                                                         
sample_young_adults=(medical_malpractice.loc[medical_malpractice['Age_Groups']=='young adults']['Amount']).sample(n=100,random_state=20)
                                                                         
sample_middle_aged=(medical_malpractice.loc[medical_malpractice['Age_Groups']=='middle-aged']['Amount']).sample(n=100,random_state=20)
                                                                         
sample_elderly=(medical_malpractice.loc[medical_malpractice['Age_Groups']=='elderly']['Amount']).sample(n=100,random_state=20)
                                                                         
stat,p_value=stats.kruskal(sample_young_adults,sample_middle_aged,sample_elderly)
                                                                         
print(stat,p_value)
                                                                         
28.689033887043138 5.891901067294474e-07
medical_malpractice['severity_log']=np.log(medical_malpractice['severity'])
                                                                         

medical_malpractice['severity_log']=np.log(medical_malpractice['Severity'])
                                                                         
sns.histplot(x=medical_malpractice['severity_log'])
                                                                         
<Axes: xlabel='severity_log', ylabel='Count'>
plt.title('Distribution of Severity Log levels')
                                                                         
Text(0.5, 1.0, 'Distribution of Severity Log levels')
plt.show()
                                                                         
plt.figure(figsize=(10,6))
                                                                         
<Figure size 1000x600 with 0 Axes>
sns.boxplot(x=medical_malpractice['specialty'],y=medical_malpractice['severity'])
                                                                         

sns.boxplot(x=medical_malpractice['Specialty'],y=medical_malpractice['Severity'])
                                                                         
<Axes: xlabel='Specialty', ylabel='Severity'>
plt.title('Distriution of severity levels by specialty')
                                                                         
Text(0.5, 1.0, 'Distriution of severity levels by specialty')
plt.xticks(rotation=45)
                                                                         
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [Text(0, 0, 'Family Practice'), Text(1, 0, 'OBGYN'), Text(2, 0, 'Cardiology'), Text(3, 0, 'Pediatrics'), Text(4, 0, 'Internal Medicine'), Text(5, 0, 'Anesthesiology'), Text(6, 0, 'Emergency Medicine'), Text(7, 0, 'Ophthamology'), Text(8, 0, 'Urological Surgery'), Text(9, 0, 'Orthopedic Surgery'), Text(10, 0, 'Neurology/Neurosurgery'), Text(11, 0, 'Occupational Medicine'), Text(12, 0, 'Resident'), Text(13, 0, 'Thoracic Surgery'), Text(14, 0, 'General Surgery'), Text(15, 0, 'Radiology'), Text(16, 0, 'Pathology'), Text(17, 0, 'Physical Medicine'), Text(18, 0, 'Plastic Surgeon'), Text(19, 0, 'Dermatology')])
plt.tight_layout()
                                                                         
plt.show()
                                                                         
import pingouin as pg
result=pg.anova(data=medical_malpractice,dv='severity_log',between='Specialty')
print(result)
      Source  ddof1  ddof2           F  p-unc       np2
0  Specialty     19  79190  259.023475    0.0  0.058511
insurance_types=medical_malpractice['Insurance'].unique()
print(insurance_types)
['Private' 'No Insurance' 'Unknown' 'Medicare/Medicaid'
 'Workers Compensation']
sample_unknown=(medical_malpractice.loc[medical_malpractice['Insurance']=='Unknown']['Severity']).sample(n=100,random_state=20)
sample_Private=(medical_malpractice.loc[medical_malpractice['Insurance']=='Private']['Severity']).sample(n=100,random_state=20)
sample_Workers_Compensation=(medical_malpractice.loc[medical_malpractice['Insurance']=='Workers Compensation']['Severity']).sample(n=100,random_state=20)
sample_No_Insurance=(medical_malpractice.loc[medical_malpractice['Insurance']=='No Insurance']['Severity']).sample(n=100,random_state=20)
sample_medicare=(medical_malpractice.loc[medical_malpractice['Insurance']=='Medicare/Medicaid']['Severity']).sample(n=100,random_state=20)
stat,p_value=stats.kruskal(sample_unknown,sample_Private,sample_Workers_Compensation,sample_No_Insurance,sample_medicare)
print(stat,p_value)
21.939239664604408 0.00020607959644835993
sample_female_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Female')&(medical_malpractice['Private_Attorney']==1),'Amount'].sample(n=100,random_state=20)
sample_female_no_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Female')&(medical_malpractice['Private_attorney']==0),'Amount'].sample(n=100,random_state=20)

sample_female_no_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Female')&(medical_malpractice['Private_Attorney']==0),'Amount'].sample(n=100,random_state=20)
sample_male_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Male')&(medical_malpractice['Private_Attorney']==1),'Amount'].sample(n=100,random_state=20)
sample_male_no_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Male')&(medical_malpractice['Private_Attorney']==0),'Amount'].sample(n=100,random_state=20)
stat,p_value=stats.mannwhitneyu(sample_female_PA,sample_female_no_PA)
print(stat,p_value)
5083.0 0.8402454078213364
sample_female_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Female')&(medical_malpractice['Private_Attorney']==1),'Amount'].sample(n=1000,random_state=20)
sample_female_no_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Female')&(medical_malpractice['Private_Attorney']==0),'Amount'].sample(n=1000,random_state=20)
stat,p_value=stats.mannwhitneyu(sample_female_PA,sample_female_no_PA)
print(stat,p_value)
554600.0 2.3556607203288866e-05
sample_male_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Male')&(medical_malpractice['Private_Attorney']==1),'Amount'].sample(n=1000,random_state=20)
sample_male_no_PA=medical_malpractice.loc[(medical_malpractice['Gender']=='Male')&(medical_malpractice['Private_Attorney']==0),'Amount'].sample(n=1000,random_state=20)
stat,p_value=stats.mannwhitneyu(sample_male_PA,sample_male_no_PA)
print(stat,p_value)
876404.0 8.650855925607534e-187
stat,p_value=stats.kruskal(sample_female_PA,sample_female_no_PA,sample_male_PA,sample_male_no_PA)
print(stat,p_value)
1284.8099808386153 2.909073235642521e-278
medical_malpractice['insurance_nominal']=medical_malpractice['Insurance'].astype('category').cat.codes
result_2=pg.ancova(data=medical_malpractice,dv='severity_log',between='Gender',covar='insurance_nominal')
print(result_2)
              Source            SS     DF          F         p-unc       np2
0             Gender     13.081299      1  72.899294  1.388068e-17  0.000920
1  insurance_nominal      7.331287      1  40.855703  1.648018e-10  0.000516
2           Residual  14213.174837  79207        NaN           NaN       NaN
medical_malpractice['log_amount']=np.log1p(medical_malpractice['Amount'])
result=pg.ancova(data=medical_malpractice,dv='log_amount',between='Private_Attorney',covar='Age')
print(result)
             Source            SS     DF             F          p-unc       np2
0  Private_Attorney  13003.915587      1  12623.666158   0.000000e+00  0.137467
1               Age   1367.687153      1   1327.694410  2.680167e-288  0.016486
2          Residual  81592.869220  79207           NaN            NaN       NaN
medical_malpractice['specialty_integer'] = medical_malpractice['Specialty'].astype('category').cat.codes
result=pg.ancova(data=medical_malpractice,dv='log_amount',between='Gender',covar='specialty_integer')
print(result)
              Source            SS     DF            F         p-unc       np2
0             Gender   2387.418483      1  2017.241690  0.000000e+00  0.024835
1  specialty_integer    519.679970      1   439.101945  3.121914e-97  0.005513
2           Residual  93741.992708  79207          NaN           NaN       NaN
print(medical_malpractice)
       Amount  Severity  Age  ...  insurance_nominal  log_amount specialty_integer
0       57041         7   62  ...                  2   10.951543                 4
1      324976         6   38  ...                  1   12.691510                 8
2      135383         4   34  ...                  3   11.815870                 1
3      829742         7   42  ...                  1   13.628871                13
4      197675         3   60  ...                  0   12.194385                 8
...       ...       ...  ...  ...                ...         ...               ...
79205   25305         4   64  ...                  3   10.138797                 5
79206   43098         3   87  ...                  3   10.671255                11
79207   35398         3   81  ...                  3   10.474439                 0
79208  154228         9   19  ...                  3   11.946194                 2
79209  168298         7    4  ...                  2   12.033497                 4

[79210 rows x 14 columns]
print(medical_malpractice.columns)
Index(['Amount', 'Severity', 'Age', 'Private_Attorney', 'Marital_Status',
       'Specialty', 'Insurance', 'Gender', 'Insurance_nominal', 'Age_Groups',
       'severity_log', 'insurance_nominal', 'log_amount', 'specialty_integer'],
      dtype='object')
result = kruskal(*[group['Severity'] for name, group in medical_malpractice.groupby(['Insurance', 'Marital_Status'])])

result = stats.kruskal(*[group['Severity'] for name, group in medical_malpractice.groupby(['Insurance', 'Marital_Status'])])
print(result)
KruskalResult(statistic=4254.538095488132, pvalue=0.0)
result=pg.ancova(dv='log_amount',between='Specialty',covar='Private_Attorney',data=medical_malpractice)
print(result)
             Source            SS     DF            F  p-unc       np2
0         Specialty  10596.203346     19   610.290849    0.0  0.127726
1  Private_Attorney   7811.490275      1  8548.188128    0.0  0.097429
2          Residual  72364.353027  79189          NaN    NaN       NaN
sample_private_att_yes=medical_malpractice.loc[medical_malpractice['Private_Attorney']==1]['Amount'].sample(n=1000,random_state=20)
sample_private_att_no=medical_malpractice.loc[medical_malpractice['Private_Attorney']==0]['Amount'].sample(n=1000,random_state=20)
stat,p_value=stats.mannwhitneyu(sample_private_att_yes,sample_private_att_no)
print(stat,p_value)
692021.5 5.148576814690996e-50
total_severity=len(medical_malpractice)
high_severity_private=medical_malpractice.loc[(medical_malpractice['Severity']>=7)&(medical_malpractice['Insurance']=='Private'),'Severity'].value_counts()
high_severity_medicare=medical_malpractice.loc[(medical_malpractice['Severity']>=7)&(medical_malpractice['Insurance']=='Medicare/Medicaid'),'Severity'].value_counts()
high_severity_works_comp=len(medical_malpractice.loc[(medical_malpractice['Severity']>=7)&(medical_malpractice['Insurance']=='Workers Compensation'),'Severity'])
high_severity_unknown=medical_malpractice.loc[(medical_malpractice['Severity']>=7)&(medical_malpractice['Insurance']=='Unknown'),'Severity'].value_counts()
private_highseverity = np.sum(high_severity_private)
prob_private_highseverity=private_highseverity/total_severity
prob_private_highseverity_percent=prob_private_highseverity*100
print('The probability of a case having a high severity level and under the private insurance type is {:.2f}%.'.format(prob_private_highseverity_percent))
The probability of a case having a high severity level and under the private insurance type is 13.87%.
sum_of_high_severity_medicare=np.sum(high_severity_medicare)
prob_high_severity_medicare=sum_of_high_severity_medicare/total_severity
percent_prob_high_severity_medicare=prob_high_severity_medicare*100
print('The probability of a case having a high severity level and under the medicare/medicaid insurance type is {:.2f}%.'.format(percent_prob_high_severity_medicare))
The probability of a case having a high severity level and under the medicare/medicaid insurance type is 2.38%.
prob_high_severity_works_comp=high_severity_works_comp/total_severity
percent_prob_high_severity_works_comp=prob_high_severity_works_comp*100
print('The probability of a case having a high severity level and under workers compensation is {:.2f}%.'.format(percent_prob_high_severity_works_comp))
The probability of a case having a high severity level and under workers compensation is 0.69%.
sum_high_severity_unknown=np.sum(high_severity_unknown)
prob_high_severity_unknown=high_severity_unknown*100
prob_high_severity_unknown=sum_high_severity_unknown/total_severity
percent_prob_high_severity_unknown=prob_high_severity_unknown*100
print('The probability of a case having a high severity level with an unknown insurance type is {:.2f}%.'.format(percent_prob_high_severity_unknown))
The probability of a case having a high severity level with an unknown insurance type is 6.78%.
bins=[0,30,60,90]
labels=['young adults', 'middle-aged', 'elderly']
medical_malpractice['age_groups']=pd.cut(medical_malpractice['Age'],bins=bins, labels=labels,right=True)
youngadults_amounts=len(medical_malpractice.loc[(medical_malpractice['Amount']>100000)&(medical_malpractice['age_groups']=='young adults'),'Amount'])
total_amounts=len(medical_malpractice['Amount'])
prob_young_adults=youngadults_amounts/total_amounts
percent_prob_young_adults=prob_young_adults*100
print('The probability of a young adult being awarded more than $100,000 is {:.2f}%.'.format(percent_prob_young_adults))
The probability of a young adult being awarded more than $100,000 is 15.02%.
middleaged_amounts=len(medical_malpractice.loc[(medical_malpractice['Amount']>100000)&(medical_malpractice['age_groups']=='middle-aged'),'Amount'])
prob_middle_aged=(middleaged_amounts/total_amounts)*100
print('The probability of a middle aged claimants being awarded more than $100,000 is {:.2f}%.'.format(prob_middle_aged))
The probability of a middle aged claimants being awarded more than $100,000 is 26.38%.
elderly_amounts=len(medical_malpractice.loc[(medical_malpractice['Amount']>100000)&(medical_malpractice['age_groups']=='elderly'),'Amount'])
prob_elderly=(elderly_amounts/total_amounts)*100
print('The probability of an elderly claimant being awarded more than $100,000 is {:.2f}%.'.format(prob_elderly))
The probability of an elderly claimant being awarded more than $100,000 is 7.62%.
print(medical_malpractice.columns)
Index(['Amount', 'Severity', 'Age', 'Private_Attorney', 'Marital_Status',
       'Specialty', 'Insurance', 'Gender', 'Insurance_nominal', 'Age_Groups',
       'severity_log', 'insurance_nominal', 'log_amount', 'specialty_integer',
       'age_groups'],
      dtype='object')
contingency_table = pd.crosstab(index=medical_malpractice['Marital_Status'], columns=medical_malpractice['Gender'], margins=True, normalize='index')
for Marital_Status in contingency_table.index[:-1]:
    for gender in contingency_table.columns[:-1]:
        probability = contingency_table.loc[Marital_status, Gender]
        print(f"Probability of severity levels for {Marital_Status} and {Gender}:\n")
        severity_probabilities = medical_malpractice.loc[(medical_malpractice['Marital_Status'] == Marital_Status) & (medical_malpractice['Gender'] == Gender), 'Severity'].value_counts(normalize=True)
        for severity, prob in severity_probabilities.items():
            print(f"Severity {Severity}: {prob * probability:.2%}")
            
SyntaxError: multiple statements found while compiling a single statement
contingency_table = pd.crosstab(index=medical_malpractice['Marital_Status'], columns=medical_malpractice['Gender'], margins=True, normalize='index')
for Marital_Status in contingency_table.index[:-1]:
    for gender in contingency_table.columns[:-1]:
        probability = contingency_table.loc[Marital_status, Gender]
        print(f"Probability of severity levels for {Marital_Status} and {Gender}:\n")
        severity_probabilities = medical_malpractice.loc[(medical_malpractice['Marital_Status'] == Marital_Status) & (medical_malpractice['Gender'] == Gender), 'Severity'].value_counts(normalize=True)
        for severity, prob in severity_probabilities.items():
            print(f"Severity {Severity}: {prob * probability:.2%}")

                                                                         
Traceback (most recent call last):
  File "<pyshell#210>", line 3, in <module>
    probability = contingency_table.loc[Marital_status, Gender]
NameError: name 'Marital_status' is not defined. Did you mean: 'Marital_Status'?
contingency_table = pd.crosstab(index=medical_malpractice['Marital_Status'], columns=medical_malpractice['Gender'], margins=True, normalize='index')
for Marital_Status in contingency_table.index[:-1]:
    for gender in contingency_table.columns[:-1]:
        probability = contingency_table.loc[Marital_Status, Gender]
        print(f"Probability of severity levels for {Marital_Status} and {Gender}:\n")
        severity_probabilities = medical_malpractice.loc[(medical_malpractice['Marital_Status'] == Marital_Status) & (medical_malpractice['Gender'] == Gender), 'Severity'].value_counts(normalize=True)
        for severity, prob in severity_probabilities.items():
            print(f"Severity {Severity}: {prob * probability:.2%}")
                                                                         
SyntaxError: multiple statements found while compiling a single statement
contingency_table = pd.crosstab(index=medical_malpractice['Marital_Status'], columns=medical_malpractice['Gender'], margins=True, normalize='index')
for Marital_Status in contingency_table.index[:-1]:
                                                                         
SyntaxError: multiple statements found while compiling a single statement
contingency_table = pd.crosstab(index=medical_malpractice['Marital_Status'], columns=medical_malpractice['Gender'], margins=True, normalize='index')
                                                                         
for Marital_Status in contingency_table.index[:-1]:
    for gender in contingency_table.columns[:-1]:
        probability = contingency_table.loc[Marital_Status, Gender]
        print(f"Probability of severity levels for {Marital_Status} and {Gender}:\n")
        severity_probabilities = medical_malpractice.loc[(medical_malpractice['Marital_Status'] == Marital_Status) & (medical_malpractice['Gender'] == Gender), 'Severity'].value_counts(normalize=True)
        for severity, prob in severity_probabilities.items():
        print(f"Severity {Severity}: {prob * probability:.2%}")
                                                                         
SyntaxError: expected an indented block after 'for' statement on line 6
for Marital_Status in contingency_table.index[:-1]:
    for gender in contingency_table.columns[:-1]:
        probability = contingency_table.loc[Marital_Status, Gender]
        print(f"Probability of severity levels for {Marital_Status} and {Gender}:\n")
        severity_probabilities = medical_malpractice.loc[(medical_malpractice['Marital_Status'] == Marital_Status) & (medical_malpractice['Gender'] == Gender), 'Severity'].value_counts(normalize=True)
        for severity, prob in severity_probabilities.items():
            print(f"Severity {Severity}: {prob * probability:.2%}")

                                                                         
Traceback (most recent call last):
  File "<pyshell#229>", line 3, in <module>
    probability = contingency_table.loc[Marital_Status, Gender]
NameError: name 'Gender' is not defined. Did you mean: 'gender'?
bins=[0,43670,98131,926411]
                                                                         
labels=['low_comp','moderate_comp','high_comp']
                                                                         
medical_malpractice['compensation_level']=pd.cut(medical_malpractice['Amount'],bins=bins,labels=labels,right=True)
                                                                         
contingency_table_amount=pd.crosstab(index=medical_malpractice['Private_Attorney'], columns=medical_malpractice['compensation_level'], margins=True, normalize='index')
                                                                         
print(crontingency_table_amount)
                                                                         
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    print(crontingency_table_amount)
NameError: name 'crontingency_table_amount' is not defined. Did you mean: 'contingency_table_amount'?
print(contingency_table_amount)
                                                                         
compensation_level  low_comp  moderate_comp  high_comp
Private_Attorney                                      
0                   0.469863       0.184357   0.345780
1                   0.137195       0.283673   0.579132
All                 0.250006       0.249994   0.500000
for Marital_Status in contingency_table.index[:-1]:
    for Gender in contingency_table.columns[:-1]:
        probability = contingency_table.loc[Marital_Status, Gender]
        print(f"Probability of severity levels for {Marital_Status} and {Gender}:\n")
        severity_probabilities = medical_malpractice.loc[(medical_malpractice['Marital_Status'] == Marital_Status) & (medical_malpractice['Gender'] == Gender), 'Severity'].value_counts(normalize=True)
        for severity, prob in severity_probabilities.items():
            print(f"Severity {Severity}: {prob * probability:.2%}")

                                                                         
Probability of severity levels for 0 and Female:

Traceback (most recent call last):
  File "<pyshell#237>", line 7, in <module>
    print(f"Severity {Severity}: {prob * probability:.2%}")
NameError: name 'Severity' is not defined. Did you mean: 'severity'?
for Marital_Status in contingency_table.index[:-1]:
    for Gender in contingency_table.columns[:-1]:
        probability = contingency_table.loc[Marital_Status, Gender]
        print(f"Probability of severity levels for {Marital_Status} and {Gender}:\n")
        severity_probabilities = medical_malpractice.loc[(medical_malpractice['Marital_Status'] == Marital_Status) & (medical_malpractice['Gender'] == Gender), 'Severity'].value_counts(normalize=True)
        for Severity, prob in severity_probabilities.items():
            print(f"Severity {Severity}: {prob * probability:.2%}")

                                                                         
Probability of severity levels for 0 and Female:

Severity 3: 10.83%
Severity 4: 7.49%
Severity 5: 4.31%
Severity 9: 2.84%
Severity 8: 1.51%
Severity 2: 0.97%
Severity 6: 0.89%
Severity 1: 0.44%
Severity 7: 0.29%
Probability of severity levels for 1 and Female:

Severity 3: 25.73%
Severity 4: 15.17%
Severity 5: 13.95%
Severity 9: 8.13%
Severity 7: 7.32%
Severity 6: 5.04%
Severity 8: 3.87%
Severity 2: 2.16%
Severity 1: 0.96%
Probability of severity levels for 2 and Female:

Severity 3: 18.53%
Severity 4: 11.60%
Severity 5: 8.92%
Severity 9: 6.02%
Severity 6: 3.08%
Severity 7: 2.81%
Severity 8: 2.76%
Severity 2: 1.60%
Severity 1: 0.82%
Probability of severity levels for 3 and Female:

Severity 3: 27.77%
Severity 4: 19.42%
Severity 9: 14.99%
Severity 5: 13.78%
Severity 6: 7.85%
Severity 2: 5.94%
Severity 8: 5.23%
Severity 1: 2.82%
Severity 7: 2.21%
Probability of severity levels for 4 and Female:

Severity 3: 13.29%
Severity 4: 8.30%
Severity 5: 5.06%
Severity 9: 4.24%
Severity 8: 1.86%
Severity 6: 1.27%
Severity 2: 0.89%
Severity 1: 0.60%
Severity 7: 0.44%
