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
	def __init__(self,x,y,img,screen):
		super(Plane, self).__init__()
		self.x = x
		self.y = y
		self.img = pygame.image.load(img)
		self.screen = screen 
		self.bulletlist = [] #存储的是子弹列表

	def Display(self):
		self.screen.blit(self.img,(self.x,self.y))
		for blt in self.bulletlist:  #循环加载子弹，每一个子弹对应一个单独的列表
			blt.Display()
			blt.Move()
			if(blt.Judge()): #judge()判断子弹是否越界（销毁对象）
				self.bulletlist.remove(blt) #删除当前的子弹
	def Fire(self):
		pass


class EnemyPlane(Plane):
	"""docstring for EnemyPlane"""
	def __init__(self,e_screen):
		super().__init__(0,0,osurl + "\\content\\smallplane.png",e_screen)
		self.direction = 0

	def MoveWhile(self): #敌机跑起来
		if(self.direction == 0):
			self.x += 1;
		elif(self.direction == 1):
			self.x -= 1;
		if(self.x == 350):
			self.direction = 1
		elif(self.x == 0):
			self.direction = 0

	def Fire(self):
		rdm = random.randint(1,200)
		if rdm == 78 or rdm == 178: #按照0.01秒（主程序刷新频率值）的循环频率，如果出78，则发射一个子弹，即加载一个图片
			self.bulletlist.append(EBullet(self.screen,self.x,self.y))
		

class HeroPlane(Plane):
	"""docstring for HeroPlane"""
	def __init__(self,h_screen):
		super().__init__(190,550,osurl + "\\content\\mplane.png",h_screen)

	def Moveleft(self):
		self.x -= 5

	def Moveright(self):
		self.x += 5

	def Moverup(self):
		self.y -= 5

	def Movedowm(self):
		self.y += 5

	def Fire(self):
		self.bulletlist.append(HBullet(self.screen,self.x,self.y))


class Bullet(object):
	"""docstring for Bullet"""
	def __init__(self,screen,x,y,img):
		super().__init__()
		self.x = x
		self.y = y
		self.img = pygame.image.load(img)
		self.screen = screen

	def Display(self):
		self.screen.blit(self.img,(self.x,self.y))

	def Move(self):
		pass

	def Judge(self):
		if(self.y < 0):
			return True
		else:
			return False

class HBullet(Bullet):
	"""docstring for Bullet"""
	def __init__(self,b_screen,x,y): #飞机所在位置的X，Y  相对偏差
		super().__init__(b_screen,x+19,y-8,osurl + "\\content\\bullet.png")

	def Move(self):
		self.y -= 3 #每次子弹去跟着上次变化Y轴


class EBullet(Bullet):
	"""docstring for Bullet"""
	def __init__(self,e_screen,x,y): #飞机所在位置的X，Y  相对偏差
		super().__init__(e_screen,x+18,y+50,osurl + "\\content\\liudan.png")

	def Move(self):
		self.y += 1 #每次子弹去跟着上次变化Y轴

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
						hero.Fire()


	def main():
		screen = pygame.display.set_mode((401,600),0,32)
		osurl = os.path.dirname(os.path.realpath(__file__))

		backurl = osurl + "\\content\\back.png" #背景图片的存放地址
		obackground = pygame.image.load(backurl)

		hero = HeroPlane(screen) #构造英雄对象
		enemy = EnemyPlane(screen) #构造敌人飞机


		while True: #一直执行
			screen.blit(obackground,(0,0))
			hero.Display()
			enemy.Display() #敌机显示
			enemy.MoveWhile() #敌机移动
			enemy.Fire() #敌机开火
			pygame.display.update() #刷新页面
			keycontrol(hero) #监听页面事件

			time.sleep(0.01) #延时执行

except Exception as e:
	print(e)
finally:
	pass

if __name__ == '__main__':
	main()