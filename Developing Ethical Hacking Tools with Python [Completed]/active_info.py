import nmap
import sys

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1], "80", argumant="-o")

print(nm_scanner)
