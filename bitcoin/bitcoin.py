import requests
import json
import sys

#"1fb918e2505f1f834259103c3a3a656db21dbb11e10adc915b9688739a0d360a"
#print(json.dumps(data, indent=4, sort_keys=True))

def main():

    try:  
        if len(sys.argv) == 1:
            print("Missing command-line argument")
            sys.exit(1)
        sys.argv[1] = float(sys.argv[1])
        amount = sys.argv[1]
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=1fb918e2505f1f834259103c3a3a656db21dbb11e10adc915b9688739a0d360a")
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
    except requests.RequestException:
        sys.exit(1)

    single_bitcoin_cost = float(data["data"]["priceUsd"])
    cost = amount * single_bitcoin_cost
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()