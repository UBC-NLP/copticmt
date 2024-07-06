 BATCH_SIZE=128
 BEAM=5
 SEED=1
 SCORING=bleu
 CHECKPOINT_PATH="PATH TO/TranslationCo/CoPARA/FairSEQ/BPE/coptic2arabic/checkpoint_last.pt" 

CUDA_VISIBLE_DEVICE=4 fairseq-generate "PATH TO/TranslationCo/CoPARA/FairSEQ/BPE/BPE_coptic_ar.tokenized.coptic-ar" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring bleu > "PATH TO/TranslationCo/scripts/training/BPE/CopticArabic/CopticToArabicBPE.txt"
