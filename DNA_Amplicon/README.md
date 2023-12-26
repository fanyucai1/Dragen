**Support for comprehensive amplicon analysis: SNV, RNA-fusion, CNV and SV**


```cs
dragen -r ${1} --fastq-file1=${2} --fastq-file2=${3} \
--output-directory=${4} --output-file-prefix=${5}
--RGSM ${5} --RGID Illumina_RGID
--enable-dna-amplicon true \
--enable-map-align=true --enable-sort=true --enable-map-align-output=true \
--enable-variant-caller=true --enable-cnv=true --enable-sv=true \
--vc-use-somatic-hotspots false \
--amplicon-target-bed=${6}
```

**maximum amplicon primer length is set to 50**
```cs
--amplicon-primer-length 50
```

The CNV segmentation bed can be modified using **cnv-segmentation-bed**
