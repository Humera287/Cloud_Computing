#!/usr/bin/env python3
"""
Sysbench Output Parser & Hypervisor Performance Comparator
Calculates percentage differences between Type-1 (Proxmox VE) and Type-2 (VMware Workstation) hypervisors.
"""

def compare_hypervisors():
    proxmox = {
        "hypervisor": "Proxmox VE (Type-1)",
        "eps": 1716.69,
        "total_time": 10.0004,
        "total_events": 17169,
        "min_lat": 0.57,
        "avg_lat": 0.58,
        "max_lat": 2.78,
        "p95_lat": 0.65,
    }

    vmware = {
        "hypervisor": "VMware Workstation (Type-2)",
        "eps": 684.51,
        "total_time": 10.0005,
        "total_events": 6846,
        "min_lat": 1.31,
        "avg_lat": 1.46,
        "max_lat": 6.16,
        "p95_lat": 1.58,
    }

    # Calculate differences
    eps_diff = ((proxmox["eps"] - vmware["eps"]) / vmware["eps"]) * 100
    events_diff = proxmox["total_events"] - vmware["total_events"]

    min_lat_diff = vmware["min_lat"] - proxmox["min_lat"]
    avg_lat_diff = ((vmware["avg_lat"] - proxmox["avg_lat"]) / vmware["avg_lat"]) * 100
    p95_lat_diff = ((vmware["p95_lat"] - proxmox["p95_lat"]) / vmware["p95_lat"]) * 100
    max_lat_diff = vmware["max_lat"] - proxmox["max_lat"]

    print("===================================================================================")
    print("      HYPERVISOR CPU PERFORMANCE COMPARISON: TYPE-1 VS TYPE-2")
    print("===================================================================================")
    print(f"Metric                         Proxmox VE (Type-1)   VMware (Type-2)     Difference")
    print("-----------------------------------------------------------------------------------")

    print(
        f"Throughput (Events/sec)        "
        f"{proxmox['eps']:<20.2f} "
        f"{vmware['eps']:<18.2f} "
        f"+{eps_diff:.2f}% (Proxmox higher)"
    )

    print(
        f"Total Events (10s)             "
        f"{proxmox['total_events']:<20} "
        f"{vmware['total_events']:<18} "
        f"+{events_diff} events"
    )

    print(
        f"Minimum Latency (ms)           "
        f"{proxmox['min_lat']:<20.2f} "
        f"{vmware['min_lat']:<18.2f} "
        f"Proxmox {min_lat_diff:.2f}ms lower"
    )

    print(
        f"Average Latency (ms)           "
        f"{proxmox['avg_lat']:<20.2f} "
        f"{vmware['avg_lat']:<18.2f} "
        f"Proxmox {avg_lat_diff:.2f}% lower"
    )

    print(
        f"95th Percentile Latency (ms)   "
        f"{proxmox['p95_lat']:<20.2f} "
        f"{vmware['p95_lat']:<18.2f} "
        f"Proxmox {p95_lat_diff:.2f}% lower"
    )

    print(
        f"Maximum Latency (ms)           "
        f"{proxmox['max_lat']:<20.2f} "
        f"{vmware['max_lat']:<18.2f} "
        f"Proxmox {max_lat_diff:.2f}ms lower"
    )

    print("===================================================================================")


if __name__ == "__main__":
    compare_hypervisors()
