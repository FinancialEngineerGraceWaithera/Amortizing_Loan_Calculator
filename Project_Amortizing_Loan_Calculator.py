# Create an amortization schedule with an option for additional monthly payments.
def create_amortization_schedule(principal, annual_rate, years, extra_payment):

    # Convert the annual interest rate to a monthly decimal rate.
    monthly_rate = annual_rate / 100 / 12
    number_of_payments = years * 12

    # Calculate the standard monthly loan payment using the amortization formula.
    payment = principal * (
        monthly_rate * (1 + monthly_rate) ** number_of_payments
    ) / (
        (1 + monthly_rate) ** number_of_payments - 1
    )

    # Initialize the outstanding loan balance.
    balance = principal

    # Create an empty list to store the monthly amortization data.
    schedule = []

    # Display the amortization schedule header.
    print("\nAMORTIZATION SCHEDULE")
    print("---------------------")
    print("Month | Payment | Interest | Principal | Balance")

    # Calculate the loan repayment details for each month.
    for month in range(1, number_of_payments + 1):
        interest = balance * monthly_rate

        # Limit the final payment to the amount actually owed.
        actual_payment = min(payment + extra_payment, balance + interest)

        # Calculate the portion of the payment applied to principal.
        principal_paid = actual_payment - interest

        # Update the outstanding loan balance.
        balance = balance - principal_paid

        # Treat very small remaining balances as fully repaid.
        if balance < 0.01:
            balance = 0

        # Store the monthly repayment details in the schedule.
        schedule.append({
            "month": month,
            "payment": actual_payment,
            "interest": interest,
            "principal": principal_paid,
            "balance": balance
        })

        # Optional detailed monthly output; commented out to keep the terminal concise.
        # print(f"{month:<5} | {actual_payment:>12,.2f} | {interest:>12,.2f} | {principal_paid:>12,.2f} | {balance:>12,.2f}")

        # Stop the schedule once the loan has been fully repaid.
        if balance == 0:
            break

        print(f"{month:<5} | {payment:>12,.2f} | {interest:>12,.2f} | {principal_paid:>12,.2f} | {balance:>12,.2f}")

    return schedule, payment, principal


# Collect the loan amount, interest rate, loan term, and additional monthly payment from the user.
loan_amount = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan term (years): "))
extra_payment = float(input("Enter extra monthly payment: "))

print(f"\nSCENARIO 1 — {annual_rate}% INTEREST")
print("------------------------------")

loan_schedule, payment, principal = create_amortization_schedule(
    loan_amount, annual_rate, years, extra_payment
)


# Display the key loan parameters.
print("\nSCENARIO 1")
print("----------")
print(f"Interest Rate: {annual_rate}%")
print(f"Loan Term: {years} years")

print("\nLOAN SUMMARY")
print("------------")
print(f"Loan Amount: {principal:,.2f}")


# Calculate the total amount paid over the life of the loan.
total_paid = sum(row["payment"] for row in loan_schedule)
print(f"Total Paid: {total_paid:,.2f}")


# Calculate the total interest paid.
scenario_1_total_interest = total_paid - principal
print(f"Total Interest: {scenario_1_total_interest:,.2f}")


# Calculate the total principal repaid.
total_principal = sum(row["principal"] for row in loan_schedule)
print(f"Total Principal Repaid: {total_principal:,.2f}")


# Calculate interest paid as a percentage of the original loan amount.
interest_percentage = (scenario_1_total_interest / principal) * 100
print(f"Interest as % of Loan: {interest_percentage:.2f}%")


# Display the standard monthly payment before any additional payment.
print(f"Monthly Payment: {payment:,.2f}")


# Display the first month's repayment details.
print(loan_schedule[0])


# Display the remaining balance after the first month's payment.
print(loan_schedule[0]["balance"])


# Optional checks used during development to inspect later repayment periods.
# These can be removed from the final version if they are no longer needed.
#
# print(loan_schedule[98]["balance"])
# print(f"{loan_schedule[98]['payment']:,.2f}")


# Perform a second scenario analysis using a different interest rate.
# Scenario 2 uses a 10% annual interest rate.
scenario_2_rate = 10

scenario_2_schedule, scenario_2_payment, scenario_2_principal = create_amortization_schedule(
    loan_amount, scenario_2_rate, years, extra_payment
)

print(f"\nSCENARIO 2 — {scenario_2_rate}% INTEREST")
print(f"Monthly Payment: {scenario_2_payment:,.2f}")


# Calculate the total amount paid under Scenario 2.
scenario_2_total_paid = sum(row["payment"] for row in scenario_2_schedule)


# Calculate the total interest paid under Scenario 2.
scenario_2_total_interest = scenario_2_total_paid - scenario_2_principal

print(f"Total Paid: {scenario_2_total_paid:,.2f}")
print(f"Total Interest: {scenario_2_total_interest:,.2f}")


# Compare the total interest paid under both scenarios.
print("Scenario 1 interest:", scenario_1_total_interest)
print("Scenario 2 interest:", scenario_2_total_interest)



