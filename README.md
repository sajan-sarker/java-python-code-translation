# Pre-trained Transformers for Java-Python Code Translation

This repository contains the complete implementation, documentation, and results of our direct research project for CSE498R. Our project focuses on developing a two-stage transformer-based system for translating Java code to Python. The system employs CodeT5 for initial Java-to-Python translation and PLBART for refining the translated Python code to correct syntactic and semantic errors while adhering to Pythonic conventions. Fine-tuned on the **[AVATAR-TC](https://github.com/PrithwishJana/CoTran/tree/main/AVATAR-TC)** dataset, the system achieves high translation accuracy, reducing manual effort and errors in code migration.



## 📌 Project Overview
The project leverages pre-trained transformer models, specifically CodeT5 and PLBART, to automate Java-to-Python code translation. The system operates in two stages:
1. **Translation:** CodeT5 translates raw Java code into Python.
2. **Refinement:** PLBART corrects syntactic and semantic errors in the translated Python code and optimizes it for brevity and Pythonic conventions.

### Key Features
- **Two-Stage Translation Pipeline:** CodeT5 translates raw Java code to Python, followed by PLBART for error correction and code optimization.
- **Custom Tokenization:** Incorporates special tokens (NEW_LINE, INDENT, DEDENT) to handle Python's strict formatting requirements.
- **Comprehensive Evaluation:** Assessed using BLEU, CodeBLEU, n-gram match, weighted n-gram match, syntax match, and dataflow match metrics.

### System Workflow Design: 

<img src="https://github.com/sajan-sarker/java-python-code-translation/blob/main/Diagrams/Workflow%20Diagram%20.png?raw=true" alt="System Design" width="400"/>

### Dataset Statistics:

| Sub-dataset        | Train   | Valid | Test |
|-------------------------|------------:|------------:|------------:|
| Aizu               | 14,019  | 41    | 190  |
| AtCoder            | 13,558  | 19    | 97   |
| Codeforces         | 28,311  | 96    | 401  |
| Google CodeJam     | 347     | 1     | 4    |
| LeetCode           | 81      | 7     | 18   |
| GeeksForGeeks      | 3,753   | 268   | 95   |
| AtCoder (extra)    | 110     | 11    | 41   |
| | |  | |
| **Total**          | 55,179  | 443   | 1,746|

## 🛠️ Technologies Used

| Tool               | Purpose                                                                       |
|-------------------------|-------------------------------------------------------------------------------|
| Python3                 | Core programming language                                                     |
| PyTorch                 | Deep neural network (MLP)                                                     |
| Kaggle                  | Cloud-based GPU training                                                      |
| HuggingFace Transformer | Pre-trained model for code translation  |

## 📊 Results Summary

| Step | Model                        | BLEU  | CodeBLEU | n-gram match | Weighted n-gram match | Syntax match | Dataflow match |
|------|------------------------------|-------|----------|---------------|------------------------|---------------|----------------|
| 1    | CodeT5-base                  | 51.72 | 0.4913   | 0.5094        | 0.5274                 | 0.4945        | 0.4338         |
| 2    | CodeT5-base + PLBART-base    | 28.92 | 0.3327   | 0.3290        | 0.3476                 | 0.3432        | 0.3109         |
|      |                              |       |          |               |                        |               |                |
| 1    | CodeT5-small                 | 51.32 | 0.4855   | 0.5067        | 0.5258                 | 0.4947        | 0.4150         |
| 2    | CodeT5-small + PLBART-base   | 41.68 | 0.4418   | 0.4168        | 0.4382                 | 0.4947        | 0.4175         |


## 📈 Future Improvements

- **Dataset Expansion:** Include real-world codebases with libraries, GUIs, and multithreading for better generalization.
- **Runtime Verification:** Integrate automated unit testing to ensure functional correctness.
- **Language-Specific Fine-Tuning:** Enhance handling of idiomatic expressions (e.g., Java's ArrayList vs. Python's list).
- **Bidirectional Translation:** Extend to Python-to-Java and other languages like C++, JavaScript, or Rust.
- **Ethical Considerations:** Address biases in training data and ensure proper licensing of code in datasets.
- **Educational Use:** Develop tools for teaching multi-language programming paradigms with code examples and comparisons.

## 🤝 Contributors

- **Sajan Kumer Sarker – 2111131642**
- **Mahzabeen Rahman Meem – 2021300642**

Faculty Supervisor: **Dr. Mohammad Ashrafuzzaman Khan**  
Department of ECE, North South University
