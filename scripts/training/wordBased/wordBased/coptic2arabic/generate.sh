BATCH_SIZE=128
BEAM=5
SEED=1
SCORING="bleu"
CHECKPOINT_PATH="PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/checkpoints/CopticToArabic/checkpoint_last.pt"

fairseq-generate "PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/coptic_ar.tokenized.coptic-ar" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring "bleu" > "PATH TO/copticmt/scripts/training/wordBased/wordBased/coptic2arabic/coptic2arabicWordbased.txt"
