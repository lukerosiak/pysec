This is Django code that compiles a list of all SEC filings from EDGAR into SQL, allows you to download them at will, and parses 50+ key accounting terms from XBRL filings. It is also a Python XBRL parser that allows you to easily extract arbitrary XBRL terms while it handles the contexts, etc. appropriately.

The XBRL parsing is translated from VB script written by Charles Hoffman, an accountant and XBRL expert, and reliably extracts more than 50 commonly used accounting terms.

To set up the index of all SEC filings:

Put this django app under manage.py and do your settings.py

In settings.py, modify DATA_DIR = '/you/directory/to/download/files/to' and set your database

python manage.py syncdb

python manage.py sec_import_index

This creates the Index() model. To download any filing, call .download() on that model instance. To get its XBRL attributes if it's an XBRL filing, call .xbrl() on it and look at the .fields attribute of the returned model.


Or if you just want to use the Python XBRL parser on a .xml file:

import xbrl

x = xbrl.XBRL(PATH TO LOCAL XML 10-K FILING)

print x.fields #a dict of the most important values

To get any XBRL term:

x.GetFactValue(XMBL TAG, "Duration" or "Instant" (depending on if it's a year-long or snapshot value))


For more basic usage, see example.py

For an example of generating a CSV of a list of companies, see management/commands/xbrl_to_csv.py

By Luke Rosiak
Released under the GNU




