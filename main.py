from stats import generate_report
import sys
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    frankenstein_report = generate_report(sys.argv[1])
    print(frankenstein_report)

main()