from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Product import Product
from Supplier import Supplier

supplier = Supplier("S001", "Yamaha", "sales@yamaha.com")


print("===== PHYSICAL PRODUCTS =====")
guitar =  PhysicalProduct ("G001", "Guitar", 50, 10,supplier, 5)
guitar.display_information()
print(guitar.get_fulfilment_info())
print() #use to make space 

drum = PhysicalProduct ("G002", "Drum", 100, 10, supplier, 10)
drum.display_information()
print(drum.get_fulfilment_info())


print("\n===== DIGITAL PRODUCTS =====")
Mac_OS = DigitalProduct ("D001", "Mac OS", 100, 100, supplier, 4500)
Mac_OS.display_information()
print(Mac_OS.get_fulfilment_info())

print("\n===== ABSTRACT CLASS TEST =====")
try:
    product = Product("P001", "Abstract Product", 0, 0, supplier)
    print("Product class instantiated successfully.")
except TypeError as e:
    print("Error:", e)

print("\n===== SUPPLIER INFORMATION =====")
guitar.get_supplier().display_information()
Mac_OS.get_supplier().display_information()
del supplier
print("\n--- after del supplier")
guitar.get_supplier().display_information()
Mac_OS.get_supplier().display_information()