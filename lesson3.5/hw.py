def connection(*_, ip, port):
    def printer(func):
        def inner(doc):
            print(f"Connected to IP: {ip}:{port}")
            func(doc)
            print(f"Close connection...")
        return inner
    return printer

@connection(ip="10.10.10.10", port="5555")
def hp(document):
    print(f"I am HP printer")
    print(f"Printing: {document}")

@connection(ip="20.20.20.20", port="7777")
def canon(document):
    print(f"I am Canon printer")
    print(f"Printing: {document}")
    
hp("document_1.doc")
canon("document_2.doc")
