# 必要なライブラリをインポート
import requests
from bs4 import BeautifulSoup
import csv

# スクレイピング先を選択するフラグ  True : オフラインのサイト  False : オンラインのサイト
is_offline = True

# サイトから情報をスクレイピング
if is_offline:
    soup = BeautifulSoup(open('./sample_site/yahoo_finance_dividend_yield_ranking.html', encoding='utf-8'), "html.parser")
else:
    url = 'https://finance.yahoo.co.jp/stocks/ranking/dividendYield'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

# 変数soupの確認 確認後下2行をコメントアウト
print(soup)
exit()

# 高配当株式の行のデータを取得
stock_rows = soup.select('スクレイピングするクラス')

# 変数stock_rowsの確認 確認後下2行をコメントアウト
print(stock_rows)
exit()

# スクレイピングしたデータを格納するリスト
scraping_data_list = list()

# 各行から高配当株式の情報を取得
for stock_row in stock_rows:
    # 株式名称をスクレイピング
    stock_name = stock_row.select('スクレイピングするクラス')[0].select_one('スクレイピングするタグ').get_text()

    # 変数stock_nameの確認 確認後下2行をコメントアウト
    print(stock_name)
    exit()

    # 株式価格をスクレイピング
    stock_price = stock_row.select('スクレイピングするクラス')[1].select_one('スクレイピングするクラス').get_text()

    # 1株当たり配当金をスクレイピング
    dividend_per_share = stock_row.select('スクレイピングするクラス')[3].select_one('スクレイピングするクラス').get_text()

    # 配当利回りをスクレイピング
    dividend_yield = stock_row.select('スクレイピングするクラス')[4].select_one('スクレイピングするクラス').get_text()

    # スクレイピングした結果をリストに格納
    scraping_data_list.append([stock_name, stock_price, dividend_per_share, dividend_yield])

    # スクレイピングした結果を出力
    print(stock_name, stock_price, dividend_per_share, dividend_yield)


# スクレイピングしたデータをCSVファイルに出力
# scraping_data.csvを書き込み専用で開く
with open('./src/scraping_data.csv', 'w') as f :
    writer = csv.writer(f)
    
    # スクレイピングしたデータを1行ずつCSVファイルに書き込み
    for scraping_data in scraping_data_list:
        writer.writerow(scraping_data)

    f.close()
