# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str)
    args = parser.parse_args()
    model = args.model

    perturbation_categories={}
    perturbation_categories["DB"]=["schema_synonym","schema_abbreviation","DBcontent_equivalence"]
    perturbation_categories["NLQ"]=["keyword_synonym","keyword_carrier","column_synonym","column_carrier","column_attribute", "column_value", "value_synonym", "multitype", "others"]
    perturbation_categories["SQL"]=["comparison","sort_order","NonDB_number","DB_text","DB_number"]

    pred_path = f"predictions/Spider-dev/{args.model}/pred.sql"
    qid_to_pred = []
    with open(pred_path, "r") as f:
        for i, line in enumerate(f.readlines()):
            qid_to_pred.append(line.strip())

    for category in perturbation_categories:
        for subcategory in perturbation_categories[category]:
            with open(f"data/{category + '_' + subcategory}/questions_pre_perturbation.json", "r") as f:
                pre_questions = json.load(f)
            if not os.path.exists(f"predictions/{category + '_' + subcategory}/{model}"):
                os.makedirs(f"predictions/{category + '_' + subcategory}/{model}")
            with open(f"predictions/{category + '_' + subcategory}/{model}/pred_pre_perturbation.sql", "w") as f:
                for q in pre_questions:
                    f.write(qid_to_pred[q["q_id_spider_dev"]] + "\n")
