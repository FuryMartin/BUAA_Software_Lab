import math
class compute_RH:
    def __init__(self,d,red_thetas,blue_thetas):
        self.d = d #光栅常数
        self.red_thetas = red_thetas #一二三级红光
        self.blue_thetas = blue_thetas #一二三级蓝光
        print("红光：")
        self.get_RH(self.red_thetas,'red')
        self.red_RHs = self.RHs #一二三级红光的里德伯常量
        self.red_uRHs = self.uRHs #一二三级红光的里德伯常量不确定度
        print("蓝光：")
        self.get_RH(self.blue_thetas,'blue')
        self.blue_RHs = self.RHs #一二三级蓝光的里德伯常量
        self.blue_uRHs = self.uRHs #一二三级蓝光的里德伯常量不确定度
        #组合两种色光的数据
        self.RHs = self.red_RHs + self.blue_RHs #两种色光所得的全部里德伯常量
        self.uRHs = self.red_uRHs + self.blue_uRHs #两种色光所得的全部里德伯常量的不确定度
        #计算加权平均值
        self.get_average()
        #打印相对误差
        self.print_difference()

    def get_RH(self,thetas,color):
        if color == 'red':
            self.n = 3
        elif color == 'blue':
            self.n = 4
        self.ud = 0.001e-6
        self.thetas = thetas
        self.utheta = 1.4078e-4
        self.half_thetas = [theta/2 for theta in thetas]
        self.half_thetas_radius = [theta*math.pi/180 for theta in self.half_thetas]
        self.lambdas = [math.sin(theta)*self.d/count for (count,theta) in enumerate(self.half_thetas_radius,start=1)]
        #print(self.lambdas)
        self.RHs = [1/(1/(math.pow(2,2))-1/(math.pow(self.n,2)))/lam for lam in self.lambdas]
        self.uRHs = [RH*math.sqrt(math.pow(self.ud/self.d,2)+math.pow(self.utheta/math.tan(self.half_thetas_radius[count]),2)) for (count, RH) in enumerate(self.RHs)]
        for lam,RH,uRH in zip(self.lambdas,self.RHs,self.uRHs):
            print("波长：\t{:.3f}nm".format(lam*1e9))
            print("里德伯常量:\t{:.7E}/m".format(RH))
            print("里德伯常量的不确定度\t{:.7E}/m".format(uRH))
            print()
    
    def get_average(self):
        self.square_ave_uRH = 1/(1/math.pow(self.uRHs[0],2)+1/math.pow(self.uRHs[1],2)+1/math.pow(self.uRHs[2],2)+1/math.pow(self.uRHs[3],2)+1/math.pow(self.uRHs[4],2)+1/math.pow(self.uRHs[5],2))
        self.ave_uRH = math.sqrt(self.square_ave_uRH)
        self.ave_RH = (self.RHs[0]/math.pow(self.uRHs[0],2)+self.RHs[1]/math.pow(self.uRHs[1],2)+self.RHs[2]/math.pow(self.uRHs[2],2)+self.RHs[3]/math.pow(self.uRHs[3],2)+self.RHs[4]/math.pow(self.uRHs[4],2)+self.RHs[5]/math.pow(self.uRHs[5],2))*self.square_ave_uRH
        print("加权平均：")
        print("里德伯常量:\t{:.7E}/m".format(self.ave_RH))
        print("里德伯常量的不确定度：\t{:.7E}/m".format(self.ave_uRH))
        print()

    def print_difference(self):
        self.theory = 10967757.8 #百度百科找到的公认实验值
        print("与标准值相对误差：\t{:.2f}%".format(abs((self.ave_RH-self.theory)*100/self.theory)))
        
if __name__ == '__main__':
    #输入光栅常数和两个列表，狭缝单位为μm，列表1为一二三级红光的2θ值，列表2为一二三级蓝光的2θ值，单位为度
    compute_RH(3.334e-6, [22+44/60,46+21/60,72+29/60],[16+47/60,33+55/60,51+54/60]) #示例，表示光栅常数为3.334μm，一二三级红光分别为[22度44分，46度21分，72度29分]，一二三级蓝光分别为[16度47分，33度55分，51度54分]
    