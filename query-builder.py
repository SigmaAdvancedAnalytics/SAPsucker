from pyrfc import Connection
import os
import re

class main():
    def __init__(self):
        ASHOST=os.getenv('AHOST')
        CLIENT=os.getenv('CLIENT')
        SYSNR=os.getenv('SYSNR')
        USER=os.getenv('USER')
        PASSWD=os.getenv('PASSWD')
        self.conn = Connection(ashost=ASHOST, sysnr=SYSNR, client=CLIENT, user=USER, passwd=PASSWD)


    def qry(self, Fields, SQLTable, Where = '', MaxRows=50, FromRow=0):
        """A function to query SAP with RFC_READ_TABLE"""

        # By default, if you send a blank value for fields, you get all of them
        # Therefore, we add a select all option, to better mimic SQL.
        if Fields[0] == '*':
            Fields = ''
        else:
            Fields = [{'FIELDNAME':x} for x in Fields] # Notice the format

        # the WHERE part of the query is called "options"
        options = [{'TEXT': x} for x in Where] # again, notice the format

        # we set a maximum number of rows to return, because it's easy to do and
        # greatly speeds up testing queries.
        rowcount = MaxRows

        # Here is the call to SAP's RFC_READ_TABLE
        tables = self.conn.call("RFC_READ_TABLE", QUERY_TABLE=SQLTable, DELIMITER='|', FIELDS = Fields, \
                                OPTIONS=options, ROWCOUNT = MaxRows, ROWSKIPS=FromRow)

        # We split out fields and fields_name to hold the data and the column names
        fields = []
        fields_name = []

        data_fields = tables["DATA"] # pull the data part of the result set
        data_names = tables["FIELDS"] # pull the field name part of the result set

        headers = [x['FIELDNAME'] for x in data_names] # headers extraction
        long_fields = len(data_fields) # data extraction
        long_names = len(data_names) # full headers extraction if you want it

        # now parse the data fields into a list
        for line in range(0, long_fields):
            fields.append(data_fields[line]["WA"].strip())

        # for each line, split the list by the '|' separator
        fields = [x.strip().split('|') for x in fields ]

        # return the 2D list and the headers
        return fields, headers
    
    
    def split_where(self, seg):
        # This magical function splits by spaces when not enclosed in quotes..
        where = seg.split(' ')
        where = [x.replace('@', ' ') for x in where]
        return where

    
    def select_parse(self, statement):
        statement = " ".join([x.strip('\t') for x in statement.upper().split('\n')])

        if 'WHERE' not in statement:
            statement = statement + ' WHERE '

        regex = re.compile("SELECT(.*)FROM(.*)WHERE(.*)")

        parts = regex.findall(statement)
        parts = parts[0]
        select = [x.strip() for x in parts[0].split(',')]
        frm = parts[1].strip()
        where = parts[2].strip()

        # splits by spaces but ignores quoted string with ''
        PATTERN = re.compile(r"""((?:[^ '"]|'[^']*'|"[^"]*")+)""")
        where = PATTERN.split(where)[1::2]

        cleaned = [select, frm, where]
        return cleaned

    
    def SQL_parser(self, statement, MaxRows=0, FromRow=0, to_dict=False):
        statement = self.select_parse(statement)

        results = self.qry(statement[0], statement[1], statement[2], MaxRows, FromRow)
        if to_dict:
            headers = statement[0]
            results2 = []
            for line in results:
                new_line = OrderedDict()
                header_counter = 0
                for field in line:
                    try:
                        new_line[headers[header_counter]] = field.strip()
                        header_counter += 1
                    except Exception as e:
                        new_line[headers[header_counter-1]] = new_line[headers[header_counter-1]]+ " " + " ".join(line[header_counter:])
                        break

                results2.append(new_line)
            results = results2
        return results


# Init the class and connect
s = main() 

# Enter the SQL query
query = "select MANDT, BUKRS, BUTXT from T001 where BUKRS <> 0"
maxrows = 10
fromrow = 0

results, headers = s.sql_query(query, maxrows, fromrow)

print "Download Complete: \n"
print headers
print results
