course_college_map = {
    "CHS": ["BDS", "BDT", "BEH", "BLT", "BMR", "BOS", "BPT", "BYT", "MAM", "MLT", "NUR", "PHA", "BSL", 'SSM'],
    "LAW": ["LLB"], # Added LLB based on the initial dataset you provided
    "CEES": ["BEC", "BYW", "EDA", "EDB", "EDP", "EEC", 'SPS'],
    "COVAB": ["BJA", "BLB", "SCB", "SCP", "SCX", "VET"],
    "COBAMS": ["ACC", "ADA", "ADJ", "ADM", "AML", "BBA", "BBC", "BBD", "BBE", "BBJ", "BHE", "BHJ", "BHM", "BIB", "BIM", "BJB", "BJJ", "BJO", "BJS", "BKE", "BLC", "BLM", "BMA", "BML", "BMM", "BMS", "BNE", "BNM", "BOM", "BPL", "BQE", "BRJ", "BRM", "BRO", "BSA", "BSF", "BSU", "BTB", "BTH", "BTT", "CEA", "CMM", "COB", "COE", "COM", "CRJ", "CRO", "ECE", "ECN", "ECO", "HMA", "HML", "HNM", "HOM", "HSJ", "HSO", "JAA", "JBE", "JOA", "MTM", "PMA", "PML", "PMM", "PNM", "PSC", "PSM", "PSU", "SEC", "TLM", "TTM", "BPS", "BST", "BUS", "SAS", "STA"],
    "CoNAS": ["BBI", "BBP", "BBT", "BCB", "BIC", "SPS"],
    "COCIS": ["BIA", "BSI", "BSJ", "BSW", "CSC", "CSE", "CSJ", "IST", "JCA", "SSE"],
    "CAES": ["AGE", "AGM", "AGR", "BAI", "BEV", "BFS", "BGS", "BHD", "BIX", "BOF", "BUP", "BWE", "FST"],
    "CEDAT": ["ARC", "BFA", "BID", "BVC", "BVL", "CCE", "CIV", "ELE", "LSG", "MEC", "BPG", "SQS"],
    "CHUSS": ["APS", "APY", "ARS", "ASE", "ASS", "BAC", "BAP", "BCE", "BEN", "BEY", "BJC", "BJE", "BLE", "BLG", "DPA", "LGM", "LIS", "MUS"],
}

course_college_map = {
    "CHS": ["BDS", "BDT", "BEH", "BLT", "BMR", "BOS", "BPT", "BYT", "MAM", "MLT", "NUR", "PHA", "BSL", 'SSM'],
    "LAW": ["LLB"], # Added LLB based on the initial dataset you provided
    "CEES": ["BEC", "BYW", "EDA", "EDB", "EDP", "EEC", 'SPS'],
    "COVAB": ["BJA", "BLB", "SCB", "SCP", "SCX", "VET"],
    "COBAMS": ["ACC", "ADA", "ADJ", "ADM", "AML", "BBA", "BBC", "BBD", "BBE", "BBJ", "BHE", "BHJ", "BHM", "BIB", "BIM", "BJB", "BJJ", "BJO", "BJS", "BKE", "BLC", "BLM", "BMA", "BML", "BMM", "BMS", "BNE", "BNM", "BOM", "BPL", "BQE", "BRJ", "BRM", "BRO", "BSA", "BSF", "BSU", "BTB", "BTH", "BTT", "CEA", "CMM", "COB", "COE", "COM", "CRJ", "CRO", "ECE", "ECN", "ECO", "HMA", "HML", "HNM", "HOM", "HSJ", "HSO", "JAA", "JBE", "JOA", "MTM", "PMA", "PML", "PMM", "PNM", "PSC", "PSM", "PSU", "SEC", "TLM", "TTM", "BPS", "BST", "BUS", "SAS", "STA"],
    "CoNAS": ["BBI", "BBP", "BBT", "BCB", "BIC", "SPS"],
    "COCIS": ["BIA", "BSI", "BSJ", "BSW", "CSC", "CSE", "CSJ", "IST", "JCA", "SSE"],
    "CAES": ["AGE", "AGM", "AGR", "BAI", "BEV", "BFS", "BGS", "BHD", "BIX", "BOF", "BUP", "BWE", "FST"],
    "CEDAT": ["ARC", "BFA", "BID", "BVC", "BVL", "CCE", "CIV", "ELE", "LSG", "MEC", "BPG", "SQS"],
    "CHUSS": ["APS", "APY", "ARS", "ASE", "ASS", "BAC", "BAP", "BCE", "BEN", "BEY", "BJC", "BJE", "BLE", "BLG", "DPA", "LGM", "LIS", "MUS"],
}



fdsasdfghj

fdsasdfghj

fdsasdfghj


