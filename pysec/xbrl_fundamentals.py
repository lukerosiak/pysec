
class FundamentantalAccountingConcepts:               

    def __init__(self,xbrl):               

        self.xbrl = xbrl


        print " "
        print "FUNDAMENTAL ACCOUNTING CONCEPTS CHECK REPORT:"
        print "XBRL instance: %s" % self.xbrl.XBRLInstanceLocation
        print "XBRL Cloud Viewer: https://edgardashboard.xbrlcloud.com/flex/viewer/XBRLViewer.html#instance=%s" % self.xbrl.XBRLInstanceLocation
        
        print "Entity regiant name: %s" % self.xbrl.fields['EntityRegistrantName']
        print "CIK: %s" % self.xbrl.fields['EntityCentralIndexKey']
        print "Entity filer category: %s" % self.xbrl.fields['EntityFilerCategory']
        print "Trading symbol: %s" % self.xbrl.fields['TradingSymbol']
        print "Fiscal year: %s" % self.xbrl.fields['DocumentFiscalYearFocus']
        print "Fiscal period: %s" % self.xbrl.fields['DocumentFiscalPeriodFocus']
        print "Document type: %s" % self.xbrl.fields['DocumentType']
        
        print "Balance Sheet Date (document period end date): %s" % self.xbrl.fields['BalanceSheetDate']
        print "Income Statement Period (YTD, current period, period start date): %s to %s" % (self.xbrl.fields['IncomeStatementPeriodYTD'], self.xbrl.fields['BalanceSheetDate'])
        
        print "Context ID for document period focus (instants): %s" % self.xbrl.fields['ContextForInstants']
        print "Context ID for YTD period (durations): %s" % self.xbrl.fields['ContextForDurations']
        print " "

       
        
        
        #Assets
        self.xbrl.fields['Assets'] = self.xbrl.GetFactValue("us-gaap:Assets", "Instant")
        if self.xbrl.fields['Assets']== None:
            self.xbrl.fields['Assets'] = 0

        #Current Assets
        self.xbrl.fields['CurrentAssets'] = self.xbrl.GetFactValue("us-gaap:AssetsCurrent", "Instant")
        if self.xbrl.fields['CurrentAssets']== None:
            self.xbrl.fields['CurrentAssets'] = 0
                
        #Noncurrent Assets
        self.xbrl.fields['NoncurrentAssets'] = self.xbrl.GetFactValue("us-gaap:AssetsNoncurrent", "Instant")
        if self.xbrl.fields['NoncurrentAssets']==None:
            if self.xbrl.fields['Assets'] and self.xbrl.fields['CurrentAssets']:
                self.xbrl.fields['NoncurrentAssets'] = self.xbrl.fields['Assets'] - self.xbrl.fields['CurrentAssets']
            else:
                self.xbrl.fields['NoncurrentAssets'] = 0
                
        #LiabilitiesAndEquity
        self.xbrl.fields['LiabilitiesAndEquity'] = self.xbrl.GetFactValue("us-gaap:LiabilitiesAndStockholdersEquity", "Instant")
        if self.xbrl.fields['LiabilitiesAndEquity']== None:
            self.xbrl.fields['LiabilitiesAndEquity'] = self.xbrl.GetFactValue("us-gaap:LiabilitiesAndPartnersCapital", "Instant")
            if self.xbrl.fields['LiabilitiesAndEquity']== None:
                self.xbrl.fields['LiabilitiesAndEquity'] = 0
        
        #Liabilities
        self.xbrl.fields['Liabilities'] = self.xbrl.GetFactValue("us-gaap:Liabilities", "Instant")
        if self.xbrl.fields['Liabilities']== None:
            self.xbrl.fields['Liabilities'] = 0
                
        #CurrentLiabilities
        self.xbrl.fields['CurrentLiabilities'] = self.xbrl.GetFactValue("us-gaap:LiabilitiesCurrent", "Instant")
        if self.xbrl.fields['CurrentLiabilities']== None:
            self.xbrl.fields['CurrentLiabilities'] = 0
                
        #Noncurrent Liabilities
        self.xbrl.fields['NoncurrentLiabilities'] = self.xbrl.GetFactValue("us-gaap:LiabilitiesNoncurrent", "Instant")
        if self.xbrl.fields['NoncurrentLiabilities']== None:
            if self.xbrl.fields['Liabilities'] and self.xbrl.fields['CurrentLiabilities']:
                self.xbrl.fields['NoncurrentLiabilities'] = self.xbrl.fields['Liabilities'] - self.xbrl.fields['CurrentLiabilities']
            else:
                self.xbrl.fields['NoncurrentLiabilities'] = 0
                
        #CommitmentsAndContingencies
        self.xbrl.fields['CommitmentsAndContingencies'] = self.xbrl.GetFactValue("us-gaap:CommitmentsAndContingencies", "Instant")
        if self.xbrl.fields['CommitmentsAndContingencies']== None:
            self.xbrl.fields['CommitmentsAndContingencies'] = 0
                
        #TemporaryEquity
        self.xbrl.fields['TemporaryEquity'] = self.xbrl.GetFactValue("us-gaap:TemporaryEquityRedemptionValue", "Instant")
        if self.xbrl.fields['TemporaryEquity'] == None:
            self.xbrl.fields['TemporaryEquity'] = self.xbrl.GetFactValue("us-gaap:RedeemablePreferredStockCarryingAmount", "Instant")
            if self.xbrl.fields['TemporaryEquity'] == None:
                self.xbrl.fields['TemporaryEquity'] = self.xbrl.GetFactValue("us-gaap:TemporaryEquityCarryingAmount", "Instant")
                if self.xbrl.fields['TemporaryEquity'] == None:
                    self.xbrl.fields['TemporaryEquity'] = self.xbrl.GetFactValue("us-gaap:TemporaryEquityValueExcludingAdditionalPaidInCapital", "Instant")
                    if self.xbrl.fields['TemporaryEquity'] == None:
                        self.xbrl.fields['TemporaryEquity'] = self.xbrl.GetFactValue("us-gaap:TemporaryEquityCarryingAmountAttributableToParent", "Instant")
                        if self.xbrl.fields['TemporaryEquity'] == None:
                            self.xbrl.fields['TemporaryEquity'] = self.xbrl.GetFactValue("us-gaap:RedeemableNoncontrollingInterestEquityFairValue", "Instant")
                            if self.xbrl.fields['TemporaryEquity'] == None:
                                self.xbrl.fields['TemporaryEquity'] = 0
                 
        #RedeemableNoncontrollingInterest (added to temporary equity)
        RedeemableNoncontrollingInterest = None
        
        RedeemableNoncontrollingInterest = self.xbrl.GetFactValue("us-gaap:RedeemableNoncontrollingInterestEquityCarryingAmount", "Instant")
        if RedeemableNoncontrollingInterest == None:
            RedeemableNoncontrollingInterest = self.xbrl.GetFactValue("us-gaap:RedeemableNoncontrollingInterestEquityCommonCarryingAmount", "Instant")
            if RedeemableNoncontrollingInterest == None:
                RedeemableNoncontrollingInterest = 0

        #This adds redeemable noncontrolling interest and temporary equity which are rare, but can be reported seperately
        if self.xbrl.fields['TemporaryEquity']:
            self.xbrl.fields['TemporaryEquity'] = float(self.xbrl.fields['TemporaryEquity']) + float(RedeemableNoncontrollingInterest)


        #Equity
        self.xbrl.fields['Equity'] = self.xbrl.GetFactValue("us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "Instant")
        if self.xbrl.fields['Equity'] == None:
            self.xbrl.fields['Equity'] = self.xbrl.GetFactValue("us-gaap:StockholdersEquity", "Instant")
            if self.xbrl.fields['Equity'] == None:
                self.xbrl.fields['Equity'] = self.xbrl.GetFactValue("us-gaap:PartnersCapitalIncludingPortionAttributableToNoncontrollingInterest", "Instant")
                if self.xbrl.fields['Equity'] == None:
                    self.xbrl.fields['Equity'] = self.xbrl.GetFactValue("us-gaap:PartnersCapital", "Instant")
                    if self.xbrl.fields['Equity'] == None:
                        self.xbrl.fields['Equity'] = self.xbrl.GetFactValue("us-gaap:CommonStockholdersEquity", "Instant")
                        if self.xbrl.fields['Equity'] == None:
                            self.xbrl.fields['Equity'] = self.xbrl.GetFactValue("us-gaap:MemberEquity", "Instant")
                            if self.xbrl.fields['Equity'] == None:
                                self.xbrl.fields['Equity'] = self.xbrl.GetFactValue("us-gaap:AssetsNet", "Instant")
                                if self.xbrl.fields['Equity'] == None:
                                    self.xbrl.fields['Equity'] = 0
        

        #EquityAttributableToNoncontrollingInterest
        self.xbrl.fields['EquityAttributableToNoncontrollingInterest'] = self.xbrl.GetFactValue("us-gaap:MinorityInterest", "Instant")
        if self.xbrl.fields['EquityAttributableToNoncontrollingInterest'] == None:
            self.xbrl.fields['EquityAttributableToNoncontrollingInterest'] = self.xbrl.GetFactValue("us-gaap:PartnersCapitalAttributableToNoncontrollingInterest", "Instant")
            if self.xbrl.fields['EquityAttributableToNoncontrollingInterest'] == None:
                self.xbrl.fields['EquityAttributableToNoncontrollingInterest'] = 0
        
        #EquityAttributableToParent
        self.xbrl.fields['EquityAttributableToParent'] = self.xbrl.GetFactValue("us-gaap:StockholdersEquity", "Instant")
        if self.xbrl.fields['EquityAttributableToParent'] == None:
            self.xbrl.fields['EquityAttributableToParent'] = self.xbrl.GetFactValue("us-gaap:LiabilitiesAndPartnersCapital", "Instant")
            if self.xbrl.fields['EquityAttributableToParent'] == None:
                self.xbrl.fields['EquityAttributableToParent'] = 0




        #BS Adjustments
        #if total assets is missing, try using current assets
        if self.xbrl.fields['Assets'] == 0 and self.xbrl.fields['Assets'] == self.xbrl.fields['LiabilitiesAndEquity'] and self.xbrl.fields['CurrentAssets'] == self.xbrl.fields['LiabilitiesAndEquity']:
            self.xbrl.fields['Assets'] = self.xbrl.fields['CurrentAssets']
        
        #Added to fix Assets
        if self.xbrl.fields['Assets'] == 0 and self.xbrl.fields['LiabilitiesAndEquity'] != 0 and (self.xbrl.fields['CurrentAssets'] == self.xbrl.fields['LiabilitiesAndEquity']):
            self.xbrl.fields['Assets'] = self.xbrl.fields['CurrentAssets']
        
        #Added to fix Assets even more
        if self.xbrl.fields['Assets'] == 0 and self.xbrl.fields['NoncurrentAssets'] == 0 and self.xbrl.fields['LiabilitiesAndEquity'] != 0 and (self.xbrl.fields['LiabilitiesAndEquity']==self.xbrl.fields['Liabilities']+self.xbrl.fields['Equity']):
            self.xbrl.fields['Assets'] = self.xbrl.fields['CurrentAssets']
        
        if self.xbrl.fields['Assets']!=0 and self.xbrl.fields['CurrentAssets']!=0:
            self.xbrl.fields['NoncurrentAssets'] = self.xbrl.fields['Assets'] - self.xbrl.fields['CurrentAssets']
        
        if self.xbrl.fields['LiabilitiesAndEquity']==0 and self.xbrl.fields['Assets']!=0:
            self.xbrl.fields['LiabilitiesAndEquity'] = self.xbrl.fields['Assets']
        
        #Impute: Equity based no parent and noncontrolling interest being present
        if self.xbrl.fields['EquityAttributableToNoncontrollingInterest']!=0 and self.xbrl.fields['EquityAttributableToParent']!=0:
            self.xbrl.fields['Equity'] = self.xbrl.fields['EquityAttributableToParent'] + self.xbrl.fields['EquityAttributableToNoncontrollingInterest']
        
        if self.xbrl.fields['Equity']==0 and self.xbrl.fields['EquityAttributableToNoncontrollingInterest']==0 and self.xbrl.fields['EquityAttributableToParent']!=0:
            self.xbrl.fields['Equity'] = self.xbrl.fields['EquityAttributableToParent']
        
        if self.xbrl.fields['Equity']==0:
            self.xbrl.fields['Equity'] = self.xbrl.fields['EquityAttributableToParent'] + self.xbrl.fields['EquityAttributableToNoncontrollingInterest']
        
        #Added: Impute Equity attributable to parent based on existence of equity and noncontrolling interest.
        if self.xbrl.fields['Equity']!=0 and self.xbrl.fields['EquityAttributableToNoncontrollingInterest']!=0 and self.xbrl.fields['EquityAttributableToParent']==0:
            self.xbrl.fields['EquityAttributableToParent'] = self.xbrl.fields['Equity'] - self.xbrl.fields['EquityAttributableToNoncontrollingInterest']
        
        #Added: Impute Equity attributable to parent based on existence of equity and noncontrolling interest.
        if self.xbrl.fields['Equity']!=0 and self.xbrl.fields['EquityAttributableToNoncontrollingInterest']==0 and self.xbrl.fields['EquityAttributableToParent']==0:
            self.xbrl.fields['EquityAttributableToParent'] = self.xbrl.fields['Equity']
        
        #if total liabilities is missing, figure it out based on liabilities and equity
        if self.xbrl.fields['Liabilities']==0 and self.xbrl.fields['Equity']!=0:
            self.xbrl.fields['Liabilities'] = self.xbrl.fields['LiabilitiesAndEquity'] - (self.xbrl.fields['CommitmentsAndContingencies'] + self.xbrl.fields['TemporaryEquity'] + self.xbrl.fields['Equity'])
        
        #This seems incorrect because liabilities might not be reported
        if self.xbrl.fields['Liabilities']!=0 and self.xbrl.fields['CurrentLiabilities']!=0:
            self.xbrl.fields['NoncurrentLiabilities'] = self.xbrl.fields['Liabilities'] - self.xbrl.fields['CurrentLiabilities']
        
        #Added to fix liabilities based on current liabilities
        if self.xbrl.fields['Liabilities']==0 and self.xbrl.fields['CurrentLiabilities']!=0 and self.xbrl.fields['NoncurrentLiabilities']==0:
            self.xbrl.fields['Liabilities'] = self.xbrl.fields['CurrentLiabilities']
        
                    
        lngBSCheck1 = self.xbrl.fields['Equity'] - (self.xbrl.fields['EquityAttributableToParent'] + self.xbrl.fields['EquityAttributableToNoncontrollingInterest'])
        lngBSCheck2 = self.xbrl.fields['Assets'] - self.xbrl.fields['LiabilitiesAndEquity']
        
        if self.xbrl.fields['CurrentAssets']==0 and self.xbrl.fields['NoncurrentAssets']==0 and self.xbrl.fields['CurrentLiabilities']==0 and self.xbrl.fields['NoncurrentLiabilities']==0:
            #if current assets/liabilities are zero and noncurrent assets/liabilities;: don't do this test because the balance sheet is not classified
            lngBSCheck3 = 0
            lngBSCheck4 = 0
        
        else:
            #balance sheet IS classified
            lngBSCheck3 = self.xbrl.fields['Assets'] - (self.xbrl.fields['CurrentAssets'] + self.xbrl.fields['NoncurrentAssets'])
            lngBSCheck4 = self.xbrl.fields['Liabilities'] - (self.xbrl.fields['CurrentLiabilities'] + self.xbrl.fields['NoncurrentLiabilities'])
        
        
        lngBSCheck5 = self.xbrl.fields['LiabilitiesAndEquity'] - (self.xbrl.fields['Liabilities'] + self.xbrl.fields['CommitmentsAndContingencies'] + self.xbrl.fields['TemporaryEquity'] + self.xbrl.fields['Equity'])
        
        if lngBSCheck1:
            print "BS1: Equity(" , self.xbrl.fields['Equity'] , ") = EquityAttributableToParent(" , self.xbrl.fields['EquityAttributableToParent'] , ") , EquityAttributableToNoncontrollingInterest(" , self.xbrl.fields['EquityAttributableToNoncontrollingInterest'] , "): " , lngBSCheck1
        if lngBSCheck2:
            print "BS2: Assets(" , self.xbrl.fields['Assets'] , ") = LiabilitiesAndEquity(" , self.xbrl.fields['LiabilitiesAndEquity'] , "): " , lngBSCheck2
        if lngBSCheck3:
            print "BS3: Assets(" , self.xbrl.fields['Assets'] , ") = CurrentAssets(" , self.xbrl.fields['CurrentAssets'] , ") , NoncurrentAssets(" , self.xbrl.fields['NoncurrentAssets'] , "): " , lngBSCheck3
        if lngBSCheck4:
            print "BS4: Liabilities(" , self.xbrl.fields['Liabilities'] , ")= CurrentLiabilities(" , self.xbrl.fields['CurrentLiabilities'] , ") , NoncurrentLiabilities(" , self.xbrl.fields['NoncurrentLiabilities'] , "): " , lngBSCheck4
        if lngBSCheck5:
            print "BS5: Liabilities and Equity(" , self.xbrl.fields['LiabilitiesAndEquity'] , ")= Liabilities(" , self.xbrl.fields['Liabilities'] , ") , CommitmentsAndContingencies(" , self.xbrl.fields['CommitmentsAndContingencies'] , "), TemporaryEquity(" , self.xbrl.fields['TemporaryEquity'] , "), Equity(" , self.xbrl.fields['Equity'] , "): " , lngBSCheck5
             
        

        #Income statement

        #Revenues
        self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:Revenues", "Duration")
        if self.xbrl.fields['Revenues'] == None:
            self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:SalesRevenueNet", "Duration")
            if self.xbrl.fields['Revenues'] == None:
                self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:SalesRevenueServicesNet", "Duration")
                if self.xbrl.fields['Revenues'] == None:
                    self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:RevenuesNetOfInterestExpense", "Duration")
                    if self.xbrl.fields['Revenues'] == None:
                        self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:RegulatedAndUnregulatedOperatingRevenue", "Duration")
                        if self.xbrl.fields['Revenues'] == None:
                            self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:HealthCareOrganizationRevenue", "Duration")
                            if self.xbrl.fields['Revenues'] == None:
                                self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:InterestAndDividendIncomeOperating", "Duration")
                                if self.xbrl.fields['Revenues'] == None:
                                    self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:RealEstateRevenueNet", "Duration")
                                    if self.xbrl.fields['Revenues'] == None:
                                        self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:RevenueMineralSales", "Duration")
                                        if self.xbrl.fields['Revenues'] == None:
                                            self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:OilAndGasRevenue", "Duration")
                                            if self.xbrl.fields['Revenues'] == None:
                                                self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:FinancialServicesRevenue", "Duration")
                                                if self.xbrl.fields['Revenues'] == None:
                                                    self.xbrl.fields['Revenues'] = self.xbrl.GetFactValue("us-gaap:RegulatedAndUnregulatedOperatingRevenue", "Duration")                                                
                                                    if self.xbrl.fields['Revenues'] == None:
                                                        self.xbrl.fields['Revenues'] = 0


        #CostOfRevenue
        self.xbrl.fields['CostOfRevenue'] = self.xbrl.GetFactValue("us-gaap:CostOfRevenue", "Duration")
        if self.xbrl.fields['CostOfRevenue'] == None:
            self.xbrl.fields['CostOfRevenue'] = self.xbrl.GetFactValue("us-gaap:CostOfServices", "Duration")
            if self.xbrl.fields['CostOfRevenue'] == None:
                self.xbrl.fields['CostOfRevenue'] = self.xbrl.GetFactValue("us-gaap:CostOfGoodsSold", "Duration")
                if self.xbrl.fields['CostOfRevenue'] == None:
                    self.xbrl.fields['CostOfRevenue'] = self.xbrl.GetFactValue("us-gaap:CostOfGoodsAndServicesSold", "Duration")
                    if self.xbrl.fields['CostOfRevenue'] == None:
                        self.xbrl.fields['CostOfRevenue'] = 0
     
        #GrossProfit
        self.xbrl.fields['GrossProfit'] = self.xbrl.GetFactValue("us-gaap:GrossProfit", "Duration")
        if self.xbrl.fields['GrossProfit'] == None:
            self.xbrl.fields['GrossProfit'] = self.xbrl.GetFactValue("us-gaap:GrossProfit", "Duration")
            if self.xbrl.fields['GrossProfit'] == None:
                self.xbrl.fields['GrossProfit'] = 0
     
        #OperatingExpenses
        self.xbrl.fields['OperatingExpenses'] = self.xbrl.GetFactValue("us-gaap:OperatingExpenses", "Duration")
        if self.xbrl.fields['OperatingExpenses'] == None:
            self.xbrl.fields['OperatingExpenses'] = self.xbrl.GetFactValue("us-gaap:OperatingCostsAndExpenses", "Duration")  #This concept seems incorrect.
            if self.xbrl.fields['OperatingExpenses'] == None:
                self.xbrl.fields['OperatingExpenses'] = 0

        #CostsAndExpenses
        self.xbrl.fields['CostsAndExpenses'] = self.xbrl.GetFactValue("us-gaap:CostsAndExpenses", "Duration")
        if self.xbrl.fields['CostsAndExpenses'] == None:
            self.xbrl.fields['CostsAndExpenses'] = self.xbrl.GetFactValue("us-gaap:CostsAndExpenses", "Duration")
            if self.xbrl.fields['CostsAndExpenses'] == None:
                self.xbrl.fields['CostsAndExpenses'] = 0
     
        #OtherOperatingIncome
        self.xbrl.fields['OtherOperatingIncome'] = self.xbrl.GetFactValue("us-gaap:OtherOperatingIncome", "Duration")
        if self.xbrl.fields['OtherOperatingIncome'] == None:
            self.xbrl.fields['OtherOperatingIncome'] = self.xbrl.GetFactValue("us-gaap:OtherOperatingIncome", "Duration")
            if self.xbrl.fields['OtherOperatingIncome'] == None:
                self.xbrl.fields['OtherOperatingIncome'] = 0
     
        #OperatingIncomeLoss
        self.xbrl.fields['OperatingIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:OperatingIncomeLoss", "Duration")
        if self.xbrl.fields['OperatingIncomeLoss'] == None:
            self.xbrl.fields['OperatingIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:OperatingIncomeLoss", "Duration")
            if self.xbrl.fields['OperatingIncomeLoss'] == None:
                self.xbrl.fields['OperatingIncomeLoss'] = 0
     
        #NonoperatingIncomeLoss
        self.xbrl.fields['NonoperatingIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:NonoperatingIncomeExpense", "Duration")
        if self.xbrl.fields['NonoperatingIncomeLoss'] == None:
            self.xbrl.fields['NonoperatingIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:NonoperatingIncomeExpense", "Duration")
            if self.xbrl.fields['NonoperatingIncomeLoss'] == None:
                self.xbrl.fields['NonoperatingIncomeLoss'] = 0

        #InterestAndDebtExpense
        self.xbrl.fields['InterestAndDebtExpense'] = self.xbrl.GetFactValue("us-gaap:InterestAndDebtExpense", "Duration")
        if self.xbrl.fields['InterestAndDebtExpense'] == None:
            self.xbrl.fields['InterestAndDebtExpense'] = self.xbrl.GetFactValue("us-gaap:InterestAndDebtExpense", "Duration")
            if self.xbrl.fields['InterestAndDebtExpense'] == None:
                self.xbrl.fields['InterestAndDebtExpense'] = 0

        #IncomeBeforeEquityMethodInvestments
        self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments", "Duration")
        if self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] == None:
            self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments", "Duration")
            if self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] == None:
                self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] = 0
     
        #IncomeFromEquityMethodInvestments
        self.xbrl.fields['IncomeFromEquityMethodInvestments'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromEquityMethodInvestments", "Duration")
        if self.xbrl.fields['IncomeFromEquityMethodInvestments'] == None:
            self.xbrl.fields['IncomeFromEquityMethodInvestments'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromEquityMethodInvestments", "Duration")
            if self.xbrl.fields['IncomeFromEquityMethodInvestments'] == None:
                self.xbrl.fields['IncomeFromEquityMethodInvestments'] = 0
     
        #IncomeFromContinuingOperationsBeforeTax
        self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments", "Duration")
        if self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] == None:
            self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "Duration")
            if self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] == None:
                self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] = 0
     
        #IncomeTaxExpenseBenefit
        self.xbrl.fields['IncomeTaxExpenseBenefit'] = self.xbrl.GetFactValue("us-gaap:IncomeTaxExpenseBenefit", "Duration")
        if self.xbrl.fields['IncomeTaxExpenseBenefit'] == None:
            self.xbrl.fields['IncomeTaxExpenseBenefit'] = self.xbrl.GetFactValue("us-gaap:IncomeTaxExpenseBenefitContinuingOperations", "Duration")
            if self.xbrl.fields['IncomeTaxExpenseBenefit'] == None:
                self.xbrl.fields['IncomeTaxExpenseBenefit'] = 0
     
        #IncomeFromContinuingOperationsAfterTax
        self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] = self.xbrl.GetFactValue("us-gaap:IncomeLossBeforeExtraordinaryItemsAndCumulativeEffectOfChangeInAccountingPrinciple", "Duration")
        if self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] == None:
            self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] = self.xbrl.GetFactValue("us-gaap:IncomeLossBeforeExtraordinaryItemsAndCumulativeEffectOfChangeInAccountingPrinciple", "Duration")
            if self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] == None:
                self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] = 0

        #IncomeFromDiscontinuedOperations
        self.xbrl.fields['IncomeFromDiscontinuedOperations'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromDiscontinuedOperationsNetOfTax", "Duration")
        if self.xbrl.fields['IncomeFromDiscontinuedOperations']== None:
            self.xbrl.fields['IncomeFromDiscontinuedOperations'] = self.xbrl.GetFactValue("us-gaap:DiscontinuedOperationGainLossOnDisposalOfDiscontinuedOperationNetOfTax", "Duration")
            if self.xbrl.fields['IncomeFromDiscontinuedOperations']== None:
                self.xbrl.fields['IncomeFromDiscontinuedOperations'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromDiscontinuedOperationsNetOfTaxAttributableToReportingEntity", "Duration")
                if self.xbrl.fields['IncomeFromDiscontinuedOperations']== None:
                    self.xbrl.fields['IncomeFromDiscontinuedOperations'] = 0

        #ExtraordaryItemsGainLoss
        self.xbrl.fields['ExtraordaryItemsGainLoss'] = self.xbrl.GetFactValue("us-gaap:ExtraordinaryItemNetOfTax", "Duration")
        if self.xbrl.fields['ExtraordaryItemsGainLoss']== None:
            self.xbrl.fields['ExtraordaryItemsGainLoss'] = self.xbrl.GetFactValue("us-gaap:ExtraordinaryItemNetOfTax", "Duration")
            if self.xbrl.fields['ExtraordaryItemsGainLoss']== None:
                self.xbrl.fields['ExtraordaryItemsGainLoss'] = 0

        #NetIncomeLoss
        self.xbrl.fields['NetIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:ProfitLoss", "Duration")
        if self.xbrl.fields['NetIncomeLoss']== None:
            self.xbrl.fields['NetIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:NetIncomeLoss", "Duration")
            if self.xbrl.fields['NetIncomeLoss']== None:
                self.xbrl.fields['NetIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:NetIncomeLossAvailableToCommonStockholdersBasic", "Duration")
                if self.xbrl.fields['NetIncomeLoss']== None:
                    self.xbrl.fields['NetIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromContinuingOperations", "Duration")
                    if self.xbrl.fields['NetIncomeLoss']== None:
                        self.xbrl.fields['NetIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:IncomeLossAttributableToParent", "Duration")
                        if self.xbrl.fields['NetIncomeLoss']== None:
                            self.xbrl.fields['NetIncomeLoss'] = self.xbrl.GetFactValue("us-gaap:IncomeLossFromContinuingOperationsIncludingPortionAttributableToNoncontrollingInterest", "Duration")
                            if self.xbrl.fields['NetIncomeLoss']== None:
                                self.xbrl.fields['NetIncomeLoss'] = 0

        #NetIncomeAvailableToCommonStockholdersBasic
        self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic'] = self.xbrl.GetFactValue("us-gaap:NetIncomeLossAvailableToCommonStockholdersBasic", "Duration")
        if self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic']== None:
            self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic'] = 0
                
        #PreferredStockDividendsAndOtherAdjustments
        self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments'] = self.xbrl.GetFactValue("us-gaap:PreferredStockDividendsAndOtherAdjustments", "Duration")
        if self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments']== None:
            self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments'] = 0
                
        #NetIncomeAttributableToNoncontrollingInterest
        self.xbrl.fields['NetIncomeAttributableToNoncontrollingInterest'] = self.xbrl.GetFactValue("us-gaap:NetIncomeLossAttributableToNoncontrollingInterest", "Duration")
        if self.xbrl.fields['NetIncomeAttributableToNoncontrollingInterest']== None:
            self.xbrl.fields['NetIncomeAttributableToNoncontrollingInterest'] = 0
                
        #NetIncomeAttributableToParent
        self.xbrl.fields['NetIncomeAttributableToParent'] = self.xbrl.GetFactValue("us-gaap:NetIncomeLoss", "Duration")
        if self.xbrl.fields['NetIncomeAttributableToParent']== None:
            self.xbrl.fields['NetIncomeAttributableToParent'] = 0

        #OtherComprehensiveIncome
        self.xbrl.fields['OtherComprehensiveIncome'] = self.xbrl.GetFactValue("us-gaap:OtherComprehensiveIncomeLossNetOfTax", "Duration")
        if self.xbrl.fields['OtherComprehensiveIncome']== None:
            self.xbrl.fields['OtherComprehensiveIncome'] = self.xbrl.GetFactValue("us-gaap:OtherComprehensiveIncomeLossNetOfTax", "Duration")
            if self.xbrl.fields['OtherComprehensiveIncome']== None:
                self.xbrl.fields['OtherComprehensiveIncome'] = 0

        #ComprehensiveIncome
        self.xbrl.fields['ComprehensiveIncome'] = self.xbrl.GetFactValue("us-gaap:ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest", "Duration")
        if self.xbrl.fields['ComprehensiveIncome']== None:
            self.xbrl.fields['ComprehensiveIncome'] = self.xbrl.GetFactValue("us-gaap:ComprehensiveIncomeNetOfTax", "Duration")
            if self.xbrl.fields['ComprehensiveIncome']== None:
                self.xbrl.fields['ComprehensiveIncome'] = 0

        #ComprehensiveIncomeAttributableToParent
        self.xbrl.fields['ComprehensiveIncomeAttributableToParent'] = self.xbrl.GetFactValue("us-gaap:ComprehensiveIncomeNetOfTax", "Duration")
        if self.xbrl.fields['ComprehensiveIncomeAttributableToParent']== None:
            self.xbrl.fields['ComprehensiveIncomeAttributableToParent'] = self.xbrl.GetFactValue("us-gaap:ComprehensiveIncomeNetOfTax", "Duration")
            if self.xbrl.fields['ComprehensiveIncomeAttributableToParent']== None:
                self.xbrl.fields['ComprehensiveIncomeAttributableToParent'] = 0
     
        #ComprehensiveIncomeAttributableToNoncontrollingInterest
        self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest'] = self.xbrl.GetFactValue("us-gaap:ComprehensiveIncomeNetOfTaxAttributableToNoncontrollingInterest", "Duration")
        if self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest']==None:
            self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest'] = self.xbrl.GetFactValue("us-gaap:ComprehensiveIncomeNetOfTaxAttributableToNoncontrollingInterest", "Duration")
            if self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest']==None:
                self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest'] = 0



        #########'Adjustments to income statement information
        #Impute: NonoperatingIncomeLossPlusInterestAndDebtExpense
        self.xbrl.fields['NonoperatingIncomeLossPlusInterestAndDebtExpense'] = self.xbrl.fields['NonoperatingIncomeLoss'] + self.xbrl.fields['InterestAndDebtExpense']

        #Impute: Net income available to common stockholders  (if it does not exist)
        if self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic']==0 and self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments']==0 and self.xbrl.fields['NetIncomeAttributableToParent']!=0:
            self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic'] = self.xbrl.fields['NetIncomeAttributableToParent']
                
        #Impute NetIncomeLoss
        if self.xbrl.fields['NetIncomeLoss']!=0 and self.xbrl.fields['IncomeFromContinuingOperationsAfterTax']==0:
            self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] = self.xbrl.fields['NetIncomeLoss'] - self.xbrl.fields['IncomeFromDiscontinuedOperations'] - self.xbrl.fields['ExtraordaryItemsGainLoss']

        #Impute: Net income attributable to parent if it does not exist
        if self.xbrl.fields['NetIncomeAttributableToParent']==0 and self.xbrl.fields['NetIncomeAttributableToNoncontrollingInterest']==0 and self.xbrl.fields['NetIncomeLoss']!=0:
            self.xbrl.fields['NetIncomeAttributableToParent'] = self.xbrl.fields['NetIncomeLoss']

        #Impute: PreferredStockDividendsAndOtherAdjustments
        if self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments']==0 and self.xbrl.fields['NetIncomeAttributableToParent']!=0 and self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic']!=0:
            self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments'] = self.xbrl.fields['NetIncomeAttributableToParent'] - self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic']

        #Impute: comprehensive income
        if self.xbrl.fields['ComprehensiveIncomeAttributableToParent']==0 and self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest']==0 and self.xbrl.fields['ComprehensiveIncome']==0 and self.xbrl.fields['OtherComprehensiveIncome']==0:
            self.xbrl.fields['ComprehensiveIncome'] = self.xbrl.fields['NetIncomeLoss']
                
        #Impute: other comprehensive income
        if self.xbrl.fields['ComprehensiveIncome']!=0 and self.xbrl.fields['OtherComprehensiveIncome']==0:
            self.xbrl.fields['OtherComprehensiveIncome'] = self.xbrl.fields['ComprehensiveIncome'] - self.xbrl.fields['NetIncomeLoss']

        #Impute: comprehensive income attributable to parent if it does not exist
        if self.xbrl.fields['ComprehensiveIncomeAttributableToParent']==0 and self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest']==0 and self.xbrl.fields['ComprehensiveIncome']!=0:
            self.xbrl.fields['ComprehensiveIncomeAttributableToParent'] = self.xbrl.fields['ComprehensiveIncome']

        #Impute: IncomeFromContinuingOperations*Before*Tax
        if self.xbrl.fields['IncomeBeforeEquityMethodInvestments']!=0 and self.xbrl.fields['IncomeFromEquityMethodInvestments']!=0 and self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax']==0:
            self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] = self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] + self.xbrl.fields['IncomeFromEquityMethodInvestments']
                
        #Impute: IncomeFromContinuingOperations*Before*Tax2 (if income before tax is missing)
        if self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax']==0 and self.xbrl.fields['IncomeFromContinuingOperationsAfterTax']!=0:
            self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] = self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] + self.xbrl.fields['IncomeTaxExpenseBenefit']
                
        #Impute: IncomeFromContinuingOperations*After*Tax
        if self.xbrl.fields['IncomeFromContinuingOperationsAfterTax']==0 and \
            (self.xbrl.fields['IncomeTaxExpenseBenefit']!=0 or self.xbrl.fields['IncomeTaxExpenseBenefit']==0) and self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax']!=0:
            self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] = self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] - self.xbrl.fields['IncomeTaxExpenseBenefit']
                
                
        #Impute: GrossProfit
        if self.xbrl.fields['GrossProfit']==0 and (self.xbrl.fields['Revenues']!=0 and self.xbrl.fields['CostOfRevenue']!=0):
            self.xbrl.fields['GrossProfit'] = self.xbrl.fields['Revenues'] - self.xbrl.fields['CostOfRevenue']
                
        #Impute: GrossProfit
        if self.xbrl.fields['GrossProfit']==0 and (self.xbrl.fields['Revenues']!=0 and self.xbrl.fields['CostOfRevenue']!=0):
            self.xbrl.fields['GrossProfit'] = self.xbrl.fields['Revenues'] - self.xbrl.fields['CostOfRevenue']
                
        #Impute: Revenues
        if self.xbrl.fields['GrossProfit']!=0 and (self.xbrl.fields['Revenues']==0 and self.xbrl.fields['CostOfRevenue']!=0):
            self.xbrl.fields['Revenues'] = self.xbrl.fields['GrossProfit'] + self.xbrl.fields['CostOfRevenue']
                
        #Impute: CostOfRevenue
        if self.xbrl.fields['GrossProfit']!=0 and (self.xbrl.fields['Revenues']!=0 and self.xbrl.fields['CostOfRevenue']==0):
            self.xbrl.fields['CostOfRevenue'] = self.xbrl.fields['GrossProfit'] + self.xbrl.fields['Revenues']
     
        #Impute: CostsAndExpenses (would NEVER have costs and expenses if has gross profit, gross profit is multi-step and costs and expenses is single-step)
        if self.xbrl.fields['GrossProfit']==0 and self.xbrl.fields['CostsAndExpenses']==0 and (self.xbrl.fields['CostOfRevenue']!=0 and self.xbrl.fields['OperatingExpenses']!=0):
            self.xbrl.fields['CostsAndExpenses'] = self.xbrl.fields['CostOfRevenue'] + self.xbrl.fields['OperatingExpenses']
                
        #Impute: CostsAndExpenses based on existance of both costs of revenues and operating expenses
        if self.xbrl.fields['CostsAndExpenses']==0 and self.xbrl.fields['OperatingExpenses']!=0 and (self.xbrl.fields['CostOfRevenue']!=0):
            self.xbrl.fields['CostsAndExpenses'] = self.xbrl.fields['CostOfRevenue'] + self.xbrl.fields['OperatingExpenses']
                
        #Impute: CostsAndExpenses
        if self.xbrl.fields['GrossProfit']==0 and self.xbrl.fields['CostsAndExpenses']==0 and self.xbrl.fields['Revenues']!=0 and self.xbrl.fields['OperatingIncomeLoss']!=0 and self.xbrl.fields['OtherOperatingIncome']!=0:
            self.xbrl.fields['CostsAndExpenses'] = self.xbrl.fields['Revenues'] - self.xbrl.fields['OperatingIncomeLoss'] - self.xbrl.fields['OtherOperatingIncome']
                
        #Impute: OperatingExpenses based on existance of costs and expenses and cost of revenues
        if self.xbrl.fields['CostOfRevenue']!=0 and self.xbrl.fields['CostsAndExpenses']!=0 and self.xbrl.fields['OperatingExpenses']==0:
            self.xbrl.fields['OperatingExpenses'] = self.xbrl.fields['CostsAndExpenses'] - self.xbrl.fields['CostOfRevenue']
                
        #Impute: CostOfRevenues single-step method
        if self.xbrl.fields['Revenues']!=0 and self.xbrl.fields['GrossProfit']==0 and \
            (self.xbrl.fields['Revenues'] - self.xbrl.fields['CostsAndExpenses']==self.xbrl.fields['OperatingIncomeLoss']) and \
            self.xbrl.fields['OperatingExpenses']==0 and self.xbrl.fields['OtherOperatingIncome']==0:
            self.xbrl.fields['CostOfRevenue'] = self.xbrl.fields['CostsAndExpenses'] - self.xbrl.fields['OperatingExpenses']

        #Impute: IncomeBeforeEquityMethodInvestments
        if self.xbrl.fields['IncomeBeforeEquityMethodInvestments']==0 and self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax']!=0:
            self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] = self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] - self.xbrl.fields['IncomeFromEquityMethodInvestments']
                
        #Impute: IncomeBeforeEquityMethodInvestments
        if self.xbrl.fields['OperatingIncomeLoss']!=0 and (self.xbrl.fields['NonoperatingIncomeLoss']!=0 and \
            self.xbrl.fields['InterestAndDebtExpense']==0 and self.xbrl.fields['IncomeBeforeEquityMethodInvestments']!=0):
            self.xbrl.fields['InterestAndDebtExpense'] = self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] - (self.xbrl.fields['OperatingIncomeLoss'] + self.xbrl.fields['NonoperatingIncomeLoss'])
        
        #Impute: OtherOperatingIncome
        if self.xbrl.fields['GrossProfit']!=0 and (self.xbrl.fields['OperatingExpenses']!=0 and self.xbrl.fields['OperatingIncomeLoss']!=0):
            self.xbrl.fields['OtherOperatingIncome'] = self.xbrl.fields['OperatingIncomeLoss'] - (self.xbrl.fields['GrossProfit'] - self.xbrl.fields['OperatingExpenses'])

        #Move IncomeFromEquityMethodInvestments
        if self.xbrl.fields['IncomeFromEquityMethodInvestments']!=0 and \
            self.xbrl.fields['IncomeBeforeEquityMethodInvestments']!=0 and self.xbrl.fields['IncomeBeforeEquityMethodInvestments']!=self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax']:
            self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] = self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] - self.xbrl.fields['IncomeFromEquityMethodInvestments']
            self.xbrl.fields['OperatingIncomeLoss'] = self.xbrl.fields['OperatingIncomeLoss'] - self.xbrl.fields['IncomeFromEquityMethodInvestments']
        
        #DANGEROUS!!  May need to turn off. IS3 had 2085 PASSES WITHOUT this imputing. if it is higher,: keep the test
        #Impute: OperatingIncomeLoss
        if self.xbrl.fields['OperatingIncomeLoss']==0 and self.xbrl.fields['IncomeBeforeEquityMethodInvestments']!=0:
            self.xbrl.fields['OperatingIncomeLoss'] = self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] + self.xbrl.fields['NonoperatingIncomeLoss'] - self.xbrl.fields['InterestAndDebtExpense']
                
       
        self.xbrl.fields['NonoperatingIncomePlusInterestAndDebtExpensePlusIncomeFromEquityMethodInvestments'] = self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] - self.xbrl.fields['OperatingIncomeLoss']
    
        #NonoperatingIncomeLossPlusInterestAndDebtExpense
        if self.xbrl.fields['NonoperatingIncomeLossPlusInterestAndDebtExpense']== 0 and self.xbrl.fields['NonoperatingIncomePlusInterestAndDebtExpensePlusIncomeFromEquityMethodInvestments']!=0:
            self.xbrl.fields['NonoperatingIncomeLossPlusInterestAndDebtExpense'] = self.xbrl.fields['NonoperatingIncomePlusInterestAndDebtExpensePlusIncomeFromEquityMethodInvestments'] - self.xbrl.fields['IncomeFromEquityMethodInvestments']
    
       
             
        lngIS1 = (self.xbrl.fields['Revenues'] - self.xbrl.fields['CostOfRevenue']) - self.xbrl.fields['GrossProfit']
        lngIS2 = (self.xbrl.fields['GrossProfit'] - self.xbrl.fields['OperatingExpenses'] + self.xbrl.fields['OtherOperatingIncome']) - self.xbrl.fields['OperatingIncomeLoss']
        lngIS3 = (self.xbrl.fields['OperatingIncomeLoss'] + self.xbrl.fields['NonoperatingIncomeLossPlusInterestAndDebtExpense']) - self.xbrl.fields['IncomeBeforeEquityMethodInvestments']
        lngIS4 = (self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] + self.xbrl.fields['IncomeFromEquityMethodInvestments']) - self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax']
        lngIS5 = (self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] - self.xbrl.fields['IncomeTaxExpenseBenefit']) - self.xbrl.fields['IncomeFromContinuingOperationsAfterTax']
        lngIS6 = (self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] + self.xbrl.fields['IncomeFromDiscontinuedOperations'] + self.xbrl.fields['ExtraordaryItemsGainLoss']) - self.xbrl.fields['NetIncomeLoss']
        lngIS7 = (self.xbrl.fields['NetIncomeAttributableToParent'] + self.xbrl.fields['NetIncomeAttributableToNoncontrollingInterest']) - self.xbrl.fields['NetIncomeLoss']
        lngIS8 = (self.xbrl.fields['NetIncomeAttributableToParent'] - self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments']) - self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic']
        lngIS9 = (self.xbrl.fields['ComprehensiveIncomeAttributableToParent'] + self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest']) - self.xbrl.fields['ComprehensiveIncome']
        lngIS10 = (self.xbrl.fields['NetIncomeLoss'] + self.xbrl.fields['OtherComprehensiveIncome']) - self.xbrl.fields['ComprehensiveIncome']
        lngIS11 = self.xbrl.fields['OperatingIncomeLoss'] - (self.xbrl.fields['Revenues'] - self.xbrl.fields['CostsAndExpenses'] + self.xbrl.fields['OtherOperatingIncome'])
        
        if lngIS1:
            print "IS1: GrossProfit(" , self.xbrl.fields['GrossProfit'] , ") = Revenues(" , self.xbrl.fields['Revenues'] , ") - CostOfRevenue(" , self.xbrl.fields['CostOfRevenue'] , "): " , lngIS1
        if lngIS2:
            print "IS2: OperatingIncomeLoss(" , self.xbrl.fields['OperatingIncomeLoss'] , ") = GrossProfit(" , self.xbrl.fields['GrossProfit'] , ") - OperatingExpenses(" , self.xbrl.fields['OperatingExpenses'] , ") , OtherOperatingIncome(" , self.xbrl.fields['OtherOperatingIncome'] , "): " , lngIS2
        if lngIS3:        
            print "IS3: IncomeBeforeEquityMethodInvestments(" , self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] , ") = OperatingIncomeLoss(" , self.xbrl.fields['OperatingIncomeLoss'] , ") - NonoperatingIncomeLoss(" , self.xbrl.fields['NonoperatingIncomeLoss'] , "), InterestAndDebtExpense(" , self.xbrl.fields['InterestAndDebtExpense'] , "): " , lngIS3
        if lngIS4:
            print "IS4: IncomeFromContinuingOperationsBeforeTax(" , self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] , ") = IncomeBeforeEquityMethodInvestments(" , self.xbrl.fields['IncomeBeforeEquityMethodInvestments'] , ") , IncomeFromEquityMethodInvestments(" , self.xbrl.fields['IncomeFromEquityMethodInvestments'] , "): " , lngIS4
        
        if lngIS5:
            print "IS5: IncomeFromContinuingOperationsAfterTax(" , self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] , ") = IncomeFromContinuingOperationsBeforeTax(" , self.xbrl.fields['IncomeFromContinuingOperationsBeforeTax'] , ") - IncomeTaxExpenseBenefit(" , self.xbrl.fields['IncomeTaxExpenseBenefit'] , "): " , lngIS5
        if  lngIS6:
            print "IS6: NetIncomeLoss(" , self.xbrl.fields['NetIncomeLoss'] , ") = IncomeFromContinuingOperationsAfterTax(" , self.xbrl.fields['IncomeFromContinuingOperationsAfterTax'] , ") , IncomeFromDiscontinuedOperations(" , self.xbrl.fields['IncomeFromDiscontinuedOperations'] , ") , ExtraordaryItemsGainLoss(" , self.xbrl.fields['ExtraordaryItemsGainLoss'] , "): " , lngIS6
        if lngIS7:
            print "IS7: NetIncomeLoss(" , self.xbrl.fields['NetIncomeLoss'] , ") = NetIncomeAttributableToParent(" , self.xbrl.fields['NetIncomeAttributableToParent'] , ") , NetIncomeAttributableToNoncontrollingInterest(" , self.xbrl.fields['NetIncomeAttributableToNoncontrollingInterest'] , "): " , lngIS7
        if lngIS8:
            print "IS8: NetIncomeAvailableToCommonStockholdersBasic(" , self.xbrl.fields['NetIncomeAvailableToCommonStockholdersBasic'] , ") = NetIncomeAttributableToParent(" , self.xbrl.fields['NetIncomeAttributableToParent'] , ") - PreferredStockDividendsAndOtherAdjustments(" , self.xbrl.fields['PreferredStockDividendsAndOtherAdjustments'] , "): " , lngIS8
        if lngIS9:
            print "IS9: ComprehensiveIncome(" , self.xbrl.fields['ComprehensiveIncome'] , ") = ComprehensiveIncomeAttributableToParent(" , self.xbrl.fields['ComprehensiveIncomeAttributableToParent'] , ") , ComprehensiveIncomeAttributableToNoncontrollingInterest(" , self.xbrl.fields['ComprehensiveIncomeAttributableToNoncontrollingInterest'] , "): " , lngIS9
        if lngIS10:
            print "IS10: ComprehensiveIncome(" , self.xbrl.fields['ComprehensiveIncome'] , ") = NetIncomeLoss(" , self.xbrl.fields['NetIncomeLoss'] , ") , OtherComprehensiveIncome(" , self.xbrl.fields['OtherComprehensiveIncome'] , "): " , lngIS10
        if lngIS11:
            print "IS11: OperatingIncomeLoss(" , self.xbrl.fields['OperatingIncomeLoss'] , ") = Revenues(" , self.xbrl.fields['Revenues'] , ") - CostsAndExpenses(" , self.xbrl.fields['CostsAndExpenses'] , ") , OtherOperatingIncome(" , self.xbrl.fields['OtherOperatingIncome'] , "): " , lngIS11



        ###Cash flow statement

        #NetCashFlow
        self.xbrl.fields['NetCashFlow'] = self.xbrl.GetFactValue("us-gaap:CashAndCashEquivalentsPeriodIncreaseDecrease", "Duration")
        if self.xbrl.fields['NetCashFlow']== None:
            self.xbrl.fields['NetCashFlow'] = self.xbrl.GetFactValue("us-gaap:CashPeriodIncreaseDecrease", "Duration")
            if self.xbrl.fields['NetCashFlow']== None:
                self.xbrl.fields['NetCashFlow'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInContinuingOperations", "Duration")
                if self.xbrl.fields['NetCashFlow']== None:
                    self.xbrl.fields['NetCashFlow'] = 0
                
        #NetCashFlowsOperating
        self.xbrl.fields['NetCashFlowsOperating'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInOperatingActivities", "Duration")
        if self.xbrl.fields['NetCashFlowsOperating']== None:
            self.xbrl.fields['NetCashFlowsOperating'] = 0
                
        #NetCashFlowsInvesting
        self.xbrl.fields['NetCashFlowsInvesting'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInInvestingActivities", "Duration")
        if self.xbrl.fields['NetCashFlowsInvesting']== None:
            self.xbrl.fields['NetCashFlowsInvesting'] = 0
                
        #NetCashFlowsFinancing
        self.xbrl.fields['NetCashFlowsFinancing'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInFinancingActivities", "Duration")
        if self.xbrl.fields['NetCashFlowsFinancing']== None:
            self.xbrl.fields['NetCashFlowsFinancing'] = 0
                
        #NetCashFlowsOperatingContinuing
        self.xbrl.fields['NetCashFlowsOperatingContinuing'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInOperatingActivitiesContinuingOperations", "Duration")
        if self.xbrl.fields['NetCashFlowsOperatingContinuing']== None:
            self.xbrl.fields['NetCashFlowsOperatingContinuing'] = 0
                
        #NetCashFlowsInvestingContinuing
        self.xbrl.fields['NetCashFlowsInvestingContinuing'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInInvestingActivitiesContinuingOperations", "Duration")
        if self.xbrl.fields['NetCashFlowsInvestingContinuing']== None:
            self.xbrl.fields['NetCashFlowsInvestingContinuing'] = 0
                
        #NetCashFlowsFinancingContinuing
        self.xbrl.fields['NetCashFlowsFinancingContinuing'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInFinancingActivitiesContinuingOperations", "Duration")
        if self.xbrl.fields['NetCashFlowsFinancingContinuing']== None:
            self.xbrl.fields['NetCashFlowsFinancingContinuing'] = 0
                
        #NetCashFlowsOperatingDiscontinued
        self.xbrl.fields['NetCashFlowsOperatingDiscontinued'] = self.xbrl.GetFactValue("us-gaap:CashProvidedByUsedInOperatingActivitiesDiscontinuedOperations", "Duration")
        if self.xbrl.fields['NetCashFlowsOperatingDiscontinued']==None:
            self.xbrl.fields['NetCashFlowsOperatingDiscontinued'] = 0
                
        #NetCashFlowsInvestingDiscontinued
        self.xbrl.fields['NetCashFlowsInvestingDiscontinued'] = self.xbrl.GetFactValue("us-gaap:CashProvidedByUsedInInvestingActivitiesDiscontinuedOperations", "Duration")
        if self.xbrl.fields['NetCashFlowsInvestingDiscontinued']== None:
            self.xbrl.fields['NetCashFlowsInvestingDiscontinued'] = 0
                
        #NetCashFlowsFinancingDiscontinued
        self.xbrl.fields['NetCashFlowsFinancingDiscontinued'] = self.xbrl.GetFactValue("us-gaap:CashProvidedByUsedInFinancingActivitiesDiscontinuedOperations", "Duration")
        if self.xbrl.fields['NetCashFlowsFinancingDiscontinued']== None:
            self.xbrl.fields['NetCashFlowsFinancingDiscontinued'] = 0
                
        #NetCashFlowsDiscontinued
        self.xbrl.fields['NetCashFlowsDiscontinued'] = self.xbrl.GetFactValue("us-gaap:NetCashProvidedByUsedInDiscontinuedOperations", "Duration")
        if self.xbrl.fields['NetCashFlowsDiscontinued']== None:
            self.xbrl.fields['NetCashFlowsDiscontinued'] = 0
                
        #ExchangeGainsLosses
        self.xbrl.fields['ExchangeGainsLosses'] = self.xbrl.GetFactValue("us-gaap:EffectOfExchangeRateOnCashAndCashEquivalents", "Duration")
        if self.xbrl.fields['ExchangeGainsLosses']== None:
            self.xbrl.fields['ExchangeGainsLosses'] = self.xbrl.GetFactValue("us-gaap:EffectOfExchangeRateOnCashAndCashEquivalentsContinuingOperations", "Duration")
            if self.xbrl.fields['ExchangeGainsLosses']== None:
                self.xbrl.fields['ExchangeGainsLosses'] = self.xbrl.GetFactValue("us-gaap:CashProvidedByUsedInFinancingActivitiesDiscontinuedOperations", "Duration")
                if self.xbrl.fields['ExchangeGainsLosses']== None:
                    self.xbrl.fields['ExchangeGainsLosses'] = 0

        ####Adjustments
        #Impute: total net cash flows discontinued if not reported
        if self.xbrl.fields['NetCashFlowsDiscontinued']==0:
            self.xbrl.fields['NetCashFlowsDiscontinued'] = self.xbrl.fields['NetCashFlowsOperatingDiscontinued'] + self.xbrl.fields['NetCashFlowsInvestingDiscontinued'] + self.xbrl.fields['NetCashFlowsFinancingDiscontinued']

        #Impute: cash flows from continuing
        if self.xbrl.fields['NetCashFlowsOperating']!=0 and self.xbrl.fields['NetCashFlowsOperatingContinuing']==0:
            self.xbrl.fields['NetCashFlowsOperatingContinuing'] = self.xbrl.fields['NetCashFlowsOperating'] - self.xbrl.fields['NetCashFlowsOperatingDiscontinued']
        if self.xbrl.fields['NetCashFlowsInvesting']!=0 and self.xbrl.fields['NetCashFlowsInvestingContinuing']==0:
            self.xbrl.fields['NetCashFlowsInvestingContinuing'] = self.xbrl.fields['NetCashFlowsInvesting'] - self.xbrl.fields['NetCashFlowsInvestingDiscontinued']
        if self.xbrl.fields['NetCashFlowsFinancing']!=0 and self.xbrl.fields['NetCashFlowsFinancingContinuing']==0:
            self.xbrl.fields['NetCashFlowsFinancingContinuing'] = self.xbrl.fields['NetCashFlowsFinancing'] - self.xbrl.fields['NetCashFlowsFinancingDiscontinued']
        
        
        if self.xbrl.fields['NetCashFlowsOperating']==0 and self.xbrl.fields['NetCashFlowsOperatingContinuing']!=0 and self.xbrl.fields['NetCashFlowsOperatingDiscontinued']==0:
            self.xbrl.fields['NetCashFlowsOperating'] = self.xbrl.fields['NetCashFlowsOperatingContinuing']
        if self.xbrl.fields['NetCashFlowsInvesting']==0 and self.xbrl.fields['NetCashFlowsInvestingContinuing']!=0 and self.xbrl.fields['NetCashFlowsInvestingDiscontinued']==0:
            self.xbrl.fields['NetCashFlowsInvesting'] = self.xbrl.fields['NetCashFlowsInvestingContinuing']
        if self.xbrl.fields['NetCashFlowsFinancing']==0 and self.xbrl.fields['NetCashFlowsFinancingContinuing']!=0 and self.xbrl.fields['NetCashFlowsFinancingDiscontinued']==0:
            self.xbrl.fields['NetCashFlowsFinancing'] = self.xbrl.fields['NetCashFlowsFinancingContinuing']
        
        
        self.xbrl.fields['NetCashFlowsContinuing'] = self.xbrl.fields['NetCashFlowsOperatingContinuing'] + self.xbrl.fields['NetCashFlowsInvestingContinuing'] + self.xbrl.fields['NetCashFlowsFinancingContinuing']
        
        #Impute: if net cash flow is missing,: this tries to figure out the value by adding up the detail
        if self.xbrl.fields['NetCashFlow']==0 and (self.xbrl.fields['NetCashFlowsOperating']!=0 or self.xbrl.fields['NetCashFlowsInvesting']!=0 or self.xbrl.fields['NetCashFlowsFinancing']!=0):
            self.xbrl.fields['NetCashFlow'] = self.xbrl.fields['NetCashFlowsOperating'] + self.xbrl.fields['NetCashFlowsInvesting'] + self.xbrl.fields['NetCashFlowsFinancing']

        
        lngCF1 = self.xbrl.fields['NetCashFlow'] - (self.xbrl.fields['NetCashFlowsOperating'] + self.xbrl.fields['NetCashFlowsInvesting'] + self.xbrl.fields['NetCashFlowsFinancing'] + self.xbrl.fields['ExchangeGainsLosses'])
        if lngCF1!=0 and (self.xbrl.fields['NetCashFlow'] - (self.xbrl.fields['NetCashFlowsOperating'] + self.xbrl.fields['NetCashFlowsInvesting'] + self.xbrl.fields['NetCashFlowsFinancing'] + self.xbrl.fields['ExchangeGainsLosses'])==(self.xbrl.fields['ExchangeGainsLosses']*-1)):       
            lngCF1 = 888888
            #What is going on here is that 171 filers compute net cash flow differently than everyone else.  
            #What I am doing is marking these by setting the value of the test to a number 888888 which would never occur naturally, so that I can differentiate this from errors.
        lngCF2 = self.xbrl.fields['NetCashFlowsContinuing'] - (self.xbrl.fields['NetCashFlowsOperatingContinuing'] + self.xbrl.fields['NetCashFlowsInvestingContinuing'] + self.xbrl.fields['NetCashFlowsFinancingContinuing'])
        lngCF3 = self.xbrl.fields['NetCashFlowsDiscontinued'] - (self.xbrl.fields['NetCashFlowsOperatingDiscontinued'] + self.xbrl.fields['NetCashFlowsInvestingDiscontinued'] + self.xbrl.fields['NetCashFlowsFinancingDiscontinued'])
        lngCF4 = self.xbrl.fields['NetCashFlowsOperating'] - (self.xbrl.fields['NetCashFlowsOperatingContinuing'] + self.xbrl.fields['NetCashFlowsOperatingDiscontinued'])
        lngCF5 = self.xbrl.fields['NetCashFlowsInvesting'] - (self.xbrl.fields['NetCashFlowsInvestingContinuing'] + self.xbrl.fields['NetCashFlowsInvestingDiscontinued'])
        lngCF6 = self.xbrl.fields['NetCashFlowsFinancing'] - (self.xbrl.fields['NetCashFlowsFinancingContinuing'] + self.xbrl.fields['NetCashFlowsFinancingDiscontinued'])
        
        
        if lngCF1:
            print "CF1: NetCashFlow(" , self.xbrl.fields['NetCashFlow'] , ") = (NetCashFlowsOperating(" , self.xbrl.fields['NetCashFlowsOperating'] , ") , (NetCashFlowsInvesting(" , self.xbrl.fields['NetCashFlowsInvesting'] , ") , (NetCashFlowsFinancing(" , self.xbrl.fields['NetCashFlowsFinancing'] , ") , ExchangeGainsLosses(" , self.xbrl.fields['ExchangeGainsLosses'] , "): " , lngCF1
        if lngCF2:
            print "CF2: NetCashFlowsContinuing(" , self.xbrl.fields['NetCashFlowsContinuing'] , ") = NetCashFlowsOperatingContinuing(" , self.xbrl.fields['NetCashFlowsOperatingContinuing'] , ") , NetCashFlowsInvestingContinuing(" , self.xbrl.fields['NetCashFlowsInvestingContinuing'] , ") , NetCashFlowsFinancingContinuing(" , self.xbrl.fields['NetCashFlowsFinancingContinuing'] , "): " , lngCF2
        if lngCF3:
            print "CF3: NetCashFlowsDiscontinued(" , self.xbrl.fields['NetCashFlowsDiscontinued'] , ") = NetCashFlowsOperatingDiscontinued(" , self.xbrl.fields['NetCashFlowsOperatingDiscontinued'] , ") , NetCashFlowsInvestingDiscontinued(" , self.xbrl.fields['NetCashFlowsInvestingDiscontinued'] , ") , NetCashFlowsFinancingDiscontinued(" , self.xbrl.fields['NetCashFlowsFinancingDiscontinued'] , "): " , lngCF3
        if lngCF4:
            print "CF4: NetCashFlowsOperating(" , self.xbrl.fields['NetCashFlowsOperating'] , ") = NetCashFlowsOperatingContinuing(" , self.xbrl.fields['NetCashFlowsOperatingContinuing'] , ") , NetCashFlowsOperatingDiscontinued(" , self.xbrl.fields['NetCashFlowsOperatingDiscontinued'] , "): " , lngCF4
        if lngCF5:
            print "CF5: NetCashFlowsInvesting(" , self.xbrl.fields['NetCashFlowsInvesting'] , ") = NetCashFlowsInvestingContinuing(" , self.xbrl.fields['NetCashFlowsInvestingContinuing'] , ") , NetCashFlowsInvestingDiscontinued(" , self.xbrl.fields['NetCashFlowsInvestingDiscontinued'] , "): " , lngCF5
        if lngCF6:
            print "CF6: NetCashFlowsFinancing(" , self.xbrl.fields['NetCashFlowsFinancing'] , ") = NetCashFlowsFinancingContinuing(" , self.xbrl.fields['NetCashFlowsFinancingContinuing'] , ") , NetCashFlowsFinancingDiscontinued(" , self.xbrl.fields['NetCashFlowsFinancingDiscontinued'] , "): " , lngCF6


        #Key ratios
        try:
            self.xbrl.fields['SGR'] = ((self.xbrl.fields['NetIncomeLoss'] / self.xbrl.fields['Revenues']) * (1 + ((self.xbrl.fields['Assets'] - self.xbrl.fields['Equity']) / self.xbrl.fields['Equity']))) / ((1 / (self.xbrl.fields['Revenues'] / self.xbrl.fields['Assets'])) - (((self.xbrl.fields['NetIncomeLoss'] / self.xbrl.fields['Revenues']) * (1 + (((self.xbrl.fields['Assets'] - self.xbrl.fields['Equity']) / self.xbrl.fields['Equity']))))))
        except:
            pass
           
        try:
            self.xbrl.fields['ROA'] = self.xbrl.fields['NetIncomeLoss'] / self.xbrl.fields['Assets']
        except:
            pass
        
        try:    
            self.xbrl.fields['ROE'] = self.xbrl.fields['NetIncomeLoss'] / self.xbrl.fields['Equity']
        except:
            pass
            
        try:    
            self.xbrl.fields['ROS'] = self.xbrl.fields['NetIncomeLoss'] / self.xbrl.fields['Revenues']
        except:
            pass           

