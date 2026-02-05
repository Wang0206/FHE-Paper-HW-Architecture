# CraterLake: A Hardware Accelerator for Efficient Unbounded Computation on Encrypted Data

**Authors:** Nikola Samardzic et al.  
**Affiliations:** Massachusetts Institute of Technology  
**Venue/Year:** ISCA 2022  
**URL:** https://dl.acm.org/doi/pdf/10.1145/3470496.3527393  

## Key Innovation

CraterLake is the first FHE accelerator designed to efficiently support unbounded multiplicative depth (bootstrapping) by handling the very large ciphertexts (tens of MBs) required for deep computations. It achieves this through a novel 2048-lane vector uniprocessor architecture and a compiler tailored to the "boosted keyswitching" algorithm, which drastically reduces the memory footprint of auxiliary keys.

## Paper Summary

- **Problem:** Prior FHE accelerators (like F1) are limited to shallow computations because they cannot efficiently handle the massive data movement and storage required for bootstrapping (refreshing noise budgets), which involves ciphertexts of 20MB+.
- **Algorithm:** Adopts "boosted keyswitching," an algorithm that reduces the auxiliary key material footprint from ~1.4 GB to ~50 MB, enabling it to fit in on-chip SRAM, though it requires specific hardware support to be efficient.
- **Architecture:** Proposes a massive vector uniprocessor with 2,048 lanes, avoiding the communication bottlenecks of multicore designs by using a novel fixed permutation network for data transposes.
- **Performance:** Demonstrates the ability to run deep neural networks (like ResNet-20) and LSTMs in real-time (milliseconds vs. minutes/hours on CPU), achieving order-of-magnitude speedups over prior state-of-the-art accelerators.

## Method / Architecture

- **Scheme/Parameters:** Targets the CKKS scheme (also supports BGV/GSW) with ciphertext sizes up to $N=64K$ and $L=60$, utilizing RNS representation with 28-bit moduli.
- **Main Kernels:** - **Boosted Keyswitching:** The dominant operation, heavily relying on Change-RNS-Base (CRB) routines.
  - **NTT:** Number-Theoretic Transforms for polynomial multiplication.
  - **Automorphisms:** For vector rotation.
- **Hardware Mapping:**
  - **Compute:** A 2048-lane vector uniprocessor divided into 8 lane groups. It includes specialized Functional Units (FUs) including a massive Change-RNS-Base (CRB) unit and a Keyswitch Hint Generator (KSHGen).
  - **Memory:** 256 MB on-chip SRAM (Register File) to store operands locally; HBM2E main memory for high bandwidth.
  - **Dataflow:** Statically scheduled with "Vector Chaining" to pipeline operations between FUs without writing back to the register file, saving ports.

## Highlights

- **New vs Prior:** Unlike F1, which uses a vector multicore approach (clusters of narrow vector units), CraterLake uses a single wide vector domain. This simplifies control and reduces the on-chip network area by 16x using a fixed permutation network instead of a crossbar.
- **Design Tradeoffs:** - **Bitwidth:** Uses 28-bit multipliers (vs 32-bit in F1) to improve area/energy efficiency by ~1.5x.
  - **Storage:** Dedicates significant area (41%) to a large 256 MB Register File to keep bootstrapping operands on-chip.
  - **Security:** Leverages boosted keyswitching which trades a slight increase in parameter size for massive reductions in key storage and compute complexity.

## Results

- **Throughput/Latency:** - ResNet-20 Inference: **249.45 ms** (vs 23 min on CPU).
  - LSTM Inference: **138.00 ms**.
  - Bootstrapping (Packed): **3.91 ms**.
- **Speedup:** - **4,600x** speedup (gmean) vs. 32-core CPU on deep benchmarks.
  - **11.2x** speedup (gmean) vs. F1+ (scaled prior accelerator).
- **Area:** **472.3 mm²** (14/12nm process).
- **Power:** **~320 W** peak power (comparable to high-end GPUs).
- **Energy Efficiency:** **201x** improvement in performance/Joule over F1+.

## Notes

- **Assumptions:** Assumes a CPU-Accelerator link (PCIe Gen 5) with ~50-130 GB/s bandwidth.
- **Limitations:** Shallow benchmarks (low multiplicative depth) see only modest gains (1.34x) over prior work because the large CRB unit is underutilized at low depth.
- **Implementation:** Evaluated via cycle-accurate simulation and RTL synthesis of components.

## BibTeX

```bibtex
@inproceedings{samardzic2022craterlake,
  author    = {Samardzic, Nikola and Feldmann, Axel and Krastev, Aleksandar and Manohar, Nathan and Genise, Nicholas and Devadas, Srinivas and Eldefrawy, Karim and Peikert, Chris and Sanchez, Daniel},
  title     = {Crater Lake: A Hardware Accelerator for Efficient Unbounded Computation on Encrypted Data},
  booktitle = {Proceedings of the 49th Annual International Symposium on Computer Architecture (ISCA)},
  year      = {2022},
  pages     = {173--187},
  doi       = {10.1145/3470496.3527393}
}
