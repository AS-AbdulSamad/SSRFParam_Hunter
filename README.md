# SSRFParam_Hunter

SSRFParam_Hunter is a command-line tool designed to aid penetration testers in quickly identifying potential security risks by searching for SSRF-related parameters within a list of URLs. It assists in uncovering URLs that may be vulnerable to SSRF attacks, enabling penetration testers to perform thorough security assessments and identify potential attack vectors.

## Features:

- **Efficient Parameter Matching:** Utilizes regular expressions for fast and accurate matching of SSRF-related parameters within URLs.
- **Grouped Results:** Organizes matched URLs by parameter, providing a clear overview of potential vulnerabilities.
- **Customizable Parameters:** Allows users to easily define and customize the list of parameters to match specific use cases or environments.
- **Simple Integration:** Run as a standalone Python script, making it easy to integrate into existing workflows or automation pipelines.

## Usage:

1. Create a text file containing a list of URLs.
2. Run the SSRFParam_Hunter.py script with the path to the URL file as an argument. Example: `python3 SSRFParam_Hunter.py urls.txt`
3. View the matched URLs grouped by parameter.

## Sample

![image](https://github.com/AS-AbdulSamad/SSRFParam_Hunter/assets/116205223/8fdb2883-4901-4eaf-b885-e6da197f0e85)


## Disclaimer:
SSRFParam_Hunter is a tool developed by ABStronics for informational and educational purposes only. While SSRFParam_Hunter aims to assist users in identifying potential security risks, it is ultimately the responsibility of the user to ensure the security of their systems and networks. ABStronics does not guarantee the accuracy, completeness, or effectiveness of SSRFParam_Hunter in detecting vulnerabilities or mitigating security threats. By using SSRFParam_Hunter, you agree that ABStronics shall not be liable for any damages or losses arising from the use or misuse of this tool.
