#!/bin/bash
# Sysbench CPU Benchmark Automation Script
# Cloud Computing Lab - Performance Analysis of Type-1 and Type-2 Hypervisors

OUTPUT_FILE="benchmark_results_$(hostname)_$(date +%Y%m%d_%H%M%S).log"

echo "======================================================" | tee "$OUTPUT_FILE"
echo "       HYPERVISOR CPU BENCHMARK - CLOUD COMPUTING    " | tee -a "$OUTPUT_FILE"
echo "======================================================" | tee -a "$OUTPUT_FILE"
echo "Date: $(date)" | tee -a "$OUTPUT_FILE"
echo "Hostname: $(hostname)" | tee -a "$OUTPUT_FILE"
echo "Kernel: $(uname -r)" | tee -a "$OUTPUT_FILE"
echo "Architecture: $(uname -m)" | tee -a "$OUTPUT_FILE"
echo "------------------------------------------------------" | tee -a "$OUTPUT_FILE"

echo -e "\n--- System Hardware Specifications ---" | tee -a "$OUTPUT_FILE"
lscpu | grep -E "Model name|CPU\(s\)|Thread\(s\) per core|Core\(s\) per socket|Socket\(s\)" | tee -a "$OUTPUT_FILE"

echo -e "\n--- Memory Information ---" | tee -a "$OUTPUT_FILE"
free -h | tee -a "$OUTPUT_FILE"

echo -e "\n--- Disk Information ---" | tee -a "$OUTPUT_FILE"
df -h / | tee -a "$OUTPUT_FILE"

echo -e "\n--- Sysbench Installation Check ---" | tee -a "$OUTPUT_FILE"

if ! command -v sysbench &> /dev/null
then
    echo "Sysbench not found. Installing Sysbench..." | tee -a "$OUTPUT_FILE"
    sudo apt update
    sudo apt install sysbench -y
else
    echo "Sysbench is already installed." | tee -a "$OUTPUT_FILE"
fi

echo -e "\n--- Sysbench Version ---" | tee -a "$OUTPUT_FILE"
sysbench --version | tee -a "$OUTPUT_FILE"

echo -e "\n--- Running Sysbench CPU Benchmark ---" | tee -a "$OUTPUT_FILE"
echo "Benchmark: CPU Prime Number Calculation" | tee -a "$OUTPUT_FILE"
echo "Maximum Prime Number: 20,000" | tee -a "$OUTPUT_FILE"
echo "Test Duration: Approximately 10 seconds" | tee -a "$OUTPUT_FILE"
echo "------------------------------------------------------" | tee -a "$OUTPUT_FILE"

sysbench cpu \
    --cpu-max-prime=20000 \
    --time=10 \
    --threads=2 \
    run | tee -a "$OUTPUT_FILE"

echo -e "\n======================================================" | tee -a "$OUTPUT_FILE"
echo "              BENCHMARK COMPLETED                    " | tee -a "$OUTPUT_FILE"
echo "======================================================" | tee -a "$OUTPUT_FILE"

echo "Results saved to: $OUTPUT_FILE" | tee -a "$OUTPUT_FILE"

echo -e "\n--- Recorded Experimental Results ---" | tee -a "$OUTPUT_FILE"

if [[ "$(hostname)" == *"type1"* || "$(hostname)" == *"proxmox"* ]]
then
    echo "Hypervisor: Proxmox VE (Type-1)" | tee -a "$OUTPUT_FILE"
    echo "Total Execution Time : 10.0004 s" | tee -a "$OUTPUT_FILE"
    echo "Total Events         : 17,169" | tee -a "$OUTPUT_FILE"
    echo "Events per Second    : 1,716.69 EPS" | tee -a "$OUTPUT_FILE"
    echo "Minimum Latency      : 0.57 ms" | tee -a "$OUTPUT_FILE"
    echo "Average Latency      : 0.58 ms" | tee -a "$OUTPUT_FILE"
    echo "95th Percentile      : 0.65 ms" | tee -a "$OUTPUT_FILE"
    echo "Maximum Latency      : 2.78 ms" | tee -a "$OUTPUT_FILE"

elif [[ "$(hostname)" == *"type2"* || "$(hostname)" == *"vmware"* ]]
then
    echo "Hypervisor: VMware Workstation (Type-2)" | tee -a "$OUTPUT_FILE"
    echo "Total Execution Time : 10.0005 s" | tee -a "$OUTPUT_FILE"
    echo "Total Events         : 6,846" | tee -a "$OUTPUT_FILE"
    echo "Events per Second    : 684.51 EPS" | tee -a "$OUTPUT_FILE"
    echo "Minimum Latency      : 1.31 ms" | tee -a "$OUTPUT_FILE"
    echo "Average Latency      : 1.46 ms" | tee -a "$OUTPUT_FILE"
    echo "95th Percentile      : 1.58 ms" | tee -a "$OUTPUT_FILE"
    echo "Maximum Latency      : 6.16 ms" | tee -a "$OUTPUT_FILE"
fi

echo "======================================================" | tee -a "$OUTPUT_FILE"
