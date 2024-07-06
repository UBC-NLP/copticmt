CUDA_VISIBLE_DEVICES=1 fairseq-train PATH TO/copticmt/CopEng/FairSEQ/M2M100/english2coptic.en-coptic \
  --finetune-from-model  "PATH TO/copticmt/scripts/FairSeqTraining/M2M100/tokenizationFiles/418M_last_checkpoint.pt"\
  --save-dir PATH TO/copticmt/CopEng/FairSEQ/M2M100/EnglishToCoptic \
  --task translation_multi_simple_epoch \
  --encoder-normalize-before \
  --lang-pairs 'en-coptic' \
  --batch-size 10 \
  --decoder-normalize-before \
  --encoder-langtok src \
  --decoder-langtok \
  --criterion cross_entropy \
  --optimizer adafactor \
  --lr-scheduler cosine \
  --lr 3e-05 \
  --max-update 40000 \
  --update-freq 100 \
  --save-interval 1 \
  --save-interval-updates 5000 \
  --keep-interval-updates 10 \
  --no-epoch-checkpoints \
  --log-format simple \
  --log-interval 2 \
  --patience 15 \
  --arch transformer_wmt_en_de_big \
  --encoder-layers 12 \
  --decoder-layers 12 \
  --share-decoder-input-output-embed \
  --share-all-embeddings \
  --ddp-backend no_c10d \
  --max-epoch 10 \
  --wandb-project "English 2 coptic M2M100" >>  PATH TO/copticmt/CopEng/FairSEQ/M2M100/english2coptic.log


  