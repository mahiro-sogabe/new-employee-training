import datetime
import pytz
import time

# タイムゾーンのリスト
time_zones = {'Japan': 'Asia/Tokyo', 'US (Los Angeles)': 'America/Los_Angeles', 'UK': 'Europe/London'}

# 表示したいタイムゾーンを選択
print('Select a timezone to display:')
for tz in time_zones.keys():
    print('- {}'.format(tz))
selected_tz = input('> ')

# デジタル時計を表示し続ける
while True:
    # 現在時刻を取得し、指定したタイムゾーンに変換
    now = datetime.datetime.now(pytz.timezone(time_zones[selected_tz]))

    # デジタル時計を表示
    print('The current time in {} is: {}'.format(selected_tz, now.strftime('%Y-%m-%d %H:%M:%S')), end='\r')

    # 1秒待って時刻を更新
    time.sleep(1)
