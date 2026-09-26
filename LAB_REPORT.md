# LABORATORY REPORT
## Performance Analysis of Type-1 and Type-2 Hypervisors

**Course Title:** Cloud Computing / Computer Networks Laboratory  
**Experiment No:** 1  
**Topic:** Comparative CPU Performance Evaluation of Proxmox VE (Type-1) and VMware Workstation (Type-2) Hypervisors  

---

## 1. Objective of the Experiment

The main objectives of this laboratory experiment are to:

1. Deploy two virtual machines with identical hardware configurations using two different hypervisor architectures:
   - **Type-1 Hypervisor**: Proxmox VE (Bare-metal)
   - **Type-2 Hypervisor**: VMware Workstation Pro (Hosted)
2. Perform a CPU-based computational benchmark using `sysbench` with the parameter `--cpu-max-prime=20000`.
3. Record important performance parameters such as total execution time, total events, events per second (throughput), minimum latency, average latency, maximum latency, and 95th percentile latency.
4. Compare the obtained benchmark results between the two hypervisors.
5. Study how hypervisor architecture, host operating system overhead, and resource abstraction can affect virtual machine CPU performance.

---

## 2. Theory & Hypervisor Classification

### 2.1 Type-1 Hypervisor (Bare-Metal Hypervisor)

A Type-1 hypervisor operates directly on the physical hardware of the system without depending on a conventional host operating system. It manages the available hardware resources and provides them to virtual machines.

- **Examples**: Proxmox VE (KVM), VMware ESXi, Microsoft Hyper-V (Core), Xen.
- **Architecture**:

 ```
  [ Guest Virtual Machine (Ubuntu) ]
                │
                ▼
  [ Proxmox VE Hypervisor (KVM Kernel) ]
                │
                ▼
  [ Physical Hardware (CPU, RAM, Disk) ]
  ```

- **Advantages**: Low virtualization overhead, efficient hardware utilization, direct support for hardware virtualization extensions such as Intel VT-x / AMD-V, better throughput, reduced latency, and suitability for large-scale virtualization environments.

### 2.2 Type-2 Hypervisor (Hosted Hypervisor)

A Type-2 hypervisor works as an application or software layer installed on top of an existing host operating system. The virtual machines depend on both the hypervisor application and the underlying host OS for resource management.

- **Examples**: VMware Workstation, Oracle VM VirtualBox, Parallels Desktop.
- **Architecture**:

 ```
  [ Guest Virtual Machine (Ubuntu) ]
                │
                ▼
  [ VMware Workstation (Hypervisor App) ]
                │
                ▼
  [ Host Operating System (Windows 11) ]
                │
                ▼
  [ Physical Hardware (CPU, RAM, Disk) ]
  ```

- **Advantages**: Simple installation, convenient graphical interface, easy desktop integration, flexible configuration, and useful networking options.
- **Disadvantages**: Additional software abstraction, possible host OS resource contention, extra CPU scheduling overhead, and increased context switching delays.

---

## 3. Hardware & Software Specifications

### Standardized Virtual Machine Specifications

Both virtual machines were configured with the same major hardware resource limits to ensure a fair comparison between the two hypervisor architectures.

| Resource Parameter | Proxmox VE (Type-1) | VMware Workstation (Type-2) |
| :--- | :--- | :--- |
| **Virtual Machine Name** | `CC-Experiment1-type1` | `CC-Experiment1-Type2` |
| **VM ID / Host Identifier** | `123` | `humeira-VMware-Virtual-Platform` |
| **Guest OS** | Ubuntu 24.04.3 LTS AMD64 | Ubuntu Linux 64-bit |
| **Virtual CPU (vCPU)** | 2 vCPU (1 socket, 2 cores) | 2 vCPU (1 processor, 2 cores) |
| **CPU Type** | x86-64-v2-AES | Default / Passthrough |
| **Memory (RAM)** | 2048 MiB (2 GB) | 2048 MB (2 GB) |
| **Virtual Hard Disk** | 20 GB (VirtIO SCSI) | 20 GB (NVMe / SCSI single file) |
| **Network Adapter** | VirtIO Bridge (`vmbr0`) | NAT (`VMnet8`) |

---

## 4. Step-by-Step Experimental Procedure

### Part A: Proxmox VE (Type-1) Workflow

