# 按照lane拆分
```cs
dragen --bcl-conversion-only true --bcl-input-directory ${1} --output-directory ${2} --force --sample-sheet  ${3}
```

# 非按lane拆分
```cs
dragen --bcl-conversion-only true --bcl-input-directory ${1} --output-directory ${2} --force --sample-sheet  ${3} --no-lane-splitting true
```

# 数据拆分输出压缩格式ora文件

## 1.压缩参考基因组

**Illumina ORA Compression Reference Files:**

<https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform/product_files.html>

## 2.命令行参数
```cs
--ora-reference=/staging/lenadata/ --fastq-compression-format=dragen
```
