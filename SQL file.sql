#creatingdatabase:
CREATE DATABASE supplychainIQ;

#creatingtables:
CREATE TABLE Products (
    ProductID VARCHAR(10) PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);

CREATE TABLE Warehouses (
    WarehouseID VARCHAR(10) PRIMARY KEY,
    Location VARCHAR(100)
);

CREATE TABLE Suppliers (
    SupplierID VARCHAR(10) PRIMARY KEY,
    SupplierName VARCHAR(255)
);

CREATE TABLE Inventory (
    ProductID VARCHAR(10),
    WarehouseID VARCHAR(10),
    Stock INT NULL,

    FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID),

    FOREIGN KEY (WarehouseID)
        REFERENCES Warehouses(WarehouseID)
);

CREATE TABLE Orders (
    OrderID VARCHAR(20),
    ProductID VARCHAR(10),
    Quantity INT,
    OrderDate DATE,

    FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID)
);

CREATE TABLE Deliveries (
    DeliveryID VARCHAR(20),
    SupplierID VARCHAR(10),
    ExpectedDate DATE,
    DeliveryDate DATE,

    FOREIGN KEY (SupplierID)
        REFERENCES Suppliers(SupplierID)
);

#Datavalidation:
SELECT COUNT(*) FROM Products;
SELECT COUNT(*) FROM Warehouses;
SELECT COUNT(*) FROM Suppliers;
SELECT COUNT(*) FROM Inventory;
SELECT COUNT(*) FROM Orders;
SELECT COUNT(*) FROM Deliveries;

#dataqualityanalysis:
#missingvalue:
SELECT *
FROM Inventory
WHERE Stock=0;

#countofthemissingvalues:
SELECT COUNT(*) AS Missing_Stock
FROM Inventory
WHERE Stock=0;

#dupilicates:
SELECT OrderID,
       COUNT(*) AS Duplicate_Count
FROM Orders
GROUP BY OrderID
HAVING COUNT(*) > 1;

#Businessanalysisqueries:
#1.Which_products_are_out_of_stock?:
SELECT
    p.ProductName,
    w.Location,
    i.Stock
FROM Inventory i
JOIN Products p
ON i.ProductID = p.ProductID
JOIN Warehouses w
ON i.WarehouseID = w.WarehouseID
WHERE i.Stock = 0;

#2.Which_products_have_low_stock?:
SELECT
    p.ProductName,
    w.Location,
    i.Stock
FROM Inventory i
JOIN Products p
ON i.ProductID = p.ProductID
JOIN Warehouses w
ON i.WarehouseID = w.WarehouseID
WHERE i.Stock BETWEEN 1 AND 50
ORDER BY i.Stock;

#3.top_selling_products:
SELECT
    p.ProductName,
    SUM(o.Quantity) AS Total_Sold
FROM Orders o
JOIN Products p
ON o.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY Total_Sold DESC;

#4.warehouse_inventory_levels:
SELECT
    w.Location,
    SUM(i.Stock) AS Total_Stock
FROM Inventory i
JOIN Warehouses w
ON i.WarehouseID = w.WarehouseID
GROUP BY w.Location
ORDER BY Total_Stock;

#5.supplier_delay_analysis:
SELECT
    SupplierID,
    AVG(DeliveryDate - ExpectedDate) AS Avg_Delay_Days
FROM Deliveries
GROUP BY SupplierID
ORDER BY Avg_Delay_Days DESC;

#6.Stockouts_Affectin_ High-Demand_Products?:
SELECT
    p.ProductName,
    SUM(o.Quantity) AS Total_Sold,
    COUNT(CASE WHEN i.Stock = 0 THEN 1 END) AS Stockout_Count
FROM Products p
JOIN Orders o
    ON p.ProductID = o.ProductID
JOIN Inventory i
    ON p.ProductID = i.ProductID
GROUP BY p.ProductName
ORDER BY Total_Sold DESC;

#7.Which_Product_Category_Has_the_Highest_Demand?:
SELECT
    p.Category,
    SUM(o.Quantity) AS Total_Sales
FROM Orders o
JOIN Products p
ON o.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Sales DESC;

#8.Which_Warehouse_Has_the_Most_Stockouts?:
SELECT
    w.Location,
    COUNT(*) AS Stockout_Count
FROM Inventory i
JOIN Warehouses w
ON i.WarehouseID = w.WarehouseID
WHERE i.Stock = 0
GROUP BY w.Location
ORDER BY Stockout_Count DESC;

#9.Which_Suppliers_Deliver_On_Time_Most_Frequently?:
SELECT
    SupplierID,
    COUNT(*) AS On_Time_Deliveries
FROM Deliveries
WHERE DeliveryDate <= ExpectedDate
GROUP BY SupplierID
ORDER BY On_Time_Deliveries DESC;

#10.Average_Inventory_by_Product_Category:
SELECT
    p.Category,
    AVG(i.Stock) AS Avg_Inventory
FROM Inventory i
JOIN Products p
ON i.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Avg_Inventory DESC;