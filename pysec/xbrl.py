from lxml import etree
from xbrl_fundamentals import FundamentantalAccountingConcepts
import re

class XBRL:
 

    def __init__(self,XBRLInstanceLocation):
                
        self.XBRLInstanceLocation = XBRLInstanceLocation        
        self.fields = {}
        
        self.EntireInstanceDocument = open(XBRLInstanceLocation,'r').read() 
        self.oInstance = etree.fromstring(self.EntireInstanceDocument)
        self.ns = {}
        for k in self.oInstance.nsmap.keys():
            if k != None:
                self.ns[k] = self.oInstance.nsmap[k]
        self.ns['xbrli'] = 'http://www.xbrl.org/2003/instance'
        self.ns['xlmns'] = 'http://www.xbrl.org/2003/instance'
                                        
        self.GetBaseInformation()        
        self.loadYear(0)

    def loadYear(self,yearminus=0):        
        currentEnd = self.getNode("//dei:DocumentPeriodEndDate").text
        asdate = re.match('\s*(\d{4})-(\d{2})-(\d{2})\s*', currentEnd)
        if asdate:
            year = int(asdate.groups()[0]) - yearminus
            thisend = '%s-%s-%s' % (year,asdate.groups()[1],asdate.groups()[2])                    
            self.GetCurrentPeriodAndContextInformation(thisend)
            FundamentantalAccountingConcepts(self)
            return True
        else:
            print currentEnd, ' is not a date'
            return False
            
    def getNodeList(self,xpath,root=None):
        if not root is not None: root = self.oInstance
        oNodelist = root.xpath(xpath,namespaces=self.ns)
        return oNodelist
        
    def getNode(self,xpath,root=None):
        oNodelist = self.getNodeList(xpath,root)
        if len(oNodelist):
            return oNodelist[0]
        return None

    def GetFactValue(self,SeekConcept, ConceptPeriodType):
                
        factValue = None
            
        if ConceptPeriodType == "Instant":
            ContextReference = self.fields['ContextForInstants']
        elif ConceptPeriodType == "Duration":
            ContextReference = self.fields['ContextForDurations']
        else:
            #An error occured
            return "CONTEXT ERROR"
        
        if not ContextReference:
            return None


        oNode = self.getNode("//" + SeekConcept + "[@contextRef='" + ContextReference + "']")
        if oNode is not None:                    
            factValue = oNode.text
            if 'nil' in oNode.keys() and oNode.get('nil')=='true':
                factValue=0
                #set the value to ZERO if it is nil
            #if type(factValue)==str:
            try:
                factValue = float(factValue)
            except:
                print 'couldnt convert %s=%s to string' % (SeekConcept,factValue)
                factValue = None
                pass
            
        return factValue   
                    
        
        

    def GetBaseInformation(self):        
                
        #Registered Name
        oNode = self.getNode("//dei:EntityRegistrantName[@contextRef]")
        if oNode is not None:
            self.fields['EntityRegistrantName'] = oNode.text
        else:
            self.fields['EntityRegistrantName'] = "Registered name not found"

        #Fiscal year
        oNode = self.getNode("//dei:CurrentFiscalYearEndDate[@contextRef]")        
        if oNode is not None:
            self.fields['FiscalYear'] = oNode.text
        else:
            self.fields['FiscalYear'] = "Fiscal year not found"

        #EntityCentralIndexKey
        oNode = self.getNode("//dei:EntityCentralIndexKey[@contextRef]")
        if oNode is not None:
            self.fields['EntityCentralIndexKey'] = oNode.text
        else:
            self.fields['EntityCentralIndexKey'] = "CIK not found"

        #EntityFilerCategory
        oNode = self.getNode("//dei:EntityFilerCategory[@contextRef]")
        if oNode is not None:
            self.fields['EntityFilerCategory'] = oNode.text
        else:
            self.fields['EntityFilerCategory'] = "Filer category not found"

        #TradingSymbol
        oNode = self.getNode("//dei:TradingSymbol[@contextRef]")
        if oNode is not None:
            self.fields['TradingSymbol'] = oNode.text
        else:
            self.fields['TradingSymbol'] = "Not provided"

        #DocumentFiscalYearFocus
        oNode = self.getNode("//dei:DocumentFiscalYearFocus[@contextRef]")
        if oNode is not None:
            self.fields['DocumentFiscalYearFocus'] = oNode.text
        else:
            self.fields['DocumentFiscalYearFocus'] = "Fiscal year focus not found"

        #DocumentFiscalPeriodFocus
        oNode = self.getNode("//dei:DocumentFiscalPeriodFocus[@contextRef]")
        if oNode is not None:
            self.fields['DocumentFiscalPeriodFocus'] = oNode.text
        else:
            self.fields['DocumentFiscalPeriodFocus'] = "Fiscal period focus not found"
        
        #DocumentType
        oNode = self.getNode("//dei:DocumentType[@contextRef]")
        if oNode is not None:
            self.fields['DocumentType'] = oNode.text
        else:
            self.fields['DocumentType'] = "Fiscal period focus not found"
        


    def GetCurrentPeriodAndContextInformation(self, EndDate):
        #Figures out the current period and contexts for the current period instance/duration contexts

        self.fields['BalanceSheetDate'] = "ERROR"
        self.fields['IncomeStatementPeriodYTD'] = "ERROR"
        
        self.fields['ContextForInstants'] = "ERROR"
        self.fields['ContextForDurations'] = "ERROR"

        #This finds the period end date for the database table, and instant date (for balance sheet):        
        UseContext = "ERROR"
        #EndDate = self.getNode("//dei:DocumentPeriodEndDate").text
        #This is the <instant> or the <endDate>
        
        #Uses the concept ASSETS to find the correct instance context
        #This finds the Context ID for that end date (has correct <instant> date plus has no dimensions):    
        oNodelist2 = self.getNodeList("//us-gaap:Assets | //us-gaap:AssetsCurrent | //us-gaap:LiabilitiesAndStockholdersEquity")
        #Nodelist of all the facts which are us-gaap:Assets
        for i in oNodelist2:
            #print i.XML
            
            ContextID = i.get('contextRef') 
            ContextPeriod = self.getNode("//xbrli:context[@id='" + ContextID + "']/xbrli:period/xbrli:instant").text
            print ContextPeriod
            
            #Nodelist of all the contexts of the fact us-gaap:Assets
            oNodelist3 = self.getNodeList("//xbrli:context[@id='" + ContextID + "']")
            for j in oNodelist3:
            
                #Nodes with the right period
                if self.getNode("xbrli:period/xbrli:instant",j) is not None and self.getNode("xbrli:period/xbrli:instant",j).text==EndDate:
                    
                    oNode4 = self.getNodeList("xbrli:entity/xbrli:segment/xbrldi:explicitMember",j)
                                        
                    if not len(oNode4):
                        UseContext = ContextID
                        print UseContext
                                                    
            
        """
        #NOTE: if the DocumentPeriodEndDate is incorrect, this attempts to fix it by looking for a few commonly occuring concepts for the current period...
        if UseContext=="ERROR":
            print 'if the DocumentPeriodEndDate is incorrect, this attempts to fix it by looking for a few commonly occuring concepts for the current period...'                    
            oNodelist_Error = self.getNode("//dei:DocumentPeriodEndDate | //us-gaap:OrganizationConsolidationAndPresentationOfFinancialStatementsDisclosureTextBlock | //us-gaap:SignificantAccountingPoliciesTextBlock")
            #print "Nodelist, trying to find alternative: " + oNodelist_Error.length
            
            ContextID = oNodelist_Error.get('contextRef')
            ContextPeriod = self.getNode("//xbrli:context[@id='" + ContextID + "']/xbrli:period/xbrli:endDate").text
            
            print "Found Alternative: " + ContextPeriod
            
            oNodelist3 = self.getNodeList("//xbrli:context[xbrli:period/xbrli:instant='" + ContextPeriod + "']")
            #print "Found alternative contexts:" + oNodelist3.length
            
            for j in oNodelist3:
                #print j.XML
                
                #Nodes with the right period
                if self.getNode("xbrli:period/xbrli:instant",j).text==ContextPeriod:
                    oNode4 = self.getNodeList("xbrli:entity/xbrli:segment/xbrldi:explicitMember",j)
                    #print "Found dimension: " + oNode4.XML
                    #WHATS GOING ON HERE                
                    
                    if len(oNode4):
                        #Not the right context
                        print "Note4: " + oNode4[0].text
                    else:
                        #print "SELECTED CONTEXT: " + oNodelist3.Item(j).selectSingleNode("./@id").text 'oNodelist3(j).XML
                        ContextID = j.get("id")
                        UseContext = ContextID
                        #print UseContext
                                        
                    #print j.XML
                                    
            #EndDate = ContextPeriod
            """           
        
       
        
        ContextForInstants = UseContext
        self.fields['ContextForInstants'] = ContextForInstants
        
        
        ###This finds the duration context
        ###This may work incorrectly for fiscal year ends because the dates cross calendar years
        #Get context ID of durations and the start date for the database table
        oNodelist2 = self.getNodeList("//us-gaap:CashAndCashEquivalentsPeriodIncreaseDecrease | //us-gaap:CashPeriodIncreaseDecrease | //us-gaap:NetIncomeLoss | //dei:DocumentPeriodEndDate")

        StartDate = "ERROR"
        StartDateYTD = "2099-01-01"
        UseContext = "ERROR"
        
        for i in oNodelist2:
            #print i.XML
            
            ContextID = i.get('contextRef')
            ContextPeriod = self.getNode("//xbrli:context[@id='" + ContextID + "']/xbrli:period/xbrli:endDate")
            #Usecontext = ContextID
            #print ContextPeriod
            
            #Nodelist of all the contexts of the fact us-gaap:Assets
            oNodelist3 = self.getNodeList("//xbrli:context[@id='" + ContextID + "']")
            for j in oNodelist3:
            
                #Nodes with the right period
                if self.getNode("xbrli:period/xbrli:endDate",j).text==EndDate:
                    
                    oNode4 = self.getNodeList("xbrli:entity/xbrli:segment/xbrldi:explicitMember",j)
                                        
                    if not len(oNode4): #Making sure there are no dimensions. Is this the right way to do it?
                    
                        #Get the year-to-date context, not the current period
                        StartDate = self.getNode("xbrli:period/xbrli:startDate",j).text
                        print "Context start date: " + StartDate
                        print "YTD start date: " + StartDateYTD
                        
                        if StartDate <= StartDateYTD:
                            #MsgBox "YTD is greater"
                            #Start date is for quarter
                            print "Context start date is less than current year to date, replace"
                            print "Context start date: " + StartDate
                            print "Current min: " + StartDateYTD
                            
                            StartDateYTD = StartDate
                            UseContext = j.get('id')
                            #MsgBox j.selectSingleNode("@id").text
                        else:
                            #MsgBox "Context is greater"
                            #Start date is for year
                            print "Context start date is greater than YTD, keep current YTD"
                            print "Context start date: " + StartDate
                            
                            StartDateYTD = StartDateYTD

                        
                        print "Use context ID: " + UseContext
                        print "Current min: " + StartDateYTD
                        print " "
                                        
                        print "Use context: " + UseContext
                            

        #Balance sheet date of current period
        self.fields['BalanceSheetDate'] = EndDate
        
        #MsgBox "Instant context is: " + ContextForInstants
        if ContextForInstants=="ERROR":
            #MsgBox "Looking for alternative instance context"
            
            ContextForInstants = self.LookForAlternativeInstanceContext()
            self.fields['ContextForInstants'] = ContextForInstants
        
        
        #Income statement date for current fiscal year, year to date
        self.fields['IncomeStatementPeriodYTD'] = StartDateYTD
        
        ContextForDurations = UseContext
        self.fields['ContextForDurations'] = ContextForDurations

        


    def LookForAlternativeInstanceContext(self):
        #This deals with the situation where no instance context has no dimensions
        #Finds something
            
        something = None
        
        #See if there are any nodes with the document period focus date
        oNodeList_Alt = self.getNodeList("//xbrli:context[xbrli:period/xbrli:instant='" + self.fields['BalanceSheetDate'] + "']")

        #MsgBox "Node list length: " + oNodeList_Alt.length
        for oNode_Alt in oNodeList_Alt:
            #Found possible contexts
            #MsgBox oNode_Alt.selectSingleNode("@id").text
            something = self.getNode("//us-gaap:Assets[@contextRef='" + oNode_Alt.get("id") + "']")
            if something:
                #MsgBox "Use this context: " + oNode_Alt.selectSingleNode("@id").text
                return oNode_Alt.get("id")
               
                    
        













