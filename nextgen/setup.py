#!/usr/bin/env python
"""Setup file and install script for NextGen sequencing analysis scripts.
"""
from setuptools import setup, find_packages

setup(name = "bcbio-nextgen",
      version = "0.1",
      author = "Brad Chapman",
      author_email = "chapmanb@50mail.com",
      description = "Automated nextgen sequencing analysis coupled with Galaxy",
      license = "BSD",
      url = "http://bcbio.wordpress.com",
      namespace_packages = ["bcbio"],
      packages = find_packages(),
      scripts = ['scripts/align_summary_report.py',
                 'scripts/analyze_finished_sqn.py',
                 'scripts/analyze_quality_recal.py',
                 'scripts/automated_initial_analysis.py',
                 'scripts/gatk_genotyper.py',
                 'scripts/illumina_finished_msg.py',
                 'scripts/picard_gatk_recalibrate.py',
                 'scripts/picard_maq_recalibrate.py',
                 'scripts/picard_sam_to_bam.py',
                 'scripts/solexa_qseq_to_fastq.py',
                 'scripts/upload_to_galaxy.py'],
      package_data = {
          'config' : ['*.yaml'],
          }
      )
