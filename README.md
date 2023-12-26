# dragen学习资料汇总

![WGS_bioinformatics_pipeline.jpg](./WGS_bioinformatics_pipeline.jpg)

## 文档

- [dragen在线帮助文档](https://support-docs.illumina.com/SW/dragen_v42/Content/SW/FrontPages/DRAGEN.htm)
- [dragen软件下载](https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform.html?langsel=/my/)
- [dragen-bio-it-platform-Getting Started Guide.pdf](Dcouments/dragen-bio-it-platform-Getting-Started-Guide.pdf)
- [dragen-platform-v4.2-guide.pdf](Dcouments/dragen-platform-v4.2-guide.pdf)
- [4.2-Customer-Release-Notes.pdf](Dcouments/4.2-Customer-Release-Notes.pdf)

## 流程使用说明

- [数据拆分](bcl2fastq/README.md)
- [遗传病WGS](WGS_germline/README.md)
- [遗传病WES](WES_germline/README.md)
- [扩增子panel_somatic](Amplicon_somatic/README.md)
- [数据压缩](ora-compression/README.md)
- [RPIP](RPIP/README.md)
- [参考基因组](hash_build/README.md)
- [测序系统误差](Systematic_noise_filtering/README.md)
- [体细胞-tumor-only](somatic_tumor_only/README.md)
- [体细胞-tumor vs normal](somatic_tumor_normal/README.md)
- [变异注释](./annotation/README.md)



## Explore recent

[DRAGEN publications:https://developer.illumina.com/news-updates/dragen-publications](https://developer.illumina.com/news-updates/dragen-publications) 


## Technical Assistance

Email: techsupport@illumina.com

## Illumina Technical Support Telephone Numbers

|Region | Toll Free |International|
|-------|-----------|------------|
|china |           | +86 400 066 5835|

## Resource

a population SNP VCF， can be used *--cnv-population-b-allele-vcf* option

https://storage.googleapis.com/gcp-public-data--broad-references/hg19/v0/1000G_phase1.snps.high_confidence.b37.vcf.gz

https://storage.googleapis.com/gcp-public-data--broad-references/hg38/v0/1000G_phase1.snps.high_confidence.hg38.vcf.gz