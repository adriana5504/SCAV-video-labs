class ColorTranslator:
    def rgb_to_yuv(r,g,b):
        y = 0.257*r + 0.504*g + 0.098*b + 16
        u = -0.148*r - 0.291*g + 0.439*b + 128
        v = 0.439*r - 0.368*g - 0.071*b + 128
        return (y,u,v)
    
    def yuv_to_rgb(y,u,v):
        r = 1.164*(y-16) + 1.596*(v-128)
        g = 1.164*(y-16) - 0.813*(v-128) - 0.391*(u-128)
        b = 1.164*(y-16) + 2.018*(u-128)
        return (r,g,b)
    
#Roundtrip differs on a few decimals because of the rounding errors in the conversion formulas. 
print(ColorTranslator.rgb_to_yuv(255,0,0))
print(ColorTranslator.yuv_to_rgb(81.535, 90.26, 239.945))



