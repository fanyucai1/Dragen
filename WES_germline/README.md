# snv+cnv+sv

```cs
dragen -f -r ${1} -1 ${2} -2 ${3} \
    --RGID Normal_RGID --RGSM Nroma_RGSM \
    --enable-map-align true \
    --enable-map-align-output true \
    --output-format bam --enable-sort true \
    --enable-duplicate-marking true \
    --enable-variant-caller true \
    --enable-vcf-compression true \
    --vc-target-bed ${4} \
    --enable-cnv true \
    --cnv-target-bed ${4} --cnv-normals-list ${5} \
    --enable-sv true --sv-exome true --sv-call-regions-bed ${4} \
    --output-file-prefix ${6} \
    --output-directory ${7}
```

# PoN建立正常样本基线
```cs
dragen -r ${1} -1 ${2} -2 ${3} \
   --RGSM ${4} --RGID illumina \
   --output-directory ${5} \
   --output-file-prefix ${4} \
   --enable-map-align true --enable-cnv true \
   --cnv-enable-gcbias-correction false \
   --cnv-enable-self-normalization false \
   --cnv-target-bed ${6} --cnv-interval-width 500
```

将 prefix.target.counts.gc-corrected.gz 文件写到PoN.txt文本文件中，其内容如下
```cs
/data/output_trio1/sample1.target.counts.gc-corrected.gz
/data/output_trio1/sample2.target.counts.gc-corrected.gz
/data/output_trio2/sample4.target.counts.gc-corrected.gz
/data/output_trio2/sample5.target.counts.gc-corrected.gz
/data/output_trio3/sample7.target.counts.gc-corrected.gz
/data/output_trio3/sample8.target.counts.gc-corrected.gz
```
附录说明正常样本数量50个左右

# CNV分析参数
```cs
--enable-cnv true
--cnv-filter-copy-ratio 0.2     #   The default value is 0.2, leading to calls less than CR=0.8 or greater than CR=1.2.
--cnv-filter-length 10000       #   Specifies the minimum event length in bases at which a reported event is marked as PASS in the output VCF file. The default is 10000
--cnv-filter-qual 10            #   PASS in the output VCF file
```
# CNV 解析度

|WGS_Coverag_per_Sample| Recommended_Resolution(bp)|
|-----------|----------|
|5X|10000|
|10X|5000|
|>=30X|1000|

*–cnv-interval-width* 用来控制解析度，WES默认是500，WGS默认是1000该参数在分析是需要设置，如果设置变小会增加分析时间

*--vc-target-bed-padding 100*

# VCF结果解释

|||||
|------------------|---|--------------------|----------|
|Diploid_or_Haploid|ALT| FORMAT:CN          |FORMAT:GT|
|Diploid|                 . |          2|          ./.|
|Diploid                |DUP         |>2          |./1|
|Diploid|                 DEL         |1           |0/1|
|Diploid|                 DEL         |0           |1/1|
|Haploid|                 .   |        1           |0|
|Haploid |                DUP  |       >1          |1|
|Haploid |                DEL   |      0  |         1|



# 参考文献

**dragen_PoN**

[Patel B, Parets S, Akana M, et al. Comprehensive genetic testing for female and male infertility using next-generation sequencing[J]. Journal of assisted reproduction and genetics, 2018, 35(8): 1489-1496.](https://link.springer.com/article/10.1007/s10815-018-1204-7)

**CNV refers to an intermediate scale structural variant, with copy number changes ranging from 1 Kb to 5 Mb of DNA**

[Kerkhof J, Schenkel L C, Reilly J, et al. Clinical validation of copy number variant detection from targeted next-generation sequencing panels[J]. The Journal of Molecular Diagnostics, 2017, 19(6): 905-920.](https://pubmed.ncbi.nlm.nih.gov/28818680/)

**CNV size cutoffs were 1 kb for losses and 2kb for gains**

[Lionel A C, Costain G, Monfared N, et al. Improved diagnostic yield compared with targeted gene sequencing panels suggests a role for whole-genome sequencing as a first-tier genetic test[J]. Genetics in Medicine, 2018, 20(4): 435-443.](https://www.nature.com/articles/gim2017119)

**high copy number calls expected to have >0.85,and high copy number loss <-1.25**

[Chaubey A, Shenoy S, Mathur A, et al. Low Pass-Genome Sequencing: Validation and diagnostic utility from 409 clinical cases of low-pass genome sequencing for the detection of copy number variants (CNVs) to replace constitutional microarray[J]. The Journal of Molecular Diagnostics, 2020.](https://pubmed.ncbi.nlm.nih.gov/32344035/)

