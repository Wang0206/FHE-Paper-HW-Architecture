# FHE Hardware Accelerators - Research Papers

A comprehensive curated list of research papers on Fully Homomorphic Encryption (FHE) hardware accelerators from top-tier computer architecture and hardware conferences.

**Time Coverage:** 2015 - Present  
**Target Conferences:** ISCA, MICRO, HPCA, ASPLOS, DAC, DATE, FPGA

> **Status Notice (Repository under construction):** This repository is currently being reconstructed. Please **do not** submit PRs that add/update paper entries (under `papers/`) for now. PRs related to **repository architecture**, **scripts**, **templates**, and **tooling** are welcome.
>
> **状态说明（仓库仍在构建/重构中）：** 当前仓库处于架构重构阶段，暂时**不要**提交新增/更新论文内容（`papers/` 目录）的 PR。欢迎提交与**仓库架构**、**脚本**、**模板**、**工具链**相关的 PR。

**How to contribute:** See [CONTRIBUTING.md](CONTRIBUTING.md).

## LLM prompt example (web UI)

If you use a web-based LLM (ChatGPT/Claude/etc.), you can upload the paper PDF and ask it to fill in our templates.

Copy/paste this prompt and attach the PDF:

```text
I uploaded the original paper PDF and two template file. Read it and produce TWO outputs:

Output A: meta.json (strict JSON)
- Must include keys: title, authors, year, venue, slug, url, key_innovation
- Optional keys: pdf_url, hardware, schemes, tags
- slug must be lowercase kebab-case
- Do NOT invent numbers. If something is unknown, omit the key or use "TODO".

Output B: README.md (Markdown)
- Do NOT paste the paper verbatim. Write your own summary.
- Results: only include numeric results if they appear in the PDF; otherwise write TODO.

Output copyable versions of .json and .md content，do not output the reference source structure in the md file.
Return the two outputs clearly separated, labeled exactly:
--- meta.json ---
{...}
--- README.md ---
# ...
```

## Table of Contents

