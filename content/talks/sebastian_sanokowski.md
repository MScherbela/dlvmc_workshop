+++
title = "Variational Annealing on Graphs for Combinatorial Optimization"
presenter = "Sebastian Sanokowski"
affiliation = "University of Linz"
start_time = 2023-07-03T15:45:00+00:00
end_time = 2023-07-03T16:30:00+00:00
session = 2
is_break = 0
+++

Several recent methods in unsupervised learning utilize probabilistic approaches to address combinatorial optimization (CO) problems by assuming statistical independence among solution variables. We demonstrate that this assumption imposes limitations on performance, particularly for challenging problem instances. Our findings support the notion that an autoregressive approach, which captures statistical dependencies among solution variables, achieves superior performance on popular CO problems. We introduce subgraph tokenization, a technique that represents the configuration of a set of solution variables using a single token. This tokenization method mitigates the drawback of the lengthy sequential sampling procedure inherent in autoregressive methods, while still maintaining expressive power. Notably, we provide theoretical justification for an annealed Free Energy regularization and empirically demonstrate its crucial role in facilitating efficient and stable learning.
(Note: We solve CO problems by formulating them as Ising Models)
