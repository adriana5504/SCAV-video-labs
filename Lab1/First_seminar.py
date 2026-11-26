# Exercise 2: RGB <-> YUV

class ColorTranslator:

    # Following the T2 (slide 40) YCbCr formula from RGB -> BT.601 (Limited range)
    def rgb_to_yuv_limited(self, r, g, b):

        r, g, b = int(r), int(g), int(b)    # Perque quan faig sa ex2_prova.py de sa imatge me surt malament (sa imatge surt rosa envers de blava)

        y = 0.257*r + 0.504*g + 0.098*b + 16
        u = -0.148*r - 0.291*g + 0.439*b + 128
        v = 0.439*r - 0.368*g - 0.071*b + 128

        y = round(max(0, min(255, y)))
        u = round(max(0, min(255, u)))
        v = round(max(0, min(255, v)))

        return (y, u, v)
    
    def yuv_to_rgb_limited(self, y, u, v):

        y, u, v = int(y), int(u), int(v)        # Perque quan faig sa ex2_prova.py de sa imatge me surt malament (sa imatge surt rosa envers de blava)

        r = 1.164*(y - 16) + 1.596*(v - 128)
        g = 1.164*(y - 16) - 0.813*(v - 128) - 0.391*(u - 128)
        b = 1.164*(y - 16) + 2.018*(u - 128)

        r = round(max(0, min(255, r)))
        g = round(max(0, min(255, g)))
        b = round(max(0, min(255, b)))

        return (r, g, b)
    
    # From https://en.wikipedia.org/wiki/YCbCr?utm_source=chatgpt.com#JPEG_conversion at the JPEG section -> BT.601 (Full-range)
    def rgb_to_yuv_full(self, r, g, b):
        y = 0.299*r + 0.587*g + 0.114*b
        u = -0.168736*r - 0.331264*g + 0.5*b + 128
        v = 0.5*r - 0.418688*g - 0.081312*b + 128

        y = round(max(0, min(255, y)))
        u = round(max(0, min(255, u)))
        v = round(max(0, min(255, v)))

        return (y, u, v)

    def yuv_to_rgb_full(self, y, u, v):
        r = y + 1.402*(v - 128)
        g = y - 0.344136*(u - 128) - 0.714136*(v - 128)
        b = y + 1.772*(u - 128)

        r = round(max(0, min(255, r)))
        g = round(max(0, min(255, g)))
        b = round(max(0, min(255, b)))

        return (r, g, b)

r, g, b = 0, 0, 255

# Limited experiments
y_limited, u_limited, v_limited = ColorTranslator().rgb_to_yuv_limited(r, g, b)
y_full, u_full, v_full = ColorTranslator().rgb_to_yuv_full(r, g, b)

r_new_limited, g_new_limited, b_new_limited = ColorTranslator().yuv_to_rgb_limited(y_limited, u_limited, v_limited)
r_new_full, g_new_full, b_new_full = ColorTranslator().yuv_to_rgb_full(y_full, u_full, v_full)

# Since the results we get differ by some decimals, we have to round the values to the nearest integer for comparison taking into account that the values must be in [0, 255]
print("EXERCISE 2:")
print("\n")
print("Limited range:")
print(r, g, b)
print(y_limited, u_limited, v_limited)
print(r_new_limited, g_new_limited, b_new_limited)
print("\n")
print("Full range:")
print(r, g, b)
print(y_full, u_full, v_full)
print(r_new_full, g_new_full, b_new_full)
print("\n")


# Exercise 3: The Chroma Lie
# We have used the following commands for exporting the images:
#ffmpeg -i ferminazo.jpg -pix_fmt yuv444p ferminazo_444.yuv (this for yuv444p)

#For blurring the image (only the chroma) we have used the following command:a
