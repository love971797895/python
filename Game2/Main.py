#!/usr/bin/python  
# -*- coding: <utf-8> -*- 
import pygame,os,sys,time

""" python 3.+的版本中，print需要用 () 
	# 获取当前文件__file__的路径
    print "os.path.realpath(__file__)=%s" % os.path.realpath(__file__)
    # 获取当前文件__file__的所在目录
    print "os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)) 　　
    # 获取当前文件__file__的所在目录
    print "os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0]　
"""

try:
	def main():
		screen = pygame.display.set_mode((482,854),0,32)
		osurl = os.path.dirname(os.path.realpath(__file__))

		backurl = osurl + "\\content\\back.png" #背景图片的存放地址
		obackground = pygame.image.load(backurl)

		#人的信息
		mplane = osurl + "\\content\\mplane.png" #要打的飞机的存放地址
		omplane = pygame.image.load(mplane)
		

		#地方飞机的信息
		
		while True:
			screen.blit(obackground,(0,0))
			screen.blit(omplane,(0,0))
			pygame.display.update()
			time.sleep(0.01) #延时执行
except Exception as e:
	print(e)
else:
	pass
finally:
	pass


if __name__ == '__main__':
	main()