

def SIMBAD(vo):
    r = vo.regsearch(servicetype = 'tap', keywords = ['Simbad'])
    return r[0].service

def Vizier(vo):
    r = vo.regsearch(servicetype = 'tap', keywords = ['Vizier'])
    k = int(np.nonzero(['obstap' not in rr['ivoid'] for rr in r])[0]) 
    return r[k].service

def get_column_names(service, table_name):
    q = " SELECT TOP 0 * "\
        "FROM " + str(table_name) + ";"
    df = service.search(q).to_table()
    return df.colnames