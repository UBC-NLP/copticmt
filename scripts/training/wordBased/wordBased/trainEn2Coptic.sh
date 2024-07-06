DROPOUT = 0.1
ATTENTION_DROPOUT = 0.1
ACTIVATION_DROPOUT = 0.1
EMBEDDING_SIZE = 512  # Corresponds to D_MODEL in the paper
ENC_FFNN = 2048  # Corresponds to D_FF, dimension of the feed-forward network in the encoder
ENCODER_LAYERS = 6
ENCODER_ATTENTION_HEADS = 8
DECODER_LAYERS = 6
DECODER_ATTENTION_HEADS = 8
DEC_FFNN = 2048  # Dimension of the feed-forward network in the decoder
EPOCH = 100  # Typical epochs are not specified in the paper; adjust based on your dataset
BATCH_SIZE = 256  # This is the effective batch size in tokens
ENCODER_LAYER_DROPOUT = 0.1  # Not specifically named in the paper, using DROPOUT for consistency
DECODER_LAYER_DROPOUT = 0.1  # Not specifically named in the paper, using DROPOUT for consistency
SOURCE_LANGUAGE = "en"
TARGET_LANGUAGE = "coptic"  # Typically German in the paper's translation tasks
LABEL_SMOOTHING = 0.1
SAVE_DIR = "PATH TO/copticmt/CopEng/FairSEQ/Wordbased/checkpoints/EnglishToCopticWordBased"
LABEL_CROSS_ENTROPY = "label_smoothed_cross_entropy"
WARMUP_UPDATES = 4000
LEARNING_POLICY = "inverse_sqrt"
WAND_PROJECT_NAME = "Transformer Translation Project"

fairseq-train "PATH TO/copticmt/CopEng/FairSEQ/Wordbased/en_coptic.tokenized.en-coptic"\
    --arch "transformer" \
    --dropout $DROPOUT \
    --attention-dropout 0     --encoder-embed-dim $EMBEDDING_SIZE \
    --encoder-ffn-embed-dim $ENC_FFNN  \
    --encoder-layers $ENCODER_LAYERS  \
    --encoder-attention-heads $ENCODER_ATTENTION_HEADS \
    --encoder-learned-pos  \
    --decoder-embed-dim $EMBEDDING_SIZE \
    --decoder-ffn-embed-dim $DEC_FFNN  \
    --decoder-layers $DECODER_LAYERS \
    --decoder-attention-heads $DECODER_ATTENTION_HEADS \
    --decoder-learned-pos   \
    --max-epoch 50  \
    --optimizer adam \
    --lr 5e-4 \
    --batch-size 256 \
    --seed 1     --encoder-layerdrop $ENCODER_LAYER_DROPOUT     --decoder-layerdrop $DECODER_LAYER_DROPOUT \
    --criterion "label_smoothed_cross_entropy"     --warmup-updates $WARMUP_UPDATES \
    --source-lang $SOURCE_LANGUAGE     --label-smoothing $LABEL_SMOOTHING \
    --lr-scheduler $lEARNING_POLICY   --save-dir $SAVE_DIR \
    --find-unused-parameters  \
    --target-lang $TARGET_LANGUAGE \
    --activation-dropout $ACTIVATION_DROPOUT  \
    --ddp-backend=no_c10d \
    --no-epoch-checkpoints --wandb-project "$WAND_PROJECT_NAME" \
    --log-format=json --log-interval=10 2>&1    |  tee  "PATH TO/copticmt/CopEng/FairSEQ/Wordbased/checkpoints/en2coptic.log"



