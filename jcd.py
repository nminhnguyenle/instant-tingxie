import easyocr



def easyocr_test():
    excl = ''':;<=>?()@[\]^_`{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´'"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
    excls = []
    for x in excl:
        excls.append(x)
    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext('./img_dir/precorrect.jpg', detail=0)
    for x in result:
        print(x.translate({ord(i): None for i in excl}))

if __name__ == "__main__":
    easyocr_test()