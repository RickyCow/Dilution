

def SIMBAD(vo):
    r = vo.regsearch(servicetype = 'tap', keywords = ['Simbad'])
    return r[0].service

def Vizier(vo):
    r = vo.regsearch(servicetype = 'tap', keywords = ['Vizier'])
    k = int(np.nonzero(['obstap' not in rr['ivoid'] for rr in r])[0]) 
    return r[k].service

def to_table(service, q):
    result = service.search(q).to_table()
    return result

def tables_simbad(service):
    tables_list = ["basic", "IDS", "IDENT", \
        "FLUX", "FILTER", "ALLFLUXES",\
        "OTYPES", "OTYPEDEF", "ALLTYPES", \
        "AUTHOR","REF", "KEYWORDS","BIBLIO", "HAS_REF", \
        "mesVar", "mesDistance", "mesDiameter", "mesPM", \
        "mesVelocities", "mesRot", "mesSPT", "mesPlx", "mesFe_H", \
        "meslUE", "mesHerschel", "mesXMM", "mesISO", \
        "H LINK"]
    return tables_list

class table_info():
    def __init__(self, service, table_name):
        self.service = service
        self.table_name = table_name
        
    def get_column_names(self):
        q = " SELECT TOP 0 * "\
                "FROM " + str(self.table_name) + ";"
        df = self.service.search(q).to_table()
        return df.colnames
        
    def get_unique_values(self, column_name):
        """
        Get distinct values from a column in a table.
        Input:
            service: pyvo.dal.tap.TAPService
            table_name: str
            column_name: str
        Output:
            list
        """
        q = " SELECT DISTINCT " + str(column_name) + " "\
            "FROM " + str(self.table_name) + ";"
        df = self.service.search(q).to_table()
        return df[column_name].tolist()