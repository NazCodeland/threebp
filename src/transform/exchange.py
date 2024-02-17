
from config import sector_industry_symbol_mapping
from extract.data import Data


class Base:

    def __init__(self, symbol, name, dfs=[None]):
        self.symbol = symbol
        self.name = name
        self.dfs = dfs if dfs is not None else []

    def __str__(self):
        return f'{self.__class__.__name__}(symbol={self.symbol}, name={self.name})'

    def get_equity_by_symbol(self, symbol):
        for sector in self.sectors:
            for industry in sector.industries:
                for equity in industry.equities:
                    if equity.symbol == symbol:
                        print("equity", equity)
                        return equity


class Exchange(Base):
    def __init__(self, symbol, name, sectors, industries, industry_equities):
        super().__init__(symbol, name)
        self.sectors = []
        self.add_sectors(sectors)  # Pass the necessary data to the method
        self.add_industries(industries)  # Pass the necessary data to the method
        self.add_equities(industry_equities)  # Pass the necessary data to the method
        
    def __str__(self):
        sectors_str = ', '.join([f'{sector.symbol} ({sector.name}, industries=[{", ".join([industry.name for industry in sector.industries])}])' for sector in self.sectors])
        return f'{self.__class__.__name__}(symbol={self.symbol}, name={self.name}, sectors=[{sectors_str}])'


    def __repr__(self):
        exchange_str = f"{self.__class__.__name__}(symbol={self.symbol}, name={self.name}, sectors=[\n"
        for sector in self.sectors:
            exchange_str += f"  {sector.__class__.__name__}(symbol={sector.symbol}, name={sector.name}, industries=[\n"
            for industry in sector.industries:
                exchange_str += f"    {industry.__class__.__name__}(symbol={industry.symbol}, name={industry.name}, equities=[\n"
                for equity in industry.equities:
                    exchange_str += f"      {equity.__class__.__name__}(symbol={equity.symbol}, name={equity.name})\n"
                exchange_str += "    ])\n"
            exchange_str += "  ])\n"
        exchange_str += "])"
        return exchange_str

    def add_sectors(self, sectors):
        for sector_data in sectors:
            sector = Sector(sector_data['symbol'], sector_data['name'])
            self.sectors.append(sector)

    def add_industries(self, industries):
        for sector in self.sectors:
            industry_symbols = sector_industry_symbol_mapping.get(sector.symbol, [])
            for industry_symbol in industry_symbols:
                industry_data = next((ind for ind in industries if ind['symbol'] == industry_symbol), None)
                if industry_data:
                    industry = Industry(industry_data['symbol'], industry_data['name'])
                    sector.add_industry(industry)

    def add_equities(self, industry_equities):
        for sector in self.sectors:
            for industry in sector.industries:
                equities_for_industry = [eq for eq in industry_equities if eq['industry'] == industry.symbol]
                for equity_data in equities_for_industry:
                    try:
                        equity = Equity(equity_data['symbol'], equity_data['name'], industry.symbol, sector.symbol)
                        industry.add_equity(equity)
                    except Exception as e:
                        print(f"Error creating Equity for symbol {equity_data['symbol']}: {e}")


    def download_all_ohlcv(self):
        all_symbols = [equity.symbol for sector in self.sectors for industry in sector.industries for equity in industry.equities]
        all_data = Data.download_price(all_symbols)
        for sector in self.sectors:
            for industry in sector.industries:
                for equity in industry.equities:
                    equity.dfs = all_data[equity.symbol]


class Sector(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.industries = []

    def __str__(self):
        return super().__str__() + f', industries={self.industries}'

    def add_industry(self, industry):
        self.industries.append(industry)

    def download_ohlcv(self):
        for industry in self.industries:
            for equity in industry.equities:
                self.dfs = equity.download_ohlcv()

class Industry(Base):
    def __init__(self, symbol, name):
        super().__init__(symbol, name)
        self.equities = []

    def __str__(self):
        return super().__str__() + f', equities={self.equities}'

    def add_equity(self, stock):
        self.equities.append(stock)

    def download_ohlcv(self):
        for equity in self.equities:
            self.dfs = equity.download_ohlcv()

class Equity(Base):

    def __init__(self, symbol, name, industry, sector, df=None):
        super().__init__(symbol, name, df)
        self.industry = industry
        self.sector = sector
        self.dfs = df

    def download_ohlcv(self):
        self.dfs = Data.download_price(self.symbol)