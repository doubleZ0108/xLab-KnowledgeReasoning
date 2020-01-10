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
Open the project in PyCharm and checkout to master branch.

## How to Run

1. put your data to `data/`
2. run `src/TransE.py` to train TransE model
4. run `src/test.py` to test your TransE model

## How to Use

- train TransE mode
- test TransE mode
- validate TransE mode

## Code Structure

```
.
├── README.md
├── data
│   └── lab
│       ├── entity2id.txt
│       ├── entityVector.txt
│       ├── relation2id.txt
│       ├── relationVector.txt
│       └── train.txt
├── doc
│   ├── Train Time - Loss figure.png
│   └── algorithm.md
└── src
    ├── TransE.py
    ├── TransEReasoning.py
    ├── __pycache__
    │   └── TransE.cpython-37.pyc
    └── test.py

5 directories, 12 files
```

