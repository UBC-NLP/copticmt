
SOURCE_LANGUAGE="coptic"
TARGET_LANGUAGE="ar"
TRAIN_PREF="PATH TO/copticmt/CoPARA/dataset/train/train.bpe"
VALID_PREF="PATH TO/copticmt/CoPARA/dataset/val/val.bpe"
TEST_PREF="PATH TO/copticmt/CoPARA/dataset/test/test.bpe"
COPTIC_EN_DEST_DIR="PATH TO/copticmt/CoPARA/FairSEQ/BPE/BPE_coptic_ar.tokenized.coptic-ar"
EN_COPTIC_DEST_DIR="PATH TO/copticmt/CoPARA/FairSEQ/BPE/BPE_ar_coptic.tokenized.ar-coptic"

SRC_THRES=0
TGT_THRES=0
COPTIC_DICT_PATH="PATH TO/copticmt/scripts/training/BPE/spmTrainer/Coptic/fairseq.coptic.vocab"
EN_DICT_PATH="PATH TO/copticmt/scripts/training/BPE/spmTrainer/Arabic/fairseq.ar.vocab"
# --srcdict $PCM_DICT_PATH     --tgtdict $EN_DICT_PATH
fairseq-preprocess \
    --source-lang $SOURCE_LANGUAGE    --srcdict $COPTIC_DICT_PATH     --tgtdict $EN_DICT_PATH --target-lang $TARGET_LANGUAGE  --align-suffix align     --trainpref  $TRAIN_PREF        --validpref $VALID_PREF     --testpref $TEST_PREF   --destdir  $COPTIC_EN_DEST_DIR     --thresholdsrc $SRC_THRES     --thresholdtgt $TGT_THRES
##
fairseq-preprocess \
    --source-lang $TARGET_LANGUAGE    --srcdict $EN_DICT_PATH     --tgtdict $COPTIC_DICT_PATH --target-lang $SOURCE_LANGUAGE  --align-suffix align     --trainpref  $TRAIN_PREF        --validpref $VALID_PREF     --testpref $TEST_PREF   --destdir  $EN_COPTIC_DEST_DIR     --thresholdsrc $TGT_THRES     --thresholdtgt $SRC_THRES








