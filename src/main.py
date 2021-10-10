import requests

# author ALIGAZY

class ALIGAZY:
    def news_func(coin_name):
        news_paper = []
        count_url = requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?')
        count = count_url.json()['data']['totalCount']
        responce = requests.get(
            url=f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit={count}&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false')
        data = responce.json()
        for i in range(0, int(count)):
            if data['data']['cryptoCurrencyList'][i]['name'].lower() == coin_name.lower():
                coin_id = data['data']['cryptoCurrencyList'][i]['id']
        news_url = requests.get(url=f'https://api.coinmarketcap.com/content/v3/news?coins={coin_id}&size=1000')
        news = news_url.json()
        for i in range(len(news['data'])):
            news_paper.append({
                'News title': news['data'][i]['meta']['title'],
                'Text': news['data'][i]['meta']['subtitle']
            })
        return news_paper










