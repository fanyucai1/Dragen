import subprocess,argparse
import os,re
import sys

docker_name="covlineages/pangolin"
def run(db,query,prefix):
    outdir=os.path.dirname(os.path.abspath(query))
    db = os.path.abspath(db)
    query=os.path.abspath(query)
    out=outdir+"/"+prefix
    outfile = open("%s.tsv" % (out), "w")
    for root, dirs, files in os.walk(db):
        for dir in dirs:
            db_dir=db+"/"+dir
            cmd = ("docker run -v %s:/database/ -v %s:/mnt %s "
                   "nextclade run --silent -D /database/ "
                   "--output-tsv /mnt/%s.%s.tsv /mnt/%s") %(db_dir,outdir,docker_name,prefix,dir,query.split("/")[-1])
            subprocess.call(cmd,shell=True)
            infile=open("%s.%s.tsv"%(out,dir),"r")
            for line in infile:
                line=line.strip()
                if line.split("\t")[2]!="clade" and re.search(r'\S',line.split("\t")[2]):
                    outfile.write("%s\n"%line)
            os.remove("%s.%s.tsv"%(out,dir))
    outfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser("")
    parser.add_argument('-d', '--db', required=True, help="Database directory")
    parser.add_argument('-p', '--prefix', required=True, help="Prefix of output files")
    parser.add_argument('-q', '--query', required=True, help="Query fasta sequence")
    args = parser.parse_args()
    run(args.db,args.query,args.prefix)