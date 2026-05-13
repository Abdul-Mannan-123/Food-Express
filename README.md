![foodexpress-banner](https://dummyimage.com/1200x280/d62828/ffffff&text=FoodExpress+Online+Food+Ordering+System)

![Language Badge](https://img.shields.io/badge/Backend-Python%20Flask-3776AB?style=for-the-badge&logo=python)
![Database Badge](https://img.shields.io/badge/Database-MySQL-4479A1?style=for-the-badge&logo=mysql)
![Frontend Badge](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20Bootstrap-7952B3?style=for-the-badge&logo=bootstrap)
![DBMS Badge](https://img.shields.io/badge/Database-3NF%20Normalized-success?style=for-the-badge)
![Project Badge](https://img.shields.io/badge/Project-DBS%20Project-orange?style=for-the-badge)

# FoodExpress — Online Food Ordering System

**DBS Project** | FAST NUCES Karachi  
**Group Members:** Bazil Uddin Khan (24K-0559), Daanial Tejani (24K-0671), Abdul Mannan (23K-0829)

---

## DESCRIPTION:

FoodExpress is a full-stack online food ordering system built using Flask and MySQL.

The project includes customer ordering functionality, admin management, real-time order tracking, restaurant menus, cart management, payment handling, and a fully normalized relational database design.

The system demonstrates practical implementation of Database Systems concepts including normalization, foreign keys, triggers, views, joins, aggregation queries, and transaction-based order processing.

---

## FEATURES:

### Customer Features
- Secure registration & login
- Password hashing
- Browse restaurants and menus
- Search food items
- Add/remove cart items
- Quantity management
- Checkout system
- Cash on Delivery & Online payment
- Real-time order tracking
- Order history

---

### Admin Panel
- Dashboard with analytics
- Manage all customer orders
- Update order status
- Customer management
- Restaurant management
- Enable/disable menu items
- Revenue overview

---

### Database Features
- 9 normalized tables
- 1NF, 2NF, 3NF compliant
- Foreign keys with CASCADE rules
- Triggers for auto calculations
- SQL Views for reporting
- Advanced JOIN & aggregate queries

---

## TECH STACK:

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Backend | Python 3 + Flask |
| Database | MySQL |
| Fonts | DM Sans, Playfair Display |
| Icons | Bootstrap Icons |

---

## QUICK START:

### Install Dependencies

```bash
pip install flask werkzeug
```

---

### Run the Application

```bash
cd food_ordering
python app.py
```

Application runs at:

```text
http://localhost:5000
```

---

## DEMO CREDENTIALS:

| Role | Email / Username | Password |
|---|---|---|
| Customer | bazil@example.com | pass123 |
| Customer | daanial@example.com | pass123 |
| Customer | manan@example.com | pass123 |
| Admin | admin | admin123 |

---

## MYSQL SETUP (OPTIONAL):

Create database:

```bash
mysql -u root -p < sql/schema.sql
```

Update `app.py` with your SQLAlchemy connection string if using MySQL persistence.

---

## INCLUDED IN `schema.sql`:

- CREATE TABLE statements
- Foreign key constraints
- Triggers
- SQL Views
- Sample data
- Advanced SQL queries
- Revenue reports
- Popular item analysis

---

## PROJECT STRUCTURE:

```text
food_ordering/
│
├── app.py
├── sql/
│   └── schema.sql
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── menu.html
│   ├── login.html
│   ├── register.html
│   ├── cart.html
│   ├── checkout.html
│   ├── my_orders.html
│   ├── track_order.html
│   ├── search_results.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── admin_orders.html
│   ├── admin_customers.html
│   ├── admin_restaurants.html
│   └── admin_menu.html
│
└── README.md
```

---

## DATABASE SCHEMA (9 TABLES):

| Table | Description |
|---|---|
| categories | Food categories |
| restaurants | Restaurant information |
| customers | Customer accounts |
| admins | Admin accounts |
| menu_items | Restaurant food items |
| orders | Customer orders |
| order_details | Order item details |
| payments | Payment records |
| reviews | Restaurant reviews |

---

## ADVANCED SQL FEATURES:

### Triggers
- Auto-update order totals
- Auto-update restaurant ratings

### Views
- Customer order summaries
- Restaurant revenue reports
- Popular food items

### Queries
- Revenue per restaurant
- Top ordered items
- High spending customers
- Average order value
- Monthly order statistics

---

## DATABASE CONCEPTS USED:

| Concept | Usage |
|---|---|
| Normalization | 1NF, 2NF, 3NF |
| Foreign Keys | Relational integrity |
| CASCADE Rules | Automatic dependency handling |
| Triggers | Auto calculations |
| Views | Reporting & analytics |
| JOINs | Multi-table queries |
| Aggregation | Revenue & statistics |

---

## SYSTEM MODULES:

```text
Customer Module
│
├── Authentication
├── Restaurant Browsing
├── Cart System
├── Order Placement
└── Order Tracking

Admin Module
│
├── Dashboard
├── Order Management
├── Customer Management
└── Restaurant Management
```

---

## FUTURE IMPROVEMENTS:
- Payment gateway integration
- Email notifications
- Delivery tracking with maps
- Recommendation system
- Mobile application
- JWT authentication
- REST API version
- Docker deployment

---

## LEARNING OUTCOMES:

This project demonstrates practical understanding of:

- Database Systems
- Relational schema design
- SQL queries & optimization
- Flask web development
- Authentication systems
- CRUD operations
- Full-stack architecture
- Real-world DBMS workflows

---

<div align="center">

Built using Flask, MySQL, and Bootstrap.

FAST NUCES Karachi — DBS Project

</div>
