cut -f1 PATH TO/copticmt/scripts/training/BPE/spmTrainer/Arabic/arabic.vocab | tail -n +4 | awk '{print $1 " 100"}' > PATH TO/copticmt/scripts/training/BPE/spmTrainer/Arabic/fairseq.ar.vocab
# cut -f1 PATH TO/copticmt/scripts/training/BPE/spmTrainer/Coptic/coptic.vocab | tail -n +4 | awk '{print $1 " 100"}' > PATH TO/copticmt/scripts/training/BPE/spmTrainer/Coptic/fairseq.coptic.vocab
# cut -f1 PATH TO/copticmt/scripts/training/BPE/spmTrainer/English/english.vocab | tail -n +4 | awk '{print $1 " 100"}' > PATH TO/copticmt/scripts/training/BPE/spmTrainer/English/fairseq.en.vocab
