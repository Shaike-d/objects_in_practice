import classes_for_main_mini_project.class_Inventory as i
import classes_for_main_mini_project.class_Product as p


def main():
    shop = i.Inventory()
    shop.add(p.Product("Pen", 5, 10))
    shop.add(p.Product("Bag", 60, 2))
    shop.add(p.Product("Notebook", 12, 5))
    shop.find("Pen").sell(4)
    shop.find("Bag").add_stock(1)

    try:
        shop.find("Notebook").sell(50)
    except ValueError as error:
        print("error:", error)
    try:
        shop.add(p.Product("Pen", 7))
    except ValueError as error:
        print("error:", error)
    try:
        shop.find("Bag").price = -3
    except ValueError as error:
        print("error:", error)
    for product in shop.by_value():
        print(product)
    print("Total:", shop.total_value)





if __name__=="__main__":
    main()