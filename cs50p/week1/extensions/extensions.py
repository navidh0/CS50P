suffix = input("File name: ").lower().strip()

if '.jpg' in suffix :
        print("image/jpeg")
elif '.jpeg' in suffix :
        print("image/jpeg")
elif '.gif' in suffix:
        print("image/gif")
elif ".png" in suffix:
        print("image/png")
elif '.pdf' in suffix:
        print("application/pdf")
elif '.txt' in suffix:
        print("text/plain")
elif '.zip' in suffix:
        print("application/zip")
else:
        print("application/octet-stream")
