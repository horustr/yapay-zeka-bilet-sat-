# -*- coding: utf-8 -*-
"""


@author: irem
"""

# -- coding: utf-8 --
"""


@author: irem
"""

# -- coding: utf-8 --
"""


@author: irem
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl



# Meslek durumu 
meslek = ctrl.Antecedent(np.arange(0, 2, 1), 'meslek')
meslek['hayir'] = fuzz.trimf(meslek.universe, [0, 0, 1])
meslek['evet'] = fuzz.trimf(meslek.universe, [0, 1, 1])

# Ekipman durumu
ekipman = ctrl.Antecedent(np.arange(0, 2, 1), 'ekipman')
ekipman['hayir'] = fuzz.trimf(ekipman.universe, [0, 0, 1])
ekipman['evet'] = fuzz.trimf(ekipman.universe, [0, 1, 1])

# Organizasyon durumu
organizasyon = ctrl.Antecedent(np.arange(0, 2, 1), 'organizasyon')
organizasyon['hayir'] = fuzz.trimf(organizasyon.universe, [0, 0, 1])
organizasyon['evet'] = fuzz.trimf(organizasyon.universe, [0, 1, 1])

# İlk yardım eğitimi durumu
ilk_yardim = ctrl.Antecedent(np.arange(0, 2, 1), 'ilk_yardim')
ilk_yardim['hayir'] = fuzz.trimf(ilk_yardim.universe, [0, 0, 1])
ilk_yardim['evet'] = fuzz.trimf(ilk_yardim.universe, [0, 1, 1])

# Arama kurtarma tecrübesi
deneyim = ctrl.Antecedent(np.arange(0, 2, 1), 'deneyim')
deneyim['hayir'] = fuzz.trimf(deneyim.universe, [0, 0, 1])
deneyim['evet'] = fuzz.trimf(deneyim.universe, [0, 1, 1])

# Puan hesaplama 
skor = ctrl.Consequent(np.arange(0, 101, 1), 'skor')         



skor['low1'] = fuzz.trimf(skor.universe, [0, 0,1])
skor['lowo'] = fuzz.trimf(skor.universe, [1, 1,3])

skor['low11'] = fuzz.trimf(skor.universe, [0, 5,10])
skor['low2'] = fuzz.trimf(skor.universe, [5,10,20])

skor['m11'] = fuzz.trimf(skor.universe, [20,30,40])
skor['m1'] = fuzz.trimf(skor.universe, [45,55,65])
skor['m2'] = fuzz.trimf(skor.universe, [60,70,80])
skor['h'] = fuzz.trimf(skor.universe, [75,100,100])

# Kurallar
rule1 = ctrl.Rule(meslek['evet'] & ekipman['evet'] & organizasyon['evet'] & ilk_yardim['evet'] & deneyim['evet'], skor['h'])



rule21 = ctrl.Rule(meslek['evet'] & ekipman['evet'] & organizasyon['evet'] & ilk_yardim['evet'], skor['m2'])
rule22 = ctrl.Rule(meslek['evet'] & ekipman['evet'] & organizasyon['evet'] & deneyim['evet'], skor['m2'])
rule23= ctrl.Rule(meslek['evet'] & ekipman['evet'] & ilk_yardim['evet'] & deneyim['evet'], skor['m2'])
rule24 = ctrl.Rule(meslek['evet']&  ilk_yardim['evet'] & organizasyon['evet'] & deneyim['evet'], skor['m2'])
rule25 = ctrl.Rule(ilk_yardim['evet'] & ekipman['evet'] & organizasyon['evet'] & deneyim['evet'], skor['m2'])

rule31 = ctrl.Rule(ekipman['evet'] & organizasyon['evet'] & ilk_yardim['evet'], skor['m1'])
rule32 = ctrl.Rule(meslek['evet'] & organizasyon['evet'] & deneyim['evet'], skor['m1'])
rule33= ctrl.Rule(meslek['evet'] & ekipman['evet'] & deneyim['evet'], skor['m1'])
rule34 = ctrl.Rule(meslek['evet'] & ilk_yardim['evet'] & organizasyon['evet'] , skor['m1'])
rule35 = ctrl.Rule(ilk_yardim['evet']&ekipman['evet'] & deneyim['evet'], skor['m1'])
rule36 = ctrl.Rule(ilk_yardim['evet']&organizasyon['evet'] & deneyim['evet'], skor['m1'])
rule37 = ctrl.Rule(ilk_yardim['evet']&meslek['evet']& deneyim['evet'], skor['m1'])
rule38 = ctrl.Rule(ekipman['evet']&meslek['evet']& organizasyon['evet'], skor['m1'])
rule39 = ctrl.Rule(ekipman['evet']&deneyim['evet']& organizasyon['evet'], skor['m1'])
rule40 = ctrl.Rule(ilk_yardim['evet']&meslek['evet']& ekipman['evet'], skor['m1'])




rule41 = ctrl.Rule(ekipman['evet'] & organizasyon['evet'], skor['low2'])
rule42 = ctrl.Rule(meslek['evet'] & organizasyon['evet'], skor['low2'])
rule43= ctrl.Rule(meslek['evet'] & ekipman['evet'], skor['low2'])
rule44 = ctrl.Rule(meslek['evet'] & ilk_yardim['evet'] , skor['low2'])
rule45 = ctrl.Rule(ilk_yardim['evet']&ekipman['evet'] , skor['low2'])
rule46 = ctrl.Rule(ilk_yardim['evet']&organizasyon['evet'], skor['low2'])
rule47 = ctrl.Rule(ilk_yardim['evet']&deneyim['evet'], skor['low2'])
rule48 = ctrl.Rule(ekipman['evet']&deneyim['evet']&meslek['hayir'] & ilk_yardim['hayir']& organizasyon['hayir'], skor['m11'])
rule49 = ctrl.Rule(deneyim['evet']& organizasyon['evet'], skor['low2'])
rule50 = ctrl.Rule(deneyim['evet']&meslek['evet'], skor['low2'])




#rule2 = ctrl.Rule(meslek['hayir'] & ekipman['hayir'] & organizasyon['hayir'] & ilk_yardim['hayir'] & deneyim['hayir'], skor['low1'])

rule3 = ctrl.Rule(ekipman['evet'], skor['lowo'])
rule4= ctrl.Rule(meslek['evet']&ekipman['hayir']&deneyim['hayir']&organizasyon['hayir']&ilk_yardim['hayir'],skor['low11'])
rule5= ctrl.Rule(deneyim['evet'],skor['lowo'])
rule6= ctrl.Rule(ilk_yardim['evet'],skor['lowo'])
rule7= ctrl.Rule(organizasyon['evet'],skor['lowo'])



#fuz kontrol sistemi
priority_ctrl = ctrl.ControlSystem([rule1,rule21, rule22,rule3, rule4,rule5, rule6,rule7, rule23, rule24, rule25, 
rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50])
priority = ctrl.ControlSystemSimulation(priority_ctrl)

# yolcu puanı hesaplama
def calculate_priority(meslek_value, ekipman_value, organizasyon_value, ilk_yardim_value, deneyim_value):
    priority.input['meslek'] = meslek_value
    priority.input['ekipman'] = ekipman_value
    priority.input['organizasyon'] = organizasyon_value
    priority.input['ilk_yardim'] = ilk_yardim_value
    priority.input['deneyim'] = deneyim_value

    priority.compute()
    return priority.output['skor']



# Örnek yolcu adaylarının puan hesaplaması
# Meslek durumu (0: hayır, 1: evet)
# Ekipman durumu (0: hayır, 1: evet)
# Organizasyon durumu (0: hayır, 1: evet)
# İlk yardım eğitimi (0: hayır, 1: evet)
# Arama kurtarma tecrübesi (0: hayır, 1: evet)


a = int(input(" CEVABINIZ EVET İSE 1 HAYIR İSE 0 TUŞUNA BASINIZ   Arama kurtarma görevlisi, sağlık çalışanı, madenci,kepçe oparetörü, inşaat çalışanı veya itfayeci misiniz? "))

b=int(input ("Yanınızda bölgede ihtiyaç duyulan çeşitli ekipmanınız var mı? (kırıcı matkap, termal kamera, sağlık malzemeleri vb.)     "))

c=int(input ("Bir ekip veya kurum (afad,akut,kızılay vb) dahilinde organizasyonunuz var mı?       "))

d=int(input (" İlk yardım eğitiminiz var mı?        "))

e=int(input ("Daha önce özellikle deprem neticesinde gerçekleşen bir arama kurtarma çalışmasına dahil oldunuz mu?  "))

t= a+b+d+c+e


if(t==0):
     print("YOLCU ADAYININ ÖNCELİK PUANI=0")

else:

    priority_skor = calculate_priority( a, b, c, d, e)
x= 1.68*priority_skor
print(f"YOLCU ADAYININ ÖNCELİK PUANI {(x)}")