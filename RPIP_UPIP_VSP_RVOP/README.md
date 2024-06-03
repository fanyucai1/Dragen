# 1.dragen数据库下载

本地服务器地址：10.88.32.74

下载脚本
```{.cs}
mkdir -p /staging/explify_china/explify-databases/
cd /staging/explify_china/
wget -O explify-dbs.sh https://illumina-explify-databases.s3.us-east-1.amazonaws.com/explify-dbs.sh
chmod +x explify-dbs.sh
```

查看可下载数据库版本
```{.cs}
./explify-dbs.sh search -d explify-databases/
    version=1.0.3
    Downloading manifest file to explify-databases/s3-manifest.txt
    6 database(s) found meeting those criteria:
    - RPIP-5.11.7
    - UPIP-7.3.7
    - Custom-1.0.0
    - RPIP-6.3.0
    - VSPv2-2.3.0
    - UPIP-8.4.0
```
数据库下载
```{.cs}
./explify-dbs.sh download -d explify-databases/ -p UPIP -v 8.4.0 -n 20
./explify-dbs.sh download -d explify-databases/ -p RPIP -v 6.3.0 -n 20
./explify-dbs.sh download -d explify-databases/ -p VSPv2 -v 2.3.0 -n 20
./explify-dbs.sh download -d explify-databases/ -p Custom -v 1.0.0 -n 20
```
check数据库
```{.cs}
./explify-dbs.sh check -d explify-databases/ -p Custom -v 1.0.0
./explify-dbs.sh check -d explify-databases/ -p UPIP -v 8.4.0
./explify-dbs.sh check -d explify-databases/ -p VSPv2 -v 2.3.0
./explify-dbs.sh check -d explify-databases/ -p RPIP -v 6.3.0
```
数据库目录结构

![数据库目录结构](./database_directory_tree.png){width=200}


备注：这个数据库非常大大概70G，如果客户安端装建议下载到移动硬盘给客户

# 2.dragen v4.2安装

<https://sapac.support.illumina.com/downloads/illumina-dragen-bio-it-platform-v4-2.html>

# 3.docker镜像下载

dragen v4硬件服务器默认安装docker,建议安装Docker v20.10 or later,数据分析需要安装2个额外的docker包：

```cs
snpeff.tar
covlineages_pangolin.tar
```

服务器路径：/staging/explify_china/Docker

安装方式一：（后台命令行）

```{.cs}
docker load -i snpeff.tar
docker load -i covlineages_pangolin.tar
```

安装方式二：（前端页面上传）
浏览器输入并输入用户名以及对应密码

http://10.88.32.74/

![首页](./main.png)

点击左边栏**数据库更新**

![数据库更新](./database_updata.png)

# 4.知识库文件更新

![知识库更新](./knowledge.png)

备注：知识库更新请联系Illumina售后技术支持

# 5.测试数据

服务器路径：/staging/explify\_china/test\_data/RPIP/

# 6.demo shell

```{.cs}
/opt/edico/bin/dragen \
  --enable-explify=true \
  --output-file-prefix RPIP_test \
  --explify-sample-list ${1} \
  --explify-test-panel-name "RPIP" \
  --explify-test-panel-version 5.11.7 \
  --explify-ref-db-dir /staging/explify_china/explify-databases/ \
  --explify-load-db-ram=true \
  --output-directory ${2} \
  --explify-ncpus=48
```

**sample list实例**

| SampleID* | 	BatchID | RunID | ControlFlag | FastQs*                           |                                   |
|-----------|----------|-------|-------------|------------------------------------|------------------------------------|
| 57        | 57       | 57    |             | /path/to/57\_S10\_R1\_001.fastq.gz | /path/to/57\_S10\_R2\_001.fastq.gz |
| 56        | 56       | 56    |             | /path/to/56\_S10\_R1\_001.fastq.gz | |

备注：\*代表必填项
