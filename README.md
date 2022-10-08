# Mall Customer Segmentation

**Context**

This data set is created only for the learning purpose of the customer segmentation concepts, also known as market basket analysis.

**Problem Statement**

You are owing a supermarket mall and through membership cards, you have some basic data about your customers like Customer ID, age, gender, annual income and spending score. Spending Score is something you assign to the customer based on your defined parameters like customer behavior and purchasing data.

---
<br />
<br />

## Table of Contents

1. [Data](#data)
2. [Repository Structure](#repository-structure)
3. [Get started](#get-started)
4. [Requirements](#requirements)
5. [Contact](#mailbox-contact)

---
<br />
<br />

## Data

This dataset is composed by the following five features:

- **CustomerID:** Unique ID assigned to the customer
- **Gender:** Gender of the customer
- **Age:** Age of the customer
- **Annual Income (k$):** Annual Income of the customer
- **Spending Score (1-100):** Score assigned by the mall based on customer behavior and spending nature.

In this particular dataset we have 200 samples to study.

---
<br />
<br />

## Repository Structure

```
File: 01. EDA.ipynb
```

This notebook presents the performed EDA.

```
File: 02. Clustering (HDBSCAN).ipynb
File: 02. Clustering (k-Means).ipynb
File: 02. Clustering (GMM).ipynb
```

Customer segmantation based on HDBSCAN, k-Means and GMM, which splitted the customer in 2 and 5 groups, respectively.

---
<br />
<br />

## Get Started

- Install Python >= 3.7
- Install requirements.txt
- Run 01. EDA.ipynb
- Run 02. Clustering (HDBSCAN).ipynb
- Run 02. Clustering (k-Means).ipynb
- Run 02. Clustering (GMM).ipynb

---
<br />
<br />

## Requirements

- python==3.7
- seaborn==0.11.1
- scikit-learn==0.24.2
- phik==0.11.2
- pandas==1.1.3
- numpy==1.20.3
- matplotlib==3.4.
- hdbscan==0.8.28
- umap==0.5.1

---
<br />
<br />

## :mailbox: Contact

Ioannis E. Livieris (livieris@gmail.com)