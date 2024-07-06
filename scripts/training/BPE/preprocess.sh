
SOURCE_LANGUAGE="coptic"
TARGET_LANGUAGE="en"
TRAIN_PREF="PATH TO/coptic-translator/dataPreperationForFairseqTrain/train_bpe/train.bpe"
VALID_PREF="PATH TO/coptic-translator/dataPreperationForFairseqTrain/val_bpe/val.bpe"
TEST_PREF="PATH TO/coptic-translator/dataPreperationForFairseqTrain/test_bpe/test.bpe"
COPTIC_EN_DEST_DIR="PATH TO/coptic-translator/dataPreperationForFairseqTrain/BPE_coptic_en.tokenized.coptic-en"
EN_COPTIC_DEST_DIR="PATH TO/coptic-translator/dataPreperationForFairseqTrain/BPE_en_coptic.tokenized.en_coptic"

SRC_THRES=0
TGT_THRES=0
COPTIC_DICT_PATH="PATH TO/coptic-translator/bpe_dict_path/fairseq.coptic.vocab"
EN_DICT_PATH="PATH TO/coptic-translator/bpe_dict_path/fairseq.en.vocab"
# --srcdict $PCM_DICT_PATH     --tgtdict $EN_DICT_PATH
fairseq-preprocess \
    --source-lang $SOURCE_LANGUAGE    --srcdict $COPTIC_DICT_PATH     --tgtdict $EN_DICT_PATH --target-lang $TARGET_LANGUAGE  --align-suffix align     --trainpref  $TRAIN_PREF        --validpref $VALID_PREF     --testpref $TEST_PREF   --destdir  $COPTIC_EN_DEST_DIR     --thresholdsrc $SRC_THRES     --thresholdtgt $TGT_THRES
##
fairseq-preprocess \
    --source-lang $TARGET_LANGUAGE    --srcdict $EN_DICT_PATH     --tgtdict $COPTIC_DICT_PATH --target-lang $SOURCE_LANGUAGE  --align-suffix align     --trainpref  $TRAIN_PREF        --validpref $VALID_PREF     --testpref $TEST_PREF   --destdir  $EN_COPTIC_DEST_DIR     --thresholdsrc $TGT_THRES     --thresholdtgt $SRC_THRES








