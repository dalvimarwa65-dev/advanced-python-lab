def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print("=" * 60)
        func(*args, **kwargs)
        print("=" * 60)
        print("END OF REPORT".center(60))
        print("=" * 60)
    return wrapper


class Report:
    company_name = "ABC Technologies Pvt. Ltd."

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

    def add_content(self, text):
        self.contents.append(text)

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    @staticmethod
    def line():
        print("-" * 60)

    def __str__(self):
        return f"Report Title : {self.title}\nAuthor : {self.author}"

    def __len__(self):
        return len(self.contents)

    @report_decorator
    def display_report(self):
        print("Company :", Report.company_name)
        print(self)
        Report.line()
        print("Report Contents:")
        for i, item in enumerate(self.contents, start=1):
            print(f"{i}. {item}")
        Report.line()
        print("Total Sections :", len(self))


def create_user_report(default_title):
    print(f"\nCreating: {default_title}")
    author = input("Enter Author Name: ")
    rep = Report(default_title, author)
    
    n = int(input("How many lines of content do you want to add? "))
    for i in range(n):
        text = input(f"Enter line {i+1}: ")
        rep.add_content(text)
        
    rep.display_report()


if __name__ == "__main__":
    while True:
        print("\n--- REPORT GENERATOR MENU ---")
        print("1. Practical Report")
        print("2. Performance Report")
        print("3. Result Report")
        print("4. Change Company Name")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_user_report("Practical Report")
        elif choice == '2':
            create_user_report("Performance Report")
        elif choice == '3':
            create_user_report("Result Report")
        elif choice == '4':
            new_comp = input("Enter new company name: ")
            Report.change_company(new_comp)
            print("Company name updated successfully.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please select between 1 and 5.")