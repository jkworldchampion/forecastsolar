from datetime import datetime


def convert_time(x):
    Ymd, HMS = x.split(' ')
    H, M, S = HMS.split(':')
    H = str(int(H)-1)
    HMS = ':'.join([H, M, S])
    return ' '.join([Ymd, HMS])

# 데이터 불러오기
train_data = pd.read_csv('data/energy.csv')
# 시간 변환
train_data['time'] = train_data['time'].apply(lambda x:convert_time(x))