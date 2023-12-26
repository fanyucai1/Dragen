# enrichment
```{.cs}
dragen -f -r ${1} \
    --tumor-fastq1=${2} --tumor-fastq2=${3} \
    --RGID-tumor tumor_RGID --RGSM-tumor ${4} \
    --fastq-file1 ${5} --fastq-file2 ${6} \
    --RGID normal_RGID --RGSM ${7} \
    --output-directory ${8} --output-file-prefix ${9} \
    --enable-duplicate-marking true --enable-sort true --output-format BAM --enable-map-align true \
    --enable-map-align-output true --enable-bam-indexing true \
    --enable-variant-caller true \
    --enable-cnv true --vc-target-bed ${10}\
    --cnv-target-bed ${10} \
    --cnv-normals-list ${11} \
    --cnv-use-somatic-vc-baf true \
    --enable-sv true \
    --sv-exome true \
    --sv-call-regions-bed ${10}
```


# amplicon_DNA
```{.cs}
dragen -f -r ${1} \
    --tumor-fastq1=${2} --tumor-fastq2=${3} \
    --RGID-tumor tumor_RGID --RGSM-tumor ${4} \
    --fastq-file1 ${5} --fastq-file2 ${6} \
    --RGID normal_RGID --RGSM ${7} \
    --output-directory ${8} --output-file-prefix ${9} \
    --enable-duplicate-marking true --enable-sort true --output-format BAM --enable-map-align true \
    --enable-map-align-output true --enable-bam-indexing true \
    --enable-variant-caller=true --enable-cnv=true --enable-sv=true \
    --enable-dna-amplicon true \
    --vc-use-somatic-hotspots false \
    --amplicon-primer-length 50 \
    --amplicon-target-bed=${10}
```