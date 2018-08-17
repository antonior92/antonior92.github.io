---
title: 'Byrd-Omojokun Trust-Region SQP'
date: 2017-06-26
permalink: /posts/2017/06/Byrd-Omojokun/
tags:
  - GSoC 2017
  - Python
  - Scipy
  - Mathematical Programming
  - Optimization
  - Trust-Region Method
  - Equality-constrained Nonlinear Programming
---

During the previous two weeks I have been implementing a 
trust-region Sequential Quadratic Programming (SQP) method. 
This method is able to solve the equality-constrained
nonlinear programming problem:

\begin{eqnarray}
  \min_x && f(x), \\\\\\
   \text{subject to } && c(x) = 0. \\\\\\
\end{eqnarray}

Quadratic Programming Subproblem
--------------------------------

Ideally at each iteration this method would solve the following
trust-region quadratic programming (QP) subproblem
in order to compute the step update $p_k$:

\begin{eqnarray}
  \min_p && \nabla f(x_k)^T p + \frac{1}{2} p^T \nabla^2_{xx} \mathcal{L}(x_k, \lambda_k)^T p, \\\\\\
   \text{subject to } && A(x_k)p + c(x_k) = 0; \\\\\\
   && \\|p\\| \le \Delta_k,
\end{eqnarray}

where $\nabla f(x_k)^T$ is the function gradient, $\nabla^2_{xx} \mathcal{L}(x_k, \lambda_k)^T$
is the Hessian (in relation to the variable $x$) of the Lagrangian, $c(x_k)$ is the constraint
and $A(x_k)$ is the Jacobian of the constraint evaluated at $x_k$.

Note that this problem may not be feasible, since the linear constraints
may not be compatible with the trust-region constraints, as illustrated in the figure
bellow:

