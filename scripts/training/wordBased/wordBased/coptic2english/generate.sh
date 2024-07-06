#!/bin/bash
export BATCH_SIZE=128
export BEAM=5
export SEED=1
export SCORING="bleu"
export CHECKPOINT_PATH="PATH TO/copticmt/CopEng/FairSEQ/Wordbased/checkpoints/CopticToEnglishWordBased/CopticToEnglishWordBased/checkpoint_last.pt"

# Continue from the previous script
fairseq-generate "PATH TO/copticmt/CopEng/FairSEQ/Wordbased/coptic_en.tokenized.coptic-en" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring $SCORING > "PATH TO/copticmt/scripts/training/wordBased/wordBased/coptic2english/coptic to english word based translation results"
