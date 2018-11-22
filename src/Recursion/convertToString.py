def convertToString(index, base):
    conver_tString = "0123456789ABCDEF"
    if index < base:
        return conver_tString[index]
    else:
        return convertToString(index//base, base) + conver_tString[index % base]
