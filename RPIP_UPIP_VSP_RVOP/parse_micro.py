# Email:yucai.fan@illumina.com
# 2014.07.19-
# version:1.0
# This script will parse json file from dragen(RPIP/UPIP/VSP).

import os,sys,re
import subprocess,argparse
import time
import json

parse=argparse.ArgumentParser("This script will parse dragen v4.3 VSPv2 json file.\n")
parse.add_argument("-j","--json",help="json file from dragen v4.3 VSPv2",required=True)
parse.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
args=parse.parse_args()

args.json=os.path.abspath(args.json)
args.outdir=os.path.abspath(args.outdir)
if not os.path.exists(args.outdir):
    subprocess.check_output("mkdir -p %s"%args.outdir,shell=True)
start=time.time()
with open(args.json, "r") as load_f:
    load_dict = json.load(load_f)#dict
    prefix =load_dict['accession']
    out = os.path.abspath(args.outdir) + "/" + prefix
    ######################################## convert one line json to multiple lines
    new_dict=json.dumps(load_dict,indent=4, sort_keys=True)#str
    with open("%s_multiple_lines.json"%(out), "w") as outfile:
        outfile.write(new_dict)
    ########################################step1:sample quality control
    out1_file = open("%s.QC.Metrics.tsv" % out, "w")
    out1_file.write("Metric\tValue\tDescription\n")

    value_name = []
    # qcReport
    qcReport = load_dict['qcReport']

    ##sampleQc
    sampleQc = qcReport['sampleQc']
    key_name = ['totalRawReads', 'uniqueReadsProportion', 'postQualityReads', 'postQualityReadsProportion',
                'removedInDehostingReadsProportion', 'libraryQScore']
    cloumn_name = ['Total Raw Reads', '% Unique Reads', 'Post-Quality Reads', '% Post-Quality Reads', '% Dehosted',
                   'library Q-Score']
    description = [
        'Number of reads in sample before read QC processing',
        'Number of distinct reads in sample before read QC processing',
        'Number of reads in sample after read QC processing',
        'Percentage of post-quality reads in sample relative to total raw reads',
        'Percentage of host reads in sample removed relative to total raw reads',
        'Quality score of the library after read QC processing',
    ]
    for key in key_name:
        if re.search(r'Proportion', key):
            sampleQc[key] = format(float(sampleQc[key]) * 100, ".2f")
        if re.search(r'Reads$', key):
            sampleQc[key] = format(int(sampleQc[key]), ",")
        value_name.append(sampleQc[key])

    ##enrichmentFactor
    enrichmentFactor = qcReport['enrichmentFactor']
    cloumn_name += ['Enrichment Factor']
    description += ['Enrichment factor value reflecting how well targeted regions were enriched']
    value_name.append(enrichmentFactor['value'])

    cloumn_name += ['Enrichment Category']
    value_name.append(enrichmentFactor['category'])
    description += ['Enrichment factor category: \'poor\', \'fair\', \'good\', or \'NC\' for not calculated']

    ##Sample_Composition
    sampleComposition = qcReport['sampleComposition']['readClassification']
    key_name = ['targetedMicrobial', 'untargeted', 'ambiguous', 'unclassified', 'lowComplexity',
                'targetedInternalControl']
    cloumn_name += ['Targeted Microbial', 'Untargeted', 'Ambiguous', 'Unclassified', 'Low Complexity',
                    'Targeted Internal Control']
    for key in key_name:
        value_name.append(format(float(sampleComposition[key]) * 100, ".2f"))
    description += ['Targeted microbial (non-IC) reference sequences',
                    'Untargeted reference sequences',
                    'More than one pathogen class',
                    'Could not be classified',
                    'Low complexity sequence',
                    'Targeted IC reference sequences'
                    ]

    for i in range(0, len(cloumn_name)):
        out1_file.write(f"{cloumn_name[i]}\t{value_name[i]}\t{description[i]}\n")
    out1_file.close()
    ########################################step2:Microorganisms
    out2_file = open("%s.microbial_enrichment_viral.tsv" % out, "w")
    microorganisms = load_dict['targetReport']['microorganisms']  # 一个物种对应多个
    cloumn_name = ['Class','Microorganism', 'Present', 'Accessions', '% Coverage', '% ANI', 'Aligned Reads', 'Median Depth',
                   'RPKM', 'Absolute Quantity']
    for i in range(0, len(cloumn_name)):
        if i == 0:
            out2_file.write("%s" % cloumn_name[i])
        else:
            out2_file.write("\t%s" % cloumn_name[i])
    description = [
        'Name of detected microorganism',
        'Whether Explify interpretation predicts that the organism is present (true/false)',
        'The accession for the reference',
        'Proportion of targeted microorganism sequence bases that appear in sequencing reads',
        'Average nucleotide identity of majority consensus sequence to targeted microorganism reference sequences',
        'The number of reads that aligned to the organism\'s target genes',
        'Median depth of reads aligned to targeted microorganism reference sequences, indicating the median number of times each targeted microorganism sequence base appears in sequencing reads',
        'Normalized representation of the number of reads aligned to targeted microorganism reference sequences (aligned reads per kilobase of targeted sequence per million reads)',
        'Numerical absolute quantification value'
    ]
    out3_file = open("%s.VSPv2.viral_variants.vcf" % (out), "w")
    out3_file.write("##fileformat=VCFv4.2\n##source=DRAGEN Microbial Enrichment Plus\n"
                    "##INFO=<ID=AF,Number=1,Type=Float,Description=\"Allele Frequency\">\n"
                    "##INFO=<ID=DP,Number=1,Type=Integer,Description=\"Read Depth\">\n"
                    "##INFO=<ID=SG,Number=1,Type=String,Description=\"Segment Name\">\n"
                    "##INFO=<ID=gene,Number=1,Type=String,Description=\"gene Name\">\n"
                    "##INFO=<ID=annotation,Number=1,Type=String,Description=\"Type of change (e.g. \"Nonsynonymous Variant\")\">\n"
                    "##INFO=<ID=product,Number=1,Type=String,Description=\"The protein product of the gene\">\n")
    out3_file.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
    for species in microorganisms:
        if re.search('viral', species['class']):
            value_name = []
            value_name.append(species['name'])  # Microorganism
            value_name.append(species['predictionInformation']['predictedPresent'])  # Present
            accessions = ""
            if 'consensusGenomeSequences' in species:  ###############output consensus sequences
                out4_file = open("%s.%s.fa" % (out, species['name']), "w")
                for key in species[
                    'consensusGenomeSequences']:  # Consensus genome information. Included for RPIP viruses only.
                    accessions += key['referenceAccession'] + ";"
                    out4_file.write(">%s|reference:%s|description:%s|reference_length:%s|maximum_alignment_length:%s"
                                    "|maximum_gap_length:%s|maximum_unaligned_length:%s"
                                    "|coverage:%s|ani:%s|aligned_read_count:%s"
                                    "|median_depth:%s\n%s\n"
                                    % (species['name'], key['referenceAccession'], key['referenceDescription'],
                                       key['referenceLength'],
                                       key['maximumAlignmentLength'], key['maximumGapLength'],
                                       key['maximumUnalignedLength'],
                                       key['coverage'], key['ani'], key['alignedReadCount'], key['medianDepth'],
                                       key['sequence']))
                out4_file.close()
            ################################################################step3:The variants object is only present for select viruses
            if 'variants' in species:
                for variant in species['variants']:
                    if not 'segment' in variant:
                        variant['segment'] = "None"
                    out3_file.write("%s\t%s\t.\t%s\t%s\t.\tPASS\tAF=%s;DP=%s;SG=%s" % (
                        variant['referenceAccession'], variant['referencePosition'], variant['referenceAllele'],
                        variant['variantAllele'],
                        variant['alleleFrequency'], variant['depth'], variant['segment']))
                    if 'gene' in variant:
                        out3_file.write(f";gene={variant['gene']}")
                    if 'annotation' in variant:
                        out3_file.write(f";annotation={variant['annotation']}")
                    if 'product' in variant:
                        out3_file.write(f";product={variant['product']}")
                    out3_file.write("\n")
            ################################################################
            value_name.append(accessions.strip(";"))  # Accessions
            value_name.append(format(float(species['coverage'] * 100), ".2f"))  # Coverage
            value_name.append(format(float(species['ani']) * 100, ".2f"))  # ANI
            value_name.append(format(int(species['alignedReadCount']), ","))  # Alinged Reads
            value_name.append(species['medianDepth'])  # Median Depth
            value_name.append(species['rpkm'])  # RPKM
            if 'absoluteQuantityRatio' in species:  # Absolute Quantity
                value_name.append(species['absoluteQuantityRatio'])
            else:
                value_name.append("NA")
            for i in range(0, len(value_name)):
                if i == 0:
                    out2_file.write(f"\n{value_name[i]}")
                else:
                    out2_file.write(f"\t{value_name[i]}")
    out2_file.close()
    out4_file.close()
end = time.time()
print("Elapse time %s seconds" % (end - start))
    ########################################step3:Antimicrobial Resistance Markers