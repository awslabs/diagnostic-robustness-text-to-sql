# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import shutil

def main():
    perturbation_categories={}
    perturbation_categories["DB"]=["schema_synonym","schema_abbreviation","DBcontent_equivalence"]
    perturbation_categories["NLQ"]=["keyword_synonym","keyword_carrier","column_synonym","column_carrier","column_attribute", "column_value", "value_synonym", "multitype", "others"]
    perturbation_categories["SQL"]=["comparison","sort_order","NonDB_number","DB_text","DB_number"]

    for category in perturbation_categories:
        for subcategory in perturbation_categories[category]:
            if category == "DB":
                shutil.copy(f"data/Spider-dev/tables.json", f"data/{category+'_'+subcategory}/tables_pre_perturbation.json")
                shutil.copytree(f"data/Spider-dev/databases", f"data/{category+'_'+subcategory}/databases_pre_perturbation")
            else:
                shutil.copy(f"data/Spider-dev/tables.json", f"data/{category+'_'+subcategory}/tables.json")
                shutil.copytree(f"data/Spider-dev/databases", f"data/{category+'_'+subcategory}/databases")

if __name__ == "__main__":
    main()