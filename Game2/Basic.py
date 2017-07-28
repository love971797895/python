#!/usr/bin/python  
# -*- coding: <utf-8> -*- 
import pygame,os,sys,time
import random
from pygame.locals import *

""" python 3.+的版本中，print需要用 () 
	# 获取当前文件__file__的路径
    print "os.path.realpath(__file__)=%s" % os.path.realpath(__file__)
    # 获取当前文件__file__的所在目录
    print "os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)) 　　
    # 获取当前文件__file__的所在目录
    print "os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0]　
"""

"""
屏幕初始化 400,600
"""


#当前的文件夹位置 
osurl = os.path.dirname(os.path.realpath(__file__))


class Plane(object):
	"""docstring for Plane"""
	def __init__(self):
		super(Plane, self).__init__()


class EnemyPlane(Plane):
	"""docstring for EnemyPlane"""
	def __init__(self,e_screen):
		super(HeroPlane).__init__()
		self.x = 0
		self.y = 0
		self.img = pygame.image.load(osurl + "\\content\\smallplane.png")
		self.e_screen = e_screen 
		self.bulletlist = [] #存储的是子弹列表
		self.direction = 0

	def EDisplay(self):#加载敌机图片
		self.e_screen.blit(self.img,(self.x,self.y))
		for blt in self.bulletlist:  #循环加载子弹，每一个子弹对应一个单独的列表
			blt.EBDisplay()
			blt.EBMove()
			# if(blt.HBjudge()): #judge()判断子弹是否越界（销毁对象）
			# 	self.bulletlist.remove(blt) #删除当前的子弹

	def MoveWhile(self): #敌机跑起来
		if(self.direction == 0):
			self.x += 1;
		elif(self.direction == 1):
			self.x -= 1;
		if(self.x == 350):
			self.direction = 1
		elif(self.x == 0):
			self.direction = 0

	def EFire(self):
		rdm = random.randint(1,200)
		if rdm == 78 or rdm == 178: #按照0.01秒（主程序刷新频率值）的循环频率，如果出78，则发射一个子弹，即加载一个图片
			self.bulletlist.append(EBullet(self.e_screen,self.x,self.y))
		

class HeroPlane(Plane):
	"""docstring for HeroPlane"""
	def __init__(self,h_screen):
		super(HeroPlane).__init__()
		self.x = 190
		self.y = 550
		self.img = pygame.image.load(osurl + "\\content\\mplane.png")
		self.h_screen = h_screen 
		self.bulletlist = [] #存储的是子弹列表

	def HDisplay(self):
		self.h_screen.blit(self.img,(self.x,self.y))
		for blt in self.bulletlist:  #循环加载子弹，每一个子弹对应一个单独的列表
			blt.HBDisplay()
			blt.HBMove()
			if(blt.HBjudge()): #judge()判断子弹是否越界（销毁对象）
				self.bulletlist.remove(blt) #删除当前的子弹

	def Moveleft(self):
		self.x -= 5

	def Moveright(self):
		self.x += 5

	def Moverup(self):
		self.y -= 5

	def Movedowm(self):
		self.y += 5

	def HFire(self):
		self.bulletlist.append(HBullet(self.h_screen,self.x,self.y))




class Bullet(object):
			"""docstring for Bullet"""
			def __init__(self):
				super(Bullet).__init__()

class HBullet(Bullet):
	"""docstring for Bullet"""
	def __init__(self,b_screen,x,y): #飞机所在位置的X，Y  相对偏差
		self.x = x + 19
		self.y = y - 8
		self.img = pygame.image.load(osurl + "\\content\\bullet.png")
		self.b_screen = b_screen

	def HBDisplay(self): #加载这个对象
		self.b_screen.blit(self.img,(self.x,self.y))

	def HBMove(self):
		self.y -= 3 #每次子弹去跟着上次变化Y轴

	def HBjudge(self): #删除当前的子弹(移除图片)
		if(self.y < 0):
			return True
		else:
			return False

class EBullet(Bullet):
	"""docstring for Bullet"""
	def __init__(self,e_screen,x,y): #飞机所在位置的X，Y  相对偏差
		self.x = x + 18
		self.y = y + 50
		self.img = pygame.image.load(osurl + "\\content\\liudan.png")
		self.e_screen = e_screen

	def EBDisplay(self): #加载这个对象
		self.e_screen.blit(self.img,(self.x,self.y))

	def EBMove(self):
		self.y += 1 #每次子弹去跟着上次变化Y轴

	def EBjudge(self): #删除当前的子弹(移除图片)
		if(self.y < 0):
			return True
		else:
			return False



try:
	def keycontrol(hero):
		for event in pygame.event.get():
				if event.type == QUIT:
					exit()  #关闭按钮
				elif event.type == KEYDOWN:
					if event.key == K_a or event.key == K_LEFT:
						hero.Moveleft()
					elif event.key == K_d or event.key == K_RIGHT:
						hero.Moveright()
					elif event.key == K_w or event.key == K_UP:
						hero.Moverup()
					elif event.key == K_s or event.key == K_DOWN:
						hero.Movedowm()
					elif event.key == K_SPACE:
						hero.HFire()


	def main():
		screen = pygame.display.set_mode((401,600),0,32)
		osurl = os.path.dirname(os.path.realpath(__file__))

		backurl = osurl + "\\content\\back.png" #背景图片的存放地址
		obackground = pygame.image.load(backurl)

		hero = HeroPlane(screen) #构造英雄对象
		enemy = EnemyPlane(screen) #构造敌人飞机


		while True: #一直执行
			screen.blit(obackground,(0,0))
			hero.HDisplay()
			enemy.EDisplay() #敌机显示
			enemy.MoveWhile() #敌机移动
			enemy.EFire() #敌机开火
			pygame.display.update() #刷新页面
			keycontrol(hero) #监听页面事件

			time.sleep(0.01) #延时执行

except Exception as e:
	print(e)
finally:
	pass


if __name__ == '__main__':
	main()