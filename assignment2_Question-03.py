# Question 03-Backend Data Processing & User Audit Tool Scenario 

users = [
    (101, "Alice", "admin", True, 1),
    (102, "Bob", "member", True, 4),
    (103, "Charlie", "editor", False, 0),
    (104, "Diana", "admin", False, 6),
    (105, "Evan", "member", True, 2),
    (106, "Fiona", "guest", True, 0),
]


total_active_users = 0
total_inactive_users = 0
total_security_alerts = 0

print("USER AUDIT PROCESSING")
print("========================================")

# Qs.03.a - Active Admin Processing
for user in users:
    user_id = user[0]
    name = user[1]
    role = user[2]
    is_active = user[3]
    login_attempts = user[4]

    # Qs.03.b - Security Audit
    if login_attempts >= 5:
        print(f"[ALERT] Account {name} is LOCKED due to excessive failed logins ({login_attempts} attempts).")
        total_security_alerts = total_security_alerts + 1

   
    if is_active == True and role == "admin":
        print(f"[GRANT] Full system access granted to {name} (ID: {user_id})")
        total_active_users = total_active_users + 1
    elif is_active == True and (role == "member" or role == "editor"):
        print(f"[GRANT] Standard access granted to {name} (ID: {user_id})")
        total_active_users = total_active_users + 1
    elif is_active == False:
        print(f"[DENIED] Account {name} is inactive.")
        total_inactive_users = total_inactive_users + 1
    else:
        if is_active == True:
            total_active_users = total_active_users + 1

# Qs.03.d - Summary Counts: 
print("\nAUDIT SUMMARY REPORT")
print("========================================")
print(f"Total Active Users Granted: {total_active_users}")
print(f"Total Inactive Accounts: {total_inactive_users}")
print(f"Total Security Alerts: {total_security_alerts}")
print("========================================")