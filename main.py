import requests
import csv


url="https://nepsealpha.com/floorsheet-live/top_summary"
r=requests.get(url).json()
data=r['top_summary']
#order by total_purch_amount
data=sorted(data,key=lambda x:x['total_purch_amount'],reverse=True)
time_day=r['asOf'].split(' ')[0]
file_path="Data/"+time_day+".csv"
with open(file_path,'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['broker_number','total_purch_amount','total_purch(%)','total_sell_amount','total_sell(%)','matching_summary','matching(%)','total_turn_over(%)','turn_over_vs_market','Buy/Sell_Ratio'])
    for i in data:
        total_purhc_percent=(i['total_purch_amount']/i['total_turn_over'])*100
        total_sell_percent=(i['total_sell_amount']/i['total_turn_over'])*100
        matching_percent=(i['matching_summary']/i['total_turn_over'])*100
        buy_sell_ratio=i['total_purch_amount']/i['total_sell_amount']
        writer.writerow([i['broker_number'],i['total_purch_amount'],total_purhc_percent,i['total_sell_amount'],total_sell_percent,i['matching_summary'],matching_percent,i['total_turn_over'],i['turn_over_vs_market'],buy_sell_ratio])