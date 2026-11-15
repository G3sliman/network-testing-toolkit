

from report import save_report
import socket
import ipaddress


def dns_lookup():

    domain = input("Enter a domain name (e.g. google.com): ").strip()

    if not domain:
        print("\nError: Domain name cannot be empty.")
        return

    try:
        results = socket.getaddrinfo(domain, None)

        ipv4_addresses = set()
        ipv6_addresses = set()

        for result in results:

            address = result[4][0]
            ip = ipaddress.ip_address(address)

            if ip.version == 4:
                ipv4_addresses.add(str(ip))
            else:
                ipv6_addresses.add(str(ip))

        print("\n========== DNS LOOKUP RESULTS ==========")
        print("Domain:", domain)

        print("\nIPv4 Addresses (A):")

        if ipv4_addresses:
            for address in sorted(ipv4_addresses):
                print("-", address)
        else:
            print("No IPv4 addresses found.")

        print("\nIPv6 Addresses (AAAA):")

        if ipv6_addresses:
            for address in sorted(ipv6_addresses):
                print("-", address)
        else:
            print("No IPv6 addresses found.")

        print("========================================")

        dns_results = {
            "domain": domain,
            "ipv4_addresses": sorted(ipv4_addresses),
            "ipv6_addresses": sorted(ipv6_addresses)
        }

        save_report("DNS Lookup", dns_results)

    except socket.gaierror:
        print("\nError: Could not resolve this domain.")
        print("Check the domain name or your network connection.")


if __name__ == "__main__":
    dns_lookup()
