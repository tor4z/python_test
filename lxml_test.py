from lxml import etree

if __name__ == "__main__":
    h1 = etree.Element("h1")
    h2 = etree.Element("h2")
    h1.text = "s"
    h2.text = "ss"
    h1.set("class", "h")
    h1.append(h2)

    # print(dir(h1))
    print(etree.tostring(h1, doctype="<!DOCTYPE html>"))
    print(etree.tostring(h1, doctype=None))