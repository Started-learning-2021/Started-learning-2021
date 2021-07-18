#Classify Market_caps by a, b, c & d rankings. Could probably instead make this a ranking, i.e. what rank in the list x rank of x companies total as an improvement 
#Want to just see the code rank first before adding functions 

class ASX_Ranking: 
    
    def __init__(self, ASX_code):
        self.ASX_code = ASX_code 
        self.Company_name = Company_name
        self.Market_Cap = Market_Cap 
        self.ASX_Rankings = []
        self.Market_Cap_Ranking_Scale = {
            "A": [1000000, 10000000],
            "B": [10000001, 100000000],
            "C": [100000001, 1000000000],
            "D": [1000000001, 1000000000000]  
        }   
        
#is this adding my ASX_Company class 

    def add_ASX_Company(self, ASX_Company):
        ASX_Company.Market_Cap_Ranking.update({self.ASX_code: 0})
        self.ASX_Rankings.append(ASX_Company)

# Loop through Market

    def get_Market_Cap_Ranking(self, Market_Cap_Ranking):  
        for Market_Cap in self.Market_Cap_Rankings.keys():
            scale = self.Market_Cap_Rankings[Market_Cap]  
            if scale[0] < Market_Cap_Ranking <= scale[1]:
                return Market_Cap_Ranking

    def return_Market_Cap_Rankings_Roster(self): 
        roster = {}
        for s in self.ASX_Rankings: 
            roster_entry = {
                "Company_name": s.Company_name + ". "
                "Listing_date": s.Listing_date + ". "
                "ASX_Rankings": s.ASX_Ranking + ". "
            }
            roster.update(roster_entry)
        return roster


