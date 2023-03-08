"""
This module contains utility functions for working with column names in dataframes.
"""

from difflib import SequenceMatcher

def get_standard_names(target_name, logger):
    print(type(target_name))
    print(type(logger))
    """
        This function will return the other standard names of the target name
    Args:
        target_name: The original name of the target column (String)
        logger: Logger object to log exceptions (Logger)
    Returns:
        list: List of all other standard names of the target name. (List)
    """
    name_dict = {
        "clarity": ["clarity", "purity", "Clar", "Clearity"],
        "color": ["color", "colour", "Colr", "col"],
        "shape": ["shape", "shp"],
        "carat": [
            "Carat",
            "CaratSize",
            "CaratWeight",
            "Ct",
            "CtSize",
            "CtWeight",
            "Weight",
            "Sz",
            "cts",
            "crtwt",
            "size",
        ],
        "fluorescent": [
            "fluor",
            "flour",
            "fluorescent",
            "Flr",
            "FlrIntensity",
            "Fluo Intensity",
            "Fluor Intensity",
            "Fluorescence",
            "Fluorescence Intensity",
            "FluorescenceIntensity",
            "FluorIntensity",
        ],
        "raprate": ["Rap", "Rapprice"],
        "length": ["M1", "Measurement", "Diameter", "length"],
        "width": ["M2", "Measurement", "Diameter", "width"],
        "depth": ["M3", "Measure", "Diameter", "depth", "height"],
        "cut": ["Cut", "CutGrade"],
        "polish": ["Finish", "Pol", "polish"],
        "symmetry": ["Sym", "Symetry", "Sym-metry", "symmetry"],
        "table": [
            "Table",
            "Table Percent",
            "TablePct",
            "TablePercent",
            "Tbl",
            "Table%",
            "Table Depth",
        ],
        "comments": [
            "Comments",
            "Remark",
            "Lab comment",
            "Cert comment",
            "Certificate comment",
            "Laboratory comment",
            "Report Comments",
        ],
        "price per carat": [
            "PerCarat",
            "PerCt",
            "Prc",
            "PriceCarat",
            "PriceCt",
            "PricePerCarat",
            "PricePerCt",
            "Px",
            "price/carat",
        ],
        "discount": [
            "disc",
            "disc%",
            "RapNet Discount %",
            "PctRapNetDiscount",
            "Rap netDisc",
            "RapnetDiscount",
            "RapnetDiscountPct",
            "RapnetDiscountPercent",
            "RapnetDiscPct",
            "RapnetDpx",
            "RapnetRapPct",
            "RDisc",
            "RDiscount",
            "RDiscountPct",
            "RDiscountPercent",
            "RDiscPct",
            "RDpx",
            "RRapPct",
            "RapNet Discount Price",
            "per",
        ],
        "total": ["amount", "total", "total price"],
        "rap price total": ["rap total", "rap value"],
        "Stock Ref": [
            "ReferenceNum",
            "ReferenceNumber",
            "Stock",
            "Stock Num",
            "Stock_no",
            "StockNo",
            "StockNum",
            "StockNumber",
            "VenderStockNumber",
            "Refno",
            "Packet No",
        ],
        "report_no": [
            "REPORTNO",
            "REPORT NO",
            "REP NO",
            "REPORT #",
            "CERT#",
            "CERTIFICATE",
            "CERTIFICATE NO",
            "CERTIFICATE #",
            "CERTI NO.",
            "REPORT",
            "CERT #",
            "CERT NO.",
            "CERTNO",
            "CERT. NO",
            "GIA OR FM",
            "REP_NO",
            "CERT_NO",
            "CERT.NO",
            "VIEW CERTIFICATE",
            "CERT NO",
            "CERTINO",
        ],
    }

    standard_names = name_dict.get(target_name)

    if standard_names is None:
        logger.exception(
            "The function could not find other satndard names for this target name"
        )
    return standard_names

def string_similarity(str1, str2):
    """
    This function computes the similarity between two strings using difflib library.

    Args:
        str1 (str): The first string. (String)
        str2 (str): The second string. (String)

    Returns:
        float: The similarity score between 0 and 1.
    """
    seq_matcher = SequenceMatcher(None, str1, str2)
    return seq_matcher.ratio()

def similarity_score_from_col_name(column_name, std_names):
    """
    This function calculates the similarity score between a given column and each 
    stanadard target column names.
    Example: column_name = "Clarity"
             std_names = ["clarity", "purity", "Clar", "Clearity"]
             Output: "1"
    Args:
        column_name: The column name (String)
        std_names: The list of standard names of the target column (List)

    Returns:
        str: The similarity score of the column and a target column (String)
    """
    # if column name matches one of the standard name then we return similarity score as 1
    if column_name.lower() in std_names:
        return 1

    # We calculate the string similarity of column name with standard names and return
    # only the highest similarity
    probs = [string_similarity(column_name, name) for name in std_names]
    return round(max(probs), 3)
    