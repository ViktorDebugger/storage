CREATE TABLE [Phone] (
  [id] integer PRIMARY KEY,
  [name] nvarchar(255),
  [price] float,
  [quantity] integer,
  [screen_diagonal] float,
  [battery_capacity] integer,
  [processor_cores] integer,
  [operating_system] nvarchar(255),
  [ram] integer,
  [rom] integer,
  [brand_id] integer
)
GO

CREATE TABLE [Brand] (
  [id] integer PRIMARY KEY,
  [name] nvarchar(255)
)
GO

CREATE TABLE [Order] (
  [id] integer PRIMARY KEY,
  [order_type] nvarchar(255),
  [phone_id] integer,
  [order_datetime] datetime,
  [quantity] integer,
  [total_price] float
)
GO

ALTER TABLE [Phone] ADD FOREIGN KEY ([brand_id]) REFERENCES [Brand] ([id])
GO

ALTER TABLE [Order] ADD FOREIGN KEY ([phone_id]) REFERENCES [Phone] ([id])
GO
