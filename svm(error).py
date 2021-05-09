from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import sklearn.svm as svm
import pandas as pd
import numpy as np

# 데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/cjfghk5697/forecastsolar/main/csv%20file/dangjin_obs_data_energy.csv')
df.drop_duplicates(inplace=True)

imp = SimpleImputer()

x= df.fillna(0).loc[:,'기온(°C)']
y = df.fillna(0).loc[:,'dangjin']

x = x.values.reshape(-1, 1) 
imp.fit_transform(x.reshape(-1, 1))

y = y.values.reshape(-1, 1) 
imp.fit_transform(y.reshape(-1, 1))


X_train, X_test, y_train, y_test = train_test_split(x,y, random_state=0)

# 모델 학습
model = svm.SVC(gamma=0.01).fit(X_train,np.ravel( y_train))
# 평가
print("훈련 세트 정확도: {:.2f}".format(model.score(X_train, y_train)))
print("테스트 세트 정확도: {:.2f}".format(model.score(X_test, y_test)))
