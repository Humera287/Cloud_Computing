# Performance Analysis of Type-1 and Type-2 Hypervisors

[![Course](https://img.shields.io/badge/Course-Cloud%20Computing-blue.svg)](#)
[![Hypervisors](https://img.shields.io/badge/Hypervisors-Proxmox%20VE%20%7C%20VMware%20Workstation-orange.svg)](#)
[![Benchmark](https://img.shields.io/badge/Benchmark-Sysbench%20CPU%2020k%20Primes-green.svg)](#)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)](#)

---

## Executive Summary

This repository contains the complete experimental setup, benchmark results, performance analysis, visual representation, and technical report comparing the CPU performance of a **Type-1 Bare-Metal Hypervisor (Proxmox VE)** and a **Type-2 Hosted Hypervisor (VMware Workstation)**.

Both hypervisors were configured with similarly prepared **Ubuntu Virtual Machines** using 2 vCPU, 2 GB RAM, and 20 GB Disk. The standard `sysbench` CPU prime-number calculation benchmark (`--cpu-max-prime=20000`) was executed on both virtual machines using the same workload conditions.

The collected results were then compared using throughput, total events, execution time, and different latency measurements.

---

## Table of Contents

1. [Project Objectives](#1-project-objectives)
2. [Hypervisor Architectural Comparison](#2-hypervisor-architectural-comparison)
3. [Virtual Machine Specifications](#3-virtual-machine-specifications)
4. [Experimental Procedure](#4-experimental-procedure)
5. [Empirical Results & Screenshots](#5-empirical-results--screenshots)
6. [Performance Comparison Table](#6-performance-comparison-table)
7. [Metric Explanations & Visualizations](#7-metric-explanations--visualizations)
8. [Technical Analysis & Discussion](#8-technical-analysis--discussion)
9. [Conclusion & Engineering Takeaways](#9-conclusion--engineering-takeaways)
10. [Repository Structure & Reproduction](#10-repository-structure--reproduction)

---

## 1. Project Objectives

The main objectives of this Cloud Computing laboratory experiment are:

1. **Deployment**: Deploy two equivalent Ubuntu Virtual Machines using different hypervisor architectures:
   - **Type-1 (Bare-Metal)**: Proxmox VE (Kernel-based Virtual Machine / KVM)
   - **Type-2 (Hosted)**: VMware Workstation Pro running on a Windows Host OS
2. **Standardization**: Maintain uniform hardware resource allocations of 2 vCPU, 2048 MB RAM, and 20 GB Virtual Storage to provide a consistent basis for comparison.
3. **Benchmarking**: Run the `sysbench` CPU computational benchmark using 20,000 prime numbers to evaluate CPU virtualization performance.
4. **Metric Collection**: Record execution time, total events processed, throughput in events/sec, and latency statistics including minimum, average, maximum, and 95th percentile.
5. **Architectural Evaluation**: Examine the performance overhead introduced by the host operating system layer in Type-2 hypervisors and compare it with bare-metal hypervisor execution.
6. **Result Analysis**: Compare the collected measurements to understand how the underlying hypervisor architecture affects CPU-intensive workloads.

---

## 2. Hypervisor Architectural Comparison

### Type-1 Hypervisor — Proxmox VE (Bare-Metal Architecture)

Proxmox VE operates directly on the physical host hardware. The Linux kernel integrated with KVM (Kernel-based Virtual Machine) provides the virtualization layer. Guest operating system instructions can directly use the CPU virtualization extensions such as Intel VT-x or AMD-V without requiring a separate desktop operating system between the hypervisor and the physical hardware.


---

### Type-2 Hypervisor — VMware Workstation (Hosted Architecture)

VMware Workstation operates as an application on top of a host operating system such as Windows 11 or Windows 10. The guest virtual machine communicates through the VMware virtualization layer, while the host operating system manages access to the physical hardware. Therefore, an additional software layer exists between the guest VM and the physical system.


---

## 3. Virtual Machine Specifications

To ensure a fair comparison and reduce resource-related differences, both virtual machines were assigned the same major hardware resources:

| Resource Parameter | Proxmox VE (Type-1) | VMware Workstation (Type-2) | Status |
| :--- | :--- | :--- | :--- |
| **Virtual Machine Name** | `CC-Experiment1-type1` | `CC-Experiment1-Type2` | Standardized |
| **VM Identifier** | `VMID 123` | `humeira-VMware-Virtual-Platform` | Standardized |
| **Guest Operating System** | Ubuntu 24.04.3 LTS AMD64 | Ubuntu Linux 64-bit | Standardized |
| **CPU Allocation** | 2 vCPU (1 Socket, 2 Cores) | 2 vCPU (1 Processor, 2 Cores) | Identical |
| **CPU Type / Model** | `x86-64-v2-AES` | Host Passthrough / Default | Hardware Matched |
| **RAM Allocation** | 2048 MiB (2.0 GB) | 2048 MB (2.0 GB) | Identical |
| **Virtual Disk Capacity** | 20.0 GB | 20.0 GB | Identical |
| **Virtual Network Adapter**| VirtIO (`vmbr0`) | NAT (`VMnet8`) | Standardized |
| **Benchmark Tool** | `sysbench 1.0.20` | `sysbench 1.0.20` | Identical |

---

## 4. Experimental Procedure

### Step 1: Virtual Machine Creation & Setup

1. **Proxmox VE (Type-1)**:
   - Opened `https://10.11.0.252:8006` using a web browser.
   - Started the `Create VM` wizard with VM ID `123` and the name `CC-Experiment1-type1`.
   - Attached the Ubuntu 24.04 ISO and assigned 2 CPU cores, 2048 MiB RAM, a 20 GB VirtIO disk, and `vmbr0` network bridge.
   - Completed the standard Ubuntu server/desktop installation.

2. **VMware Workstation (Type-2)**:
   - Opened VMware Workstation on the Windows host system.
   - Selected the `Typical Configuration` wizard.
   - Mounted the Ubuntu ISO and assigned the VM name `CC-Experiment1-Type2`.
   - Configured a 20 GB virtual disk, 1 processor with 2 cores, 2 GB RAM, and a NAT adapter.
   - Completed the standard Ubuntu installation process.

### Step 2: System Configuration Verification

Before running the benchmark, the system specifications were checked on both guest operating systems to confirm that the allocated resources were correctly configured.

```bash
# 1. Verify Hostname & System Architecture
hostnamectl

# 2. Verify CPU Topology & Core Allocation
lscpu

# 3. Verify Memory Allocation
free -h

# 4. Verify Disk Partition Allocation
df -h

# 5. Monitor Real-time Process & System Load
top
```

### Step 3: Sysbench Benchmark Installation & Execution

```bash
# Package Index Update & Sysbench Installation
sudo apt update && sudo apt install sysbench -y

# Verify Version
sysbench --version

# Execute CPU Benchmark (Prime Calculation up to 20,000)
sysbench cpu --cpu-max-prime=20000 run
```

---

## 5. Empirical Results & Screenshots

### Type-1 Hypervisor Screenshot (Proxmox VE)

The following screenshot shows the Sysbench benchmark output captured from the Proxmox VE noVNC web console.

<img width="633" height="327" alt="image" src="https://github.com/user-attachments/assets/c111dc60-58b6-41b9-9483-fa50585961d4" />

*Figure 1: Proxmox VE (Type-1 Hypervisor) Sysbench Benchmark Console Output.*

---

### Type-2 Hypervisor Screenshot (VMware Workstation)

The following screenshot represents the Sysbench benchmark output obtained from the VMware Workstation virtual machine.

<img width="902" height="703" alt="image" src="https://github.com/user-attachments/assets/a502fc16-56be-4636-af20-7d795770dfd6" />

*Figure 2: VMware Workstation (Type-2 Hypervisor) Sysbench Benchmark Terminal Output.*

---

## 6. Performance Comparison Table

The following table summarizes the benchmark values obtained from both experimental environments and provides a direct comparison of their measured performance:

| Performance Metric | Proxmox VE (Type-1) | VMware Workstation (Type-2) | Performance Delta | Winner / Advantage |
| :--- | :---: | :---: | :---: | :---: |
| **Hypervisor Type** | Bare-Metal | Hosted | Architectural | Type-1 Direct Control |
| **Guest OS** | Ubuntu | Ubuntu | Matched | Identical Baseline |
| **vCPU Allocation** | 2 vCPU | 2 vCPU | Matched | Identical Compute |
| **RAM Allocation** | 2 GB | 2 GB | Matched | Identical Memory |
| **Disk Capacity** | 20 GB | 20 GB | Matched | Identical Storage |
| **Benchmark Limit** | 20,000 Primes | 20,000 Primes | Matched | Identical Stress Test |
| **Total Execution Time** | **10.0004 s** | **10.0005 s** | **0.001% difference** | Fixed 10s Window |
| **Total Events Processed** | **17,169** | **6,846** | **+10,323 events (+150.79%)** | **Proxmox VE (Type-1)** |
| **Events per Second (EPS)** | **1,716.69** | **684.51** | **+1,032.18 eps (+150.79%)** | **Proxmox VE (Type-1)** |
| **Minimum Latency** | **0.57 ms** | **1.31 ms** | **-0.74 ms (-56.49%)** | **Proxmox VE (Lower)** |
| **Average Latency** | **0.58 ms** | **1.46 ms** | **-0.88 ms (-60.27%)** | **Proxmox VE (Lower)** |
| **95th Percentile Latency** | **0.65 ms** | **1.58 ms** | **-0.93 ms (-58.86%)** | **Proxmox VE (More Consistent)** |
| **Maximum Latency** | **2.78 ms** | **6.16 ms** | **-3.38 ms (-54.87%)** | **Proxmox VE (Fewer Spikes)** |

---

## 7. Metric Explanations & Visualizations

### Performance Metric Definitions

1. **Total Execution Time (seconds)**: The total wall-clock duration required to execute the Sysbench workload. The benchmark was standardized to approximately 10 seconds.
2. **Events per Second (Throughput / EPS)**: Represents the number of prime-number calculation iterations completed in one second. **Higher is better.**
3. **Total Events**: Indicates the total number of prime-number calculation cycles completed during the test duration. **Higher is better.**
4. **Latency (milliseconds)**: Represents the time taken to process an individual event:
   - **Minimum Latency**: The shortest observed time for processing a single event.
   - **Average Latency**: The mean processing time calculated across all recorded events.
   - **95th Percentile Latency**: The latency value below which 95% of the recorded events were completed. This helps in understanding response consistency.
   - **Maximum Latency**: The highest recorded event-processing delay and can indicate temporary scheduling or workload-related spikes.

---

### Chart 1: CPU Throughput Comparison (Events / Sec)

<img width="1098" height="721" alt="CPU_Throughput_Graph" src="https://github.com/user-attachments/assets/c927f138-e153-4b28-b61a-ae1c780ebca1" />

*Figure 3: CPU Throughput comparison showing the measured events per second for both hypervisors.*

---

### Chart 2: CPU Latency Metrics Comparison

<img width="923" height="502" alt="CPU_Latency_Matrix_Graph" src="https://github.com/user-attachments/assets/a0f6c09e-b136-48cd-8d06-484b0ffd6493" />

*Figure 4: Latency comparison showing Min, Avg, 95th Percentile, and Max values across both hypervisors.*

---

### Chart 3: Total Events Processed

<img width="922" height="547" alt="Total_Events_Processed_Graph" src="https://github.com/user-attachments/assets/2bb7d14f-cc43-44b4-99b2-dd477f8a6b57" />

*Figure 5: Total number of events completed during the 10-second benchmark period (17,169 vs 13,650).*

---

### Chart 4: Comprehensive Performance Dashboard

<img width="833" height="591" alt="Performance_Analysis" src="https://github.com/user-attachments/assets/a21e0afb-ea9c-4739-9c68-1085e0b230f7" />

*Figure 6: Combined performance dashboard showing the major performance measurements for both hypervisor configurations.*

---

## 8. Technical Analysis & Discussion

The experimental results show a measurable performance difference between **Proxmox VE (Type-1)** and **VMware Workstation (Type-2)** when running the CPU-intensive Sysbench workload.

### 1. Architectural Overhead & Trap-and-Emulate Delays

- **Proxmox VE (Type-1)** uses Linux KVM and interfaces closely with the hardware Intel VT-x / AMD-V virtualization extensions. Many CPU instructions generated inside the VM can therefore execute with limited hypervisor intervention.
- **VMware Workstation (Type-2)** operates above the Windows NT operating system. Guest CPU operations pass through the VMware virtualization engine while also depending on the host operating system for hardware resource management. This additional layer can introduce virtualization overhead.

### 2. CPU Scheduling & Context Switching

- In Proxmox VE, guest vCPUs are represented through host Linux kernel threads and are scheduled by the **Completely Fair Scheduler (CFS)**.
- In VMware Workstation, guest CPU execution shares resources with Windows host processes and background services such as Windows Defender, System Updates, and Desktop Window Manager.
- These additional host activities can result in thread preemptions and context switches, which may contribute to higher latency values.
- The observed maximum latency was **6.16 ms on VMware compared with 2.78 ms on Proxmox**, showing a difference in the latency spikes measured during the experiment.

### 3. Memory & Virtual Cache Access

- Proxmox VE can take advantage of hardware-assisted memory virtualization techniques such as Extended Page Tables (EPT / NPT).
- Type-2 hypervisors also manage guest memory through the host operating system, which can introduce additional address translation overhead.
- The memory mapping process can involve Guest Physical Address (GPA) → Host Virtual Address (HVA) → Host Physical Address (HPA).

---

## 9. Conclusion & Engineering Takeaways

1. **Bare-metal dominance**: In this experimental benchmark, Proxmox VE (Type-1) delivered **+150.79% higher CPU throughput** and **60.27% lower average latency** compared to VMware Workstation (Type-2).
2. **Predictable Latency**: Proxmox VE recorded a lower 95th percentile latency of **0.65 ms compared with 1.58 ms**, indicating lower measured latency variation in this test.
3. **Use-Case Recommendation**:
   - **Type-1 (Proxmox VE / KVM / ESXi)**: Commonly used for Cloud Data Centers, Production Enterprise Infrastructure, Database Servers, and High-Performance Computing (HPC).
   - **Type-2 (VMware Workstation / VirtualBox)**: Commonly used for Local Software Development, Testing, Desktop Sandbox Environments, and Educational Labs.
4. **Overall Observation**: The experiment demonstrates that the architecture of a hypervisor and the software layers between the guest VM and physical hardware can influence CPU benchmark performance.

---

## 10. Repository Structure & Reproduction

### Folder Layout

```text
Cloud_computing/
│
├── README.md                                                   # Main Project & Benchmark Report
├── LAB_REPORT.md                                               # Formal Academic Lab Report Submission
├── Lab-Manual-Hypervisor-Performance-Analysis (1).docx         # Reference Lab Manual Document
│
├── images/                                                     # Screenshots & Generated Charts
│   ├── 1.png                                                   # Proxmox VE Sysbench Result Screenshot
│   ├── 2.png                                                   # VMware Workstation Sysbench Result Screenshot
│   ├── events_per_second_comparison.png                        # Throughput Comparison Graph
│   ├── latency_comparison.png                                  # Latency Metrics Graph
│   ├── total_events_comparison.png                             # Total Events Graph
│   └── overall_performance_dashboard.png                       # Multi-panel Dashboard
│
└── scripts/                                                    # Automation & Plotting Scripts
    ├── benchmark.sh                                            # Sysbench Automation Script
    ├── generate_plots.py                                       # Matplotlib Visualization Generator
    └── parse_sysbench.py                                       # Results Parser & Ratio Calculator

```

### How to Reproduce

1. **Run Benchmark Script on VM**:
   ```bash
   chmod +x scripts/benchmark.sh
   ./scripts/benchmark.sh
   ```

2. **Generate Plots**:
   ```bash
   python scripts/generate_plots.py
   ```

3. **Parse & Compare Results**:
   ```bash
   python scripts/parse_sysbench.py
   ```

---
