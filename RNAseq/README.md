# RNA 数据分析: 表达定量 +可变剪切+基因融合+变异检测
```cs
dragen -f –r ${1} -1 ${2} -2 ${3} \
--output-file-prefix ${4} --output-directory ${5} \
--RGID RGID --RGSM ${4} \
--annotation-file ${6} \
--rrna-filter-enable=true \
--enable-duplicate-marking=true \
--dupmark-version=hash \
--enable-rna=true \
--enable-variant-caller=true \
--enable-rna-gene-fusion true \
--enable-rna-quantification true
```

# GFF3/GTF注释文件下载:https://www.gencodegenes.org/

# 结果输出
```cs
基因水平表达定量        <prefix>.quant.genes.sf
转录本表达量           <prefix>.quant.sf
可变剪切              <prefix>.SJ.out.tab
基因融合              <prefix>.fusion_candidates.final
变异检测              <prefix>.hard-filtered.vcf.gz
```