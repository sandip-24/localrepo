def manager():

    def manage_customer():
        print("Choose your option:")
        print("1. Add customer")
        print("2. Edit customer details")
        print("3. Delete customer data")
        add_customer()

    manage_customer()

    def add_customer():
        name = str(input("Enter name:"))
        return name