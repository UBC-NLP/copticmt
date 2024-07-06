
SOURCE_LANGUAGE="coptic"
TARGET_LANGUAGE="ar"
TRAIN_PREF="PATH TO/copticmt/CoPARA/dataset/train/train"
VALID_PREF="PATH TO/copticmt/CoPARA/dataset/val/val"
TEST_PREF="PATH TO/copticmt/CoPARA/dataset/test/test"
COPTIC_EN_DEST_DIR="PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/coptic_ar.tokenized.coptic-ar"
EN_COPTIC_DEST_DIR="PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/ar_coptic.tokenized.ar-coptic"
SRC_THRES=0
TGT_THRES=0

fairseq-preprocess     --source-lang $SOURCE_LANGUAGE     --target-lang $TARGET_LANGUAGE     --trainpref  $TRAIN_PREF     --validpref $VALID_PREF    --testpref $TEST_PREF    --destdir  $COPTIC_EN_DEST_DIR     --thresholdsrc $SRC_THRES     --thresholdtgt $TGT_THRES
#now create the data_bin file for the second direction in which the target now is coptic and the source is english
fairseq-preprocess     --source-lang $TARGET_LANGUAGE     --target-lang $SOURCE_LANGUAGE     --trainpref  $TRAIN_PREF     --validpref $VALID_PREF    --testpref $TEST_PREF    --destdir  $EN_COPTIC_DEST_DIR     --thresholdsrc $TGT_THRES     --thresholdtgt $SRC_THRES
