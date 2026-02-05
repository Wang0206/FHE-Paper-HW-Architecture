# Hypnos: A Hardware-Software Co-Design Framework for Memory-Efficient Homomorphic Processing

**Authors:** Haoxuan Wang, Yinghao Yang, Shangjie Pan, Hang Lu, Xiaowei Li  
**Venue/Year:** IEEE TCAD 2026  
**URL:** TODO: DOI or publisher URL  


## Key Innovation

Hypnos proposes a hardware-software co-design framework that integrates a "Homomorphic Encryption Paged Management Unit" (HEPMU). By managing memory at the granularity of individual RNS components rather than entire ciphertexts, and pairing this with a compiler that performs RNS-aware static analysis, Hypnos solves the memory fragmentation issue in CKKS and significantly reduces the PCIe communication overhead.

## Repo Summary

- **Co-Design Framework:** Integrates an ARM CPU directly within the accelerator architecture to orchestrate execution locally, eliminating the dependency on the host CPU for fine-grained scheduling.
- **Fine-Grained Memory Management:** Introduces the HEPMU to manage memory pages at the RNS-component level, adapting to dynamic data size changes caused by rescaling.
- **Compiler Automation:** Includes the Hypnos Compiler which performs RNS-aware static analysis to generate metadata and hardware commands, optimizing data placement and transfer timing.
- **Performance Gains:** Outperforms state-of-the-art ASIC and FPGA solutions in data-intensive applications by reducing memory fragmentation and communication bottlenecks.

## Method / Architecture

- **Target Scheme:** Primarily targets CKKS (supports dynamic rescaling), but principles apply to BFV/BGV.
- **Kernels:** - **NTT:** Radix-8 design with optimizations.
  - **Modular Arithmetic:** Uses Barrett Reduction for modular multiplication.
  - **Management:** Dedicated units for key-switching, rescaling, and rotation.
- **Architecture Mapping:**
  - **Heterogeneous Platform:** Implemented on the Qiankun FPGA Card featuring an ARM Cortex-A72 (Processing System) and FPGA logic (Programmable Logic) connected via NoC.
  - **HEPMU:** Handles ID-to-address translation using Key/Ciphertext Tables (KT/CT) and manages page replacement (LRU).
  - **Memory Hierarchy:** Utilizes uncacheable shared system memory for bulk storage and a local scratchpad (Register Files/BRAM) for active computation, managed via DMA.

## Highlights

- **New vs Prior Accelerators:** Unlike prior works (ARK, Craterlake) that assume abundant on-chip memory or rely on host-driven PCIe transfers of full ciphertexts, Hypnos manages data movement locally at the sub-ciphertext level.
- **Design Tradeoffs:** The design trades off the complexity of a dedicated memory management unit (HEPMU) and metadata generation for a massive reduction in PCIe bandwidth usage and improved effective memory capacity.

## Results

- **Throughput/Latency:**
  - **ResNet-20:** 5.73s (Hypnos) vs 15.61s (ASIC ARK) vs 27.07s (FPGA Poseidon).
  - **PSI:** 267.57ms vs 422.73ms (ARK) vs 689.79ms (Poseidon).
  - **PIR:** 83.24ms vs 306.10ms (ARK) vs 389.77ms (Poseidon).
- **Communication:** Reduced PCIe traffic by 4.85x compared to traditional architectures.
- **Energy Efficiency:** Achieves up to 30.1x (vs ARK) and 20.7x (vs Poseidon) improvement in Energy-Delay Product (EDP) for ResNet-20.
- **Resource Utilization:** FPGA implementation uses ~50% LUTs, ~32% FFs, ~65% BRAM, and ~67% DSPs on the XCVP1502.

## Notes

- **Limitations:** For computationally intensive applications with small memory footprints (e.g., small-scale LR-Train), Hypnos (FPGA) does not match the raw compute performance of specialized ASICs like Sharp, though it still beats other FPGAs.
- **Assumptions:** The system assumes the workload is data-intensive enough that the working set exceeds on-chip memory, which is where the paging mechanism provides the most benefit.

## BibTeX

```bibtex
@article{wang2026hypnos,
  title={Hypnos: A Hardware-Software Co-Design Framework for Memory-Efficient Homomorphic Processing},
  author={Wang, Haoxuan and Yang, Yinghao and Pan, Shangjie and Lu, Hang and Li, Xiaowei},
  journal={IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems},
  year={2026},
  publisher={IEEE}
}