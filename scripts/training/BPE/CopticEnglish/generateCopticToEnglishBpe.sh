 BATCH_SIZE=128
 BEAM=5
 SEED=1
 SCORING=bleu
 CHECKPOINT_PATH="PATH TO/TranslationCo/CopEng/FairSEQ/BPE/oldCheckpoints/checkpoints/coptic2English/checkpoint_best.pt" 

CUDA_VISIBLE_DEVICES=7 fairseq-generate "PATH TO/TranslationCo/CopEng/FairSEQ/BPE/oldCheckpoints/BPE_coptic_en.tokenized.coptic-en" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring bleu > "PATH TO/TranslationCo/scripts/training/BPE/CopticEnglish/CopticToEnglishBPE.txt"
