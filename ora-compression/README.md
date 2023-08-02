# 压缩参考基因组

**Illumina DRAGEN Systematic Noise Files:**

<https://sapac.support.illumina.com/sequencing/sequencing_software/dragen-bio-it-platform/product_files.html>

# 数据压缩命令
```cs
dragen  --ora-input ${1} --ora-input2 ${2} \
      --output-directory ${3} \
      --ora-reference ${4} \
      --enable-ora true --enable-map-align false --ora-use-hw true
针对于人的压缩比率在1/5,针对于其他物种大概为1/2
```

# 解压缩命令
```cs
dragen -1 ${1} \
--output-directory ${2} \
--ora-reference ${3} \
--output-file-prefix ${4} \
--interleaved --RGID RGID --RGSM ${4} \
--enable-ora true --enable-map-align false --ora-decompress true
```

# dragen可以直接读取ora文件
```cs
dragen -r ${1} -1 ${2} -2 ${3} \
--ora-reference ${4} --output-directory ${5} \
--output-file-prefix ${6} --RGID RGID --RGSM RGSM \
--enable-variant-caller true
```

# 数据拆分直接生成压缩格式文件
```cs
dragen --bcl-conversion-only true --bcl-input-directory ${1} \
--output-directory ${2} --force --sample-sheet  ${3} --ora-reference=${4} \
--fastq-compression-format=dragen
```

# 生信软件兼容

| 软件     | 	版本 |
|--------|-----|
| BWA    | 0.7.15 |	Fastq|
| FastQC |0.11.9	|Fastq|


