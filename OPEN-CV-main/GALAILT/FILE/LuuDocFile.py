#Cach ghi de chac chan co close()

# f=open("csdl.txt","w",encoding="UTF-8")
# try:
#     for i in range(10):
#         f.write(f"hahaha {i}\n")
# finally:
#     f.close()
with open("csdl.txt","r",encoding="UTF-8") as f:
    # for i in range(10):
    #     f.write(f"hahaha{i}\n")
    #Doc file
    # print(f.read())
    #Doc x ki tu dau
    # print(f.read(2))
    #Doc 1 dong
    # print(f.readline())
    #Doc dong tai vi tri x
    print(f.readline()[2])


#Doc tat ca cac dong f.readlines()