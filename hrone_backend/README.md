# HROne Backend Task – FastAPI + MongoDB

This is a backend API developed using FastAPI and MongoDB for the HROne Backend Intern Hiring Challenge. It provides basic product and order management features like creation, listing, filtering, and pagination.

---

## Project Structure

hrone_backend/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── config.py # Loads environment variables from .env
│ ├── db.py # Connects to MongoDB using Motor
│ ├── models/
│ │ ├── product_model.py # Pydantic model for Product
│ │ └── order_model.py # Pydantic model for Order
│ ├── routes/
│ │ ├── product_routes.py # Product APIs
│ │ └── order_routes.py # Order APIs
├── .env # MongoDB connection string (ignored in Git)
├── .gitignore # Files/folders to exclude from Git
├── requirements.txt # Python dependencies
├── README.md # Project documentation



---

## Technologies Used

- FastAPI
- Python 3.10+
- MongoDB Atlas
- Motor (Async MongoDB driver)
- Uvicorn (ASGI server)
- Pydantic

---

## Features

- Add new products
- List products with optional filters (name, size)
- Pagination for products and orders
- Create orders for users
- Fetch all orders for a specific user

---

## API Endpoints

### POST `/products`
Create a product.

#### Sample Request Body:
```json
{
  "name": "Samsung Galaxy M32",
  "price": 12999.99,
  "size": "medium",
  "description": "A powerful phone with AMOLED display"
}


GET /products
List products.

Query Parameters:
name (optional): filter by name

size (optional): filter by size

limit (optional): pagination

offset (optional): pagination

POST /orders
Create an order.

Sample Request Body:

{
  "user_id": "user123",
  "products": ["<product_id_1>", "<product_id_2>"]
}


GET /orders/{user_id}
Get orders for a specific user.

Query Parameters:
limit (optional)

offset (optional)


How to Run Locally

1. Clone the repository

git clone https://github.com/your-username/hrone-backend-task.git
cd hrone-backend-task

2. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate   # For Windows

3. Install dependencies

pip install -r requirements.txt

4. Add .env file
Create a .env file in the root directory:

MONGO_URL=your_mongodb_connection_string

5. Start the server

uvicorn app.main:app --reload

Visit:
http://127.0.0.1:8000/docs