my_dict = {
    "hrthrh": {
        "email": "angela@gmail.com",
        "password": "%&*E0Mnm4Hjgn6l#1"
    },
    "hrhrhrjyyrejwr": {
        "email": "angela@gmail.com",
        "password": "3vp!0o$0F%5Nx+ho"
    },
    "jytrejje": {
        "email": "angela@gmail.com",
        "password": "))djP48Yburt*"
    },
    "yejejetjetj": {
        "email": "angela@gmail.com",
        "password": "qALV1A(V1b2(B0#ab&"
    },
    "etyjytejet": {
        "email": "angela@gmail.com",
        "password": "83mBB+%oFm$mLo$"
    },
    "nmnmemem": {
        "email": "angela@gmail.com",
        "password": "Xn+FHX$*rp81P"
    },
    "Amazon": {
        "email": "angela@gmail.com",
        "password": "Xn+FHX$*rp81P"
    }
}

print(my_dict["Amazon"]["password"])

input_website = input("Enter the website name: ")

if input_website in my_dict:
    password = my_dict[input_website]["password"]
    print("Password is: " , password )
else:
    print("Not found!")