---
layout: default
title:
permalink: /msc
---



## Project \#1: Machine Learning Tools for Automated Image-based ECG

*In collaboration with  [Fabio Bonassi](https://bonassifabio.github.io/) and [Jiawei Li](https://www.uu.se/en/contact-and-organisation/staff?query=N25-547)*.

Cardiovascular diseases are the leading cause of death worldwide, and the electrocardiogram (ECG)
remains essential for their diagnosis. While most AI research has focused on raw ECG signals, hospitals and telehealth 
systems often store ECGs as images, creating new challenges and opportunities for automated analysis. This project will 
investigate deep learning methods tailored to image-based ECGs, aiming to improve interpretability, robustness to noise
and artifacts, and clinical relevance. As part of the work, you will gain experience with cutting-edge computer vision 
techniques, work on some of the world’s largest open ECG datasets, and contribute to developing AI tools with direct 
clinical impact.

**Some relevant literature:**

* “[Automatic diagnosis of the 12-lead ECG using a deep neural network](https://doi.org/10.1038/s41467-020-15432-4)”. Nat Commun, 2020\.
* [Automated multilabel diagnosis on electrocardiographic images and signals.](https://doi.org/10.1038/s41467-022-29153-3)  Nat Commun, 2022\.

**Prerequisites:** Linear algebra, programming (Python), statistical machine learning, and deep learning. Knowledge of signal processing techniques is a merit.


----

## Project \#2: Federated Learning for Physiological Signals

*In collaboration with  [José Mairton Barros da Silva Jr.](https://user.it.uu.se/~josba597/)*

Strict regulations on patient data protection in Sweden and many other countries limit how medical data
can be stored, processed, and shared, creating challenges for developing and maintaining high-quality machine learning 
algorithms for ECG interpretation. This thesis will investigate federated learning methods as a privacy-preserving
alternative to centralized training, with a focus on ECG analysis. The goal is to develop frameworks that enable 
collaborative model training across healthcare institutions while ensuring compliance with data protection laws
and maintaining model performance. The student will implement and evaluate federated learning approaches in which
models are trained locally and only model parameters—not patient data—are shared, and may also explore techniques 
such as differential privacy and strategies for robust performance evaluation.

**Some relevant literature:**

* “[Automatic diagnosis of the 12-lead ECG using a deep neural network](https://doi.org/10.1038/s41467-020-15432-4)”. Nat Commun, 2020\.   
*  “[Communication-Efficient Learning of Deep Networks from Decentralized Data](https://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf),” AISTATS, 2016\.  
* [Federated machine learning in healthcare: A systematic review.](https://doi.org/10.1016/j.xcrm.2024.101419) Cell reports, 2024\.  
* [The future of digital health with federated learning](https://doi.org/10.1038/s41746-020-00323-1).npj Digit. Med, 2020\.

**Prerequisites:** Linear algebra, programming (Python), statistical machine learning, and deep learning. Knowledge of signal processing techniques is a merit.


----

## Project \#3: Machine Learning Tools for Breathing Signals
*In collaboration with researchers from Karolinska Institutet [Artin Arshmian](https://ki.se/personer/artin-arshamian) and [Reza Baboukani](https://ki.se/en/people/reza-ebrahimian-baboukani)*.

 Breathing patterns are not only vital for sustaining life but also carry rich information: a recent 
study in Current Biology (Soroka et al., 2025) showed that long-term nasal airflow contains unique “respiratory 
fingerprints” that can identify individuals with near-biometric accuracy (∼97%) and correlate with physiological 
traits such as body mass index (BMI) and emotional state. Yet, these results were restricted to nasal breathing, 
leaving open questions about whether similar signatures exist in oral breathing and whether combining nasal/oral 
breathing with heart rate signals can improve the prediction of physiological markers. In this project, the student 
will analyze a rich dataset collected under both nasal and oral breathing conditions with synchronized heart rate recordings during rest (5 minutes) and task performance (45 minutes), developing and applying statistical and machine learning models to assess the predictive power of these signals for physiological markers, sex, and age, as well as their potential for individual identification across breathing modes. The work bridges biomedical signal processing, statistical learning, and digital health, with potential implications for novel biomarkers.

**Some relevant literature:**

* [“Humans have nasal respiratory fingerprints,”](https://doi.org/10.1016/j.cub.2025.05.008) *Current Biology*, 2025, 

**Prerequisites:** Linear algebra, programming (Python), statistical machine learning. Knowledge of deep learning and signal processing techniques is a merit.

----

## Project \#4: Distilling ECG segmentation models for differentiable ECG segmentation

Traditional ECG segmentation methods typically rely on combinations of filter banks and thresholding with manually set
parameters, which, while effective, limit flexibility and integration with modern machine learning frameworks. This
project aims to distill knowledge from well-established ECG segmentation algorithms into differentiable models and 
then combine these with limited cardiologist-annotated ECG data to train end-to-end segmentation networks. The approach
leverages the interpretability and robustness of classical signal-processing techniques while enabling gradient-based 
optimization and deep learning integration.



**Some relevant literature:**

* “[Automatic diagnosis of the 12-lead ECG using a deep neural network](https://doi.org/10.1038/s41467-020-15432-4)”. Nat Commun, 2020\.
* "[Wavelet-Based ECG Delineator: Evaluation on Standard Databases](https://diec.unizar.es/~laguna/personal/publicaciones/wavedet_tbme04.pdf)"  IEEE TBME, 2004

**Prerequisites:** Linear algebra, programming (Python), statistical machine learning, and deep learning. Knowledge of signal processing techniques is a merit.

----

## Project \#5: Reinforcement learning to conciliate making measurements and predictions for ECG

This project explores how reinforcement learning can be used to reconcile ECG measurements (e.g., intervals, amplitudes) with predictions
of cardiac abnormalities. The idea is to generate a dataset containing both automated measurements and diagnostic predictions, and then
train a reinforcement learning model—using methods such as GRPO (Generalized Reinforcement Policy Optimization)—to encourage consistency 
between the two outputs. By aligning measurement-based reasoning with prediction-based classification, the resulting model could provide
more interpretable and clinically reliable ECG analysis.

**Some relevant literature:**

* “[Automatic diagnosis of the 12-lead ECG using a deep neural network](https://doi.org/10.1038/s41467-020-15432-4)”. Nat Commun, 2020\.

**Prerequisites:** Linear algebra, programming (Python), statistical machine learning, and deep learning. Knowledge of signal processing techniques is a merit.

----

## Project \#6: Adversarial training for age prediction


----

## Project \#7: Adversarial training for autorregressive models

