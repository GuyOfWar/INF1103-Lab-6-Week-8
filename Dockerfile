FROM python:3.11-slim
WORKDIR /app
COPY inventory_manager.py .
COPY Product.py .
COPY Inventory.py .
CMD [ "python", "inventory_manager.py" ]