![screenshot 2017-06-09 13 52 38](https://antonior92.github.io/files/TrustRegionSQP.png)

According to Nocedal and Wright \[1\](p. 546):

> To resolve the possible conflict between the linear constraints  and the trust-region constraints, 
it is not appropriate simply to increase the trust-region until the step satisfying the 
linear constraints intersects the trust region. This approach would defeat the purpose of using the 
trust region in the first place as a way to define a region within which we trust the model to accurately
reflect the behavior of the objective and constraint functions. Analytically, it would harm the convergence
properties of the algorithm.

> A more appropriate viewpoint is that there is no reason to satisfy the linearized constraints exactly 
at every step; rather, we should aim to improve the feasibility of these constraints at each step and to
satisfy them exactly only if the trust-region constraint permits it. 

The Byrd-Omojokun approach \[4\] to deal with the incompatibility 
of the linear constraints is to modify the QP subproblem
allowing more flexibility.
This approach solves the subproblem:

\begin{eqnarray}
  \min_p && \nabla f(x_k)^T p + \frac{1}{2} p^T \nabla^2_{xx} \mathcal{L}(x_k, \lambda_k) d, \\\\\\
   \text{subject to } && A(x_k)p + c(x_k) = r_k; \\\\\\
   && \\|p\\| \le \Delta_k,
\end{eqnarray}

where $r_k$ is adjusted such that the constraints are always compatible.
This problem is solved in a two steps procedure:

1. The first step is to solve the subproblem:

\begin{eqnarray}
  \min_v && \\|A(x_k)v + c(x_k)\\|^2, \\\\\\
   \text{subject to } && \\|v\\| \le \eta \Delta_k,
\end{eqnarray}
for $0<\eta<1$ (In our implementation $\eta=0.8$ is being used).

Denoting the solution of the above subproblem $v_k$ we define $r_k$ as:
\begin{equation}
  r_k = A(x_k)v + c_k.
\end{equation}
Note that for this choice of $r_k$ the linear constraints $A(x_k)p + c(x_k) = r_k$ 
are always compatible with trust-region constraints $\\|p\\| \le \Delta_k$.

2. The second step is to solve the subproblem:
\begin{eqnarray}
  \min_p && \nabla f(x_k)^T p + \frac{1}{2} p^T \nabla^2_{xx} \mathcal{L}(x_k, \lambda_k) p, \\\\\\
   \text{subject to } && A(x_k)p + c(x_k) = r_k; \\\\\\
   && \\|p\\| \le \Delta_k,
\end{eqnarray}
for the value of $r_k$ computer at the last step.

Both substeps are solved in rather economical fashion using efficient methods to
get an *inexact* solution to each of the subproblems. The first step is solved using
a variation of the *dogleg* procedure (described in \[2\], p.886)
and the second step using the projected conjugate gradient algorithm described on the previous blog
post ([link](https://antonior92.github.io/posts/2017/05/projected-CG/))

Algorithm Overview
------------------

There are a few points about this algorithm that deserve some attention.
The first of them is that while the solution of the trust-region QP subproblem
doesn't gives a way of calculating the Lagrange multipliers $\lambda_k$,
these Lagrange multipliers are still needed in order to compute
$\nabla^2_{xx} \mathcal{L}(x_k, \lambda_k)$.

An approximation of those Lagrange multipliers is obtained 
minimizing a least squares problem, as described in \[1\],
p. 539. The basic idea is to try to select the Lagrange multipliers
such that the first-order optimality condition:
\begin{equation}
\\|\nabla_{x} \mathcal{L}(x^\*, \lambda^\*)\\| = \\|\nabla f(x^\*) + A(x^\*)\lambda^\*\\| = 0,
\end{equation}
is satisfied as closely as possible on a given point $x_k$ (That is not necessarily
optimum). This is done by selecting $\lambda_k$ as the solution to the least squares
problem:
\begin{equation}
\min_\lambda \\|\nabla f(x_k) + A(x_k)\lambda\\| = 0.
\end{equation}

Another important element of the algorithm is the merit function:
\begin{equation}
\phi(x; \mu) = f(x) + \mu \\|c(x)\\|.
\end{equation}
It combines the constraints and the objective function
into a single number that can be used to compare two
points and to reject or accept a given step.
The penalty parameter $\mu$ is usually update
through the iterations and it is important for the global convergence
of the algorithm it to be monotonically increasing. Some guidelines about
how to choose it are provided on \[2\], p.891.


The trust region radius selection and the step rejection mechanism
are both based on the ratio $\rho_k$. This ratio measures the 
agreement between the model and the obtained results. It
is computed as:
\begin{equation}
\rho_k = \frac{\text{actual reduction}}{\text{predicted reduction}},
\end{equation}
where:
\begin{equation}
\text{actual reduction} = \phi(x_k; \mu) -  \phi(x_k + p_k; \mu),
\end{equation}
is the reduction on the merit function. And:
\begin{equation}
\text{predicted reduction} = q_{\mu}(0) -  q_{\mu}(p_k),
\end{equation}
is the reduction of the local model:
\begin{equation}
q_{\mu}(p) = \nabla f(x_k)^T p + \frac{1}{2} p^T \nabla^2_{xx} \mathcal{L}(x_k, \lambda_k) p + \mu\\|c(x_k)+A(x_k)p\\|.
\end{equation}

The algorithm basic steps for a single iteration are summarized next:

- Compute $f(x_k)$, $\nabla f(x_k)$, $c(x_k)$ and $A(x_k)$;
- Compute least squares Lagrange multipliers $\lambda_k$;
- Compute $\nabla^2_{xx} \mathcal{L}(x_k, \lambda_k)$;
- Apply dogleg method in order to compute $v_k$ and $r_k$ (such that the resulting problem is feasible);
- Compute $p_k$ using the projected CG method;
- Choose penalty parameter $\mu_k$;
- Compute reduction ratio $\rho_k$;
- Accept or reject step $p_k$ depending on reduction ratio $\rho_k$;
- Enlarge or reduce trust-radius depending on reduction ratio $\rho_k$;




Test Results
------------

Next I present the results of the implemented solver on the test problem ``ELEC`` from the CUTEst
collection.

This problem is described in \[3\], problem 2, and consist of given $n_p$ electrons, find the 
equilibrium state distribution (of minimal Coulomb potential) of the electrons positioned on a 
conducting sphere.

The performance of other commercial solvers (according to \[1\]) is presented on the table bellow:
![screenshot 2017-06-22 18 04 34](https://antonior92.github.io/files/ELECtable.png)

I choose this problem because the KNITRO package performs well on it, so our solver is expected to perform well on it as well, since the underlying principle is the same.

For $n_p = 200$ the performance of our implementation is:

    time = 6.3 sec
    f = 1.84391e+04 
    c violation = 1.3e-15
    optimality = 3.5e-07
    niter = 103
    
The execution time is very competitive and the final value of ``f`` 
seems very close to the one obtained by the KNITRO package. 
The constraint violation also seems to be ok.
 
The norm of the gradient of the Lagrangian $\\|\nabla_{x} \mathcal{L}(x, \lambda) \\|$ should be zero
at the solution point and is used as a measure of the optimality along the iterations. It is displayed
on the graph bellow:

![optimality_elec](https://antonior92.github.io/files/optimality_elec_soc.png)

The decay of this optimality measure seems consistent along the interactions.

This SQP equality constrained solver is one of the elements of an
interior points method that will be described in the following
posts.


References
----------
\[1\]&nbsp;&nbsp;&nbsp;[Jorge Nocedal, and Stephen J. Wright. "Numerical optimization"
Second Edition (2006).][1]

\[2\]&nbsp;&nbsp;&nbsp; [Richard H. Byrd, Mary E. Hribar, and Jorge Nocedal. "An interior point algorithm for large-scale nonlinear programming." SIAM Journal on Optimization 9.4 (1999): 877-900.][2]

\[3\]&nbsp;&nbsp;&nbsp;  [Dolan, Elizabeth D., Jorge J. Moré, and Todd S. Munson. "Benchmarking optimization software with COPS 3.0." Argonne National Laboratory Research Report (2004).][3]

\[4\]&nbsp;&nbsp;&nbsp; [Marucha Lalee, Jorge Nocedal, and Todd Plantenga. "On the implementation of an algorithm for large-scale equality constrained optimization." SIAM Journal on Optimization 8.3 (1998): 682-706.][4]


[1]: http://www.bioinfo.org.cn/~wangchao/maa/Numerical_Optimization.pdf

[2]: http://ai2-s2-pdfs.s3.amazonaws.com/0c1c/4bbdd7467c5ba1818b2e7a360e768b067d2c.pdf

[3]: ftp://140.221.6.23/pub/tech_reports/reports/TM-273.pdf

[4]: https://pdfs.semanticscholar.org/f60c/96056858acc5a582587d19b065fd72175daa.pdf

