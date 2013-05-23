from pysec import xbrl
import csv

from pysec.models import *
from django.core.management.base import NoArgsCommand

import os
import psycopg2



class Command(NoArgsCommand):
    help = "Put the 50+ common accounting terms from an arbitrary list of 10ks into a spreadsheet"
    
    def handle_noargs(self, **options):

        headers = ['EntityRegistrantName', 'EntityCentralIndexKey', 'EntityFilerCategory', 'TradingSymbol', 'FiscalYear', 'FiscalPeriod', 'DocumentType', 'PeriodStartDate', 'DocumentPeriodEndDate', 'Assets', 'CurrentAssets', 'NoncurrentAssets', 'LiabilitiesAndEquity', 'Liabilities', 'CurrentLiabilities', 'NoncurrentLiabilities', 'CommitmentsAndContingencies', 'TemporaryEquity', 'Equity', 'EquityAttributableToParent', 'EquityAttributableToNoncontrollingInterest', 'Revenues', 'CostOfRevenue', 'GrossProfit', 'OperatingExpenses', 'CostsAndExpenses', 'OtherOperatingIncome', 'OperatingIncomeLoss', 'NonoperatingIncomeLoss', 'InterestAndDebtExpense', 'NonoperatingIncomeLossPlusInterestAndDebtExpense', 'IncomeBeforeEquityMethodInvestments', 'IncomeFromEquityMethodInvestments', 'IncomeFromContinuingOperationsBeforeTax', 'IncomeTaxExpenseBenefit', 'IncomeFromContinuingOperationsAfterTax', 'IncomeFromDiscontinuedOperations', 'ExtraordaryItemsGainLoss', 'NetIncomeLoss', 'NetIncomeAttributableToParent', 'NetIncomeAttributableToNoncontrollingInterest', 'PreferredStockDividendsAndOtherAdjustments', 'NetIncomeAvailableToCommonStockholdersBasic', 'ComprehensiveIncome', 'OtherComprehensiveIncome', 'NetCashFlowsOperating', 'NetCashFlowsOperatingContinuing', 'NetCashFlowsOperatingDiscontinued', 'NetCashFlowsInvesting', 'NetCashFlowsInvestingContinuing', 'NetCashFlowsInvestingDiscontinued', 'NetCashFlowsFinancing', 'NetCashFlowsFinancingContinuing', 'NetCashFlowsFinancingDiscontinued', 'NetCashFlowsContinuing', 'NetCashFlowsDiscontinued', 'ExchangeGainsLosses', 'NetCashFlow', 'ComprehensiveIncomeAttributableToParent', 'ComprehensiveIncomeAttributableToNoncontrollingInterest', 'SGR', 'ROA', 'ROE', 'ROS', 'SECFilingPage', 'LinkToXBRLInstance']

        fout = csv.DictWriter(open('/home/luke/research/sec/pysec/test.csv','w'),headers)
        fout.writeheader()

        #this SQL is just a way of getting a list of particular CIKs I want
        conn = psycopg2.connect("dbname=recovery")
        cur = conn.cursor()
        cur.execute("SELECT cik, ticker FROM index WHERE cik is not null and use='1';")
        rows = cur.fetchall()
        for row in rows:
            cik = row[0]
            print cik
            for year in range(2011,2014):
                latest = Index.objects.filter(form='10-K',cik=cik,quarter__startswith=year).order_by('-date')
                if len(latest):
                    latest = latest[0]
                    latest.download()
                    x = latest.xbrl()
                    if x==None:
                        print 'no xbrl for ', cik, year
                        continue
                                        
                    d = {}
                    for f in headers:
                        if f in x.fields.keys():
                            d[f] = x.fields[f]
                        else:
                            d[f] = ''
                    d['FiscalPeriod'] = x.fields['DocumentFiscalPeriodFocus']
                    d['FiscalYear'] = x.fields['DocumentFiscalYearFocus']
                    d['DocumentPeriodEndDate'] = x.fields['BalanceSheetDate']
                    d['PeriodStartDate'] = x.fields['IncomeStatementPeriodYTD']
                    d['SECFilingPage'] = latest.index_link()
                    d['LinkToXBRLInstance'] = latest.xbrl_link() 
                    
                    
                    fout.writerow( d )
               
