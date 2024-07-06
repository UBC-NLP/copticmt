fairseq-preprocess \
  --source-lang coptic --target-lang ar \
  --trainpref PATH TO/copticmt/CoPARA/dataset/train/train.m2m100 \
  --validpref PATH TO/copticmt/CoPARA/dataset/val/val.m2m100 \
  --testpref PATH TO/copticmt/CoPARA/dataset/test/test.m2m100 \
  --thresholdsrc 0 --thresholdtgt 0 \
  --destdir PATH TO/copticmt/CoPARA/FairSEQ/M2M100/coptic_arabic.coptic-ar \
  --srcdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/data_dict.128k.txt --tgtdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/data_dict.128k.txt

fairseq-preprocess \
  --source-lang ar --target-lang coptic \
  --trainpref PATH TO/copticmt/CoPARA/dataset/train/train.m2m100 \
  --validpref PATH TO/copticmt/CoPARA/dataset/val/val.m2m100 \
  --testpref PATH TO/copticmt/CoPARA/dataset/test/test.m2m100 \
  --thresholdsrc 0 --thresholdtgt 0 \
  --destdir PATH TO/copticmt/CoPARA/FairSEQ/M2M100/arabic_coptic.ar-coptic \
  --srcdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/data_dict.128k.txt --tgtdict PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/data_dict.128k.txt
