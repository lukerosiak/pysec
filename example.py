from pysec.models import *

"""get a file from the index. it may or may not be present on our hard disk. if it's not, it will be downloaded
the first time we try to access it, or you can call .download() explicitly"""
filing = Index.objects.filter(form='10-K',cik=1090872).order_by('-date')[0]

print filing.name

"""initialize XBRL parser and populate an attribute called fields with a dict of 50 common terms"""
x = latest.xbrl()

print x.fields['FiscalYear']

print x.fields

"""fetch arbitrary XBRL tags representing eiter an Instant or a Duration in time"""
print 'Tax rate', x.GetFactValue('us-gaap:EffectiveIncomeTaxRateContinuingOperations','Duration')

if x.loadYear(1): 
    """Most 10-Ks have two or three previous years contained in them for the major values. This call switches the contexts
    to the prior year (set it to 2 or 3 instead of 1 to go back further) and reloads the fundamental concepts.
    Any calls to GetFactValue will use that year's value from that point on."""
                    
    print x.fields['FiscalYear']

    print x.fields

    print 'Tax rate', x.GetFactValue('us-gaap:EffectiveIncomeTaxRateContinuingOperations','Duration')
            

