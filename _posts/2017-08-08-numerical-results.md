---
title: 'Numerical Results'
date: 2017-08-08
permalink: /posts/2017/00/NumericalResults/
tags:
  - GSoC 2017
  - Python
  - Scipy
  - Mathematical Programming
  - Optimization
---

In this blog post, I will present numerical results obtained
solving problems from the CUTEst collection \[1\] using the algorithms
implemented during my GSoC project.

Let us consider two solvers:

1. A Sequential Quadratic Programming (SQP) solver for equality-constrained problems, of the type:
\begin{eqnarray}
  \min_x && f(x), \\\\\\
   \text{subject to } && c(x) = 0. \\\\\\
\end{eqnarray}
A detailed description of this method can be found [here](https://antonior92.github.io/posts/2017/06/Byrd-Omojokun/).
2. An interior point solver capable of solving general nonlinear programing problems of the type:
\begin{eqnarray}
  \min_x && f(x), \\\\\\
   \text{subject to } && c_E(x) = 0,\\\\\\
   && c_I(x) \le 0,
\end{eqnarray}
This solver uses the SQP solver as a substep and is described
[here](https://antonior92.github.io/posts/2017/07/interior-point-method/).

The table bellow describes the performance of the SQP solver on large-scale
equality constrained problems.

|   name   |  n  |  m  | nnz  |  niters  | f evals  | CG iters |   time   |   opt    |  c viol  |
|---------:|----:|----:|-----:|---------:|---------:|---------:|---------:|---------:|---------:|
|  HAGER2  |10001|5000 |15000 |    7     |    7     |    6     |   4.96   |1.6947e-08|1.8914e-12|
|  HAGER3  |10001|5000 |15000 |    7     |    7     |    6     |   4.98   |6.2766e-08|1.8369e-12|
| ORTHREGA |2053 |1024 | 7168 |    73    |   113    |   178    |   9.5    |1.5134e-08|2.0262e-15|
| ORTHREGC |1005 | 500 | 3500 |    42    |    67    |    81    |   0.75   |8.8626e-08|8.1001e-16|
| ORTHREGD*|10003|5000 |25000 |    16    |    16    |    16    |   51.0   |6.5561e-08|7.1054e-13|
| DTOC1ND* |2998 |1996 |13972 |    17    |    17    |    28    |   1.25   |7.4098e-08|2.2138e-13|
|  DTOC2   |2998 |1996 | 7984 |    12    |    12    |   221    |   1.26   |3.8127e-08|6.5081e-12|
|  DTOC3   |14999|9998 |34993 |    10    |    10    |    8     |  26.15   |1.8746e-08|3.5527e-15|
|  DTOC4   |14999|9998 |34993 |    7     |    7     |    6     |   18.5   |2.8176e-08|6.5436e-12|
|  DTOC5   |9999 |4999 |14997 |    9     |    9     |    8     |   7.97   |2.9281e-08|2.0709e-12|
|  DTOC6   |2001 |1000 | 3000 |    19    |    19    |    38    |   0.5    |2.8538e-08|8.0491e-16|
| EIGENA2  |2550 |1275 |125000|    5     |    5     |    4     |   0.39   |2.8422e-14|0.0000e+00|
| EIGENC2  | 462 | 231 | 9261 |    29    |    36    |   295    |   0.43   |7.0736e-08|4.4869e-16|
|  ARTIF   |1002 |1000 | 3000 |    11    |    11    |    0     |   0.16   |0.0000e+00|4.9495e-10|
| BRATU3D  |4913 |3375 |23625 |    6     |    6     |    0     |   6.32   |0.0000e+00|1.7761e-10|

\* Solver is working with non-default initial trust-radius/penalty.

The interior point method was also tested on a set of large-scale problems and the results are
displayed on the table bellow:

|   name   |  n  |  m  | nnz  |  niters  | f evals  | CG iters |   time   |   opt    |  c viol  |
|---------:|----:|----:|-----:|---------:|---------:|---------:|---------:|---------:|---------:|
| CORKSCRW | 456 | 350 | 1050 |    61    |    53    |   177    |   0.62   |1.1608e-08|2.3709e-10|
| COSHFUN* | 61  | 20  | 118  |   393    |   718    |   2408   |   1.69   |2.5143e-08|2.8721e-08|
| DIXCHLNV | 100 | 50  | 2550 |    34    |    25    |   249    |   0.32   |2.2829e-08|5.5511e-16|
|  HAGER4  |2001 |1000 | 3000 |    40    |    31    |   194    |   1.32   |6.7230e-08|1.9438e-12|
| HIMMELBK | 24  | 14  | 336  |    93    |   100    |   100    |   0.32   |5.5796e-08|1.2075e-08|
|  NGONE** | 100 |1273 | 4996 |   1001   |   1953   |   3409   |  121.27  |8.2771e-07|4.0800e-10|
| OPTCNTRL | 32  | 20  |  70  |    64    |    55    |    71    |   0.33   |7.0090e-08|7.8022e-08|
| OPTMASS  |1210 |1005 | 3216 |   152    |   269    |   145    |   2.3    |4.6736e-13|1.8061e-11|
| ORTHREGF |1205 | 400 | 3200 |    37    |    30    |    45    |   1.3    |3.0486e-08|5.7454e-14|
| SVANBERG | 500 | 500 | 4500 |    39    |    31    |   2211   |   2.26   |2.5408e-08|3.0900e-08|
| READING1 | 202 | 100 | 400  |    40    |    56    |    32    |   0.3    |2.6524e-08|1.1029e-10|

\* Solver is working with non-default initial trust-radius/penalty/barrier parameter.

\*\* Fails to convege

For each problem the above tables provides the number of variable ``n``, the number of constraints ``m``, 
the number of nonzero jacobian elements ``nnz``, the number of iterations ``niters``,
the number of function evaluations ``f evals``,  the number of CG iteractions ``CG iters``,
the total running time ``time``, the optimality of the solution ``opt`` (gradient of the lagrangian norm)
and the constraint violation ``c_viol`` (norm of the constraints).

The solver fails to converge with the desired optimality in the problem ``NGONE`` and gets interrupted
for reaching 1000 iteration. Nevertheless it does get very close to a solution.


I have also tested both solvers on many nonlinear small problems to test their robustness.
The results are displayed on the table bellow. For problems with no inequalities constraints
the ``equality_constrained_sqp`` method is used, otherwise the interior point method ``tr_interior_point`` 
is used. This choice is motivated by the fact that the interior point solver does not offers any advantages 
in relation to ``equality_constrained_sqp`` when no inequality constraints are present
and, on the other hand, the SQP solver cannot deals with inequality constraints.

|   name   |  n  |  m  |  niters  | f evals  | CG iters |   time   |   opt    |  c viol  |         method          |
|---------:|----:|----:|---------:|---------:|---------:|---------:|---------:|---------:|:-----------------------:|
|   HS7    |  2  |  1  |    9     |    9     |    8     |   0.02   |1.7663e-15|2.6645e-14|equality_constrained_sqp |
|   HS10   |  2  |  1  |    19    |    14    |    20    |   0.06   |1.6462e-08|1.6433e-08|    tr_interior_point    |
|   HS11   |  2  |  1  |    12    |    8     |    11    |   0.04   |3.5341e-08|2.6238e-09|    tr_interior_point    |
|   HS13   |  2  |  1  |    27    |    18    |    22    |   0.11   |4.1431e-08|4.4427e-08|    tr_interior_point    |
|   HS14   |  2  |  2  |    14    |    9     |    8     |   0.05   |1.1981e-08|1.3775e-09|    tr_interior_point    |
|   HS16   |  2  |  2  |    21    |    15    |    19    |   0.09   |5.9156e-12|3.1605e-14|    tr_interior_point    |
|   HS17   |  2  |  2  |    36    |    28    |    42    |   0.14   |4.1628e-08|2.1239e-10|    tr_interior_point    |
|   HS19   |  2  |  2  |    51    |    43    |    45    |   0.21   |1.7639e-12|1.0397e-14|    tr_interior_point    |
|   HS20   |  2  |  3  |    15    |    11    |    13    |   0.06   |1.0765e-10|7.6798e-13|    tr_interior_point    |
|   HS22   |  2  |  2  |    15    |    11    |    12    |   0.05   |4.4231e-08|2.3549e-09|    tr_interior_point    |
|   HS24   |  2  |  3  |    21    |    13    |    12    |   0.08   |3.1179e-08|1.2526e-16|    tr_interior_point    |
|   HS26   |  3  |  1  |    22    |    22    |    41    |   0.06   |1.2174e-10|4.9481e-08|equality_constrained_sqp |
|   HS28   |  3  |  1  |    3     |    3     |    3     |   0.01   |9.8334e-16|4.4409e-16|equality_constrained_sqp |
|   HS31   |  3  |  1  |    12    |    8     |    18    |   0.05   |6.8221e-08|5.1291e-10|    tr_interior_point    |
|   HS32   |  3  |  2  |    26    |    17    |    23    |   0.12   |1.7249e-08|7.9836e-13|    tr_interior_point    |
|   HS33   |  3  |  2  |    30    |    24    |    25    |   0.11   |5.4584e-08|8.4626e-14|    tr_interior_point    |
|   HS39   |  4  |  2  |    16    |    16    |    18    |   0.04   |1.3941e-11|3.9848e-12|equality_constrained_sqp |
|   HS46   |  5  |  2  |    29    |    49    |    70    |   0.08   |9.4806e-08|3.3307e-16|equality_constrained_sqp |
|   HS51   |  5  |  3  |    10    |    10    |    9     |   0.03   |9.6031e-08|4.4409e-16|equality_constrained_sqp |
|   HS52   |  5  |  3  |    2     |    2     |    2     |   0.01   |3.5527e-15|1.1102e-16|equality_constrained_sqp |
|   HS53   |  5  |  3  |    16    |    8     |    8     |   0.06   |3.5548e-08|1.7764e-15|    tr_interior_point    |
|   HS63   |  3  |  2  |    13    |    8     |    7     |   0.05   |1.2935e-09|1.6548e-08|    tr_interior_point    |
|   HS64   |  3  |  1  |    34    |    30    |    53    |   0.15   |1.2576e-08|6.8588e-11|    tr_interior_point    |
|   HS65   |  3  |  1  |    22    |    17    |    32    |   0.1    |1.1647e-08|1.3055e-08|    tr_interior_point    |
|   HS70   |  4  |  1  |    46    |    50    |    87    |   0.21   |3.6633e-08|5.4290e-14|    tr_interior_point    |
|   HS71   |  4  |  2  |    20    |    15    |    26    |   0.09   |1.9529e-11|2.6958e-10|    tr_interior_point    |
|   HS72   |  4  |  2  |    26    |    21    |    41    |   0.11   |1.5971e-11|2.9104e-11|    tr_interior_point    |
|   HS73   |  4  |  3  |    18    |    14    |    23    |   0.08   |6.6664e-08|8.6237e-08|    tr_interior_point    |
|   HS74   |  4  |  5  |    18    |    12    |    11    |   0.08   |5.9286e-12|2.2775e-09|    tr_interior_point    |
|   HS75   |  4  |  5  |   104    |   101    |   100    |   0.53   |2.4438e-08|8.2036e-10|    tr_interior_point    |
|   HS77   |  5  |  2  |    18    |    20    |    34    |   0.05   |6.3707e-08|3.7303e-14|equality_constrained_sqp |
|   HS78   |  5  |  3  |    5     |    5     |    4     |   0.01   |7.5462e-11|6.1410e-11|equality_constrained_sqp |
|   HS79   |  5  |  3  |    7     |    7     |    12    |   0.02   |1.7792e-11|1.2566e-11|equality_constrained_sqp |
|   HS80   |  5  |  3  |    17    |    10    |    8     |   0.06   |5.5398e-12|7.7953e-10|    tr_interior_point    |
|   HS81   |  5  |  3  |    17    |    10    |    8     |   0.06   |5.5400e-12|7.7953e-10|    tr_interior_point    |
|   HS83   |  5  |  3  |    56    |    47    |    84    |   0.26   |8.5807e-08|1.4211e-14|    tr_interior_point    |
|   HS84   |  5  |  3  |    30    |    21    |    39    |   0.13   |7.9979e-08|2.3283e-10|    tr_interior_point    |
|   HS85*  |  5  | 21  |   142    |   257    |   142    |   0.75   |5.1953e-08|7.0781e-08|    tr_interior_point    |
|   HS86   |  5  | 10  |    21    |    15    |    38    |   0.09   |4.0448e-08|6.5503e-15|    tr_interior_point    |
|   HS93   |  6  |  2  |    26    |    19    |    67    |   0.12   |8.1024e-10|1.0978e-12|    tr_interior_point    |
|   HS95   |  6  |  4  |   181    |   176    |   176    |   0.55   |4.9185e-08|1.8147e-11|    tr_interior_point    |
|   HS96   |  6  |  4  |   226    |   227    |   230    |   0.7    |3.7408e-08|7.4934e-11|    tr_interior_point    |
|   HS97*  |  6  |  4  |   595    |   601    |   630    |   1.87   |2.7109e-08|1.8602e-09|    tr_interior_point    |
|   HS98*  |  6  |  4  |   412    |   413    |   592    |   1.34   |4.1266e-08|2.3293e-09|    tr_interior_point    |
|   HS99** |  7  |  2  |    86    |   142    |   158    |   0.17   |2.6963e-04|2.9104e-11|    tr_interior_point    |
|  HS100   |  7  |  4  |    29    |    22    |    92    |   0.11   |5.4858e-08|3.9712e-14|    tr_interior_point    |
|  HS104*  |  8  |  5  |    47    |    39    |   151    |   0.22   |5.2744e-08|1.5324e-10|    tr_interior_point    |
|  HS105   |  8  |  1  |    46    |    42    |   149    |   0.27   |3.0374e-08|4.9440e-17|    tr_interior_point    |
|  HS106   |  8  |  6  |   256    |   346    |   333    |   0.94   |5.9059e-08|6.8528e-09|    tr_interior_point    |
|  HS107   |  9  |  6  |    17    |    13    |    26    |   0.07   |6.4559e-10|2.6756e-13|    tr_interior_point    |
|  HS108   |  9  | 13  |   112    |   159    |   179    |   0.41   |9.9895e-08|1.3809e-10|    tr_interior_point    |
|  HS109** |  9  | 10  |   1001   |   1001   |   1157   |   4.3    |9.9912e-02|4.4244e+04|    tr_interior_point    |
|  HS111   | 10  |  3  |    27    |    20    |    47    |   0.11   |3.4073e-08|8.4907e-12|    tr_interior_point    |
|  HS112*  | 10  |  3  |    38    |    31    |    74    |   0.17   |1.1989e-08|9.7145e-17|    tr_interior_point    |
|  HS113   | 10  |  8  |    39    |    31    |   115    |   0.15   |4.7649e-08|1.6342e-13|    tr_interior_point    |
|  HS114*  | 10  | 11  |    86    |    88    |   271    |   0.44   |5.3934e-08|2.1956e-12|    tr_interior_point    |
|  HS116   | 13  | 14  |   145    |   157    |   465    |   0.62   |4.3199e-08|1.3091e-12|    tr_interior_point    |
|  HS117   | 15  |  5  |    38    |    29    |   117    |   0.18   |4.8370e-08|4.0625e-13|    tr_interior_point    |
|  HS118   | 15  | 17  |    58    |    49    |    89    |   0.29   |7.7744e-08|1.4211e-14|    tr_interior_point    |
|  HS119   | 16  |  8  |    38    |    29    |   112    |   0.19   |5.3776e-08|8.8818e-16|    tr_interior_point    |


\* Solver is working with non-default initial trust-radius/penalty/barrier parameter.

\*\* Fails to convege

The algorithm fails on ``HS99`` and on ``HS109``. In the first it fails but it does terminate very close to an solution.
And in the problem ``HS109``, it fails because the Jacobian matrix becomes singular.



References
==========
\[1\]&nbsp;&nbsp;&nbsp;  [Gould, Nicholas IM, Dominique Orban, and Philippe L. Toint. "CUTEst: a constrained and unconstrained testing environment with safe threads for mathematical optimization." Computational Optimization and Applications 60.3 (2015): 545-557.][1]


[1]: ftp://www.hsl.rl.ac.uk/pub/nimg/pubs/GoulOrbaToin15_coap.pdf

