from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import os
import time

def getTopText() :
	topText = input("Enter the top text (maximum 32 characters) : ")
	if len(topText) > 32 :
		print("The top text length is "+str(len(topText))+". Enter new top text again.")
		return None
	else :
		return topText
def getBottomText() :
	bottomText = input("Enter the bottom text (maximum 32 characters) : ")
	if len(bottomText) > 32 :
		print("The bottom text length is "+str(len(bottomText))+". Enter new bottom text again.")
		return None
	else :
		return bottomText

minimumWidth = 500

if len(sys.argv) > 1 :
	try :
		img = Image.open(sys.argv[1])

		width = img.size[0]
		height = img.size[1]

		if(width >= minimumWidth and height >= minimumWidth) :
			topText = getTopText()
			while (topText == None) :
				topText = getTopText()
			topText = topText.upper()

			bottomText = getBottomText()
			while (bottomText == None) :
				bottomText = getBottomText()
			bottomText = bottomText.upper()

			saveToFolder = os.path.dirname(os.path.realpath(__file__))
			filename = str(round(time.time()))+"-"+os.path.basename(sys.argv[1])

			# resize image
			wpercent = (minimumWidth / float(width) )
			hsize = int( float(height) * float(wpercent) )
			img = img.resize((minimumWidth, hsize), Image.ANTIALIAS)

			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype("/Library/Fonts/Impact.ttf", 40)
			textWidthTop, texHeightTop = draw.textsize(topText, font=font)
			centerXTop = (minimumWidth - textWidthTop) / 2

			# black stroke for top text
			draw.text((centerXTop - 2, -2), topText, (0, 0, 0), font=font)
			draw.text((centerXTop + 2, -2), topText, (0, 0, 0), font=font)
			draw.text((centerXTop - 2, 2), topText, (0, 0, 0), font=font)
			draw.text((centerXTop + 2, 2), topText, (0, 0, 0), font=font)

			# white top text
			draw.text((centerXTop, 0), topText, (255, 255, 255), font=font)

			bottomY = hsize - 10 - 40
			textWidthBottom, texHeightBottom = draw.textsize(bottomText, font=font)
			centerXBottom = (minimumWidth - textWidthBottom) / 2

			# black stroke for bottom text
			draw.text((centerXBottom - 2, bottomY - 2), bottomText, (0, 0, 0), font=font)
			draw.text((centerXBottom + 2, bottomY- 2), bottomText, (0, 0, 0), font=font)
			draw.text((centerXBottom - 2, bottomY + 2), bottomText, (0, 0, 0), font=font)
			draw.text((centerXBottom + 2, bottomY + 2), bottomText, (0, 0, 0), font=font)

			# white bottom text
			draw.text((centerXBottom, bottomY), bottomText, (255, 255, 255), font=font)

			img.save(filename)
			print("Success - the meme file was saved to "+saveToFolder+"/"+filename)
		else :
			print("The image is too small - minimum size 600x600")
	except OSError as e:
		print(e)
else :
	print("Error - enter image path")
