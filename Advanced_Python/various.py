from string import Template
def main():
    """
    b=bytes([0x41,0x42,0x43,0x44])
    print(b)
    s="This a string"
    print(s)
    s2=b.decode("utf-8")
    print(s+s2)
    b2=s.encode("utf-8")
    print(b+b2)
    #utf-32
    b3=s.encode('utf-32')
    print(b3)
"""
    templ=Template('You are watching ${title} by ${author}')
    str2=templ.substitute(title="Matsamplokos",author="Fousekis")
    print(str2)
main()
