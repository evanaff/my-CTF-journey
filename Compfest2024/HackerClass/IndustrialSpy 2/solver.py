from scapy.all import *

dictionary = {
    "0x0" : "_",
    "0x1" : "ErrorRollOver1",
    "0x2" : "POSTFail",
    "0x3" : "ErrorUndefined1",
    "0x4" : "a",
    "0x5" : "b",
    "0x6" : "c",
    "0x7" : "d",
    "0x8" : "e",
    "0x9" : "f",
    "0xa" : "g",
    "0xb" : "h",
    "0xc" : "i",
    "0xd" : "j",
    "0xe" : "k",
    "0xf" : "l",
    "0x10" : "m",
    "0x11" : "n",
    "0x12" : "o",
    "0x13" : "p",
    "0x14" : "q",
    "0x15" : "r",
    "0x16" : "s",
    "0x17" : "t",
    "0x18" : "u",
    "0x19" : "v",
    "0x1a" : "w",
    "0x1b" : "x",
    "0x1c" : "y",
    "0x1d" : "z",
    "0x1e" : "1",
    "0x1f" : "2",
    "0x20" : "3",
    "0x21" : "4",
    "0x22" : "5",
    "0x23" : "6",
    "0x24" : "7",
    "0x25" : "8",
    "0x26" : "9",
    "0x27" : "0",
    "0x28" : " [Return] ",
    "0x29" : "ESCAPE",
    "0x2a" : "DELETE",
    "0x2b" : "  ",
    "0x2c" : " ",
    "0x2D" : "-",
    "0x2e" : "=",
    "0x2f" : "[",
    "0x30" : "]",
    "0x31" : "\\",
    "0x32" : "Non-US",
    "0x33" : ";",
    "0x34" : "‘",
    "0x35" : "Grave",
    "0x36" : ",",
    "0x37" : ".",
    "0x38" : "/"
}

dictionary2 = {
    "0x0" : "",
    "0x1" : "ErrorRollOver1",
    "0x2" : "POSTFail",
    "0x3" : "ErrorUndefined1",
    "0x4" : "A",
    "0x5" : "B",
    "0x6" : "C",
    "0x7" : "D",
    "0x8" : "E",
    "0x9" : "F",
    "0xa" : "G",
    "0xb" : "H",
    "0xc" : "I",
    "0xd" : "J",
    "0xe" : "K",
    "0xf" : "L",
    "0x10" : "M",
    "0x11" : "N",
    "0x12" : "O",
    "0x13" : "P",
    "0x14" : "Q",
    "0x15" : "R",
    "0x16" : "S",
    "0x17" : "T",
    "0x18" : "U",
    "0x19" : "v",
    "0x1a" : "2",
    "0x1b" : "X",
    "0x1c" : "Y",
    "0x1d" : "Z",
    "0x1e" : "!",
    "0x1f" : "@",
    "0x20" : "#",
    "0x21" : "$",
    "0x22" : "%",
    "0x23" : "∧",
    "0x24" : "&",
    "0x25" : "*",
    "0x26" : "(",
    "0x27" : ")",
    "0x28" : "Return",
    "0x29" : "ESCaPE",
    "0x2a" : "DELETE",
    "0x2b" : "Tab",
    "0x2c" : "Spacebar",
    "0x2d" : "_",
    "0x2e" : "+",
    "0x2f" : "{",
    "0x30" : "}",
    "0x31" : "\\",
    "0x32" : "^5",
    "0x33" : ":",
    "0x34" : "“",
    "0x35" : "",
    "0x36" : "<",
    "0x37" : ">",
    "0x38" : "?"
}

packets = rdpcap("traffic.pcapng")

typing = ""

for i in range (6, 649, 4):
    if hex(packets[i].load[-8]) == '0x2':
        typing += dictionary2[f"{hex(packets[i+2].load[-6])}"]
    else:
        typing += dictionary[f"{hex(packets[i].load[-6])}"]

print(typing)