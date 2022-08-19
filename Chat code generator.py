import codecs

def menu():
    print (60 * "-")
    print ("1. Coin")
    print ("2. Item")
    print ("3. NPC String")
    print ("4. Map Link")
    print ("5. PvP Game")
    print ("6. Skill Link")
    print ("7. Trait Link")
    print ("8. User")
    print ("9. Recipe Link")
    print ("10. Wardrobe Link")
    print ("11. Outfit Link")
    print ("12. WvW Objective Link")
    print ("13. Exit")
    print (60 * "-")
  
    loop=True      
    while loop:          # To keep the loop going as long as necessary.
        
        choice = int(input("Enter your choice [1-13]: "))
        
        if choice>=1 and choice<=12:
            print(f"Menu {choice} has been selected.")
            LinkHeader = format(choice, '02x') # Menu choice is converted into hexadecimal.
            return LinkHeader
        elif choice==13:
            exit()
        else:
            print("Wrong option, try again:")

def IntegerConversion(ObjectID):
    ItemHex = format(ObjectID, '02x')
    if len(ItemHex)%2 == 1:
        ItemHex = "0" + ItemHex # Adds a 0 to display value as a full byte.
    ItemHex = LittleEndian(ItemHex)
    return ItemHex

def LittleEndian(ItemHex): # Converts the hexadecimal into a 3-byte little-endian integer.
    HexLength = len(ItemHex)
    if HexLength == 2:
        ItemHex = ItemHex + "0000"
    elif HexLength == 4:
        HexLen1 = ItemHex[0:2]
        HexLen2 = ItemHex[2:4]
        ItemHex = HexLen2 + HexLen1 + "00"
    elif HexLength == 6:
        HexLen1 = ItemHex[0:2]
        HexLen2 = ItemHex[2:4]
        HexLen3 = ItemHex[4:6]
        ItemHex = HexLen3 + HexLen2 + HexLen1
    return ItemHex

def HexCombine(LinkHeader, ItemHex, LinkFooter):
    if LinkHeader == "02":
        ItemQty = int(input("How much of the item: ")) # Adds a byte for the item quantity.
        ItemQty = format(ItemQty, '02x')
        FullHex = LinkHeader + ItemQty + ItemHex + LinkFooter
    else:
        FullHex = LinkHeader + ItemHex + LinkFooter
    return FullHex

def HexConversion(FullHex):
    ObjectB64 = codecs.encode(codecs.decode(FullHex, 'hex'), 'base64').decode() # First the hexadecimal is decoded into bytes format, then encoded into Base64. After, it's decoded into str format.
    return ObjectB64

def main():
    LinkHeader = menu()
    LinkFooter = "00"
    ObjectID = int(input("Item ID: "))
    ItemHex = IntegerConversion(ObjectID)
    FullHex = HexCombine(LinkHeader, ItemHex, LinkFooter)
    ObjectB64 = (HexConversion(FullHex)).strip()
    ChatCode = (f"[&{ObjectB64}]")
    print(ChatCode)
    NewCode = input("""
Press the enter key to generate another code.
Any other input closes the program:
""")
    if NewCode == "":
        main()
    else:
        exit()

main()
