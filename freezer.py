from flask_frozen import Freezer
from portfolio_app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()