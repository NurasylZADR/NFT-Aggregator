from src import request, database
import json

def getTokenR(network, address):
    response = request.info(network, address)
    m = json.loads(response.text)
    token = database.nft
    try:
        token = database.nft(
            str(m.get("mint")), str(m.get("standard")), str(m.get("name")), str(m.get("symbol")),
            str(m.get("metaplex").get("metadataUrl")),
            str(m.get("metaplex").get("updateAuthority")),
            int(m.get("metaplex").get("sellerFeeBasisPoints")),
            int(m.get("metaplex").get("primarySaleHappened")),
            bool(m.get("metaplex").get("isMutable")),
            bool(m.get("metaplex").get("masterEdition")),
            str(m.get("metaplex").get("owners")[0].get("address")),
            int(m.get("metaplex").get("owners")[0].get("verified")),
            int(m.get("metaplex").get("owners")[0].get("share")))
    except AttributeError:
        print("bad request")
    finally:
        database.add(token)
        return token


def getTokenD(address):
    token = database.nft(database.get(address).mint,
            database.get(address).standard,
            database.get(address).name,
            database.get(address).symbol,
            database.get(address).metaplex_metadataUrl,
            database.get(address).metaplex_updateAuthority,
            database.get(address).metaplex_sellerFeeBasisPoints,
            database.get(address).metaplex_primarySaleHappened,
            database.get(address).metaplex_isMutable,
            database.get(address).metaplex_masterEdition,
            database.get(address).metaplex_owners_address,
            database.get(address).metaplex_owners_verified,
            database.get(address).metaplex_owners_share)