1. Open the Proxmox VE web management console using `https://10.11.0.252:8006`.
2. Select **Create VM** and configure the VM ID as `123` with the name `CC-Experiment1-type1`.
3. Attach the Ubuntu ISO image and allocate 2 CPU cores, 2048 MiB RAM, and a 20 GB virtual disk.
4. Start the virtual machine, complete the Ubuntu installation, and check the system configuration using:
 ```bash
 hostnamectl
 lscpu
 free -h
 df -h
 top
```
5. Install Sysbench and execute the CPU benchmark:
   ```bash
   sudo apt update && sudo apt install sysbench -y
   sysbench cpu --cpu-max-prime=20000 run

### Part B: VMware Workstation (Type-2) Workflow

1. Launch VMware Workstation on Windows host.
2. Select **Create a New Virtual Machine** $\rightarrow$ **Typical**.
3. Browse and select Ubuntu ISO image.
4. Set VM Name to `CC-Experiment1-Type2` and location.
5. Allocate 20 GB Disk, customize hardware to 2 vCPU, 2 GB RAM, NAT network.
6. Power on VM, complete Ubuntu installation, verify system state (`lscpu`, `free -h`).
7. Install and run Sysbench:
   ```bash
   sudo apt update && sudo apt install sysbench -y
   sysbench cpu --cpu-max-prime=20000 run
   ```

   ---

   ## 5. Experimental Observations & Data Collection

### Primary Benchmark Outputs

#### 1. Proxmox VE (Type-1 Hypervisor) Output:

<img width="633" height="327" alt="Output2 jpg" src="https://github.com/user-attachments/assets/db28fbb1-47c0-4686-8df1-af18f8ad859b" />

#### 2. VMware Workstation (Type-2 Hypervisor) Output:

<img width="902" height="703" alt="Output1 jpg" src="https://github.com/user-attachments/assets/00ffa56c-b3bf-4509-bb33-7c183dbbcf18" />

## 6. Consolidated Performance Comparison Table

| Performance Metric | Proxmox VE (Type-1) | VMware Workstation (Type-2) | Difference / Delta | Remarks |
| :--- | :---: | :---: | :---: | :--- |
| **Total Execution Time** | **10.0004 s** | **10.0005 s** | 0.0001 s | Standard 10-second test window |
| **Total Events Processed** | **17,169** | **6846** | **+10,323 events** | **Proxmox VE +150.79% capacity** |
| **Events per Second (EPS)**| **1,716.69** | **684.51** | **+1,032.18 eps** | **Proxmox VE +150.79% throughput** |
| **Minimum Latency** | **0.57 ms** | **1.31 ms** | **-0.74 ms** | **Proxmox VE 56.49% lower** |
| **Average Latency** | **0.58 ms** | **1.46 ms** | **-0.88 ms** | **Proxmox VE 60.27% lower** |
| **95th Percentile Latency**| **0.65 ms** | **1.58 ms** | **-0.93 ms** | **Proxmox VE 58.86% lower** |
| **Maximum Latency** | **2.78 ms** | **6.16 ms** | **-3.38 ms** | **Proxmox VE 54.87% lower** |

---

## 7. Performance Visualization

### Figure 1: CPU Throughput (Events/sec)

<img width="1080" height="721" alt="image" src="https://github.com/user-attachments/assets/52337b0e-95d0-449c-a804-dd5f14d1b354" />

### Figure 2: Latency Distribution Comparison

<img width="923" height="502" alt="CPU_Latency_Matrix_Graph" src="https://github.com/user-attachments/assets/1d345c08-aa87-40af-a130-c3d59ae8bfaa" />

### Figure 3: Total Events Processed

<img width="922" height="547" alt="Total_Events_Processed_Graph" src="https://github.com/user-attachments/assets/04d7120d-4407-44cc-93fc-5a976e53bc1d" />

---

## 8. Technical Analysis & Discussion

### 8.1 Throughput Analysis

The benchmark evaluates the number of prime-number calculations that can be performed within the fixed 10-second testing period. Proxmox VE completed 17,169 events with a throughput of 1,716.69 events/sec, whereas VMware Workstation completed 6,846 events at 684.51 events/sec.

- **Percentage Improvement**:
  $$\text{Improvement} = \frac{1716.69 - 684.51}{684.51} \times 100\% = 150.79\%$$

The measured results show a noticeable difference in CPU processing throughput between the two virtualization environments. The higher event rate indicates that more computational operations were completed during the same test duration.

### 8.2 Latency & Overhead Analysis

- **Average Latency**: The average latency recorded for Proxmox VE was 0.58 ms per event, while VMware Workstation recorded 1.46 ms. This represents a difference of approximately 0.88 ms between the two configurations.
- **Root Cause**:
  1. **Host OS Context Switches**: In a Type-2 hypervisor, CPU operations are managed through the host Windows operating system, which can introduce additional scheduling and context-switching overhead.
  2. **Privileged Mode Transitions**: Proxmox VE uses KVM-based virtualization and hardware-assisted CPU virtualization, which reduces some of the additional processing required between the guest system and physical hardware.
  3. **Resource Management Overhead**: VMware Workstation depends on the host operating system for resource allocation, which may result in additional CPU scheduling overhead during execution.
  4. **Virtualization Abstraction**: The additional software layer in a hosted hypervisor can increase the amount of processing required for certain operations and may affect latency.

---

## 9. Conclusion

1. **Type-1 hypervisors (Proxmox VE)** showed higher CPU throughput in the conducted experiment, achieving approximately 150.79% more events per second and around 60.27% lower average latency than the tested Type-2 configuration.
2. The experimental results indicate that the additional host operating system layer and resource management overhead associated with Type-2 virtualization can influence CPU benchmark performance.
3. Proxmox VE processed a greater number of events within the same 10-second test period and also recorded lower latency values across the measured latency parameters.
4. The comparison demonstrates that hypervisor architecture can have a measurable effect on CPU-intensive virtual machine workloads.
5. **Engineering Recommendation**: Type-1 hypervisors are suitable for environments where efficient resource utilization and virtualization performance are important, while Type-2 hypervisors can be useful for desktop-based development, testing, and laboratory experimentation.

---
 
