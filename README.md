# README.md

## Introduction
The Coptic language, rooted in the historical landscapes of Egypt, continues to serve as a vital liturgical medium for the Coptic Orthodox and Catholic Churches across Egypt, North Sudan, Libya, and the United States, with approximately ten million speakers worldwide. However, the scarcity of digital resources in Coptic has resulted in its exclusion from digital systems, thereby limiting its accessibility and preservation in modern technological contexts. Our research addresses this issue by developing the most extensive parallel Coptic-centered corpus to date. This corpus comprises about 8,000 parallel sentences between Arabic and Coptic, and more than 24,000 parallel sentences between English and Coptic. We have also developed the first neural machine translation system between Coptic, English, and Arabic. Lastly, we evaluate the capability of leading proprietary Large Language Models (LLMs) to translate to and from Coptic using a few-shot learning approach (in-context learning).

## Coptic-Arabic Dataset

### Dataset Creation

To create the Coptic-Arabic dataset, we have included several scripts to facilitate data collection, preprocessing, and cleaning. Below are the instructions to run these scripts.

1. **Data Collection Script**: Collects raw data from various sources.
    ```bash
    python3 /path/to/copticmt/CoPARA/scripts/python/CreateParallelFirstscript.py
    ```
2. **Data Preprocessing Script**: 
    - Then we need to remove the diacritics from the Arabic
    ```bash
    python3 /path/to/copticmt/CoPARA/scripts/python/diacritics.py
    ```

### Dataset Split

The dataset is split into training, validation, and test sets as follows:

- Training Set: 80%
- Validation Set: 10%
- Test Set: 10%

3. **Split the data into three parallel files (train, dev, test)**
    ```bash
    python3 /path/to/copticmt/CoPARA/scripts/python/1_DataSplit.py
    ```

4. **Create TSV file for the mT5 model**
    ```bash
    python3 /path/to/copticmt/CoPARA/scripts/python/2_textToTsv.py
    ```

### Coptic-Arabic Parallel Sentences

Below is a table showing sample parallel sentences from the Coptic-Arabic dataset:

| Coptic Sentence                  | Arabic Sentence                              |
|----------------------------------|----------------------------------------------|
| ⲫⲁⲓ ⲉⲧⲁϥⲧⲁⲙⲟⲛ ⲉⲧⲉⲧⲉⲛⲁⲅⲁⲡⲏ ϧⲉⲛ ⲡⲓⲡⲛⲁ̅ | وَهُوَ نَفْسُهُ أَخْبَرَنَا بِمَا لَكُمْ مِنَ الْمَحَبَّةِ فِي الرُّوحِ. |
| ⲉϯ ⲛⲟⲩⲉⲙⲓ ⲛⲧⲉ ⲫⲛⲟϩⲉⲙ ⲙⲡⲉϥⲗⲁⲟⲥ ϧⲉⲛ ⲟⲩⲭⲱ ⲉⲃⲟⲗ ⲛⲧⲉ ϩⲁⲛⲛⲟⲃⲓ. | لِتُعْطِيَ شَعْبَهُ الْمَعْرِفَةَ بِأَنَّ الْخَلاَصَ هُوَ بِمَغْفِرَةِ خَطَايَاهُمْ |
| ϧⲉⲛ ⲟⲩⲙⲉⲣⲟⲥ ⲅⲁⲣ ⲧⲉⲛⲉⲙⲓ ⲟⲩⲟϩ ϧⲉⲛ ⲟⲩⲙⲉⲣⲟⲥ ⲧⲉⲛⲉⲣⲡⲣⲟⲫⲏⲧⲉⲩⲓⲛ. | فَإِنَّ مَعْرِفَتَنَا جُزْئِيَّةٌ وَنُبُوءَتَنَا جُزْئِيَّةٌ. |
| ⲫϯ ⲇⲉ ⲁϥⲧⲟⲩⲛⲟⲥϥ ⲉⲃⲟⲗϧⲉⲛ ⲛⲏⲉⲑⲙⲱⲟⲩⲧ | وَلَكِنَّ اللهَ أَقَامَهُ مِنْ بَيْنِ الأَمْوَاتِ، |

