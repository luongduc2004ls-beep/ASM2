import json

FILE_NAME = "products.json"

def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)

            # Kiểm tra dữ liệu có phải list không
            if isinstance(data, list):
                return data
            else:
                print("Dữ liệu trong file không hợp lệ, khởi tạo danh sách rỗng.")
                return []

    except FileNotFoundError:
        print("Chưa có file dữ liệu, khởi tạo kho trống.")
        return []

def save_data(products):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def add_product(products):
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    quantity = int(input("Nhập số lượng tồn kho: "))

    new_id = f"SP{len(products) + 1:02d}"

    product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    products.append(product)
    print("Đã thêm sản phẩm!")
    return products

def update_product(products):
    pid = input("Nhập mã sản phẩm cần cập nhật: ")

    for product in products:
        if product["id"] == pid:
            product["name"] = input("Tên mới: ")
            product["brand"] = input("Thương hiệu mới: ")
            product["price"] = int(input("Giá mới: "))
            product["quantity"] = int(input("Số lượng mới: "))
            print("Đã cập nhật thành công!")
            return

    print("Không tìm thấy sản phẩm.")

def delete_product(products):
    pid = input("Nhập mã sản phẩm cần xóa: ")

    for product in products:
        if product["id"] == pid:
            products.remove(product)
            print("Đã xóa!")
            return

    print("Không tìm thấy sản phẩm.")

def search_product_by_name(products):
    if not products:
        print("Kho hàng trống!")
        return

    keyword = input("Nhập tên sản phẩm cần tìm: ").lower()
    found = False

    print("-" * 70)
    print(f"{'Mã':<6} {'Tên':<30} {'Hãng':<10} {'Giá':<10} {'SL':<5}")
    print("-" * 70)

    for p in products:
        if keyword in p.get("name", "").lower():
            print(
                f"{p.get('id', 'N/A'):<6} "
                f"{p.get('name', 'N/A'):<30} "
                f"{p.get('brand', 'N/A'):<10} "
                f"{p.get('price', 0):<10} "
                f"{p.get('quantity', 0):<5}"
            )
            found = True

    if not found:
        print("Không tìm thấy sản phẩm phù hợp.")
    else:
        print("-" * 70)

def display_all_products(products):
    if products is None or len(products) == 0:
        print("Kho hàng trống.")
        return

    print("-" * 70)
    print(f"{'Mã':<6} {'Tên':<30} {'Hãng':<10} {'Giá':<10} {'SL':<5}")
    print("-" * 70)

    for p in products:
        print(f"{p['id']:<6} {p['name']:<30} {p['brand']:<10} {p['price']:<10} {p['quantity']:<5}")

    print("-" * 70)
