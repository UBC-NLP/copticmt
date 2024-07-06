fairseq-preprocess \
  --source-lang coptic --target-lang en \
  --trainpref PATH TO/copticmt/CopEng/dataset/train/train.m2m100 \
  --validpref PATH TO/copticmt/CopEng/dataset/val/val.m2m100 \
  --testpref PATH TO/copticmt/CopEng/dataset/test/test.m2m100 \
  --thresholdsrc 0 --thresholdtgt 0 \
  --destdir PATH TO/copticmt/CopEng/FairSEQ/M2M100/coptic2english.coptic-en \
  --srcdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/model_dict.128k.txt --tgtdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/model_dict.128k.txt

fairseq-preprocess \
  --source-lang en --target-lang coptic \
  --trainpref PATH TO/copticmt/CopEng/dataset/train/train.m2m100 \
  --validpref PATH TO/copticmt/CopEng/dataset/val/val.m2m100 \
  --testpref PATH TO/copticmt/CopEng/dataset/test/test.m2m100 \
  --thresholdsrc 0 --thresholdtgt 0 \
  --destdir PATH TO/copticmt/CopEng/FairSEQ/M2M100/english2coptic.en-coptic \
  --srcdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/model_dict.128k.txt --tgtdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/model_dict.128k.txt