
# Input Data

The input data for the pipeline consists of fastq files. However, for the pipeline to consume the data, it needs to be provided in the form of a CSV
file that includes metadata. Below is an example of the CSV file format that is expected, along with a detailed description of each column.

Table: Example input data csv file format

<table class="table table-striped table-hover table-condensed table-responsive" style="width: auto !important; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> sample_id </th>
   <th style="text-align:left;"> type </th>
   <th style="text-align:left;"> assay </th>
   <th style="text-align:left;"> platform </th>
   <th style="text-align:left;"> read1 </th>
   <th style="text-align:left;"> read2 </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> example </td>
   <td style="text-align:left;"> template </td>
   <td style="text-align:left;"> documentation </td>
   <td style="text-align:left;"> mkdocs </td>
   <td style="text-align:left;"> example.1.fastq.gz </td>
   <td style="text-align:left;"> example.2.fastq.gz </td>
  </tr>
</tbody>
</table>Table: Column description for input data csv file

<table class="table table-striped table-hover table-condensed table-responsive" style="width: auto !important; margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> Column Name </th>
   <th style="text-align:left;"> Description </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> sample_id </td>
   <td style="text-align:left;"> Text representating the name or id of the sample being analysed </td>
  </tr>
  <tr>
   <td style="text-align:left;"> type </td>
   <td style="text-align:left;"> Type of the sample, eg. tumor or normal </td>
  </tr>
  <tr>
   <td style="text-align:left;"> assay </td>
   <td style="text-align:left;"> Assay of the sample, eg. tumorWGS, myeloid, solidtumor etc </td>
  </tr>
  <tr>
   <td style="text-align:left;"> platform </td>
   <td style="text-align:left;"> Name of the paltform used for sequencing, eg. illumina </td>
  </tr>
  <tr>
   <td style="text-align:left;"> read1 </td>
   <td style="text-align:left;"> Full path to the read 1 fastq file </td>
  </tr>
  <tr>
   <td style="text-align:left;"> read2 </td>
   <td style="text-align:left;"> Full path to the read 2 fastq file </td>
  </tr>
</tbody>
</table>
