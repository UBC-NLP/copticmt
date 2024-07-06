SOURCE_LANGUAGE=coptic
TARGET_LANGUAGE=ar
TRAIN_PREF="PATH TO/coptic-translator/CoPARA/datasetForFairseq/train/train"
VALID_PREF="PATH TO/coptic-translator/CoPARA/datasetForFairseq/dev/val"
TEST_PREF="PATH TO/coptic-translator/CoPARA/datasetForFairseq/test/test"
COPTIC_AR_DEST_DIR="PATH TO/coptic-translator/fairseqCheckpointsCoPAra/sanityCheck/coptic_ar.tokenized.coptic-ar"
AR_COPTIC_DEST_DIR="PATH TO/coptic-translator/fairseqCheckpointsCoPAra/sanityCheck/ar_coptic.tokenized.ar-coptic"
SRC_THRES=0
TGT_THRES=0

fairseq-preprocess     --source-lang $SOURCE_LANGUAGE     --target-lang $TARGET_LANGUAGE     --trainpref  $TRAIN_PREF     --validpref $VALID_PREF    --testpref $TEST_PREF    --destdir  $COPTIC_AR_DEST_DIR     --thresholdsrc $SRC_THRES     --thresholdtgt $TGT_THRES
