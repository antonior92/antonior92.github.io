---
title: 'GSoC 2017 - Scipy: Large-scale Constrained Optimization'
date: 2017-05-08
permalink: /posts/2017/05/GSoC-proposal/
tags:
  - GSoC 2017
  - Python
  - Scipy
  - Mathematical Programming
  - Optimization
---

This year I was chosen as the student for Google Summer of Code. I’ll be working on one of the core Python scientific libraries called Scipy. My task is to implement a constrained optimization algorithm able to deal with large (and possibly sparse) problems.

The nonlinear optimization problem consists of finding the value of a vector $x\in \mathbb{R}^n$ that minimizes a function $f(x)$ inside a region $\Omega$. It is very common to specify  $\Omega$ using equality and inequality constraints, as expressed in the following mathematical expression:

\begin{eqnarray}
  \min_x && f(x), \\\\\\
   \text{subject to } && c_E(x) = 0,\\\\\\
   && c_I(x) \le 0,
\end{eqnarray}

where $x\in \mathbb{R}^n$ is a vector of unknowns, $f$ is called the objective function and $c_E$ and $c_I$ are vectorial functions used to delimit the feasible region $\Omega$.

Great many applications can be formulated as the above optimization problem: $x$ could be the control action applied to a robot arm in order to follow a given trajectory, being the function $f(x)$ minimized in order to get the optimal control action while avoiding colliding with obstacles (represented by the constraints); alternatively, the problem could represent the designing of a portfolio of investments to maximize expected  return while maintaining an acceptable level of risk; or, the estimation of parameters of  a model, minimizing the error between the model prediction and the observed values, while imposing a series of constraints to the model. 

It suffice to say that optimization is very important to several applications in engineering, science and finance and I believe that a quality open source solver, as the one I intend to implement, could be of great use to people from diverse areas.

My GSoC accepted proposal can be found in the following [link](https://antonior92.github.io/files/GSoC2017.pdf)
and I will, in the following months, upload content related to aplications and the implementation of the algorithm.


