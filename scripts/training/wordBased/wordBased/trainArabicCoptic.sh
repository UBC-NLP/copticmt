CUDA_VISIBLE_DEVICES=4,5,6,7 fairseq-train "PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/ar_coptic.tokenized.ar-coptic" \
    --arch "transformer" \
    --dropout 0.1 \
    --attention-dropout 0.1 \
    --activation-dropout 0.1 \
    --encoder-embed-dim 512 \
    --encoder-ffn-embed-dim 2048 \
    --encoder-layers 6 \
    --encoder-attention-heads 8 \
    --encoder-learned-pos \
    --decoder-embed-dim 512 \
    --decoder-ffn-embed-dim 2048 \
    --decoder-layers 6 \
    --decoder-attention-heads 8 \
    --decoder-learned-pos \
    --max-epoch 100 \
    --optimizer adam \
    --lr 5e-4 \
    --batch-size 256 \
    --seed 1 \
    --encoder-layerdrop 0.1 \
    --decoder-layerdrop 0.1 \
    --criterion "label_smoothed_cross_entropy" \
    --warmup-updates 4000 \
    --source-lang "ar" \
    --target-lang "coptic" \
    --label-smoothing 0.1 \
    --lr-scheduler "inverse_sqrt" \
    --save-dir "PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/checkpoints/ArabicToCoptic" \
    --find-unused-parameters \
    --ddp-backend=no_c10d \
    --no-epoch-checkpoints \
    --wandb-project "Transformer Translation Arabic To Coptic another final run" \
    --log-format=json --log-interval=10 2>&1 | tee "PATH TO/copticmt/CoPARA/FairSEQ/Wordbased/checkpoints/arabic2coptic.log"

