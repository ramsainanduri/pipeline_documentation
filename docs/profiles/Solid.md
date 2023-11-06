## Solid


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
- **HTML_Report:** An HTML documentation report is a text-based file format used to present information in a web browser, including text, images, and hyperlinks, typically used for displaying project documentation and results
- **Markdown_Files:** A Markdown file is a lightweight markup language used to format and structure plain text documents, often used for creating documentation, README files, and notes


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
      <td>BIOMARKERS_TO_JSON</td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.9.2</td>
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
      <td>CNVKIT2SCARHRD</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>CNVKIT_BACKBONE</td>
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
      <td>CNVKIT_CALL_TC</td>
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
      <td>CNVKIT_EXONS</td>
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
      <td>COYOTE_SEGMENTS</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
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
      <td>FFPE_PON_FILTER</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
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
      <td>FILTER_MANTA</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>FILTER_MANTA_TUMOR</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
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
      <td>GATK2VCF</td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.9.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>GATKCOV_BAF</td>
      <td><a href="https://gatk.broadinstitute.org/hc/en-us" target="_blank">gatk4</a></td>
      <td>v4.1.9.0-SNAPSHOT</td>
      <td>https://github.com/broadinstitute/gatk/issues</td>
    </tr>
    <tr>
      <td>GATKCOV_CALL</td>
      <td><a href="https://gatk.broadinstitute.org/hc/en-us" target="_blank">gatk4</a></td>
      <td>v4.1.9.0-SNAPSHOT</td>
      <td>https://github.com/broadinstitute/gatk/issues</td>
    </tr>
    <tr>
      <td>GATKCOV_COUNT</td>
      <td><a href="https://gatk.broadinstitute.org/hc/en-us" target="_blank">gatk4</a></td>
      <td>v4.1.9.0-SNAPSHOT</td>
      <td>https://github.com/broadinstitute/gatk/issues</td>
    </tr>
    <tr>
      <td>GENEFUSE</td>
      <td><a href="nan" target="_blank">genefuse</a></td>
      <td>v0.8.0</td>
      <td>-</td>
    </tr>
    <tr>
      <td>GENEFUSE_JSON_TO_VCF</td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v3.9.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>JOIN_FUSIONS</td>
      <td><a href="https://github.com/J35P312/SVDB" target="_blank">svdb</a></td>
      <td>v2.2.0</td>
      <td>https://github.com/J35P312/SVDB/issues</td>
    </tr>
    <tr>
      <td>JOIN_TUMOR</td>
      <td><a href="https://github.com/J35P312/SVDB" target="_blank">svdb</a></td>
      <td>v2.2.0</td>
      <td>https://github.com/J35P312/SVDB/issues</td>
    </tr>
    <tr>
      <td>LOWCOV</td>
      <td><a href="https://github.com/biod/sambamba" target="_blank">sambamba</a></td>
      <td>v0.8.0</td>
      <td>https://github.com/biod/sambamba/issues</td>
    </tr>
    <tr>
      <td>MANTA</td>
      <td><a href="https://github.com/Illumina/manta" target="_blank">manta</a></td>
      <td>v1.6.0</td>
      <td>https://github.com/Illumina/manta/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v2.7.15</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MANTA_FUSIONS</td>
      <td><a href="https://github.com/Illumina/manta" target="_blank">manta</a></td>
      <td>v1.6.0</td>
      <td>https://github.com/Illumina/manta/issues</td>
    </tr>
    <tr>
      <td></td>
      <td><a href="https://www.python.org/" target="_blank">python</a></td>
      <td>v2.7.15</td>
      <td>-</td>
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
      <td>MERGE_GATK_TUMOR</td>
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
      <td>MSISENSOR</td>
      <td><a href="nan" target="_blank">msisensor-pro</a></td>
      <td>v1.2.0</td>
      <td>-</td>
    </tr>
    <tr>
      <td>PON_FILTER</td>
      <td><a href="https://www.perl.org/" target="_blank">perl</a></td>
      <td>v5.26.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SCARHRD</td>
      <td><a href="nan" target="_blank">Rscript</a></td>
      <td>v4.1.0</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SENTIEON_QC</td>
      <td><a href="https://support.sentieon.com/manual/" target="_blank">sentieon</a></td>
      <td>v202112</td>
      <td>-</td>
    </tr>
    <tr>
      <td>SEQTK</td>
      <td><a href="https://github.com/lh3/seqtk" target="_blank">seqtk</a></td>
      <td>v1.3-r106</td>
      <td>https://github.com/lh3/seqtk/issues</td>
    </tr>
    <tr>
      <td>SNPEFF</td>
      <td><a href="https://github.com/pcingola/SnpEff" target="_blank">snpEff</a></td>
      <td>v4.3t</td>
      <td>https://github.com/pcingola/SnpEff/issues</td>
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
