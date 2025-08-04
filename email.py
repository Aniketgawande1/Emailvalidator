import re 
import argparse

EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email: str) -> bool:
    """Check if the provided email is valid"""
    return re.match(EMAIL_PATTERN, email) is not None

def main():
    parser = argparse.ArgumentParser(description="CLI-BASED Email Validator")

    # Optional --interactive flag
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in Interactive mode"
    )

    # Positional optional email argument
    parser.add_argument(
        "email",
        nargs="?",
        help="Email address to validate"
    )

    args = parser.parse_args()

    if args.interactive:
        while True:
            email = input("Enter an email to validate (or type 'exit' to quit): ")
            if email.lower() == 'exit':
                print("Goodbye!")
                break
            result = is_valid_email(email)
            print("✅ Valid" if result else "❌ Invalid")

    elif args.email:
        result = is_valid_email(args.email)
        print(f"✅ {args.email} is valid" if result else f"❌ {args.email} is invalid")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
