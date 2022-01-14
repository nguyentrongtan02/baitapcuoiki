def isThuanNghich(n):
    str1 = str(n);     # ep kieu so n thanh chuoi
    str3 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str3):
        return True;
    else:
        return False;
        #nguyentrongtan
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
