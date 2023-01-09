import requests
def info(network, address):
    url = "https://solana-gateway.moralis.io/nft/" + network + "/" + address + "/metadata"
    headers = {
        "accept": "application/json",
        "X-API-Key": "8nXrMHY4geAUkLfNt4vHbeghTqfm0w0Ml8nT2DuDfxmgQoebG0PMkA81aMmGfXwX"
    }
    response = requests.get(url, headers=headers)
    return response
