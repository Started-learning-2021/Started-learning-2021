class ASX_Company: 

    def __init__(self, ASX_code, Company_name, Listing_date, GICs_industry_group, Market_Cap):
        self.ASX_code = ASX_code
        self.Company_name = Company_name
        self.Listing_date = Listing_date
        self.GICs_industry_group = GICs_industry_group
        self.Market_Cap = Market_Cap
        self.ASX_Rankings = {}
