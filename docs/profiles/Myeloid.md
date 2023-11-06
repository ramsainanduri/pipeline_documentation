## Myeloid

### Description

The input data for the pipeline consists of fastq files. However, for the pipeline to consume the data, it needs to be provided in the form of a CSV file that includes metadata...


### Input CSV

<div class="table table-striped table-bordered table-hover table-condensed table-responsive">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>sample_id</th>
      <th>type</th>
      <th>assay</th>
      <th>platform</th>
      <th>read1</th>
      <th>read2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>example</td>
      <td>template</td>
      <td>documentation</td>
      <td>mkdocs</td>
      <td>example.1.fastq.gz</td>
      <td>example.2.fastq.gz</td>
    </tr>
  </tbody>
</table>
</div>
### Column Descriptions

- **sample_id:** Text representing the name or id of the sample being analyzed
- **type:** Type of the sample, e.g., tumor or normal
- **assay:** Assay of the sample, e.g., tumorWGS, myeloid, solidtumor, etc.
- **platform:** Name of the platform used for sequencing, e.g., illumina
- **read1:** Full path to the read 1 fastq file
- **read2:** Full path to the read 2 fastq file

### Output Files

- **BAM:** A BAM file is a compressed binary file format used to store and index high-throughput sequencing data, such as DNA sequence reads aligned to a reference genome
- **VCF:** A VCF file is a text file format used to store and annotate genetic variation data, such as single nucleotide polymorphisms (SNPs) and small insertions/deletions (indels), identified from sequencing data.

### Software Versions

<div class="table table-striped table-bordered table-hover table-condensed table-responsive">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Process</th>
      <th>Tool</th>
      <th>Version</th>
      <th>External_Contact_Person</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AGGREGATE_VCFS</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>ANNOTATE_VEP</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>BQSR_UMI</td>
      <td><a href="https://support.sentieon.com/manual/" target="_blank">sentieon</a></td>
      <td>v202112</td>
      <td>-</td>
    </tr>
    <tr>
      <td>BWA_UMI</td>
      <td><a href="https://github.com/lh3/bwa" target="_blank">bwa</a></td>
      <td>v0.7.17-r1188</td>
      <td>https://github.com/lh3/bwa/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://support.sentieon.com/manual/" target="_blank">sentieon</a></td>
      <td>v202112</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CNVKIT_BATCH</td>
      <td><a href="https://cnvkit.readthedocs.io/en/stable/" target="_blank">cnvkit</a></td>
      <td>v0.9.9</td>
      <td>https://github.com/etal/cnvkit/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.7.1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CNVKIT_CALL</td>
      <td><a href="https://cnvkit.readthedocs.io/en/stable/" target="_blank">cnvkit</a></td>
      <td>v0.9.9</td>
      <td>https://github.com/etal/cnvkit/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.7.1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CNVKIT_GENS</td>
      <td><a href="https://cnvkit.readthedocs.io/en/stable/" target="_blank">cnvkit</a></td>
      <td>v0.9.9</td>
      <td>https://github.com/etal/cnvkit/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.7.1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CNVKIT_PLOT</td>
      <td><a href="https://cnvkit.readthedocs.io/en/stable/" target="_blank">cnvkit</a></td>
      <td>v0.9.9</td>
      <td>https://github.com/etal/cnvkit/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.7.1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CONCATENATE_VCFS</td>
      <td><a href="https://github.com/vcftools/vcftools" target="_blank">vcftools</a></td>
      <td>v0.1.16</td>
      <td>https://github.com/vcftools/vcftools/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://genome.sph.umich.edu/wiki/Vt" target="_blank">vt-decompose</a></td>
      <td>v0.5</td>
      <td>Adiran (atks@umich.edu)</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://genome.sph.umich.edu/wiki/Vt" target="_blank">vt-normalize</a></td>
      <td>v0.5</td>
      <td>Adiran (atks@umich.edu)</td>
    </tr>
    <tr>
      <td>CONTAMINATION</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.28.1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CUSTOM_DUMPSOFTWAREVERSIONS</td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.11.0</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://yaml.org/" target="_blank">yaml</a></td>
      <td>v6.0</td>
      <td>-</td>
    </tr>
    <tr>
      <td>FILTER_FOR_CNV</td>
      <td><a href="https://github.com/arq5x/bedtools2" target="_blank">bedtools</a></td>
      <td>v2.30.0</td>
      <td>https://github.com/arq5x/bedtools2/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://github.com/samtools/htslib" target="_blank">bgzip</a></td>
      <td>v1.12</td>
      <td>https://github.com/samtools/htslib/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://github.com/samtools/htslib" target="_blank">tabix</a></td>
      <td>v1.12</td>
      <td>https://github.com/samtools/htslib/issues</td>
    </tr>
    <tr>
      <td>FREEBAYES</td>
      <td><a href="https://github.com/freebayes/freebayes" target="_blank">freebayes</a></td>
      <td>v1.3.5</td>
      <td>https://github.com/freebayes/freebayes/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://github.com/biopet/vcffilter" target="_blank">vcffilter</a></td>
      <td>v1.0.2</td>
      <td>https://github.com/biopet/vcffilter/issues</td>
    </tr>
    <tr>
      <td>LOWCOV</td>
      <td><a href="https://github.com/biod/sambamba" target="_blank">sambamba</a></td>
      <td>v0.8.0</td>
      <td>https://github.com/biod/sambamba/issues</td>
    </tr>
    <tr>
      <td>MARKDUP</td>
      <td><a href="https://support.sentieon.com/manual/" target="_blank">sentieon</a></td>
      <td>v202112</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MARK_GERMLINES</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MERGE_GENS</td>
      <td><a href="https://github.com/arq5x/bedtools2" target="_blank">bedtools</a></td>
      <td>v2.30.0</td>
      <td>https://github.com/arq5x/bedtools2/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://github.com/samtools/htslib" target="_blank">bgzip</a></td>
      <td>v1.12</td>
      <td>https://github.com/samtools/htslib/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://github.com/samtools/htslib" target="_blank">tabix</a></td>
      <td>v1.12</td>
      <td>https://github.com/samtools/htslib/issues</td>
    </tr>
    <tr>
      <td>PON_FILTER</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SENTIEON_QC</td>
      <td><a href="https://support.sentieon.com/manual/" target="_blank">sentieon</a></td>
      <td>v202112</td>
      <td>-</td>
    </tr>
    <tr>
      <td>TNSCOPE</td>
      <td><a href="https://support.sentieon.com/manual/" target="_blank">sentieon</a></td>
      <td>v202010.01</td>
      <td>-</td>
    </tr>
    <tr>
      <td>VARDICT</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://github.com/AstraZeneca-NGS/VarDict" target="_blank">vardict</a></td>
      <td>v1.8.2</td>
      <td>https://github.com/AstraZeneca-NGS/VarDict/issues</td>
    </tr>
    <tr>
      <td>Workflow</td>
      <td><a href="https://www.nextflow.io/" target="_blank">Nextflow</a></td>
      <td>v23.04.2</td>
      <td>https://github.com/nextflow-io/nextflow/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://github.com/Clinical-Genomics-Lund/SomaticPanelPipeline" target="_blank">SomaticPanelPipeline</a></td>
      <td>v1.0dev</td>
      <td>https://github.com/Clinical-Genomics-Lund/SomaticPanelPipeline/issues</td>
    </tr>
  </tbody>
</table>
</div>
