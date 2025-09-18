import json


def write_member_list():
    members = []
    print("\n=== Member Registration ===")
    while True:
        print("\nPlease enter the following information:")
        name = input("  - Name (or type 'finish' to finish): ").strip()
        if name.lower() == "finish":
            break
        company = input("  - Company: ").strip()
        email = input("  - Email: ").strip()
        if email not in [m["email"] for m in members]:
            members.append({"name": name, "company": company, "email": email})
            print(f"  > Registered: {name} ({email}) from {company}")
        else:
            print(
                "  ! This email is already registered. Please enter a different email."
            )

    with open("members.json", "w") as f:
        json.dump(members, f, indent=4)
    print("\n✔ Member list saved to members.json\n")


def analyze_member_list():
    try:
        with open("members.json", "r") as f:
            members = json.load(f)
            print("\n=== Conference Member Analysis ===\n")
            print(
                f"Number of delegates expected to attend the conference: \033[1m{len(members)}\033[0m\n"
            )
            companies = {}
            for member in members:
                company = member["company"]
                if company in companies:
                    companies[company] += 1
                else:
                    companies[company] = 1
            companies = dict(
                sorted(companies.items(), key=lambda item: item[1], reverse=True)
            )
            print("List of companies and the number of delegates registered from each:")
            print("----------------------------------------------")
            print(f"{'Company':<30} | {'Number of Delegates':>18}")
            print("----------------------------------------------")
            for company, count in companies.items():
                print(f"{company:<30} | {count:>18}")
            print("----------------------------------------------\n")
    except FileNotFoundError:
        print("\n! No member list found. Please write a member list first.\n")
    except json.JSONDecodeError:
        print(
            "\n! Error reading the member list. Please ensure the file is correctly formatted.\n"
        )


if __name__ == "__main__":
    while True:
        print("\n==============================")
        print("  Conference - Delegate Manager")
        print("==============================")
        print("1. Register delegate list")
        print("2. Analyze delegate list")
        print("3. Exit")
        choice = input("\nSelect an option (1-3): ").strip()

        if choice == "1":
            write_member_list()
        elif choice == "2":
            analyze_member_list()
        elif choice == "3":
            print("\nThank you for using the program. Goodbye!\n")
            break
        else:
            print("\n! Invalid choice. Please try again.\n")
