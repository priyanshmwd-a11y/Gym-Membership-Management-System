# Gym Membership Management System

## Overview
A command-line Python application for managing gym members, membership plans, payments, renewals, and reports.

## Features
- Add, view, search, update, and remove members
- Automatic member IDs
- Input validation
- Monthly, Quarterly, and Yearly membership plans
- Membership start and expiry dates
- Cash, UPI, and Card payment methods
- Paid/Pending payment status
- Revenue and plan-wise reports
- JSON data storage

## Technologies
Python 3, JSON, Command Line Interface, Git/GitHub

## Run
```bash
python3 main.py
```

## Test
```bash
python3 tests/test_gym.py
```

## Project Structure
`main.py` - main flow  
`members.py` - member management  
`memberships.py` - membership and payment  
`reports.py` - analytics  
`storage.py` - JSON storage  
`validators.py` - validation  
`payments.py` - payment module  
`members.json` - stored data  
`tests/` - tests













## Screenshots

### Main Menu
![Main Menu](screenshots/01-main-menu.png)

### Member Added
![Member Added](screenshots/02-member-added.png)

### Member Details
![Member Details](screenshots/03-member-details.png)

### Membership Assigned
![Membership Assigned](screenshots/04-membership-assigned.png)

### Payment Recorded
![Payment Recorded](screenshots/05-payment-recorded.png)

### Reports & Analytics
![Reports](screenshots/06-reports.png)

### Revenue Summary
![Revenue](screenshots/07-revenue.png)

