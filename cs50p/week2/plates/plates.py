def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 :
        return False
    elif not s.isalnum():
        return False
    elif not (s[0].isalpha() and s[1].isalpha()):
        return False
    first_num = len(s)-1
    for char in s:
        if char.isnumeric():
            if char == '0':
                return False
            first_num = s.index(char)
            break
    for char in s:
        if s.index(char)<= first_num:
            pass
        else:
            if char.isalpha():
                return False

    return True
main()










# همه ی پلاک ها باید حداقل با دو حرف شروع شود
# حداکثر 6 کاراکتر (حروف یا اعداد) و حداقل 2 کاراکتر داشته باشد
# اعداد را نمی توان در وسط یک بشقاب استفاده کرد. آنها باید در پایان بیایند. به عنوان مثال، AAA222
# یک… بشقاب روشویی قابل قبول است. AAA22A قابل قبول نخواهد بود. اولین عدد استفاده شده نمی تواند "0" باشد."
# هیچ نقطه، فاصله یا علامت نقطه گذاری مجاز نیست.
