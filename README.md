# Data-Mining

# Drug Activity Analysis

Problem Scenario: 

You are tasked with developing predictive models to determine, given a specific compound, whether it is active (1) or not (0). The compounds are small organic molecules that have the potential to bind to a target site on a receptor, thus exhibiting a desired activity. The first step in drug discovery involves identifying and isolating the receptor, followed by testing numerous small molecules for their binding capabilities. Your goal is to distinguish between active (binding) compounds and inactive (non-binding) ones, which aids in designing new compounds with desirable properties for drug development.

Key Objectives:

1) Feature Selection/Reduction Technique: Implement or utilize a feature selection or reduction technique to identify the most relevant features from the dataset. Since molecules can be represented by thousands of binary features representing their topological shapes and other characteristics, selecting meaningful features can enhance model performance.

2) Experiment with Various Classification Models: Explore and experiment with various classification models to develop the best binary classification model for drug activity prediction. Consider algorithms such as logistic regression, decision trees, random forests, support vector machines (SVM), and others to evaluate their effectiveness in this context.

3) Addressing Imbalanced Data: The dataset provided is likely to be imbalanced, with a potentially unequal distribution between active and inactive compounds. Consider techniques to handle imbalanced data, such as oversampling the minority class, undersampling the majority class, or utilizing more advanced methods like SMOTE (Synthetic Minority Over-sampling Technique).

4) F1 Scoring Metric: Due to the imbalanced nature of the dataset, the F1-score will be used as the scoring metric instead of accuracy. The F1-score considers both precision and recall, making it suitable for imbalanced classification problems. Aim to optimize the F1-score while developing your models.

Task:

Your task is to preprocess the dataset, apply a feature selection or reduction technique, experiment with different classification models, address the issue of imbalanced data, and optimize the F1-score. By achieving these objectives, you will create a robust predictive model for drug activity prediction.

**************************

# Drug Activity Analysis - Adaboost from Scratch

Implementation of Adaboost from Scratch for the above defined Problem scenario

***************************

# K-Means from Scratch

Problem Scenario 1: K-Means with 3 clusters for Iris Dataset

You have been given the famous Iris dataset, which consists of measurements of four different attributes (sepal length, sepal width, petal length, and petal width) for three different species of iris flowers (setosa, versicolor, and virginica). Your task is to apply the K-Means clustering algorithm to this dataset, aiming to cluster the iris flowers into three distinct groups.

Using the K-Means algorithm with three clusters, you need to determine the optimal clustering solution by minimizing the within-cluster sum of squares. By assigning each iris flower to one of the three clusters based on the similarity of their attribute measurements, you aim to discover any underlying patterns or similarities among the different species of iris flowers.

Task:

Your objective is to apply the K-Means algorithm to the Iris dataset, choose an appropriate number of clusters (in this case, three clusters), and interpret the clustering results to gain insights into the relationship between the measured attributes and the species of iris flowers.

*******

Problem Scenario 2: K-Means with 10 clusters for Handwritten Digits

You have a dataset of handwritten digit images, where each image represents a single digit from 0 to 9. The dataset contains a large number of handwritten digit samples with corresponding pixel values representing the intensity of the pixels.

Your task is to apply the K-Means clustering algorithm to this dataset, aiming to cluster the handwritten digit images into ten distinct groups, one for each digit from 0 to 9.

Using the K-Means algorithm with ten clusters, you need to find patterns and similarities among the handwritten digits based on their pixel intensity values. By clustering the digits into distinct groups, you aim to identify common characteristics within each digit category and differentiate between different digit representations.

Task:

Your objective is to apply the K-Means algorithm to the handwritten digits dataset, select the appropriate number of clusters (in this case, ten clusters), and analyze the clustering results to gain insights into the similarities and variations in the handwritten digit representations.
