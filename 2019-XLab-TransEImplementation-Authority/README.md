# 2019-XLab-TransEImplementation
[TOC]

------

## Introduction

Transforms triples into low-dimensional vectors, which we call embedding vectors. After they become vectors, many mathematical methods can be used for further processing.

## How to Build

### Environment Requirements

- **OS**: macOS Catalina 10.15.2
- **IDE**: PyCharm 2019.3
- **libraries**: _pickle, numpy, theano

### Get the Project

- get the code from gitlab/github
	
	> git clone https://github.com/baiyanquan/2019-XLab-TransEImplementation.git

### Import the Project to IDE
Open the project in PyCharm and checkout to Authority branch.

## How to Run

1. put your data to `data/`
2. run `WN/WN_parse.py` first to generate `.pkl`
3. run `WN/WN_TransE.py` to train TransE model
4. run `WN/WN_test.py` to test your TransE model

## How to Use

- generate `.pkl` files
- train TransE mode
- test TransE mode
- validate TransE mode

## Code Structure

```
.
├── FB
│   ├── FB_evaluation.py
│   ├── FB_parse.py
│   ├── FB_test.out
│   └── FB_test.py
├── LICENSE.md
├── README.md
├── WN
│   ├── WN_TransE
│   │   ├── best_valid_model.pkl
│   │   ├── current_model.pkl
│   │   ├── current_state.pkl
│   │   └── orig_state.pkl
│   ├── WN_TransE.out
│   ├── WN_TransE.py
│   ├── WN_evaluation.py
│   ├── WN_parse.py
│   ├── WN_test.out
│   ├── WN_test.py
│   └── test
│       ├── best_valid_model.pkl
│       ├── current_model.pkl
│       ├── current_state.pkl
│       └── orig_state.pkl
├── WN_exp.py
├── data
│   └── wordnet-mlj12
│       ├── README
│       ├── Wordnet3.0-LICENSE
│       ├── wordnet-mlj12-definitions.txt
│       ├── wordnet-mlj12-test.txt
│       ├── wordnet-mlj12-train.txt
│       └── wordnet-mlj12-valid.txt
├── doc
│   └── Train Time - Loss figure.png
├── dockerfile
├── model.py
└── run.sh

7 directories, 31 files
```

