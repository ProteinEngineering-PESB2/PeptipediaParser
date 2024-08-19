# Peptipedia v2.0: A peptide sequence database and user-friendly web platform. A major update


This repository contains reproducible data preprocessing for creating the Peptipedia database. <br>
Gabriel Cabas-Mora<sup>1</sup>, Anamaría Daza<sup>2</sup>, Nicole Soto-García<sup>1</sup>, Valentina Garrido<sup>1</sup>, Diego Alvarez<sup>3,4</sup>, Marcelo Navarrete<sup>3,4</sup> , Lindybeth Sarmiento-Varón<sup>3</sup>, Julieta H. Sepúlveda<sup>5</sup>, Álvaro Olivera-Nappa<sup>2</sup>, Mehdi D. Davari<sup>6</sup>, Roberto Uribe-Paredes<sup>1</sup> and David Medina-Ortiz<sup>1,2*</sup>.<br>

Peptipedia v2.0: A peptide sequence database and user-friendly web platform. A major update <br>

https://www.biorxiv.org/content/10.1101/2024.07.11.603053v1<br>

<sup>*1*</sup><sub>Departamento de Ingeniería en Computación, Universidad de Magallanes, Av. Pdte. Manuel Bulnes 01855, 6210427, Punta Arenas, Chile.</sub> <br>
<sup>*2*</sup><sub>Centre for Biotechnology and Bioengineering, CeBiB, Universidad de Chile, Avenida Beauchef 851, 8320000, Santiago, Chile.</sub> <br>
<sup>*3*</sup><sub>Centro Asistencial de Docencia e Investigación, CADI, Universidad de Magallanes, Av. Los Flamencos 01364, 6210005, Punta Arenas, Chile.</sub> <br>
<sup>*4*</sup><sub>Escuela de Medicina, Universidad de Magallanes, Av. Pdte. Manuel Bulnes 01855, 6210427, Punta Arenas, Chile.</sub> <br>
<sup>*5*</sup><sub>Facultad de Ciencias de la Salud, Universidad de Magallanes, Av. Pdte. Manuel Bulnes 01855, 6210427, Punta Arenas, Chile.</sub> <br>
<sup>*6*</sup><sub>Department of Bioorganic Chemistry, Leibniz Institute of Plant Biochemistry, Weinberg 3, 06120, Halle, Germany.</sub> <br>
<sup>*\**</sup><sub>Corresponding author</sub> <br>

---
## Table of Contents
- [A summary of the proposed work](#summary)
- [Requirements and instalation](#requirements)
---

<a name="summary"></a>

# Peptipedia v2.0: A peptide sequence database and user-friendly web platform. A major update
In recent years, peptides have gained significant relevance due to their therapeutic properties. The surge in peptide production and synthesis has generated vast amounts of data, enabling the creation of comprehensive databases and information repositories. Advances in sequencing techniques and artificial intelligence have further accelerated the design of tailor-made peptides. However, leveraging these techniques requires versatile and continuously updated storage systems, along with tools that facilitate peptide research and the implementation of machine learning for predictive systems. This work introduces Peptipedia v2.0, one of the most comprehensive public repositories of peptides, supporting biotechnological research by simplifying peptide study and annotation. Peptipedia v2.0 has expanded its collection by over 45% with peptide sequences that have reported biological activities. The functional biological activity tree has been revised and enhanced, incorporating new categories such as cosmetic and dermatological activities, molecular binding, and anti-ageing properties. Utilizing protein language models and machine learning, more than 90 binary classification models have been trained, validated, and incorporated into Peptipedia v2.0. These models exhibit average sensitivities and specificities of 0.877 ± 0.0530 and 0.873 ± 0.054, respectively, facilitating the annotation of more than 3.6 million peptide sequences with unknown biological activities, also registered in Peptipedia v2.0. Additionally, Peptipedia v2.0 introduces description tools based on structural and ontological properties and user-friendly machine-learning tools to facilitate the application of machine-learning strategies to study peptide sequences. Peptipedia v2.0 is accessible under the Creative Commons CC BY-NC-ND 4.0 license at https://peptipedia.cl/.

<a name="requirements"></a>

## Requirements and instalation.

This preprocessing workflow uses some python libraries listed on requirements.txt.
The raw data and auxiliar data used in this workflow are stored [here](https://drive.google.com/drive/folders/1IDNhWmROMfdpgj6ADunBgVb0YBBBaJui?usp=drive_link).

## Execute workflow.
Using an appropiate conda environment, and adding auxiliar_data and raw_data to main path, execute run_processing.sh.