- [Repository Layout](#repository-layout)
- [Index (by Year)](#index-by-year)
  - [2026](#2026)
  - [2025](#2025)
  - [2024](#2024)
  - [2023](#2023)
  - [2022](#2022)
  - [2021](#2021)
  - [2020](#2020)
  - [2019](#2019)
  - [2018](#2018)
  - [2017](#2017)
  - [2016](#2016)
  - [2015](#2015)
- [Index (by Venue)](#index-by-venue)
  - [ASPLOS](#asplos)
  - [DAC](#dac)
  - [DATE](#date)
  - [HPCA](#hpca)
  - [IEEE-TCAD](#ieee-tcad)
  - [ISCA](#isca)
  - [MICRO](#micro)
- [Contributing](#contributing)
- [License](#license)

## Repository Layout

- `README.md`: Project overview + auto-generated index
- `papers/<year>/<venue>/<slug>/meta.json`: Paper metadata (used to build index)
- `papers/<year>/<venue>/<slug>/README.md`: Per-paper summary
- `templates/`: Templates for `meta.json` and per-paper `README.md`
- `scripts/`: Helper scripts for validating and rebuilding the index

---

<!--
This section is auto-generated.
Run: python3 scripts/build_index.py
-->

<!-- INDEX:START -->

# Index (by Year)

## 2026

### IEEE-TCAD 2026
- **Title:** [Hypnos: A Hardware-Software Co-Design Framework for Memory-Efficient Homomorphic Processing](papers/2026/IEEE-TCAD/hypnos-wang-tcad-2026/README.md)  
  **Authors:** Haoxuan Wang et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Introduces a Homomorphic Encryption Paged Management Unit (HEPMU) to manage memory at the granularity of individual RNS components, significantly reducing memory fragmentation and PCIe transfer overhead.


## 2025

### DAC 2025
- **Title:** [Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection](papers/2025/DAC/ares-fhe-psi-accelerator/README.md)  
  **Authors:** Haoxuan Wang, Yinghao Yang, Jinkai Zhang, Hang Lu, Xiaowei Li  
  **Affiliations:** Institute of Computing Technology, Chinese Academy of Sciences  
  **Key Innovation:** A near-storage FPGA accelerator for FHE-based PSI that introduces Lazy Relinearization to remove redundant computations and decouples memory-bound vs. compute-bound tasks.


## 2024

### DAC 2024
- **Title:** [Hardware-Software Co-Design for TFHE Bootstrapping](papers/2024/DAC/hw-sw-codesign-tfhe-bootstrapping/README.md)  
  **Authors:** Zhang et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Co-designed TFHE bootstrapping with custom instruction set extensions

### ISCA 2024
- **Title:** [BTS: An Accelerator for Bootstrappable Fully Homomorphic Encryption](papers/2024/ISCA/bts-accelerator-bootstrappable-fhe/README.md)  
  **Authors:** Feldmann et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Specialized bootstrapping acceleration with optimized modular arithmetic units

### MICRO 2024
- **Title:** [REED: Chiplet-Based Accelerator for Fully Homomorphic Encryption](papers/2024/MICRO/reed-chiplet-accelerator/README.md)  
  **Authors:** Kim et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Chiplet-based architecture with inter-chiplet communication optimization for FHE operations


## 2023

### ASPLOS 2023
- **Title:** [CHOCO: Client-Optimized Algorithms and Acceleration for Encrypted Compute Offloading](papers/2023/ASPLOS/choco-client-optimized-offloading/README.md)  
  **Authors:** Tan et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Client-side preprocessing and optimized packing schemes for reduced computation

### DAC 2023
- **Title:** [MATCHA: A Fast and Energy-Efficient Accelerator for Fully Homomorphic Encryption over the Torus](papers/2023/DAC/matcha-accelerator-fhe-torus/README.md)  
  **Authors:** Kim et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Torus-based FHE with optimized polynomial multiplication and bootstrapping

### HPCA 2023
- **Title:** [CraterLake: A Hardware Accelerator for Efficient Unbounded Computation on Encrypted Data](papers/2023/HPCA/craterlake-unbounded-encrypted-computation/README.md)  
  **Authors:** Feldmann et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Function unit for modular arithmetic and slot-aware scratchpad memory management

### MICRO 2023
- **Title:** [ARK: Fully Homomorphic Encryption Accelerator with Runtime Data Generation and Inter-Operation Key Reuse](papers/2023/MICRO/ark-runtime-data-generation-key-reuse/README.md)  
  **Authors:** Yoo et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Runtime key generation and inter-operation key reuse to reduce memory overhead


## 2022

### ASPLOS 2022
- **Title:** [HACE: Hardware-Software Co-Design for Fully Homomorphic Encryption Applications](papers/2022/ASPLOS/hace-hw-sw-codesign-fhe/README.md)  
  **Authors:** Morshed et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Software-hardware interface with automated operator fusion for FHE workloads

### HPCA 2022
- **Title:** [BumbleBee: Secure Two-party Inference Framework for Large Transformers](papers/2022/HPCA/bumblebee-two-party-transformers/README.md)  
  **Authors:** Lu et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Two-party computation framework for transformer models using FHE primitives
- **Title:** [FAB: An FPGA-based Accelerator for Bootstrappable Fully Homomorphic Encryption](papers/2022/HPCA/fab-fpga-bootstrappable-fhe/README.md)  
  **Authors:** Sav et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** FPGA-based bootstrapping with optimized NTT and automorphism operations

### MICRO 2022
- **Title:** [Phantom: General-Purpose Tunable Privacy-Preserving Neural Network Inference Using Homomorphic Encryption](papers/2022/MICRO/phantom-pp-nn-inference/README.md)  
  **Authors:** Ghodsi et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Configurable privacy levels with hybrid encryption schemes for neural networks


## 2021

### DATE 2021
- **Title:** [HEAX: High-Performance Architecture for Computation on Encrypted Data](papers/2021/DATE/heax-encrypted-data-architecture/README.md)  
  **Authors:** Morshed et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Specialized memory hierarchy for managing large ciphertext and key data

### HPCA 2021
- **Title:** [F1: A Fast and Programmable Accelerator for Fully Homomorphic Encryption](papers/2021/HPCA/f1-programmable-fhe-accelerator/README.md)  
  **Authors:** Samardzic et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Programmable datapath with flexible NTT engine and unified key-switching unit

### MICRO 2021
- **Title:** [Accelerating Encrypted Execution via NTT in Homomorphic Encryption](papers/2021/MICRO/accelerating-encrypted-execution-ntt/README.md)  
  **Authors:** Park et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Optimized NTT hardware units with efficient memory access patterns


## 2020

### DAC 2020
- **Title:** [CryptoPIM: In-Memory Acceleration for Lattice-based Cryptographic Hardware](papers/2020/DAC/cryptopim-in-memory-lattice-crypto/README.md)  
  **Authors:** Ahn et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Processing-in-memory architecture for lattice-based cryptography including FHE

### HPCA 2020
- **Title:** [FPGA-based High-Performance Parallel Architecture for Homomorphic Computing on Encrypted Data](papers/2020/HPCA/fpga-parallel-homomorphic-computing/README.md)  
  **Authors:** Turan et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Parallel processing units with efficient interconnect for FHE operations

### MICRO 2020
- **Title:** [SHARP: A Short-Word Hierarchical Accelerator for Robust and Practical Fully Homomorphic Encryption](papers/2020/MICRO/sharp-short-word-hierarchical-accelerator/README.md)  
  **Authors:** Chielle et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Short-word arithmetic optimization for resource-efficient FHE computation


## 2019

### ASPLOS 2019
- **Title:** [GAZELLE: A Low Latency Framework for Secure Neural Network Inference](papers/2019/ASPLOS/gazelle-secure-nn-inference/README.md)  
  **Authors:** Juvekar et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Hybrid protocol combining homomorphic encryption with garbled circuits for neural networks

### DAC 2019
- **Title:** [An Efficient Homomorphic Comparison Hardware for Resource-Constrained Devices](papers/2019/DAC/homomorphic-comparison-hardware/README.md)  
  **Authors:** Morshed et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Lightweight comparison operations on encrypted data for edge devices


## 2018

### DATE 2018
- **Title:** [Hardware Acceleration of Fully Homomorphic Encryption](papers/2018/DATE/hardware-acceleration-fhe/README.md)  
  **Authors:** Roy et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Modular arithmetic accelerator with optimized polynomial operations

### HPCA 2018
- **Title:** [FPGA-Accelerated Homomorphic Computation with Application to Recommendation Systems](papers/2018/HPCA/fpga-accelerated-homomorphic-recommendation/README.md)  
  **Authors:** Doroz et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Application-specific optimization for recommendation systems using FHE on FPGAs


## 2017

### DAC 2017
- **Title:** [Accelerating Homomorphic Evaluation on Reconfigurable Hardware](papers/2017/DAC/accelerating-homomorphic-evaluation-reconfigurable/README.md)  
  **Authors:** Cousins et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Reconfigurable architecture supporting multiple FHE schemes


## 2016

### DATE 2016
- **Title:** [High-Performance FV Somewhat Homomorphic Encryption on GPUs](papers/2016/DATE/high-performance-fv-gpus/README.md)  
  **Authors:** Dai et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** GPU-based acceleration of Fan-Vercauteren scheme with optimized memory management

### HPCA 2016
- **Title:** [A Custom Accelerator for Homomorphic Encryption Applications](papers/2016/HPCA/custom-accelerator-homomorphic-encryption/README.md)  
  **Authors:** Cousins et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Custom datapath for polynomial arithmetic with optimized NTT


## 2015

### DAC 2015
- **Title:** [Accelerating Somewhat Homomorphic Evaluation using FPGAs](papers/2015/DAC/accelerating-somewhat-homomorphic-fpgas/README.md)  
  **Authors:** Doroz et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** FPGA implementation with pipelined NTT and modular reduction units

### DATE 2015
- **Title:** [Evaluating the Potential of Graphics Processors for Homomorphic Computation](papers/2015/DATE/evaluating-gpus-homomorphic-computation/README.md)  
  **Authors:** Wang et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** GPU parallelization strategies for homomorphic operations

# Index (by Venue)

## ASPLOS

### ASPLOS 2023
- **Title:** [CHOCO: Client-Optimized Algorithms and Acceleration for Encrypted Compute Offloading](papers/2023/ASPLOS/choco-client-optimized-offloading/README.md)  
  **Authors:** Tan et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Client-side preprocessing and optimized packing schemes for reduced computation

### ASPLOS 2022
- **Title:** [HACE: Hardware-Software Co-Design for Fully Homomorphic Encryption Applications](papers/2022/ASPLOS/hace-hw-sw-codesign-fhe/README.md)  
  **Authors:** Morshed et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Software-hardware interface with automated operator fusion for FHE workloads

### ASPLOS 2019
- **Title:** [GAZELLE: A Low Latency Framework for Secure Neural Network Inference](papers/2019/ASPLOS/gazelle-secure-nn-inference/README.md)  
  **Authors:** Juvekar et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Hybrid protocol combining homomorphic encryption with garbled circuits for neural networks


## DAC

### DAC 2025
- **Title:** [Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection](papers/2025/DAC/ares-fhe-psi-accelerator/README.md)  
  **Authors:** Haoxuan Wang, Yinghao Yang, Jinkai Zhang, Hang Lu, Xiaowei Li  
  **Affiliations:** Institute of Computing Technology, Chinese Academy of Sciences  
  **Key Innovation:** A near-storage FPGA accelerator for FHE-based PSI that introduces Lazy Relinearization to remove redundant computations and decouples memory-bound vs. compute-bound tasks.

### DAC 2024
- **Title:** [Hardware-Software Co-Design for TFHE Bootstrapping](papers/2024/DAC/hw-sw-codesign-tfhe-bootstrapping/README.md)  
  **Authors:** Zhang et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Co-designed TFHE bootstrapping with custom instruction set extensions

### DAC 2023
- **Title:** [MATCHA: A Fast and Energy-Efficient Accelerator for Fully Homomorphic Encryption over the Torus](papers/2023/DAC/matcha-accelerator-fhe-torus/README.md)  
  **Authors:** Kim et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Torus-based FHE with optimized polynomial multiplication and bootstrapping

### DAC 2020
- **Title:** [CryptoPIM: In-Memory Acceleration for Lattice-based Cryptographic Hardware](papers/2020/DAC/cryptopim-in-memory-lattice-crypto/README.md)  
  **Authors:** Ahn et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Processing-in-memory architecture for lattice-based cryptography including FHE

### DAC 2019
- **Title:** [An Efficient Homomorphic Comparison Hardware for Resource-Constrained Devices](papers/2019/DAC/homomorphic-comparison-hardware/README.md)  
  **Authors:** Morshed et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Lightweight comparison operations on encrypted data for edge devices

### DAC 2017
- **Title:** [Accelerating Homomorphic Evaluation on Reconfigurable Hardware](papers/2017/DAC/accelerating-homomorphic-evaluation-reconfigurable/README.md)  
  **Authors:** Cousins et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Reconfigurable architecture supporting multiple FHE schemes

### DAC 2015
- **Title:** [Accelerating Somewhat Homomorphic Evaluation using FPGAs](papers/2015/DAC/accelerating-somewhat-homomorphic-fpgas/README.md)  
  **Authors:** Doroz et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** FPGA implementation with pipelined NTT and modular reduction units


## DATE

### DATE 2021
- **Title:** [HEAX: High-Performance Architecture for Computation on Encrypted Data](papers/2021/DATE/heax-encrypted-data-architecture/README.md)  
  **Authors:** Morshed et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Specialized memory hierarchy for managing large ciphertext and key data

### DATE 2018
- **Title:** [Hardware Acceleration of Fully Homomorphic Encryption](papers/2018/DATE/hardware-acceleration-fhe/README.md)  
  **Authors:** Roy et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Modular arithmetic accelerator with optimized polynomial operations

### DATE 2016
- **Title:** [High-Performance FV Somewhat Homomorphic Encryption on GPUs](papers/2016/DATE/high-performance-fv-gpus/README.md)  
  **Authors:** Dai et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** GPU-based acceleration of Fan-Vercauteren scheme with optimized memory management

### DATE 2015
- **Title:** [Evaluating the Potential of Graphics Processors for Homomorphic Computation](papers/2015/DATE/evaluating-gpus-homomorphic-computation/README.md)  
  **Authors:** Wang et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** GPU parallelization strategies for homomorphic operations


## HPCA

### HPCA 2023
- **Title:** [CraterLake: A Hardware Accelerator for Efficient Unbounded Computation on Encrypted Data](papers/2023/HPCA/craterlake-unbounded-encrypted-computation/README.md)  
  **Authors:** Feldmann et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Function unit for modular arithmetic and slot-aware scratchpad memory management

### HPCA 2022
- **Title:** [BumbleBee: Secure Two-party Inference Framework for Large Transformers](papers/2022/HPCA/bumblebee-two-party-transformers/README.md)  
  **Authors:** Lu et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Two-party computation framework for transformer models using FHE primitives
- **Title:** [FAB: An FPGA-based Accelerator for Bootstrappable Fully Homomorphic Encryption](papers/2022/HPCA/fab-fpga-bootstrappable-fhe/README.md)  
  **Authors:** Sav et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** FPGA-based bootstrapping with optimized NTT and automorphism operations

### HPCA 2021
- **Title:** [F1: A Fast and Programmable Accelerator for Fully Homomorphic Encryption](papers/2021/HPCA/f1-programmable-fhe-accelerator/README.md)  
  **Authors:** Samardzic et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Programmable datapath with flexible NTT engine and unified key-switching unit

### HPCA 2020
- **Title:** [FPGA-based High-Performance Parallel Architecture for Homomorphic Computing on Encrypted Data](papers/2020/HPCA/fpga-parallel-homomorphic-computing/README.md)  
  **Authors:** Turan et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Parallel processing units with efficient interconnect for FHE operations

### HPCA 2018
- **Title:** [FPGA-Accelerated Homomorphic Computation with Application to Recommendation Systems](papers/2018/HPCA/fpga-accelerated-homomorphic-recommendation/README.md)  
  **Authors:** Doroz et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Application-specific optimization for recommendation systems using FHE on FPGAs

### HPCA 2016
- **Title:** [A Custom Accelerator for Homomorphic Encryption Applications](papers/2016/HPCA/custom-accelerator-homomorphic-encryption/README.md)  
  **Authors:** Cousins et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Custom datapath for polynomial arithmetic with optimized NTT


## IEEE-TCAD

### IEEE-TCAD 2026
- **Title:** [Hypnos: A Hardware-Software Co-Design Framework for Memory-Efficient Homomorphic Processing](papers/2026/IEEE-TCAD/hypnos-wang-tcad-2026/README.md)  
  **Authors:** Haoxuan Wang et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Introduces a Homomorphic Encryption Paged Management Unit (HEPMU) to manage memory at the granularity of individual RNS components, significantly reducing memory fragmentation and PCIe transfer overhead.


## ISCA

### ISCA 2024
- **Title:** [BTS: An Accelerator for Bootstrappable Fully Homomorphic Encryption](papers/2024/ISCA/bts-accelerator-bootstrappable-fhe/README.md)  
  **Authors:** Feldmann et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Specialized bootstrapping acceleration with optimized modular arithmetic units


## MICRO

### MICRO 2024
- **Title:** [REED: Chiplet-Based Accelerator for Fully Homomorphic Encryption](papers/2024/MICRO/reed-chiplet-accelerator/README.md)  
  **Authors:** Kim et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Chiplet-based architecture with inter-chiplet communication optimization for FHE operations

### MICRO 2023
- **Title:** [ARK: Fully Homomorphic Encryption Accelerator with Runtime Data Generation and Inter-Operation Key Reuse](papers/2023/MICRO/ark-runtime-data-generation-key-reuse/README.md)  
  **Authors:** Yoo et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Runtime key generation and inter-operation key reuse to reduce memory overhead

### MICRO 2022
- **Title:** [Phantom: General-Purpose Tunable Privacy-Preserving Neural Network Inference Using Homomorphic Encryption](papers/2022/MICRO/phantom-pp-nn-inference/README.md)  
  **Authors:** Ghodsi et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Configurable privacy levels with hybrid encryption schemes for neural networks

### MICRO 2021
- **Title:** [Accelerating Encrypted Execution via NTT in Homomorphic Encryption](papers/2021/MICRO/accelerating-encrypted-execution-ntt/README.md)  
  **Authors:** Park et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Optimized NTT hardware units with efficient memory access patterns

### MICRO 2020
- **Title:** [SHARP: A Short-Word Hierarchical Accelerator for Robust and Practical Fully Homomorphic Encryption](papers/2020/MICRO/sharp-short-word-hierarchical-accelerator/README.md)  
  **Authors:** Chielle et al.  
  **Affiliations:** TODO: Affiliations (institutions / companies)  
  **Key Innovation:** Short-word arithmetic optimization for resource-efficient FHE computation

<!-- INDEX:END -->

---

## Contributing

This list is actively maintained. If you know of any FHE hardware accelerator papers from top-tier conferences that should be included, please submit a pull request or open an issue.

If you're submitting a PR, please follow [CONTRIBUTING.md](CONTRIBUTING.md) to ensure the paper metadata and per-paper README are generated consistently.

**Star history:**

[![Star History Chart](https://api.star-history.com/svg?repos=Wang0206/FHE-Paper-HW-Architecture&type=Date)](https://star-history.com/#Wang0206/FHE-Paper-HW-Architecture&Date)

## License

This curated list is available under CC0 1.0 Universal (public domain).
