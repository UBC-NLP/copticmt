 BATCH_SIZE=128
 BEAM=5
 SEED=1
 SCORING=bleu
 CHECKPOINT_PATH="PATH TO/TranslationCo/CoPARA/FairSEQ/BPE/ArabicToCoptic/checkpoint_best.pt" 

CUDA_VISIBLE_DEVICE=5 fairseq-generate "PATH TO/TranslationCo/CoPARA/FairSEQ/BPE/BPE_ar_coptic.tokenized.ar-coptic" \
    --batch-size $BATCH_SIZE \
    --beam $BEAM \
    --path $CHECKPOINT_PATH \
    --seed $SEED \
    --scoring bleu > "PATH TO/TranslationCo/scripts/training/BPE/CopticArabic/ArabicToCopticBPE.txt"
