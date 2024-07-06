DROPOUT=0.3
ATTENTION_DROPOUT=0.1  # Change this to the default value
ACTIVATION_DROPOUT=0.3
EMBEDDING_SIZE=512  # Change this to the default value
ENC_FFNN=2048  # Change this to the default value
ENCODER_LAYERS=6  # Change this to the default value
ENCODER_ATTENTION_HEADS=8  # Change this to the default value
DECODER_LAYERS=6  # Change this to the default value
DECODER_ATTENTION_HEADS=8  # Change this to the default value
DEC_FFNN=2048  # Change this to the default value
EPOCH=200
BATCH_SIZE=64
ENCODER_LAYER_DROPOUT=0.1  # Change this to the default value
DECODER_LAYER_DROPOUT=0.1  # Change this to the default value
SOURCE_LANGUAGE="coptic"
TARGET_LANGUAGE="en"
LABEL_SMOOTHING=0.1
SAVE_DIR="PATH TO/coptic-translator/checkpointWordBased/Coptic2EnglishWordBasedSeq2SeqTransformer"
LABEL_CROSS_ENTROPY="label_smoothed_cross_entropy"
WARMUP_UPDATES=4000
LEARNING_POLICY="inverse_sqrt"  # Corrected the typo in the variable name
WAND_PROJECT_NAME="Coptic2EN 6-6 Layers Translation Word Translation"

fairseq-train "PATH TO/coptic-translator/fairseqwordBased/coptic_en.tokenized.coptic-en" \
    --arch transformer \
    --dropout $DROPOUT \
    --attention-dropout $ATTENTION_DROPOUT \
    --encoder-embed-dim $EMBEDDING_SIZE \
    --encoder-ffn-embed-dim $ENC_FFNN \
    --encoder-layers $ENCODER_LAYERS \
    --encoder-attention-heads $ENCODER_ATTENTION_HEADS \
    --encoder-learned-pos \
    --decoder-embed-dim $EMBEDDING_SIZE \
    --decoder-ffn-embed-dim $DEC_FFNN \
    --decoder-layers $DECODER_LAYERS \
    --decoder-attention-heads $DECODER_ATTENTION_HEADS \
    --decoder-learned-pos \
    --max-epoch $EPOCH \
    --optimizer adam \
    --lr 5e-4 \
    --batch-size $BATCH_SIZE \
    --seed 1 \
    --encoder-layerdrop $ENCODER_LAYER_DROPOUT \
    --decoder-layerdrop $DECODER_LAYER_DROPOUT \
    --criterion $LABEL_CROSS_ENTROPY \
    --warmup-updates $WARMUP_UPDATES \
    --source-lang $SOURCE_LANGUAGE \
    --label-smoothing $LABEL_SMOOTHING \
    --lr-scheduler $LEARNING_POLICY \
    --save-dir $SAVE_DIR \
    --find-unused-parameters \
    --target-lang $TARGET_LANGUAGE \
    --activation-dropout $ACTIVATION_DROPOUT \
    --ddp-backend=no_c10d \
    --no-epoch-checkpoints \
    --wandb-project "$WAND_PROJECT_NAME" \
    --log-format=json \
    --log-interval=10 2>&1 | tee "PATH TO/coptic-translator/training/wordBased/fairseqDefaultTranssfomer.log"
