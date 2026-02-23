from product_manager import *

def main():
    products = load_data()
    print(f"Đã tải {len(products)} sản phẩm")

    while True:

        print("""
====== QUẢN LÝ KHO SẢN PHẨM ======
1. Thêm sản phẩm
2. cập nhật sản phẩm
3. Xóa sản phẩm
4. Tìm kiếm theo tên
5. Hiển thị tất cả
0. Thoát
""")

        choice = input("Chọn: ")

        if choice == "1":
            products = add_product(products)
        elif choice == "2":
            update_product(products)
        elif choice == "3":
            delete_product(products)
        elif choice == "4":
            search_product_by_name(products)
        elif choice == "5":
            display_all_products(products)
        elif choice == "0":
            save_data(products)
            print("Đã lưu dữ liệu. Thoát.")
            break
        elif choice == "6":
            products = load_data()
            print("Tải lại dữ liệu thành công!")
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
    
