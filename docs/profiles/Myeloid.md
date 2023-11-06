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

