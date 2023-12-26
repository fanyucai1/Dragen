# 1.人类参考基因组

![hash_build](./hash_build_human.png)

构建图形基因Graph references的参数：*--ht-apply-graph=true*

## 建议在线下载
<https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform/product_files.html>

## 本地构建
### hg38
DNA+CNV+RNA
```cs
dragen --build-hash-table true
--output-directory /staging/hash_table/human/hg38_alt-masked_graph_cnv_hla_rna/ \
--ht-reference hg38.fa \
--ht-num-threads 40 \
--ht-seed-len 27 \
--ht-build-rna-hashtable true --enable-cnv true \
--ht-build-hla-hashtable true \
--ht- hla-reference /opt/edico/resources/hla/HLA_resource.v2.fasta.gz
--ht-apply-graph=true \
--ht-pop-alt-contigs /opt/edico/liftover/pop_altContig.fa.gz \
--ht-pop-alt-liftover /opt/edico/liftover/pop_liftover.sam.gz \
--ht-pop-snps /opt/edico/liftover/pop_snps.vcf.gz \
--ht-suppress-mask=true \
--ht-mask-bed /opt/edico/fasta_mask/hg38_alt_mask.bed \
--ht-alt-liftover /opt/edico/liftover/bwa-kit_hs38DH_liftover.sam \
--ht-suppress-decoys=true
--ht-decoys /opt/edico/liftover/hs_decoys.fa
```
methylation
```cs
dragen --build-hash-table true
--output-directory /staging/hash_table/human/hg38_methylation/ \
--ht-reference hg38.fa \
--ht-num-threads 40 \
--ht-seed-len 27 \
--ht-methylated-combined=true
--ht-methylated=true \
--ht-alt-liftover /opt/edico/liftover/bwa-kit_hs38DH_liftover.sam
```


## fasta文件下载

**hg19:**<https://ilmn-dragen-giab-samples.s3.amazonaws.com/FASTA/hg19.fa>

**hg38:**<https://ilmn-dragen-giab-samples.s3.amazonaws.com/FASTA/hg38.fa>

**hs37d5:**<https://ilmn-dragen-giab-samples.s3.amazonaws.com/FASTA/hs37d5.fa>


# 2. 非人物种

![hash_build_Non-Human](./hash_build_Non-Human.png)

构建图形基因Graph references的参数：*--ht-apply-graph=true*

DNA+CNV+RNA
```cs
    dragen --output-directory /staging/to/###_CNV_RNA/ \
    --build-hash-table true --ht-reference ##.fa \
    --enable-cnv true \
    --ht-num-thread 40 --ht-build-rna-hashtable true
```
methylation
```cs
    dragen --output-directory /staging/to/###_methylation/ \
    --build-hash-table true --ht-reference ###.fa \
    --ht-num-thread 40 --ht-methylated true \
    --ht-methylated-combined=true
```
