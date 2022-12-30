# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:29:46 2022

@author: LPD-GS-User
"""

from huggingface_hub import hf_hub_download
from transformers import AutoConfig, AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import pandas as pd
import numpy as np
# hf_hub_download(repo_id="deepset/tinyroberta-squad2", filename="config.json", cache_dir= r"C:\Users\LPD-GS-User\Documents\Text_Recognition\tiny_roberta")
config = AutoConfig.from_pretrained("C:\\Users\\LPD-GS-User\\Documents\\Text_Recognition\\tiny_roberta\\models--deepset--tinyroberta-squad2\\snapshots\\20891f44e15bf4a3caf0429fd9319f2632839125\\config.json")

# load model
model_name = "deepset/tinyroberta-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# load first pass csv
pass_one_csv = pd.read_csv(r'C:\Users\LPD-GS-User\Documents\Text_Recognition\DPDC\Data\DMS\pdf_extraction_pass_one.csv')

conditions = pass_one_csv.Condition.to_list()

gpr  = []
commencement = []
expiry = []
gfa = []


questions_list = ['What is the gross plot ratio?', 'What is the commencement date?', 'What is the expiry date?', 'What is the gross floor area?']


nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

def QnA(questions_list = questions_list, gpr = gpr, commencement = commencement, expiry = expiry, gfa = gfa, conditions = conditions):
    
    for c in conditions:
        answers = []
        try:
            np.isnan(c)
            for i in range(4): answers.append(np.nan)
        except:
            for q in questions_list:
                QA_input = {
                    'question': q,
                    'context': c
                    }
                res = nlp(QA_input)
                res_df = pd.DataFrame.from_dict(data = res, orient = 'index').reset_index()
                if float(res_df.iloc[0,1]) < 0.2:
                    answer = ''
                else:
                    answer = res_df.iloc[3,1]
                answers.append(answer)
        gpr.append(answers[0])
        commencement.append(answers[1])
        expiry.append(answers[2])
        gfa.append(answers[3])

    return gpr, commencement, expiry, gfa
        
gpr, commencement, expiry, gfa = QnA()    

supp_df = {'GPR': gpr, 'GFA': gfa, 'Commencement Date': commencement, 'Expiry Date': expiry}
supp_df = pd.DataFrame(supp_df)

pass_one_csv_enhanced = pass_one_csv.reset_index(drop = True).join(supp_df.reset_index(drop = True))
pass_one_csv_enhanced.to_csv(r'C:\Users\LPD-GS-User\Documents\Text_Recognition\DPDC\Data\DMS\pdf_extraction_pass_one_enhanced.csv', index=False)
