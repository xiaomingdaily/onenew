import whois
hosts = "days.com"
# ��20190719��������������Ƿ��ע��.
def checkIfReg(host):
    try:
        whois.whois(rawhosts)
        return True
    except:
        return False

for iii in range(100,999):
    rawhosts = str(iii)+hosts
    if not checkIfReg(rawhosts):
        print(rawhosts + " can be Register ... ")
