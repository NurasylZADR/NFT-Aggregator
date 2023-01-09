from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()
app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres://:postgres@localhost:5432/python"
db.init_app(app)

class nft(db.Model):
    mint = db.Column(db.String, primary_key = True)
    standard = db.Column(db.String)
    name = db.Column(db.String)
    symbol = db.Column(db.String)
    metaplex_metadataUrl = db.Column(db.String)
    metaplex_updateAuthority = db.Column(db.String)
    metaplex_sellerFeeBasisPoints = db.Column(db.Integer)
    metaplex_primarySaleHappened = db.Column(db.Integer)
    metaplex_isMutable = db.Column(db.Boolean)
    metaplex_masterEdition = db.Column(db.Boolean)
    metaplex_owners_address = db.Column(db.String)
    metaplex_owners_verified = db.Column(db.Integer)
    metaplex_owners_share = db.Column(db.Integer)

    def __init__(self, mint, standard, name, symbol,
                 metaplex_metadataUrl, metaplex_updateAuthority,
                 metaplex_sellerFeeBasisPoints,
                 metaplex_primarySaleHappened,
                 metaplex_isMutable, metaplex_masterEdition,
                 metaplex_owners_address, metaplex_owners_verified,
                 metaplex_owners_share):
        self.mint = mint
        self.standard = standard
        self.name = name
        self.symbol = symbol
        self.metaplex_metadataUrl = metaplex_metadataUrl
        self.metaplex_updateAuthority = metaplex_updateAuthority
        self.metaplex_sellerFeeBasisPoints = metaplex_sellerFeeBasisPoints
        self.metaplex_primarySaleHappened = metaplex_primarySaleHappened
        self.metaplex_isMutable = metaplex_isMutable
        self.metaplex_masterEdition = metaplex_masterEdition
        self.metaplex_owners_address = metaplex_owners_address
        self.metaplex_owners_verified = metaplex_owners_verified
        self.metaplex_owners_share = metaplex_owners_share

with app.app_context():
    db.create_all()

def add(token):
    db.session.add(nft, token)
    db.session.commit()
def get(address):
    if(len(nft.query.filter_by(mint = address).all())) != 0:
        return nft.query.filter_by(mint = address).all()
    else:
        return ""





