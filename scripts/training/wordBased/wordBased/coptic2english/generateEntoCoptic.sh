BATCH_SIZE=128
BEAM=5
SEED=1
SCORING="bleu"
CHECKPOINT_PATH="PATH TO/copticmt/CopEng/FairSEQ/Wordbased/checkpoints/EnglishToCopticWordBased/checkpoint_last.pt"

fairseq-generate "PATH TO/copticmt/CopEng/FairSEQ/Wordbased/en_coptic.tokenized.en-coptic" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring "bleu" > "PATH TO/copticmt/scripts/training/wordBased/wordBased/coptic2english/english to coptic word based generation results.txt"
