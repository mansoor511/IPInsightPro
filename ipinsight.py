#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                         IP INSIGHT PRO v2.0                               ║
║                   Advanced IP Information Tool                          ║
║                                                                           ║
║                      Coded by: MANSOOR BIK KAMALI                         ║
║                         Ethical Hacking Tool                              ║
║                    For Educational Purposes Only                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import requests
import socket
import json
import sys
import os
import time
from datetime import datetime
import ipaddress
import dns.resolver
import whois
import pyfiglet
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

class IPInsightPro:
    def __init__(self):
        self.api_key = ""  # Optional: Add your API key for more features
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def banner(self):
        """Display beautiful banner"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # ASCII Art with pyfiglet
        banner_text = pyfiglet.figlet_format("IP Insight Pro", font="slant")
        print(Fore.CYAN + banner_text)
        
        print(Fore.YELLOW + "═" * 70)
        print(Fore.GREEN + "║" + Fore.WHITE + " " * 68 + Fore.GREEN + "║")
        print(Fore.GREEN + "║" + Fore.CYAN + "         Advanced IP Information Tool - Version 2.0" + " " * 20 + Fore.GREEN + "║")
        print(Fore.GREEN + "║" + Fore.MAGENTA + "              Coded by: MANSOOR BIK KAMALI" + " " * 28 + Fore.GREEN + "║")
        print(Fore.GREEN + "║" + Fore.RED + "              For Educational Purposes Only" + " " * 29 + Fore.GREEN + "║")
        print(Fore.GREEN + "║" + Fore.WHITE + " " * 68 + Fore.GREEN + "║")
        print(Fore.YELLOW + "═" * 70)
        print()
        
    def show_menu(self):
        """Display main menu"""
        print(Fore.CYAN + "\n" + "═" * 50)
        print(Fore.YELLOW + "📋 MAIN MENU")
        print(Fore.CYAN + "═" * 50)
        print(Fore.GREEN + "1." + Fore.WHITE + " My IP Information (My IP)")
        print(Fore.GREEN + "2." + Fore.WHITE + " Target IP Information")
        print(Fore.GREEN + "3." + Fore.WHITE + " IP to Domain Reverse Lookup")
        print(Fore.GREEN + "4." + Fore.WHITE + " Domain to IP Lookup")
        print(Fore.GREEN + "5." + Fore.WHITE + " IP Geolocation Map")
        print(Fore.GREEN + "6." + Fore.WHITE + " IP Range Scanner")
        print(Fore.GREEN + "7." + Fore.WHITE + " DNS Records Lookup")
        print(Fore.GREEN + "8." + Fore.WHITE + " Whois Information")
        print(Fore.GREEN + "9." + Fore.WHITE + " IP Abuse Check")
        print(Fore.GREEN + "10." + Fore.WHITE + " Bulk IP Check")
        print(Fore.GREEN + "11." + Fore.WHITE + " IP Calculator (CIDR)")
        print(Fore.GREEN + "12." + Fore.WHITE + " Exit")
        print(Fore.CYAN + "═" * 50)
        
    def get_my_ip(self):
        """Get public IP information"""
        try:
            print(Fore.YELLOW + "\n[+] Fetching your IP information...")
            
            # Get IP from multiple sources
            response1 = self.session.get('https://api.ipify.org?format=json')
            ip_data1 = response1.json()
            
            response2 = self.session.get('http://ip-api.com/json/')
            ip_data2 = response2.json()
            
            response3 = self.session.get('https://ipapi.co/json/')
            ip_data3 = response3.json()
            
            print(Fore.GREEN + "\n" + "═" * 50)
            print(Fore.CYAN + "📡 YOUR IP INFORMATION")
            print(Fore.GREEN + "═" * 50)
            
            print(Fore.YELLOW + f"IP Address: " + Fore.WHITE + f"{ip_data1['ip']}")
            print(Fore.YELLOW + f"Country: " + Fore.WHITE + f"{ip_data2.get('country', 'N/A')}")
            print(Fore.YELLOW + f"Country Code: " + Fore.WHITE + f"{ip_data2.get('countryCode', 'N/A')}")
            print(Fore.YELLOW + f"Region: " + Fore.WHITE + f"{ip_data2.get('regionName', 'N/A')}")
            print(Fore.YELLOW + f"City: " + Fore.WHITE + f"{ip_data2.get('city', 'N/A')}")
            print(Fore.YELLOW + f"Zip Code: " + Fore.WHITE + f"{ip_data2.get('zip', 'N/A')}")
            print(Fore.YELLOW + f"Latitude: " + Fore.WHITE + f"{ip_data2.get('lat', 'N/A')}")
            print(Fore.YELLOW + f"Longitude: " + Fore.WHITE + f"{ip_data2.get('lon', 'N/A')}")
            print(Fore.YELLOW + f"Timezone: " + Fore.WHITE + f"{ip_data2.get('timezone', 'N/A')}")
            print(Fore.YELLOW + f"ISP: " + Fore.WHITE + f"{ip_data2.get('isp', 'N/A')}")
            print(Fore.YELLOW + f"Organization: " + Fore.WHITE + f"{ip_data2.get('org', 'N/A')}")
            print(Fore.YELLOW + f"AS: " + Fore.WHITE + f"{ip_data2.get('as', 'N/A')}")
            print(Fore.YELLOW + f"Mobile: " + Fore.WHITE + f"{ip_data2.get('mobile', 'N/A')}")
            print(Fore.YELLOW + f"Proxy: " + Fore.WHITE + f"{ip_data2.get('proxy', 'N/A')}")
            print(Fore.YELLOW + f"Hosting: " + Fore.WHITE + f"{ip_data2.get('hosting', 'N/A')}")
            
            # Google Maps link
            lat = ip_data2.get('lat', '0')
            lon = ip_data2.get('lon', '0')
            print(Fore.YELLOW + f"Google Maps: " + Fore.BLUE + f"https://www.google.com/maps?q={lat},{lon}")
            
            print(Fore.GREEN + "═" * 50)
            
        except Exception as e:
            print(Fore.RED + f"[-] Error: {e}")
    
    def get_ip_info(self, ip):
        """Get detailed information about an IP address"""
        try:
            # Validate IP
            socket.inet_aton(ip)
            
            print(Fore.YELLOW + f"\n[+] Fetching information for IP: {ip}")
            
            # Get information from multiple APIs
            response = self.session.get(f'http://ip-api.com/json/{ip}')
            data = response.json()
            
            if data.get('status') == 'fail':
                print(Fore.RED + "[-] Invalid IP address or API limit reached")
                return
            
            print(Fore.GREEN + "\n" + "═" * 60)
            print(Fore.CYAN + f"🎯 IP INFORMATION: {ip}")
            print(Fore.GREEN + "═" * 60)
            
            # Basic Information
            print(Fore.YELLOW + "\n📌 Basic Information:")
            print(Fore.WHITE + f"  • IP: " + Fore.CYAN + f"{data.get('query', ip)}")
            print(Fore.WHITE + f"  • Status: " + Fore.GREEN + f"{data.get('status', 'N/A')}")
            
            # Location Information
            print(Fore.YELLOW + "\n📍 Location Information:")
            print(Fore.WHITE + f"  • Country: " + Fore.CYAN + f"{data.get('country', 'N/A')}")
            print(Fore.WHITE + f"  • Country Code: " + Fore.CYAN + f"{data.get('countryCode', 'N/A')}")
            print(Fore.WHITE + f"  • Region: " + Fore.CYAN + f"{data.get('regionName', 'N/A')}")
            print(Fore.WHITE + f"  • City: " + Fore.CYAN + f"{data.get('city', 'N/A')}")
            print(Fore.WHITE + f"  • Zip Code: " + Fore.CYAN + f"{data.get('zip', 'N/A')}")
            print(Fore.WHITE + f"  • Latitude: " + Fore.CYAN + f"{data.get('lat', 'N/A')}")
            print(Fore.WHITE + f"  • Longitude: " + Fore.CYAN + f"{data.get('lon', 'N/A')}")
            
            # Network Information
            print(Fore.YELLOW + "\n🌐 Network Information:")
            print(Fore.WHITE + f"  • ISP: " + Fore.CYAN + f"{data.get('isp', 'N/A')}")
            print(Fore.WHITE + f"  • Organization: " + Fore.CYAN + f"{data.get('org', 'N/A')}")
            print(Fore.WHITE + f"  • AS Number: " + Fore.CYAN + f"{data.get('as', 'N/A')}")
            print(Fore.WHITE + f"  • Timezone: " + Fore.CYAN + f"{data.get('timezone', 'N/A')}")
            
            # Additional Information
            print(Fore.YELLOW + "\n🔍 Additional Information:")
            print(Fore.WHITE + f"  • Mobile Connection: " + Fore.CYAN + f"{data.get('mobile', 'N/A')}")
            print(Fore.WHITE + f"  • Proxy/VPN: " + Fore.CYAN + f"{data.get('proxy', 'N/A')}")
            print(Fore.WHITE + f"  • Hosting Provider: " + Fore.CYAN + f"{data.get('hosting', 'N/A')}")
            
            # Google Maps Link
            lat = data.get('lat', '0')
            lon = data.get('lon', '0')
            print(Fore.YELLOW + f"\n🗺️  Google Maps Link:")
            print(Fore.BLUE + f"  https://www.google.com/maps?q={lat},{lon}")
            
            print(Fore.GREEN + "\n" + "═" * 60)
            
        except socket.error:
            print(Fore.RED + "[-] Invalid IP address format")
        except Exception as e:
            print(Fore.RED + f"[-] Error: {e}")
    
    def reverse_dns(self, ip):
        """Reverse DNS lookup"""
        try:
            print(Fore.YELLOW + f"\n[+] Performing reverse DNS lookup for {ip}")
            hostname = socket.gethostbyaddr(ip)
            print(Fore.GREEN + f"[+] Hostname: {hostname[0]}")
        except:
            print(Fore.RED + "[-] No reverse DNS record found")
    
    def domain_to_ip(self, domain):
        """Convert domain to IP address"""
        try:
            print(Fore.YELLOW + f"\n[+] Resolving domain: {domain}")
            ip = socket.gethostbyname(domain)
            print(Fore.GREEN + f"[+] IP Address: {ip}")
            
            # Get all IPs
            ips = socket.gethostbyname_ex(domain)
            if len(ips[2]) > 1:
                print(Fore.YELLOW + "[+] All IPs:")
                for ip_addr in ips[2]:
                    print(Fore.WHITE + f"  • {ip_addr}")
                    
        except:
            print(Fore.RED + "[-] Could not resolve domain")
    
    def ip_to_domain(self, ip):
        """Find domains hosted on IP"""
        try:
            print(Fore.YELLOW + f"\n[+] Finding domains for IP: {ip}")
            response = self.session.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
            domains = response.text.split('\n')
            
            print(Fore.GREEN + "[+] Found domains:")
            for domain in domains[:10]:  # Show first 10
                if domain:
                    print(Fore.WHITE + f"  • {domain}")
                    
        except:
            print(Fore.RED + "[-] No domains found or API limit reached")
    
    def dns_lookup(self, domain):
        """Perform DNS lookup"""
        print(Fore.YELLOW + f"\n[+] DNS lookup for {domain}")
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(Fore.GREEN + f"\n[+] {record} Records:")
                for rdata in answers:
                    print(Fore.WHITE + f"  • {rdata}")
            except:
                pass
    
    def whois_lookup(self, domain):
        """Perform WHOIS lookup"""
        try:
            print(Fore.YELLOW + f"\n[+] WHOIS lookup for {domain}")
            domain_info = whois.whois(domain)
            
            print(Fore.GREEN + "\n" + "═" * 50)
            print(Fore.CYAN + "📋 WHOIS INFORMATION")
            print(Fore.GREEN + "═" * 50)
            
            print(Fore.YELLOW + f"Domain Name: " + Fore.WHITE + f"{domain_info.domain_name}")
            print(Fore.YELLOW + f"Registrar: " + Fore.WHITE + f"{domain_info.registrar}")
            print(Fore.YELLOW + f"Creation Date: " + Fore.WHITE + f"{domain_info.creation_date}")
            print(Fore.YELLOW + f"Expiration Date: " + Fore.WHITE + f"{domain_info.expiration_date}")
            print(Fore.YELLOW + f"Name Servers: " + Fore.WHITE + f"{domain_info.name_servers}")
            
            print(Fore.GREEN + "═" * 50)
            
        except Exception as e:
            print(Fore.RED + f"[-] WHOIS lookup failed: {e}")
    
    def ip_calculator(self, cidr):
        """Calculate IP range from CIDR"""
        try:
            network = ipaddress.ip_network(cidr, strict=False)
            print(Fore.GREEN + "\n" + "═" * 50)
            print(Fore.CYAN + "📊 IP CALCULATOR RESULTS")
            print(Fore.GREEN + "═" * 50)
            
            print(Fore.YELLOW + f"Network: " + Fore.WHITE + f"{network.network_address}")
            print(Fore.YELLOW + f"Broadcast: " + Fore.WHITE + f"{network.broadcast_address}")
            print(Fore.YELLOW + f"Netmask: " + Fore.WHITE + f"{network.netmask}")
            print(Fore.YELLOW + f"Prefix Length: " + Fore.WHITE + f"{network.prefixlen}")
            print(Fore.YELLOW + f"Number of Hosts: " + Fore.WHITE + f"{network.num_addresses - 2}")
            print(Fore.YELLOW + f"First Usable: " + Fore.WHITE + f"{list(network.hosts())[0] if network.num_addresses > 2 else 'N/A'}")
            print(Fore.YELLOW + f"Last Usable: " + Fore.WHITE + f"{list(network.hosts())[-1] if network.num_addresses > 2 else 'N/A'}")
            
            print(Fore.GREEN + "═" * 50)
            
        except Exception as e:
            print(Fore.RED + f"[-] Invalid CIDR: {e}")
    
    def main(self):
        """Main execution"""
        while True:
            self.banner()
            self.show_menu()
            
            choice = input(Fore.YELLOW + "\n👉 Select an option [1-12]: " + Fore.WHITE)
            
            if choice == '1':
                self.get_my_ip()
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '2':
                ip = input(Fore.YELLOW + "Enter IP address: " + Fore.WHITE)
                self.get_ip_info(ip)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '3':
                ip = input(Fore.YELLOW + "Enter IP address: " + Fore.WHITE)
                self.ip_to_domain(ip)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '4':
                domain = input(Fore.YELLOW + "Enter domain name: " + Fore.WHITE)
                self.domain_to_ip(domain)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '5':
                ip = input(Fore.YELLOW + "Enter IP address: " + Fore.WHITE)
                self.get_ip_info(ip)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '6':
                cidr = input(Fore.YELLOW + "Enter CIDR (e.g., 192.168.1.0/24): " + Fore.WHITE)
                self.ip_calculator(cidr)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '7':
                domain = input(Fore.YELLOW + "Enter domain name: " + Fore.WHITE)
                self.dns_lookup(domain)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '8':
                domain = input(Fore.YELLOW + "Enter domain name: " + Fore.WHITE)
                self.whois_lookup(domain)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '9':
                ip = input(Fore.YELLOW + "Enter IP address: " + Fore.WHITE)
                self.get_ip_info(ip)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '10':
                print(Fore.YELLOW + "\n[+] Bulk IP Check (Enter IPs separated by comma)")
                ips = input(Fore.YELLOW + "IPs: " + Fore.WHITE)
                for ip in ips.split(','):
                    self.get_ip_info(ip.strip())
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '11':
                cidr = input(Fore.YELLOW + "Enter CIDR (e.g., 192.168.1.0/24): " + Fore.WHITE)
                self.ip_calculator(cidr)
                input(Fore.CYAN + "\nPress Enter to continue...")
                
            elif choice == '12':
                print(Fore.GREEN + "\n[+] Thanks for using IP Insight Pro!")
                print(Fore.CYAN + "[+] Coded by: MANSOOR BIK KAMALI")
                sys.exit(0)
                
            else:
                print(Fore.RED + "[-] Invalid option!")
                time.sleep(1)

if __name__ == "__main__":
    try:
        tool = IPInsightPro()
        tool.main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Exiting...")
        sys.exit(0)
