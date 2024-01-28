from utils import database as db
from utils import constant

def get_products(limit=None, offset=0, include_out_of_stock=False):
    """
    Retrieve a list of products based on provided filters.

    Args:
        limit (int, optional): Maximum number of products to retrieve.
        offset (int, optional): Number of products to skip from the beginning.
        include_out_of_stock (bool, optional): Include out-of-stock products in the result.

    Returns:
        dict: A dictionary containing 'data' (list of products) and 'page' information.
    """
    # Set filters based on parameters
    filters = {}
    if not include_out_of_stock:
        filters['ProductQuantity'] = {"$gt": 0}

    # Get total records count with applied filters
    total_records = db.get_total_records(constant.PRODUCT_TABLE, filters)

    # Fetch products with pagination support
    products = db.fetch(table=constant.PRODUCT_TABLE, filters=filters, limit=limit, skip=offset)

    # Process fetched products data
    data = []
    for document in products:
        document["ProductId"] = str(document.pop("_id"))
        data.append(document)
    print(f"\n\n data: {data}")

    # Set default values for offset and limit if not provided
    offset = offset or 0
    limit = limit or total_records

    # Prepare pagination information
    page = {
        "limit": limit,
        "nextOffSet": offset + limit if offset + limit < total_records else None,
        "prevOffSet": offset - limit if offset - limit >= 0 else None,
        "total": total_records
    }

    # Return result as a dictionary
    return {
        "data": data,
        "page": page,
    }

def place_order(**kwargs):
    """
    Place a new order and return the order ID.

    Args:
        **kwargs: Order details including user address.

    Returns:
        str: The ID of the newly placed order.
    """
    # Extract user address information and insert into the USER_ADDRESS_TABLE
    user_address = kwargs.pop("userAddress")
    address_id = str(db.insert(constant.USER_ADDRESS_TABLE, [user_address])[0])

    # Update order details with the inserted address ID
    kwargs['address_id'] = address_id

    # Insert order details into the ORDER_TABLE and retrieve the order ID
    order_id = str(db.insert(constant.ORDER_TABLE, [kwargs])[0])

    # Return the order ID
    return order_id
