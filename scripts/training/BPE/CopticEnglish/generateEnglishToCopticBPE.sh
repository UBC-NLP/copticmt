 BATCH_SIZE=128
 BEAM=5
 SEED=1
 SCORING=bleu
 CHECKPOINT_PATH="PATH TO/TranslationCo/CopEng/FairSEQ/BPE/oldCheckpoints/checkpoints/english2coptic/checkpoint_best.pt" 

CUDA_VISIBLE_DEVICE=3,4 fairseq-generate "PATH TO/TranslationCo/CopEng/FairSEQ/BPE/oldCheckpoints/BPE_en_coptic.tokenized.en-coptic" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring bleu > "PATH TO/TranslationCo/scripts/training/BPE/CopticEnglish/englishTocopticBPE.txt"
