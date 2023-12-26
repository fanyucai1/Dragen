dragen -f -r ${1} \
    --tumor-fastq1 ${2} --tumor-fastq2 ${3} \
    --output-directory=${4} --output-file-prefix=${5} \
    --RGID-tumor tumor_RGID --RGSM-tumor ${5} \
    --amplicon-target-bed=${6} \
    --enable-dna-amplicon true --enable-map-align=true \
    --enable-sort=true --enable-map-align-output=true \
    --enable-variant-caller=true --enable-cnv=true --enable-sv=true