# Define district clusters and regions
cluster_map = {
    "URBAN-CITY": [
        "KAMPALA", 
        "MBARARA", 
        "JINJA", 
        "GULU", 
        "ARUA", 
        "LIRA", 
        "MASAKA", 
        "MBALE", 
        "WAKISO", 
        "HOIMA"
    ],
    "SEMI-URBAN": [
        "BUSHENYI", "IBANDA", "IGANGA", "KASESE", "KIBOGA",
        "KYOTERA", "KIRYANDONGO", "KITGUM", "KAMULI",
        "KAMWENGE", "KAYUNGA", "MASINDI", "MPIGI", "MUKONO",
        "MITYANA", "NEBBI", "NTUNGAMO", "PALLISA", "RUKUNGIRI",
        "SOROTI", "TORORO"
    ],
    "RURAL-AGRICULTURAL": [
        "ADJUMANI", "AGAGO", "ALEBTONG", "AMOLATAR", "AMURIA",
        "AMURU", "APAC", "BUDAKA", "BUDUDA", "BUGIRI", "BUGWERI",
        "BUHWEJU", "BUIKWE", "BUKEDEA", "BUKOMANSIMBI", "BULAMBULI",
        "BULIISA", "BUNDIBUGYO", "BUNYANGABU", "BUTALEJA",
        "BUTAMBALA", "BUTEMBO", "BUYENDE", "DOKOLO", "GOMBA",
        "ISINGIRO", "KABERAMAIDO", "KALIRO", "KALUNGU",
        "KANUNGU", "KATAKWI", "KAZO", "KIBAALE", "KIBUKU",
        "KIKUUBE", "KIRUHURA", "KISORO", "KOBOKO", "KOLE",
        "KUMI", "KYANKWANZI", "KYEGEGWA", "KYENJOJO", "LAMWO",
        "LUUKA", "LUWEERO", "LWENGO", "MANAFWA", "MARACHA",
        "MAYUGE", "MITOOMA", "MOROTO", "MOYO", "MUBENDE",
        "NAKASEKE", "NAKASONGOLA", "NAMAYINGO", "NAMISINDWA",
        "NAMUTUMBA", "NGORA", "OBONGI", "OMORO", "OTUKE",
        "OYAM", "PAKWACH", "RAKAI", "RUBANDA", "RUBIRIZI",
        "RUKIGA", "SEMBABULE", "SERERE", "SHEEMA", "SIRONKO",
        "YUMBE", "ZOMBO"
    ],
    "REMOTE-UNDERDEVELOPED": [
        "ABIM", "AMUDAT", "BUVUMA", "BUKWO", "KAABONG", "KAPELABYONG",
        "KALANGALA", "KOTIDO", "KWEEN", "MADIOKOLLO", "NAPAK",
        "NAKAPIRIPIRIT", "NABILATUK", "NTOROKO", "TEREGO", 
        "KARENGA", "NON UGANDAN"
    ]
}


region_map = {
    "CENTRAL": [
        "BUIKWE", "BUKOMANSIMBI", "BUTAMBALA", "BUVUMA", "GOMBA", 
        "KALANGALA", "KALUNGU", "KAMPALA", "KAYUNGA", "KIBOGA", 
        "KYANKWANZI", "LUWEERO", "LWENGO", "LYANTONDE", "MASAKA", 
        "MITYANA", "MPIGI", "MUBENDE", "MUKONO", "NAKASEKE", 
        "NAKASONGOLA", "RAKAI", "SEMBABULE", "WAKISO", "KYOTERA", 
        "KASSANDA"
    ],
    "EASTERN": [
        "AMURIA", "BUDAKA", "BUDUDA", "BUGIRI", "BUKEDEA", 
        "BULAMBULI", "BUSIA", "BUTALEJA", "BUTEBO", "BUYENDE", 
        "IGANGA", "JINJA", "KALIRO", "KAMULI", "KAPCHORWA", 
        "KATAKWI", "KUMI", "KABERAMAIDO", "MANAFWA", "MAYUGE", 
        "MBALE", "NAMAYINGO", "NAMUTUMBA", "NGORA", "PALLISA", 
        "SERERE", "SIRONKO", "SOROTI", "TORORO", "NAMISINDWA", 
        "BUKWO", "KIBUKU", "LUUKA"
    ],
    "NORTHERN": [
        "ABIM", "ADJUMANI", "AGAGO", "ALEBTONG", "AMOLATAR", 
        "AMUDAT", "AMURU", "APAC", "ARUA", "DOKOLO", "GULU", 
        "KAABONG", "KITGUM", "KOBOKO", "KOLE", "KOTIDO", 
        "KWANIA", "KWEEN", "LIRA", "MADI OKOLLO", "MARACHA", 
        "MOROTO", "MOYO", "NABILATUK", "NAKAPIRIPIRIT", "NAPAK", 
        "NEBBI", "NWOYA", "NTOROKO", "OBONGI", "OMORO", 
        "OTUKE", "OYAM", "PADER", "PAKWACH", "YUMBE", "ZOMBO"
    ],
    "WESTERN": [
        "BUHWEJU", "BULIISA", "BUNDIBUGYO", "BUNYANGABU", "BUSHENYI", 
        "HOIMA", "IBANDA", "ISINGIRO", "KABALE", "KABAROLE", 
        "KAGADI", "KAKUMIRO", "KAKUMILO", "KAMWENGE", "KANUNGU", 
        "KASESE", "KIBAALE", "KIRUHURA", "KIRYANDONGO", "KISORO", 
        "KYEGEGWA", "KYENJOJO", "LAMWO", "MASINDI", "MBARARA", 
        "MITOOMA", "NTUNGAMO", "RUBANDA", "RUBIRIZI", "RUKIGA", 
        "RUKUNGIRI", "SHEEMA"
    ]
}



def classify_cluster(district):
    for cluster, districts in cluster_map.items():
        if district in districts:
            return cluster
    return "OTHER"

def classify_region(district):
    for region, districts in region_map.items():
        if district in districts:
            return region
    return "UNKNOWN"

# Apply mappings
df['cluster'] = df['dname'].apply(classify_cluster)
df['region'] = df['dname'].apply(classify_region)

df[['dname', 'cluster', 'region']].drop_duplicates().head(10)
