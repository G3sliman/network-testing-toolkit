# Network Testing and Diagnostics Toolkit

A Python-based network diagnostics toolkit designed to help users perform basic network testing and troubleshooting through a simple command-line menu.

## Features

- **IP Address Information:** Identifies IP version and address type, and displays local subnet information when available.
- **Network Interfaces:** Displays local IP addresses, subnet masks, and default gateways.
- **Ping Testing:** Checks network reachability and calculates packet loss and average response time.
- **DNS Lookup:** Retrieves IPv4 and IPv6 addresses associated with a domain.
- **Traceroute:** Displays the network path toward a destination.
- **TCP Port Testing:** Checks TCP connectivity to a specified host and port.
- **JSON Reports:** Automatically saves test results as JSON files.
- **Saved Reports:** Allows users to view previously generated reports.

## Technologies Used

- Python 3
- Socket
- Subprocess
- IP Address
- JSON
- Regular Expressions
- Operating System Detection

## Requirements

- Python 3
- Windows or Kali Linux
- Internet or network connectivity for external network tests

The project uses Python's standard library, so no external Python packages are required.

## How to Run

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project directory:

```bash
cd network-testing-toolkit
```

Run on Windows:

```bash
python main.py
```

Run on Kali Linux:

```bash
python3 main.py
```

## Project Structure

```text
network-testing-toolkit/
├── main.py
├── ip_info.py
├── network_info.py
├── ping_test.py
├── dns_lookup.py
├── traceroute.py
├── port_test.py
├── report.py
├── README.md
└── reports/
```

## Reports

Test results are saved automatically in JSON format inside the `reports/` directory.

Reports include relevant information such as:

- Tool name
- Timestamp
- Destination
- Test results
- Network response information

## Learning Objectives

This project helped me develop practical knowledge of:

- IP addressing and subnetting
- ICMP and network reachability
- DNS resolution
- Network routing and traceroute
- TCP connectivity
- Python automation
- JSON data handling
- Error handling and subprocess management

## Responsible Use

Use this toolkit only on networks and systems you own or have explicit permission to test.

## Future Improvements

- More detailed network diagnostics
- Improved cross-platform compatibility
- Additional network testing features
- Enhanced report analysis
