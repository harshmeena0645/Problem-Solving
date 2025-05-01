num = complex(input("Enter a complex number (e.g., 3+4j): "))

real_part = num.real
imaginary_part = num.imag

if real_part > imaginary_part:
    print(real_part ,' is greater than ',imaginary_part)
elif imaginary_part > real_part:
    print(imaginary_part,' is greater than ',real_part)
else:
    print(real_part , imaginary_part,'are equal')
