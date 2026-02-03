# Hypnos: A Hardware-Software Co-Design Framework for Memory-Efficient Homomorphic Processing

[cite_start]**Authors:** Haoxuan Wang, Yinghao Yang, Shangjie Pan, Hang Lu, Xiaowei Li [cite: 5]  
[cite_start]**Venue/Year:** IEEE TCAD 2026 [cite: 1]  
**URL:** TODO: DOI or publisher URL  


## Key Innovation

Hypnos proposes a hardware-software co-design framework that integrates a "Homomorphic Encryption Paged Management Unit" (HEPMU). [cite_start]By managing memory at the granularity of individual RNS components rather than entire ciphertexts, and pairing this with a compiler that performs RNS-aware static analysis, Hypnos solves the memory fragmentation issue in CKKS and significantly reduces the PCIe communication overhead[cite: 64, 66, 68].

## Repo Summary

- [cite_start]**Co-Design Framework:** Integrates an ARM CPU directly within the accelerator architecture to orchestrate execution locally, eliminating the dependency on the host CPU for fine-grained scheduling[cite: 274].
- [cite_start]**Fine-Grained Memory Management:** Introduces the HEPMU to manage memory pages at the RNS-component level, adapting to dynamic data size changes caused by rescaling[cite: 11, 68].
- [cite_start]**Compiler Automation:** Includes the Hypnos Compiler which performs RNS-aware static analysis to generate metadata and hardware commands, optimizing data placement and transfer timing[cite: 456, 470].
- [cite_start]**Performance Gains:** Outperforms state-of-the-art ASIC and FPGA solutions in data-intensive applications by reducing memory fragmentation and communication bottlenecks[cite: 71].

## Method / Architecture

- [cite_start]**Target Scheme:** Primarily targets CKKS (supports dynamic rescaling), but principles apply to BFV/BGV[cite: 80, 143].
- [cite_start]**Kernels:** - **NTT:** Radix-8 design with optimizations[cite: 289].
  - [cite_start]**Modular Arithmetic:** Uses Barrett Reduction for modular multiplication[cite: 289].
  - [cite_start]**Management:** Dedicated units for key-switching, rescaling, and rotation[cite: 320, 322].
- **Architecture Mapping:**
  - [cite_start]**Heterogeneous Platform:** Implemented on the Qiankun FPGA Card featuring an ARM Cortex-A72 (Processing System) and FPGA logic (Programmable Logic) connected via NoC[cite: 280, 614].
  - [cite_start]**HEPMU:** Handles ID-to-address translation using Key/Ciphertext Tables (KT/CT) and manages page replacement (LRU)[cite: 414, 454].
  - [cite_start]**Memory Hierarchy:** Utilizes uncacheable shared system memory for bulk storage and a local scratchpad (Register Files/BRAM) for active computation, managed via DMA[cite: 426, 488].

## Highlights

- [cite_start]**New vs Prior Accelerators:** Unlike prior works (ARK, Craterlake) that assume abundant on-chip memory or rely on host-driven PCIe transfers of full ciphertexts, Hypnos manages data movement locally at the sub-ciphertext level[cite: 47, 261].
- [cite_start]**Design Tradeoffs:** The design trades off the complexity of a dedicated memory management unit (HEPMU) and metadata generation for a massive reduction in PCIe bandwidth usage and improved effective memory capacity[cite: 278, 497].

## Results

- **Throughput/Latency:**
  - [cite_start]**ResNet-20:** 5.73s (Hypnos) vs 15.61s (ASIC ARK) vs 27.07s (FPGA Poseidon)[cite: 623].
  - [cite_start]**PSI:** 267.57ms vs 422.73ms (ARK) vs 689.79ms (Poseidon)[cite: 623].
  - [cite_start]**PIR:** 83.24ms vs 306.10ms (ARK) vs 389.77ms (Poseidon)[cite: 623].
- [cite_start]**Communication:** Reduced PCIe traffic by 4.85x compared to traditional architectures[cite: 72].
- [cite_start]**Energy Efficiency:** Achieves up to 30.1x (vs ARK) and 20.7x (vs Poseidon) improvement in Energy-Delay Product (EDP) for ResNet-20[cite: 73].
- [cite_start]**Resource Utilization:** FPGA implementation uses ~50% LUTs, ~32% FFs, ~65% BRAM, and ~67% DSPs on the XCVP1502[cite: 724].

## Notes

- [cite_start]**Limitations:** For computationally intensive applications with small memory footprints (e.g., small-scale LR-Train), Hypnos (FPGA) does not match the raw compute performance of specialized ASICs like Sharp, though it still beats other FPGAs[cite: 636].
- [cite_start]**Assumptions:** The system assumes the workload is data-intensive enough that the working set exceeds on-chip memory, which is where the paging mechanism provides the most benefit[cite: 632].

## BibTeX

```bibtex
@article{wang2026hypnos,
  title={Hypnos: A Hardware-Software Co-Design Framework for Memory-Efficient Homomorphic Processing},
  author={Wang, Haoxuan and Yang, Yinghao and Pan, Shangjie and Lu, Hang and Li, Xiaowei},
  journal={IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems},
  year={2026},
  publisher={IEEE}
}