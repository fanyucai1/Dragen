import os,re
import subprocess
import argparse

parser=argparse.ArgumentParser("Download Database which target_micro need.")
parser.add_argument("-d","--database",help="output directory",required=True,default=os.getcwd())
args=parser.parse_args()

args.datbase=os.path.abspath(args.database)
os.removedirs(args.datbase)
os.mkdir(args.database)
#####################################https://clades.nextstrain.org/dataset
database_name=['nextstrain/sars-cov-2',
               'nextstrain/flu/h1n1pdm/ha/CY121680','nextstrain/flu/h1n1pdm/ha/MW626062','nextstrain/flu/h1n1pdm/na/MW626056','nextstrain/flu/h1n1pdm/pa','nextstrain/flu/h1n1pdm/mp','nextstrain/flu/h1n1pdm/np','nextstrain/flu/h1n1pdm/ns','nextstrain/flu/h1n1pdm/pb2','nextstrain/flu/h1n1pdm/pb1',
               'nextstrain/flu/h3n2/ha/CY163680','nextstrain/flu/h3n2/ha/EPI1857216','nextstrain/flu/h3n2/na/EPI1857215','nextstrain/flu/h3n2/pb1','nextstrain/flu/h3n2/np','nextstrain/flu/h3n2/ns','nextstrain/flu/h3n2/mp','nextstrain/flu/h3n2/pa','nextstrain/flu/h3n2/pb2',
               'nextstrain/flu/vic/ha/KX058884','nextstrain/flu/vic/na/CY073894','nextstrain/flu/yam/ha/JN993010',
               'nextstrain/rsv/a/EPI_ISL_412866','nextstrain/rsv/b/EPI_ISL_1653999',
               'nextstrain/mpox/all-clades',
               'community/neherlab/hiv-1/hxb2',
               'community/moncla-lab/iav-h5/ha/all-clades']

docker="docker run -v %s:/database/ covlineages/pangolin nextclade dataset get "%(args.datbase)

for name in database_name:
     dir_name=re.sub(r'/', "_",name)
     os.makedirs("%s/%s"%(args.database,dir_name))
     cmd=docker+"--name \'%s\' --output-dir \'/database/%s\'"%(name,dir_name)
     subprocess.check_call(cmd,shell=True)

