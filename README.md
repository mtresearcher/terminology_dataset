TERMINOLGOY DATA SET
====================

We are releasing the data set used in the ACL paper

[Training Neural Machine Translation To Apply Terminology Constraints](https://www.aclweb.org/anthology/P19-1294/). Georgiana Dinu, Prashant Mathur, Marcello Federico and Yaser Al-Onaizan. ACL 2019 (Short).

The folder contain 4 files in two folders and a script with a README.  
The terminology files from IATE and Wiktionary data are in the form: {wikt,iate}.{NUM}.terminology.tsv where NUM represents the number of sentences. 

Files containing 414 and 727 lines are the ones with perfect match on the target side. (Results in Table 2)
Files containing 581 and 975 lines are the ones with approximate match on the target side. (Results in Table 4)

For example, terminology file `iate.414.terminology.tsv' contain 2N+2 columns where N is the number of terminology matches in a sentence.

```
0	21      interview       Interview
1	51      prize   Preisgeld
2	77      China   China 
3	80      trade   Handel
4	86      side    Seite
5	87      budgetary       Haushaltsdefizit
6	88      side    Seite   solution        Lösung
7	113     forced prostitution     Zwangsprostitution
```

The first column is the sentence ID from the WMT 17 test set (containing 3000 lines) which can be downloaded from WMT 2017 website [1].
Each terminology match is represented in three columns: Source, Target and Target (BPE). You can ignore the third column of every terminology. 

To get the news test 2017 with the terminology, run the following:

```
wget http://data.statmt.org/wmt17/translation-task/test.tgz && tar -xvf && cd test/
cat newstest2017-ende-src.en.sgm | grep "seg id" | perl -pe "s/<seg id=\"[0-9]*\">//g" | perl -pe "s/<\/seg>//g" > newstest2017.en
cat newstest2017-ende-ref.de.sgm | grep "seg id" | perl -pe "s/<seg id=\"[0-9]*\">//g" | perl -pe "s/<\/seg>//g" > newstest2017.de

for term_file in iate/iate.{414,581}.terminology.tsv
do
python print_lines.py -l=<(cut -f2 ${term_file}) < newstest2017.en > newstest2017-${term_file}.en
python print_lines.py -l=<(cut -f2 ${term_file}) < newstest2017.de > newstest2017-${term_file}.de
done

for term_file in wiktionary/wikt.{727,975}.terminology.tsv
do
python print_lines.py -l=<(cut -f2 ${term_file}) < newstest2017.en > newstest2017-${term_file}.en
python print_lines.py -l=<(cut -f2 ${term_file}) < newstest2017.de > newstest2017-${term_file}.de
done
```

Licences
--------

Wiktionary is provided under CC-BY-SA 3.0 License. No copyright on IATE terminology. The script is released under Apache 2.0. 


[1] http://data.statmt.org/wmt17/translation-task/test.tgz
