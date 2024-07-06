BATCH_SIZE=128
BEAM=5
SEED=1
SCORING="bleu"
CHECKPOINT_PATH="PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/checkpoints/ArabicToCoptic/checkpoint_last.pt"

fairseq-generate "PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/ar_coptic.tokenized.ar-coptic" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring "bleu" > "PATH TO/copticmt/scripts/training/wordBased/wordBased/coptic2arabic/arabic2copticWordbased.txt"
