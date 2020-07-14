## test file
"test.eval.csv" file includes English name, Chinese name of companies, and score of the translation in three dimensions evaluated by two annotators. 

This file is divided by comma and the comma is included in some companies' name are in quotation marks, so please use csv package read it directly.

### format 
> En_name,Zh_name,Fluency_z, Pronun_z, Meaning_z, Fluency_w, Pronun_w, Meaning_w

where "fluency", "pronun" and "meaning" are three dimension of evaluation. ".\*_z" and ".\*_w" mean *annotator Zhang* and *annotator Wei*.

### Kappa coefficient
The kappa coefficient in three dimensions are
>+ Fluency: 0.6826
>+ Pronunciation: 0.6205
>+ Meaning: 0.6465