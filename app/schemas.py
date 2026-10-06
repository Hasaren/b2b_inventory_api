from datetime import datetime, date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=50)
    name: str = Field(min_length=1, max_length=200)
    unit_price: Decimal = Field(gt=0)
    reorder_point: int = Field(default=10, ge=0)
    initial_stock: int = Field(default=0, ge=0)


class ProductRead(ORMModel):
    id: int
    sku: str
    name: str
    unit_price: Decimal
    reorder_point: int
    stock_quantity: int


class CustomerCreate(BaseModel):
    company_name: str = Field(min_length=1, max_length=200)
    business_number: str = Field(min_length=1, max_length=20)
    contact_name: str | None = None
    contact_email: str | None = None


class CustomerRead(ORMModel):
    id: int
    company_name: str
    business_number: str
    contact_name: str | None
    contact_email: str | None


class StockAdjustment(BaseModel):
    amount: int


class InventoryRead(BaseModel):
    product_id: int
    sku: str
    name: str
    quantity: int
    reorder_point: int
    needs_reorder: bool


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    customer_id: int
    items: list[OrderItemCreate] = Field(min_length=1)


class OrderItemRead(ORMModel):
    product_id: int
    quantity: int
    unit_price: Decimal


class OrderRead(ORMModel):
    id: int
    customer_id: int
    status: str
    ordered_at: datetime
    items: list[OrderItemRead]
    total_amount: Decimal


class DashboardSummary(BaseModel):
    product_count: int
    customer_count: int
    order_count: int
    total_sales: Decimal
    low_stock_count: int

class OrderImportResult(BaseModel):
    total_rows: int
    orders_created: int
    products_created: int
    customers_created: int

class WeeklyPoint(BaseModel):
    week_start: date
    quantity: float

class ProductForecast(BaseModel):
    product_id: int
    sku: str
    name: str
    model: str
    backtest_wape: float | None
    active_week_ratio: float
    history: list[WeeklyPoint]
    forecast: list[WeeklyPoint]

class ExcludedProduct(BaseModel):
    product_id: int
    sku: str
    name: str
    active_week_ratio: float
    reason: str

class ForecastOverview(BaseModel):
    weeks: int
    min_active_week_ratio: float
    forecasts: list[ProductForecast]
    excluded: list[ExcludedProduct]