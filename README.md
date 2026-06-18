# SupplyChainIQ - Inventory & Supply Chain Analytics Platform

## Project Overview

SupplyChainIQ is an end-to-end Supply Chain and Inventory Analytics project developed using PostgreSQL, Python, and Power BI. The project focuses on inventory monitoring, warehouse management, supplier performance analysis, and business intelligence reporting.

The goal of this project is to help organizations make data-driven decisions by identifying stock shortages, monitoring inventory levels, analyzing supplier reliability, and tracking product demand trends.

---

## Business Problem

Supply chain operations generate large volumes of data across products, warehouses, suppliers, inventory, and deliveries. Without proper analytics, organizations may face:

* Frequent stockouts
* Overstocking issues
* Delayed supplier deliveries
* Poor inventory visibility
* Inefficient warehouse management

This project addresses these challenges through data analysis and interactive dashboards.

---

## Technology Stack

### Database

* PostgreSQL

### Data Analysis

* Python
* Pandas
* Matplotlib

### Business Intelligence

* Power BI
* DAX

### Version Control

* Git
* GitHub

---

## Database Schema

### Products

* ProductID
* ProductName
* Category

### Warehouses

* WarehouseID
* Location

### Suppliers

* SupplierID
* SupplierName

### Inventory

* ProductID
* WarehouseID
* Stock

### Orders

* OrderID
* ProductID
* Quantity
* OrderDate

### Deliveries

* DeliveryID
* SupplierID
* ExpectedDate
* DeliveryDate

---

## SQL Analysis Performed

* Out-of-Stock Product Analysis
* Low Stock Product Detection
* Top Selling Products
* Category-wise Demand Analysis
* Warehouse Inventory Analysis
* Supplier Reliability Analysis
* Supplier Delay Analysis
* Stockout Risk Identification
* Inventory Aggregation Reports

---

## Python Analysis

Exploratory Data Analysis (EDA) was performed to identify:

* Stockout trends
* Inventory distribution
* Supplier delivery delays
* Business performance patterns

Libraries Used:

* Pandas
* Matplotlib

---

## Power BI Dashboard

### Page 1: Executive Summary

#### KPI Cards

* Total Orders
* Total Products
* Total Inventory
* Total Suppliers
* Stockout Count

#### Visualizations

* Top 10 Selling Products
* Sales by Category
* Inventory by Warehouse
* Interactive Date Slicer

---

### Page 2: Inventory & Supplier Performance

#### Visualizations

* Out-of-Stock Products
* Low Stock Products
* Supplier Delay Analysis
* On-Time vs Delayed Deliveries
* Interactive Filters and Slicers

---

## Key Business Insights

* Identified products at risk of stockout
* Monitored inventory distribution across warehouses
* Evaluated supplier delivery performance
* Analyzed sales demand by category
* Improved visibility into supply chain operations

---

## Project Structure

SupplyChainIQ-Inventory-Supply-Chain-Analytics-Platform/

├── Dataset/

├── SQL Queries/

├── Python EDA/

├── Power BI Dashboard/

├── Dashboard Screenshots/

└── README.md

---

## Future Enhancements

* Demand Forecasting using Machine Learning
* Inventory Optimization Models
* Real-Time Dashboard Integration
* Automated Supplier Performance Monitoring
* Predictive Stockout Alerts

---

## Author

Ranjani

Aspiring Data Analyst | SQL | Python | Power BI | Data Visualization

LinkedIn: Add your LinkedIn profile link here

GitHub: https://github.com/ranjanida2004

---

⭐ If you found this project useful, feel free to star the repository.
