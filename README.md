# Network Testing and Diagnostics Toolkit

A Python-based network diagnostics toolkit designed to help users perform basic network testing and troubleshooting through a simple command-line application.

The project combines multiple networking utilities into one program, making it easier to inspect network configurations, test connectivity, resolve domain names, trace network routes, and check TCP port availability.

## Features

- **IP Address Information:** Identifies IP versions and address types, and displays local subnet information when available.
- **Network Interfaces:** Displays local IP addresses, subnet masks, and default gateways.
- **Ping Testing:** Checks network reachability and calculates packet loss and average response time.
- **DNS Lookup:** Retrieves IPv4 and IPv6 addresses associated with a domain name.
- **Traceroute:** Displays the network path toward a destination.
- **TCP Port Testing:** Checks TCP connectivity to a specified host and port.
- **JSON Reports:** Automatically saves diagnostic results in JSON format.
- **Saved Reports:** Allows users to view previously generated diagnostic reports.

## Technologies Used

- Python 3
- Socket
- IP Address
- Subprocess
- JSON
- Regular Expressions
- Operating System Detection
- Pathlib and Datetime

## Requirements

- Python 3
- Windows or Kali Linux
- Network connectivity for external network tests
- Git (for cloning the repository)

The project uses Python's standard library, so no external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/G3sliman/network-testing-toolkit.git
```

Navigate into the project directory:

```bash
cd network-testing-toolkit
```

## How to Run

### Windows

```bash
python main.py
```

### Kali Linux

```bash
python3 main.py
```

Note: Linux networking utilities such as `ip`, `traceroute`, or `tracepath` may be required for certain features.

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
└── .gitignore
```

## Reporting System

The toolkit automatically saves diagnostic results as JSON files inside the `reports/` directory.

Reports can contain information such as:

- Diagnostic tool name
- Timestamp
- Destination IP or hostname
- Test results
- Network response information

Users can also view previously generated reports through the application menu.

## Learning Objectives

This project helped me develop practical knowledge and experience in:

- IP addressing and subnetting
- Network interfaces and configuration
- ICMP and network reachability
- DNS resolution
- Network routing and traceroute
- TCP connectivity and port testing
- Python automation and modular programming
- JSON data handling
- Error handling and subprocess management
- Cross-platform command execution

## Responsible Use

Use this toolkit only on networks and systems you own or have explicit permission to test.

This project is intended for basic network diagnostics and educational purposes. It is not a replacement for advanced network security assessment tools.

## Future Improvements

- Add more advanced network diagnostic features.
- Improve cross-platform compatibility and testing.
- Add more detailed network analysis.
- Improve report visualization and analysis.
- Expand error handling and diagnostic capabilities.

## Author

**G3sliman**

GitHub: https://github.com/G3sliman
