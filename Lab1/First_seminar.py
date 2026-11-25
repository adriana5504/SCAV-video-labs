class ColorTranslator:
    # Following the T2 (slide 40) YCbCr formula from RGB
    def rgb_to_yuv(self, r, g, b):  # BT.601 Limited range
        y = 0.257*r + 0.504*g + 0.098*b + 16
        u = -0.148*r - 0.291*g + 0.439*b + 128
        v = 0.439*r - 0.368*g - 0.071*b + 128
        return (y, u, v)
    
    def yuv_to_rgb(self, y, u, v):
        r = 1.164*(y - 16) + 1.596*(v - 128)
        g = 1.164*(y - 16) - 0.813*(v - 128) - 0.391*(u - 128)
        b = 1.164*(y - 16) + 2.018*(u - 128)
        return (r, g, b)

r, g, b = 255, 0, 0

y, u, v = ColorTranslator().rgb_to_yuv(r, g, b)

r_new, g_new, b_new = ColorTranslator().yuv_to_rgb(y, u, v)

#Roundtrip differs on a few decimals because of the rounding errors in the conversion formulas. 
print(r, g, b)
print(y, u, v)
print(r_new, g_new, b_new)


#For exercice 3) The chroma lie we have used the following commands for exporting the images:
#ffmpeg -i ferminazo.jpg -pix_fmt yuv444p ferminazo_444.yuv (this for yuv444p)

#For blurring the image (only the chroma) we have used the following command:
