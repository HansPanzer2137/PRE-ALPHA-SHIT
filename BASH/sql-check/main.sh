#!/bin/bash

# Set the target database name
database="mydatabase"

# Test for SQL injection vulnerabilities
echo "Testing for SQL injection vulnerabilities..."
injection_test=$(curl --silent --data "test=1' OR '1'='1" "http://localhost/$database/vulnerabilities")
if [[ $injection_test =~ "SQL syntax" ]]; then
  echo "SQL injection vulnerability found!"
else
  echo "No SQL injection vulnerabilities detected."
fi

# Test for cross-site scripting vulnerabilities
echo "Testing for cross-site scripting vulnerabilities..."
xss_test=$(curl --silent --data "test=<script>alert('XSS')</script>" "http://localhost/$database/vulnerabilities")
if [[ $xss_test =~ "<script>alert" ]]; then
  echo "Cross-site scripting vulnerability found!"
else
  echo "No cross-site scripting vulnerabilities detected."
fi
