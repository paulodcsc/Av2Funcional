check_account = True

have_withdrawal_permission = (lambda: True) if check_account else (lambda: False)

can_withdraw = [have_withdrawal_permission() for _ in range(1)]

if can_withdraw[0]:
    withdrawal_amount = 100 
    update_account_balance = (lambda balance, amount: balance - amount)

    account_balance = 1000  
    account_balance = update_account_balance(account_balance, withdrawal_amount)
    print("Withdrawal amount: ${}".format(withdrawal_amount))
    print("Updated account balance: ${}".format(account_balance))
else:
    print("Withdrawal not allowed")

can_deposit = [True if check_account else False for _ in range(1)]

if can_deposit[0]:
    deposit_amount = 200 
    update_account_balance = (lambda balance, amount: balance + amount)

    account_balance = update_account_balance(account_balance, deposit_amount)
    print("Deposit amount: ${}".format(deposit_amount))
    print("Updated account balance: ${}".format(account_balance))

print("End")
