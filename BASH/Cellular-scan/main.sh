#!/bin/bash

# Scan for cellular networks
cellular-scanner

# Extract the GSM network information from the scan results
gsm_networks=$(cellular-scanner | grep "^GSM")

# Print the GSM network information
echo "Detected GSM networks:"
echo "$gsm_networks"
