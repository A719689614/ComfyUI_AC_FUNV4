from .AC_FUN import AC_FUN
from .AC_FUNV4 import ac_pil2tensor,tensor2pil
from  PIL import Image
import cv2

class AC_Trans(AC_FUN):
    math = ["vertical","horizontal"]
    boolean = ["flip","rotate","scale","None"]
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                "image":("IMAGE",),
                "boolean":(s.boolean,),
                "math":(s.math,),
                "rotate":("INT",{"min":-360, "max":360, "step":1,"default":0}),
                "scale_percent":("INT",{"min":0, "max":100, "step":1,"default":1})
                }
                }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "ac_trans"

    def ac_trans(self, image, math="vertical",boolean="None",rotate=0,scale_percent=0):
        pil = tensor2pil(image)
        image = pil
        if boolean == "flip":
            if math == "vertical":
                vertical_image = image.transpose(Image.FLIP_TOP_BOTTOM)
                return (ac_pil2tensor(vertical_image),)
            if math == "horizontal":
                horizontal_image = image.transpose(Image.FLIP_LEFT_RIGHT)
                return (ac_pil2tensor(horizontal_image),)
        
        if boolean == "None":
            return (image,)
        
        if boolean == "rotate":
            rotated_image = image.rotate(rotate)
            return (ac_pil2tensor(rotated_image),)
        
        if boolean == "scale":
            scale_percent = 50 
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            return (ac_pil2tensor(resized_image),)
        
