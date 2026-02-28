# Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection

**Authors:** Haoxuan Wang, Yinghao Yang, Jinkai Zhang, Hang Lu, Xiaowei Li  
**Affiliations:** Institute of Computing Technology, Chinese Academy of Sciences  
**Venue/Year:** DAC 2025  
**URL:** https://ieeexplore.ieee.org/document/11133120  

## Key Innovation

Ares is a hardware-software co-designed accelerator for FHE-based Private Set Intersection (PSI) that leverages Near-Data Processing (NDP) on SmartSSDs to minimize data movement overhead. It introduces a "Lazy Relinearization" strategy to eliminate redundant FHE operations and employs a decoupled architecture to balance memory-bound and compute-bound tasks.

## Paper Summary

- **Problem:** Existing general-purpose FHE accelerators are inefficient for PSI because they fail to address the massive data transfer overheads (PCIe bottlenecks) caused by large databases and underutilize hardware due to mismatched computational patterns.
- **Solution:** The authors propose Ares, which integrates storage and computation using a Computational Storage Device (CSD).
- **Optimization:** A new "Lazy Relinearization" technique reduces the number of expensive relinearization steps in the PSI polynomial evaluation phase without altering protocol accuracy.
- **Architecture:** Ares features a specialized pipeline that separates tasks into a Memory-Bound (MB) region (for plaintext multiplication and addition) and a Compute-Bound (CB) region (for homomorphic multiplication and accumulation), interconnected by a dedicated buffer.

## Method / Architecture

- **Target Scheme:** BFV (Brakerski-Fan-Vercauteren) scheme.
- **Target Application:** Private Set Intersection (PSI) where the sender holds a large database and the receiver holds a query set.
- **Hardware Platform:** Implemented on a Samsung SmartSSD (NDP platform) containing a Kintex UltraScale+ KU15P FPGA.
- **Key Kernels:**
  - **Polynomial Evaluation:** The core workload, decomposed into sub-polynomials.
  - **Lazy Relinearization:** Delays relinearization until after aggregation, rather than performing it after every multiplication.
  - **Hardware Units:** Includes specialized modules for Modular Multiplication (MM), Modular Addition (MA), Number Theoretic Transform (NTT), and localized buffers (PEIR Buffer, EVK Buffer).

## Highlights

- **Near-Data Processing:** By processing data directly on the SmartSSD, Ares alleviates the PCIe bus contention that bottlenecks standard host-accelerator setups.
- **Decoupled Design:** The architecture explicitly splits the workload into Memory-Bound (MB) and Compute-Bound (CB) regions, enabling better resource allocation and pipeline efficiency compared to monolithic FHE accelerators.
- **Lazy Relinearization:** A protocol-aware optimization that exploits the limited depth of PSI circuits to skip redundant relinearization steps, which are typically mandatory in general FHE computation.

## Results

- **Speedup vs. CPU:** 47.99x speedup relative to an Intel Xeon W-1370 CPU.
- **Speedup vs. SOTA FPGA Accelerators:** 1.79x improvement over Poseidon and 1.93x over FAB on large-scale datasets.
- **Energy Efficiency:** 7.96x improvement over Poseidon and 10.95x over FAB.
- **Resource Usage:** Uses 2–5x fewer FPGA resources (LUTs/BRAMs) compared to baseline FHE accelerators while achieving comparable or better performance for PSI tasks.

## Notes

- **Limitations:** The performance gain on small datasets is less pronounced (approx. 1.38x) due to memory access latency still being a factor, though it excels on large/very-large datasets.
- **Assumptions:** The experiments assume the database is stored on the SmartSSD's internal SSD and that the sender performs the heavy polynomial evaluation tasks.
- **Comparison:** Baselines (FAB, Poseidon) were general-purpose FHE accelerators adapted for comparison, as they did not natively implement the specific PSI protocol optimizations.

## BibTeX

```bibtex
@INPROCEEDINGS{11133120,
  author={Wang, Haoxuan and Yang, Yinghao and Zhang, Jinkai and Lu, Hang and Li, Xiaowei},
  booktitle={2025 62nd ACM/IEEE Design Automation Conference (DAC)}, 
  title={Ares: High Performance Near-Storage Accelerator for FHE-based Private Set Intersection}, 
  year={2025},
  pages={1-6}
  }