## Coptic-English Dataset

### Dataset Creation

To create the Coptic-English dataset, similar scripts as the Coptic-Arabic dataset are used with different source URLs and preprocessing steps specific to English data.

### Dataset Split

The dataset is split into training, validation, and test sets as follows:

- Training Set: 80%
- Validation Set: 10%
- Test Set: 10%

### Coptic-English Parallel Sentences

Below is a table showing sample parallel sentences from the Coptic-English dataset:

| Coptic Sentence                  | English Sentence                             |
|----------------------------------|----------------------------------------------|
| ⲛⲁⲓ ⲉⲧϥϩⲱⲛ ⲙⲡⲁⲓⲧⲉⲓ ⲙⲙⲟⲛ ⲙⲙⲟⲟⲩ ⁛—   | those whom He hath....................       |
| ⲉⲓϣⲁϫⲉ ⲉⲙⲙⲛⲧⲣϥϣⲡϩⲙⲟⲧ ·             | I mean that not all have given thanks.      |
| ⲛⲉⲧϩⲏϣ ⲛϥⲃⲟⲏⲑⲉⲓ ⲉⲣⲟⲟⲩ            | Those who were in distress, he relieved.    |
| ⲛⲉⲩⲛⲧⲁϥ ⲟⲩⲥϩⲓⲙⲉ ⲇⲉ ⲙⲙⲁⲩ ⲛⲧⲟⲥ ϩⲱⲱⲥ ⲟⲛ ⲛⲉⲥϣⲙϣⲉ ⲉⲓⲇⲱⲗⲟⲛ ⲡⲉ · | And he had a wife who was herself a worshipper of idols, |

## Neural Machine Translation System

We have developed the first neural machine translation (NMT) system for Coptic, English, and Arabic. Our NMT system is utilizing various tools including our baseline training Seq2Seq transformers model on word level tokenization, then BPE tokenization for the Seq2Seq Transformer model, as well as we have fine-tuned M2M100 translation model on the Coptic-Arabic and Coptic-English as well as using the mT5.

The next machine translation model we have used is via zero-shot and few-shot in which we have used various sets of LLMs such as (LLaMA3 7B, 70B, Gemini, Claude v1.3)

### Bash Scripts for Training NMT Models

#### Seq2Seq Transformer Model 

#####  Arabic-Coptic WordBased
```bash
bash PATH TO/copticmt/scripts/training/BPE/preprocess.sh
bash PATH TO/copticmt/scripts/training/BPE/train.sh
bash PATH TO/copticmt/scripts/training/BPE/generate.sh
```
##### Arabic-Coptic BPE
```bash
#!/bin/bash
# Train Seq2Seq Transformer model
bash PATH TO/copticmt/scripts/training/BPE/CopticArabic/preprocess.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticArabic/trainArabCop.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticArabic/trainCoArab.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticArabic/generateArabictoCoptic.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticArabic/generatecopticToArabicBpe.sh
```

##### English-Coptic BPE
```bash
#!/bin/bash
# Train Seq2Seq Transformer model
bash PATH TO/copticmt/scripts/training/BPE/CopticEnglish/preprocess.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticEnglish/trainCopEn.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticEnglish/trainEnCop.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticEnglish/generateCopticToEnglishBpe.sh
bash PATH TO/copticmt/scripts/training/BPE/CopticEnglish/generateEnglishToCopticBPE.sh
```

#### M2M100 finetuning

##### Arabic-Coptic
```bash
#!/bin/bash
# Train M2M100 Transformer model

```

##### English-Coptic
```bash
#!/bin/bash
# Train M2M100 Transformer model
```


#### mT5 model


##### Arabic-Coptic
```bash
#!/bin/bash
python3 /PATH TO/copticmt/t5_translation/02_Translation.py --tsv_file "PATH TO/copticmt/CoPARA/dataset/tsv/CopticArabicProcessedTrain.tsv "
```

##### English-Coptic
```bash
#!/bin/bash

python3  /PATH TO/copticmt/t5_translation/02_Translation.py --tsv_file "PATH TO/copticmt/CopEng/copticEnglish.csv"
```