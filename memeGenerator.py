from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import os
import time
import textwrap

def getTopText() :
	topText = input("Enter the top text (maximum 60 characters) : ")
	if len(topText) > 60 :
		print("The top text length is "+str(len(topText))+". Enter new top text again.")
		return None
	else :
		return topText
def getBottomText() :
	bottomText = input("Enter the bottom text (maximum 60 characters) : ")
	if len(bottomText) > 60 :
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

			topParagraph = textwrap.wrap(topText, width=25)

			bottomText = getBottomText()
			while (bottomText == None) :
				bottomText = getBottomText()
			bottomText = bottomText.upper()

			bottomParagraph = textwrap.wrap(bottomText, width=25)

			saveToFolder = os.path.dirname(os.path.realpath(__file__))
			filename = str(round(time.time()))+"-"+os.path.basename(sys.argv[1])

			# resize image
			wpercent = (minimumWidth / float(width) )
			hsize = int( float(height) * float(wpercent) )
			img = img.resize((minimumWidth, hsize), Image.ANTIALIAS)

			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype("/Library/Fonts/Impact.ttf", 40)

			# top text
			topY = 0
			for topLine in topParagraph :
				textWidthTop, texHeightTop = draw.textsize(topLine, font=font)
				centerXTop = (minimumWidth - textWidthTop) / 2

				# black stroke for top text
				draw.text((centerXTop - 2, topY - 2), topLine, (0, 0, 0), font=font)
				draw.text((centerXTop + 2, topY - 2), topLine, (0, 0, 0), font=font)
				draw.text((centerXTop - 2, topY + 2), topLine, (0, 0, 0), font=font)
				draw.text((centerXTop + 2, topY + 2), topLine, (0, 0, 0), font=font)

				# white top text
				draw.text((centerXTop, topY), topLine, (255, 255, 255), font=font)
				topY += 40

			if len(bottomText) >= 50 :
				bottomY = hsize - 10 - 120 # 3 line text
			elif len(bottomText) >= 25 and len(bottomText) < 50  :
				bottomY = hsize - 10 - 80 # 2 line text
			else :
				bottomY = hsize - 10 - 40 # 1 line text

			# bottom text
			for bottomLine in bottomParagraph :
				textWidthBottom, texHeightBottom = draw.textsize(bottomLine, font=font)
				centerXBottom = (minimumWidth - textWidthBottom) / 2

				# black stroke for bottom text
				draw.text((centerXBottom - 2, bottomY - 2), bottomLine, (0, 0, 0), font=font)
				draw.text((centerXBottom + 2, bottomY - 2), bottomLine, (0, 0, 0), font=font)
				draw.text((centerXBottom - 2, bottomY + 2), bottomLine, (0, 0, 0), font=font)
				draw.text((centerXBottom + 2, bottomY + 2), bottomLine, (0, 0, 0), font=font)

				# white bottom text
				draw.text((centerXBottom, bottomY), bottomLine, (255, 255, 255), font=font)
				bottomY += 40

			img.save(filename)
			print("Success - the meme file was saved to "+saveToFolder+"/"+filename)
		else :
			print("The image is too small - minimum size 600x600")
	except OSError as e:
		print(e)
else :
	print("Error - enter image path")
