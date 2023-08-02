**SNV+CNV**
```cs
 dragen -f -r ${1} \
    -1 ${2} -2 ${3} --output-directory ${4} --output-file-prefix ${5} \
    --RGID Illumina_RGID --RGSM ${5} \
    --enable-map-align true \
    --enable-map-align-output true \
    --output-format BAM \
    --enable-duplicate-marking true \
    --enable-sort true \
    --enable-variant-caller true \
    --vc-enable-vcf-output true \
    --enable-vcf-compression true \
    --enable-cnv true \
    --cnv-enable-self-normalization true \
```

**SV**
```cs
--enable-sv true
```

**repeat**
```cs
--repeat-genotype-enable true
--repeat-genotype-specs /opt/edico/repeat-specs/hg19_expanded/
```

**gvcf**
```cs
--vc-emit-ref-confidence GVCF
```

**DRAGEN-ML**:typically removes 30-50% of SNP FPs, with smaller gains on INDELS. FN counts are reduced by 10% or more. 
```cs
--vc-ml-dir=/opt/edico/resources/ml_model/hg19 --vc-ml-enable-recalibration=true
```

**Star Allele Caller星号等位基因**：用于药物基因组
```cs
--enable-star-allele true
```

**Targeted callers**:输出<prefix>.targeted.vcf.gz and <prefix>.targeted.json
```
--enable-targeted=true
```

**High Sensitivity Mode**
```cs
--vc-enable-high-sensitivity-mode=true
```

