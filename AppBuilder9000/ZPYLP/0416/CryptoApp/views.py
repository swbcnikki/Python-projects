from django.shortcuts import render, redirect, get_object_or_404
from .models import Currency, CoinStatus
from .forms import CurrencyForm, CoinStatusForm, SearchForm
import requests


def home(request):
    return render(request, 'CryptoApp/CryptoApp_home.html')


def add_currency(request):
    form = CurrencyForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CryptoApp_home')
    content = {'form': form}
    return render(request, 'CryptoApp/CryptoApp_AddCurrency.html', content)


def add_status(request):
    form = CoinStatusForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CryptoApp_home')
    content = {'form': form}
    return render(request, 'CryptoApp/CryptoApp_AddStatus.html', content)


def display(request):
    cryptos = CoinStatus.CoinStatuses.all()
    context = {'cryptos': cryptos}
    return render(request, 'CryptoApp/CryptoApp_display.html', context)


def details(request, record_id):
    # TODO: Try doing this with get_object_or_404() method.
    coins = CoinStatus.CoinStatuses.filter(id=record_id)
    this_coin = coins[0]
    # Create dictionary for use on details page
    coin_detail = {
        'coin_name': this_coin.currency.chain_name,
        'coin_unit': this_coin.currency.coin_unit,
        'chain_type': this_coin.currency.chain_type,
        'launch_date': this_coin.currency.launch_date,
        'value': this_coin.value,
        'as_of_date': this_coin.as_of_date,
        'supply': this_coin.supply,
        'market_cap': this_coin.market_cap,
        'transactions_per_sec': this_coin.transactions_per_sec
    }
    context = {'coin_detail': coin_detail}
    return render(request, 'CryptoApp/CryptoApp_details.html', context)


def edit(request, record_id):
    coin = get_object_or_404(Currency, pk=record_id)
    if request.method == "POST":
        edit_currency_form = CurrencyForm(request.POST, instance=coin)
        if edit_currency_form.is_valid():
            coin.save()
            return redirect('CryptoApp_details', record_id=coin.id)
    else:
        edit_currency_form = CurrencyForm(instance=coin)
    return render(request, 'CryptoApp/CryptoApp_edit.html', {'form': edit_currency_form})


def update(request, record_id):
    coin = get_object_or_404(CoinStatus, pk=record_id)
    if request.method == "POST":
        update_status_form = CoinStatusForm(request.POST, instance=coin)
        if update_status_form.is_valid():
            coin.save()
            return redirect('CryptoApp_details', record_id=coin.id)
    else:
        update_status_form = CoinStatusForm(instance=coin)
    return render(request, 'CryptoApp/CryptoApp_update.html', {'form': update_status_form})


def delete(request, record_id):
    coin = get_object_or_404(Currency, pk=record_id)
    if request.method == 'POST':
        coin.delete()
        return redirect('CryptoApp_display')
    context = {'coin': coin}
    return render(request, 'CryptoApp/CryptoApp_delete.html', context)


def trending(request):
    response = requests.get('https://api.coingecko.com/api/v3/search/trending')
    print(response.status_code)
    # Response from coingecko.com comes as dictionary where we want only the 'coins' value
    # That value is a list of the currencies with info stored as key-value pairs
    coins = response.json()['coins']  # Now we have a list of dictionaries each with one key: 'item'
    trend = {}
    counter = 1
    for items in coins:
        name = 'name' + str(counter)
        symbol = 'symbol' + str(counter)
        market_cap_rank = 'market_cap_rank' + str(counter)
        item = items.get('item') # Getting the value from each dictionary 'item'
        trend.update({name: item.get('name'), symbol: item.get('symbol'),
                      market_cap_rank: item.get('market_cap_rank')})
        counter += 1
    context = {'trend': trend}
    return render(request, 'CryptoApp/CryptoApp_trending.html', context)


def lookup(request):
    form = SearchForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            return render(request, 'CryptoApp/CryptoApp_results.html')
    content = {'form': form}
    return render(request, 'CryptoApp/CryptoApp_lookup.html', content)


def results(request):
    if request.method == "POST":
        get_coin = request.POST["search_name"].lower()
        try:
            api_request = ("https://api.coingecko.com/api/v3/coins/{}?localization=false&tickers=false&market_data"
                       "=false&community_data=false&developer_data=false&sparkline=false".format(get_coin))
            answer = requests.get(api_request)
            print(answer.status_code)
            all_info = answer.json()
            description = all_info.get("description")
            # Selecting which elements from json response to present in template
            coin_info = {
                "name": all_info.get("name"),
                "symbol": all_info.get("symbol").upper(),
                "description": description.get("en"),  # Description of currency.
                "block_time_in_minutes": all_info.get("block_time_in_minutes"),
                "genesis_date": all_info.get("genesis_date"),
                "hashing_algorithm": all_info.get("hashing_algorithm"),
                "liquidity_score": all_info.get("liquidity_score"),
                "market_cap_rank": all_info.get("market_cap_rank")
            }
        except:
            coin_info = {'name': "No record found"}
        response = {'coin_info': coin_info}
    return render(request, 'CryptoApp/CryptoApp_results.html', response)
