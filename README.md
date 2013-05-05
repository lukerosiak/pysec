This is the in-progress code to parse key accounting concepts from XBRL documents, coupled with a tool that downloads the index of filings from the SEC's EDGAR, puts them into SQL, and downloads specified filings. 


The XBRL parsing is translated from VB script written by Charles Hoffman, an accountant and XBRL expert, and reliably extracts more than 50 commonly used accounting terms.

just:

import xbrl
x = xbrl.XBRL(PATH TO LOCAL XML 10-K FILING)
print x.fields #a dict of the most important values

To get any XBRL term:

x.GetFactValue(XMBL TAG, "Duration" or "Instant" (depending on if it's a year-long or snapshot value))

To set up the index of all SEC filings:

python manage.py syncdb
python manage.py sec_import_index

This creates the Index() model. To download any filing, call .download() on that model instance. To get its XBRL attributes if it's an XBRL filing, call .xbrl() on it and look at the .fields attribute of the returned model.



By Luke Rosiak
Released under the GNU
