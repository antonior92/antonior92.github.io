---
title: 'Equivalent formulations of logistic regression'
date: 2023-08-01
permalink: /posts/2023/08/formulations-logistic
tags:
  - Logistic regression
---

[Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) can be formulated in multiple ways. 
This note clarifies the equivalence between the formulations.

Consider a supervised learning problem with pairs of input and outputs $\\{(x_i, y_i)\\}_{i=1}^n$ 
where $x_i \in \mathbb{R}^n$. Logistic regression can be written as the minimization problem:

\begin{equation}
   \min_\beta \frac{1}{n} \sum_{i=1}^n \ell(y_i, \beta^\top x_i)
\end{equation}
Where $\beta \in \mathbb{R}^n$ is the parameter vector that is being estimated and $\ell$ is the loss function.

- **First formulation:** we consider $y \in \\{-1, +1\\}$ and the loss function
  \begin{equation}
      \ell_1(y_i, \beta^\top x_i) =  - \log\big(\sigma(y_i \beta^\top x_i)\big)
  \end{equation}
    This formulation appear when we want to talk about Logistic regression in more general contexts.
    Many classifiers can be written as:
    \begin{equation}
       \min_\beta \frac{1}{n} \sum_{i=1}^n \ell(y_i \beta^\top x_i)
    \end{equation}
    one traditional example is the hinge loss $\ell(z) = \max\\{0, 1-z\\}$, which is equivalent to SVM with soft margins.
    So writting the logistic regression this can be useful if you want to apply general results to it.

- **Second formulation:**  we consider $y \in \\{0, +1\\}$ and the loss function
  \begin{equation}
   \ell_2(y_i, \beta^\top x_i) =  - y_i \log\big(\sigma (\beta^\top x_i)\big) - (1- y_i) \log\big(\sigma (\beta^\top x_i)\big)
  \end{equation}
  where sigma is a sigmoid $\sigma(z) = (1- \exp(-z))^{-1}$. This second formulation appear when you want to show that ridge regression is the solution of 
maximum likelihood estimation.
  

## Equivalence between formulations

The formulations are equivalent. Assume 
$y \in \\{-1, +1\\}$ and let  $\tilde{y} = \frac{y+1}{2}\in \\{0, +1\\}$ and . That is:
- $\tilde{y}= 1 \Leftrightarrow y= +1$, and;
-  $\tilde{y}= 0 \Leftrightarrow y=-1$,

then,
\begin{equation}
\ell_1(y, \beta^\top x) =  \ell_2(\tilde{y}, \beta^\top x)
\end{equation}

*Proof.* 
On the one hand:
\begin{equation}
    \ell_1(+1, \beta^\top x) = \log(1 + \exp(-\beta^\top x)) = - \log(\sigma(\beta^\top x)) = \ell_2 (+1, \beta^\top x)
\end{equation}

On the other hand:

\begin{eqnarray}
    \ell_1(-1, \beta^\top x) &=& \log(1 + \exp(\beta^\top x)) \\\\\\
 &=&- \log\Big(\frac{1}{1 + \exp(\beta^\top x)}\Big) \\\\\\
 &=&  - \log\Big(\frac{\exp(-\beta^\top x)}{1 + \exp(-\beta^\top x)}\Big) \\\\\\
 &=& - \log(1 - \sigma(\beta^\top x)) \\\\\\
 &=&  \ell_2 (0, \beta^\top x)
\end{eqnarray}



