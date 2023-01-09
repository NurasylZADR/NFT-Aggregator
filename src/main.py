from flask import Flask, render_template, request
from src import database, request as r, Connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    token = database.nft
    address = request.form.get("password")
    if request.method == "POST":
        if database.get(address) != "":
            token = Connector.getTokenByD(address)
        else:
            token = Connector.getTokenByR("mainnet", address)

    return render_template("index.html",
        mintl=str(token.mint),
        standardl=str(token.standard),
        namel=str(token.name),
        symboll=str(token.symbol),
        metadataUrll=str(token.metaplex_metadataUrl),
        updateAuthorityl=str(token.metaplex_updateAuthority),
        sellerFeeBasisPointsl=str(token.metaplex_sellerFeeBasisPoints),
        primarySaleHappenedl=str(token.metaplex_primarySaleHappened),
        isMutablel=str(token.metaplex_isMutable),
        masterEditionl=str(token.metaplex_masterEdition),
        owners_addressl=str(token.metaplex_owners_address),
        owners_verifiedl=str(token.metaplex_owners_verified),
        owners_sharel=str(token.metaplex_owners_share))

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port=8080)