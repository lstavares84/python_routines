#Tabela de distância entre as capitais
distancias = {
'SE':{'SE': 0,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': 294,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 356,'MA': None,'SP': None,'PI': None,'ES': None},
'PA':{'SE': None,'PA': 0,'MG': None,'RR': 6083,'DF': 716,'MS': None,'MT': 2941,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': 5298,'RN': None,'TO': 1283,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': 806,'SP': None,'PI': None,'ES': None},
'MG':{'SE': None,'PA': None,'MG': 0,'RR': None,'DF': None,'MS': 1453,'MT': None,'PR': None,'SC': None,'CE': None,'GO': 906,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': 434,'BA': 1372,'MA': None,'SP': 586,'PI': None,'ES': 524},
'RR':{'SE': None,'PA': None,'MG': None,'RR': 0,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': 785,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'DF':{'SE': None,'PA': None,'MG': 716,'RR': None,'DF': 0,'MS': 1134,'MT': 1133,'PR': None,'SC': None,'CE': None,'GO': 209,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': 973,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 1446,'MA': None,'SP': None,'PI': None,'ES': None},
'MS':{'SE': None,'PA': None,'MG': 1453,'RR': None,'DF': 1134,'MS': 0,'MT': 694,'PR': 991,'SC': None,'CE': None,'GO': 935,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': 1014,'PI': None,'ES': None},
'MT':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': 1133,'MS': 694,'MT': 0,'PR': None,'SC': None,'CE': None,'GO': 934,'PB': None,'AP': None,'AL': None,'AM': 2357,'RN': None,'TO': 1784,'RS': None,'RO': 1456,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'PR':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': 991,'MT': None,'PR': 0,'SC': 300,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': 408,'PI': None,'ES': None},
'SC':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': 300,'SC': 0,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': 476,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'CE':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': 0,'GO': None,'PB': 688,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': 800,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': 634,'ES': None},
'GO':{'SE': None,'PA': None,'MG': 906,'RR': None,'DF': 209,'MS': 935,'MT': 934,'PR': None,'SC': None,'CE': None,'GO': 0,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': 874,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 1643,'MA': None,'SP': None,'PI': None,'ES': None},
'PB':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': 688,'GO': None,'PB': 0,'AP': None,'AL': None,'AM': None,'RN': 185,'TO': None,'RS': None,'RO': None,'PE': 120,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'AP':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': 0,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'AL':{'SE': 294,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': 0,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': 285,'AC': None,'RJ': None,'BA': 632,'MA': None,'SP': None,'PI': None,'ES': None},
'AM':{'SE': 5215,'PA': 5298,'MG': 3951,'RR': 785,'DF': None,'MS': 3051,'MT': 2357,'PR': 4036,'SC': 4443,'CE': 5763,'GO': 3291,'PB': 5808,'AP': None,'AL': 5491,'AM': 0,'RN': 5985,'TO': 4141,'RS': 4563,'RO': 901,'PE': 5698,'AC': 1445,'RJ': 4374,'BA': 5009,'MA': 5335,'SP': 3971,'PI': 5267,'ES': 4476},
'RN':{'SE': 788,'PA': 2108,'MG': 2348,'RR': 6770,'DF': None,'MS': 3534,'MT': 3543,'PR': 3365,'SC': 3662,'CE': 537,'GO': 2618,'PB': 185,'AP': None,'AL': 572,'AM': 5985,'RN': 0,'TO': 2345,'RS': 4066,'RO': 4998,'PE': 297,'AC': 5533,'RJ': 2625,'BA': 1126,'MA': 1607,'SP': 2947,'PI': 1171,'ES': 2178},
'TO':{'SE': 1662,'PA': 1283,'MG': 1690,'RR': 4926,'DF': 973,'MS': 1785,'MT': 1784,'PR': 2036,'SC': 2336,'CE': 2035,'GO': 874,'PB': 2253,'AP': None,'AL': 1851,'AM': 4141,'RN': 2345,'TO': 0,'RS': 2747,'RO': None,'PE': 2058,'AC': 3764,'RJ': 2124,'BA': 1454,'MA': 1386,'SP': 1776,'PI': 1401,'ES': 2214},
'RS':{'SE': 3296,'PA': 3852,'MG': 1712,'RR': 5348,'DF': None,'MS': 1518,'MT': 2206,'PR': 711,'SC': 476,'CE': 4242,'GO': 1847,'PB': 3889,'AP': None,'AL': 3572,'AM': 4563,'RN': 4066,'TO': 2747,'RS': 0,'RO': 3662,'PE': 3779,'AC': 4196,'RJ': 1553,'BA': 3090,'MA': 3891,'SP': 1109,'PI': 3804,'ES': 2001},
'RO':{'SE': 4230,'PA': 4397,'MG': 3050,'RR': 1686,'DF': None,'MS': 2150,'MT': 1456,'PR': 3135,'SC': 3442,'CE': 4862,'GO': 2390,'PB': 4822,'AP': None,'AL': 4505,'AM': 901,'RN': 4998,'TO': None,'RS': 3662,'RO': 0,'PE': 4712,'AC': 544,'RJ': 3473,'BA': 4023,'MA': 4434,'SP': 3070,'PI': 4366,'ES': 3575},
'PE':{'SE': 501,'PA': 2074,'MG': 2061,'RR': 6483,'DF': None,'MS': 3247,'MT': 3255,'PR': 3078,'SC': 3375,'CE': 800,'GO': 2332,'PB': 120,'AP': None,'AL': 285,'AM': 5698,'RN': 297,'TO': 2058,'RS': 3779,'RO': 4712,'PE': 0,'AC': 5243,'RJ': 2338,'BA': 839,'MA': 1573,'SP': 2660,'PI': 1137,'ES': 1831},
'AC':{'SE': 4763,'PA': 4931,'MG': 3584,'RR': 2230,'DF': None,'MS': 2684,'MT': 1990,'PR': 3669,'SC': 3976,'CE': 5396,'GO': 2924,'PB': 5356,'AP': None,'AL': 5039,'AM': 1445,'RN': 5533,'TO': 3764,'RS': 4196,'RO': 544,'PE': 5243,'AC': 0,'RJ': 4007,'BA': 4457,'MA': 4968,'SP': 3604,'PI': 4900,'ES': 4109},
'RJ':{'SE': 1855,'PA': 3250,'MG': 434,'RR': 5159,'DF': None,'MS': 1444,'MT': 2017,'PR': 852,'SC': 1144,'CE': 2805,'GO': 1338,'PB': 2448,'AP': None,'AL': 2131,'AM': 4374,'RN': 2625,'TO': 2124,'RS': 1553,'RO': 3473,'PE': 2338,'AC': 4007,'RJ': 0,'BA': 1649,'MA': 3015,'SP': 429,'PI': 2579,'ES': 521},
'BA':{'SE': 356,'PA': 2100,'MG': 1372,'RR': 5794,'DF': 1446,'MS': 2568,'MT': 2566,'PR': 2385,'SC': 2682,'CE': 1389,'GO': 1643,'PB': 949,'AP': None,'AL': 632,'AM': 5009,'RN': 1126,'TO': 1454,'RS': 3090,'RO': 4023,'PE': 839,'AC': 4457,'RJ': 1649,'BA': 0,'MA': 1599,'SP': 1962,'PI': 1163,'ES': 1202},
'MA':{'SE': 1578,'PA': 806,'MG': 2738,'RR': 6120,'DF': None,'MS': 2979,'MT': 2978,'PR': 3230,'SC': 3537,'CE': 1070,'GO': 2054,'PB': 1660,'AP': None,'AL': 1672,'AM': 5335,'RN': 1607,'TO': 1386,'RS': 3891,'RO': 4434,'PE': 1573,'AC': 4968,'RJ': 3015,'BA': 1599,'MA': 0,'SP': 2970,'PI': 446,'ES': 2607},
'SP':{'SE': 2187,'PA': 2933,'MG': 586,'RR': 4756,'DF': None,'MS': 1014,'MT': 1614,'PR': 408,'SC': 705,'CE': 3127,'GO': 926,'PB': 2770,'AP': None,'AL': 2453,'AM': 3971,'RN': 2947,'TO': 1776,'RS': 1109,'RO': 3070,'PE': 2660,'AC': 3604,'RJ': 429,'BA': 1962,'MA': 2970,'SP': 0,'PI': 2792,'ES': 882},
'PI':{'SE': 1142,'PA': 947,'MG': 2302,'RR': 6052,'DF': None,'MS': 2911,'MT': 2910,'PR': 3143,'SC': 3450,'CE': 634,'GO': 1986,'PB': 1224,'AP': None,'AL': 1236,'AM': 5267,'RN': 1171,'TO': 1401,'RS': 3804,'RO': 4366,'PE': 1137,'AC': 4900,'RJ': 2579,'BA': 1163,'MA': 446,'SP': 2792,'PI': 0,'ES': 2171},
'ES':{'SE': 1408,'PA': 3108,'MG': 524,'RR': 5261,'DF': None,'MS': 1892,'MT': 2119,'PR': 1300,'SC': 1597,'CE': 2397,'GO': 1428,'PB': 2001,'AP': None,'AL': 1684,'AM': 4476,'RN': 2178,'TO': 2214,'RS': 2001,'RO': 3575,'PE': 1831,'AC': 4109,'RJ': 521,'BA': 1202,'MA': 2607,'SP': 882,'PI': 2171,'ES': 0}

}

#distancias = {
#'SE':{'SE': 0,'PA': 2079,'MG': 1578,'RR': 6000,'DF': 1652,'MS': 2765,'MT': 2775,'PR': 2595,'SC': 2892,'CE': 1183,'GO': 1848,'PB': 611,'AP': None,'AL': 294,'AM': 5215,'RN': 788,'TO': 1662,'RS': 3296,'RO': 4230,'PE': 501,'AC': 4763,'RJ': 1855,'BA': 356,'MA': 1578,'SP': 2187,'PI': 1142,'ES': 1408},
#'PA':{'SE': 2079,'PA': 0,'MG': 2824,'RR': 6083,'DF': 2120,'MS': 2942,'MT': 2941,'PR': 3193,'SC': 3500,'CE': 1610,'GO': 2017,'PB': 2161,'AP': None,'AL': 2173,'AM': 5298,'RN': 2108,'TO': 1283,'RS': 3852,'RO': 4397,'PE': 2074,'AC': 4931,'RJ': 3250,'BA': 2100,'MA': 806,'SP': 2933,'PI': 947,'ES': 3108},
#'MG':{'SE': 1578,'PA': 2824,'MG': 0,'RR': 4736,'DF': 716,'MS': 1453,'MT': 1594,'PR': 1004,'SC': 1301,'CE': 2528,'GO': 906,'PB': 2171,'AP': None,'AL': 1854,'AM': 3951,'RN': 2348,'TO': 1690,'RS': 1712,'RO': 3050,'PE': 2061,'AC': 3584,'RJ': 434,'BA': 1372,'MA': 2738,'SP': 586,'PI': 2302,'ES': 524},
#'RR':{'SE': 6000,'PA': 6083,'MG': 4736,'RR': 0,'DF': 4275,'MS': 3836,'MT': 3142,'PR': 4821,'SC': 5128,'CE': 6548,'GO': 4076,'PB': 6593,'AP': None,'AL': 6279,'AM': 785,'RN': 6770,'TO': 4926,'RS': 5348,'RO': 1686,'PE': 6483,'AC': 2230,'RJ': 5159,'BA': 5794,'MA': 6120,'SP': 4756,'PI': 6052,'ES': 5261},
#'DF':{'SE': 1652,'PA': 2120,'MG': 716,'RR': 4275,'DF': 0,'MS': 1134,'MT': 1133,'PR': 1366,'SC': 1673,'CE': 2200,'GO': 209,'PB': 2245,'AP': None,'AL': 1930,'AM': 3490,'RN': 2422,'TO': 973,'RS': 2027,'RO': 2589,'PE': 2135,'AC': 3123,'RJ': 1148,'BA': 1446,'MA': 2157,'SP': 1015,'PI': 1789,'ES': 1239},
#'MS':{'SE': 2765,'PA': 2942,'MG': 1453,'RR': 3836,'DF': 1134,'MS': 0,'MT': 694,'PR': 991,'SC': 1298,'CE': 3407,'GO': 935,'PB': 3357,'AP': None,'AL': 3040,'AM': 3051,'RN': 3534,'TO': 1785,'RS': 1518,'RO': 2150,'PE': 3247,'AC': 2684,'RJ': 1444,'BA': 2568,'MA': 2979,'SP': 1014,'PI': 2911,'ES': 1892},
#'MT':{'SE': 2775,'PA': 2941,'MG': 1594,'RR': 3142,'DF': 1133,'MS': 694,'MT': 0,'PR': 1679,'SC': 1986,'CE': 3406,'GO': 934,'PB': 3366,'AP': None,'AL': 3049,'AM': 2357,'RN': 3543,'TO': 1784,'RS': 2206,'RO': 1456,'PE': 3255,'AC': 1990,'RJ': 2017,'BA': 2566,'MA': 2978,'SP': 1614,'PI': 2910,'ES': 2119},
#'PR':{'SE': 2595,'PA': 3193,'MG': 1004,'RR': 4821,'DF': 1366,'MS': 991,'MT': 1679,'PR': 0,'SC': 300,'CE': 3541,'GO': 1186,'PB': 3188,'AP': None,'AL': 2871,'AM': 4036,'RN': 3365,'TO': 2036,'RS': 711,'RO': 3135,'PE': 3078,'AC': 3669,'RJ': 852,'BA': 2385,'MA': 3230,'SP': 408,'PI': 3143,'ES': 1300},
#'SC':{'SE': 2892,'PA': 3500,'MG': 1301,'RR': 5128,'DF': 1673,'MS': 1298,'MT': 1986,'PR': 300,'SC': 0,'CE': 3838,'GO': 1493,'PB': 3485,'AP': None,'AL': 3168,'AM': 4443,'RN': 3662,'TO': 2336,'RS': 476,'RO': 3442,'PE': 3375,'AC': 3976,'RJ': 1144,'BA': 2682,'MA': 3537,'SP': 705,'PI': 3450,'ES': 1597},
#'CE':{'SE': 1183,'PA': 1610,'MG': 2528,'RR': 6548,'DF': 2200,'MS': 3407,'MT': 3406,'PR': 3541,'SC': 3838,'CE': 0,'GO': 2482,'PB': 688,'AP': None,'AL': 1075,'AM': 5763,'RN': 537,'TO': 2035,'RS': 4242,'RO': 4862,'PE': 800,'AC': 5396,'RJ': 2805,'BA': 1389,'MA': 1070,'SP': 3127,'PI': 634,'ES': 2397},
#'GO':{'SE': 1848,'PA': 2017,'MG': 906,'RR': 4076,'DF': 209,'MS': 935,'MT': 934,'PR': 1186,'SC': 1493,'CE': 2482,'GO': 0,'PB': 2442,'AP': None,'AL': 2125,'AM': 3291,'RN': 2618,'TO': 874,'RS': 1847,'RO': 2390,'PE': 2332,'AC': 2924,'RJ': 1338,'BA': 1643,'MA': 2054,'SP': 926,'PI': 1986,'ES': 1428},
#'PB':{'SE': 611,'PA': 2161,'MG': 2171,'RR': 6593,'DF': 2245,'MS': 3357,'MT': 3366,'PR': 3188,'SC': 3485,'CE': 688,'GO': 2442,'PB': 0,'AP': None,'AL': 395,'AM': 5808,'RN': 185,'TO': 2253,'RS': 3889,'RO': 4822,'PE': 120,'AC': 5356,'RJ': 2448,'BA': 949,'MA': 1660,'SP': 2770,'PI': 1224,'ES': 2001},
#'AP':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': 0,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
#'AL':{'SE': 294,'PA': 2173,'MG': 1854,'RR': 6279,'DF': 1930,'MS': 3040,'MT': 3049,'PR': 2871,'SC': 3168,'CE': 1075,'GO': 2125,'PB': 395,'AP': None,'AL': 0,'AM': 5491,'RN': 572,'TO': 1851,'RS': 3572,'RO': 4505,'PE': 285,'AC': 5039,'RJ': 2131,'BA': 632,'MA': 1672,'SP': 2453,'PI': 1236,'ES': 1684},
#'AM':{'SE': 5215,'PA': 5298,'MG': 3951,'RR': 785,'DF': 3490,'MS': 3051,'MT': 2357,'PR': 4036,'SC': 4443,'CE': 5763,'GO': 3291,'PB': 5808,'AP': None,'AL': 5491,'AM': 0,'RN': 5985,'TO': 4141,'RS': 4563,'RO': 901,'PE': 5698,'AC': 1445,'RJ': 4374,'BA': 5009,'MA': 5335,'SP': 3971,'PI': 5267,'ES': 4476},
#'RN':{'SE': 788,'PA': 2108,'MG': 2348,'RR': 6770,'DF': 2422,'MS': 3534,'MT': 3543,'PR': 3365,'SC': 3662,'CE': 537,'GO': 2618,'PB': 185,'AP': None,'AL': 572,'AM': 5985,'RN': 0,'TO': 2345,'RS': 4066,'RO': 4998,'PE': 297,'AC': 5533,'RJ': 2625,'BA': 1126,'MA': 1607,'SP': 2947,'PI': 1171,'ES': 2178},
#'TO':{'SE': 1662,'PA': 1283,'MG': 1690,'RR': 4926,'DF': 973,'MS': 1785,'MT': 1784,'PR': 2036,'SC': 2336,'CE': 2035,'GO': 874,'PB': 2253,'AP': None,'AL': 1851,'AM': 4141,'RN': 2345,'TO': 0,'RS': 2747,'RO': None,'PE': 2058,'AC': 3764,'RJ': 2124,'BA': 1454,'MA': 1386,'SP': 1776,'PI': 1401,'ES': 2214},
#'RS':{'SE': 3296,'PA': 3852,'MG': 1712,'RR': 5348,'DF': 2027,'MS': 1518,'MT': 2206,'PR': 711,'SC': 476,'CE': 4242,'GO': 1847,'PB': 3889,'AP': None,'AL': 3572,'AM': 4563,'RN': 4066,'TO': 2747,'RS': 0,'RO': 3662,'PE': 3779,'AC': 4196,'RJ': 1553,'BA': 3090,'MA': 3891,'SP': 1109,'PI': 3804,'ES': 2001},
#'RO':{'SE': 4230,'PA': 4397,'MG': 3050,'RR': 1686,'DF': 2589,'MS': 2150,'MT': 1456,'PR': 3135,'SC': 3442,'CE': 4862,'GO': 2390,'PB': 4822,'AP': None,'AL': 4505,'AM': 901,'RN': 4998,'TO': None,'RS': 3662,'RO': 0,'PE': 4712,'AC': 544,'RJ': 3473,'BA': 4023,'MA': 4434,'SP': 3070,'PI': 4366,'ES': 3575},
#'PE':{'SE': 501,'PA': 2074,'MG': 2061,'RR': 6483,'DF': 2135,'MS': 3247,'MT': 3255,'PR': 3078,'SC': 3375,'CE': 800,'GO': 2332,'PB': 120,'AP': None,'AL': 285,'AM': 5698,'RN': 297,'TO': 2058,'RS': 3779,'RO': 4712,'PE': 0,'AC': 5243,'RJ': 2338,'BA': 839,'MA': 1573,'SP': 2660,'PI': 1137,'ES': 1831},
#'AC':{'SE': 4763,'PA': 4931,'MG': 3584,'RR': 2230,'DF': 3123,'MS': 2684,'MT': 1990,'PR': 3669,'SC': 3976,'CE': 5396,'GO': 2924,'PB': 5356,'AP': None,'AL': 5039,'AM': 1445,'RN': 5533,'TO': 3764,'RS': 4196,'RO': 544,'PE': 5243,'AC': 0,'RJ': 4007,'BA': 4457,'MA': 4968,'SP': 3604,'PI': 4900,'ES': 4109},
#'RJ':{'SE': 1855,'PA': 3250,'MG': 434,'RR': 5159,'DF': 1148,'MS': 1444,'MT': 2017,'PR': 852,'SC': 1144,'CE': 2805,'GO': 1338,'PB': 2448,'AP': None,'AL': 2131,'AM': 4374,'RN': 2625,'TO': 2124,'RS': 1553,'RO': 3473,'PE': 2338,'AC': 4007,'RJ': 0,'BA': 1649,'MA': 3015,'SP': 429,'PI': 2579,'ES': 521},
#'BA':{'SE': 356,'PA': 2100,'MG': 1372,'RR': 5794,'DF': 1446,'MS': 2568,'MT': 2566,'PR': 2385,'SC': 2682,'CE': 1389,'GO': 1643,'PB': 949,'AP': None,'AL': 632,'AM': 5009,'RN': 1126,'TO': 1454,'RS': 3090,'RO': 4023,'PE': 839,'AC': 4457,'RJ': 1649,'BA': 0,'MA': 1599,'SP': 1962,'PI': 1163,'ES': 1202},
#'MA':{'SE': 1578,'PA': 806,'MG': 2738,'RR': 6120,'DF': 2157,'MS': 2979,'MT': 2978,'PR': 3230,'SC': 3537,'CE': 1070,'GO': 2054,'PB': 1660,'AP': None,'AL': 1672,'AM': 5335,'RN': 1607,'TO': 1386,'RS': 3891,'RO': 4434,'PE': 1573,'AC': 4968,'RJ': 3015,'BA': 1599,'MA': 0,'SP': 2970,'PI': 446,'ES': 2607},
#'SP':{'SE': 2187,'PA': 2933,'MG': 586,'RR': 4756,'DF': 1015,'MS': 1014,'MT': 1614,'PR': 408,'SC': 705,'CE': 3127,'GO': 926,'PB': 2770,'AP': None,'AL': 2453,'AM': 3971,'RN': 2947,'TO': 1776,'RS': 1109,'RO': 3070,'PE': 2660,'AC': 3604,'RJ': 429,'BA': 1962,'MA': 2970,'SP': 0,'PI': 2792,'ES': 882},
#'PI':{'SE': 1142,'PA': 947,'MG': 2302,'RR': 6052,'DF': 1789,'MS': 2911,'MT': 2910,'PR': 3143,'SC': 3450,'CE': 634,'GO': 1986,'PB': 1224,'AP': None,'AL': 1236,'AM': 5267,'RN': 1171,'TO': 1401,'RS': 3804,'RO': 4366,'PE': 1137,'AC': 4900,'RJ': 2579,'BA': 1163,'MA': 446,'SP': 2792,'PI': 0,'ES': 2171},
#'ES':{'SE': 1408,'PA': 3108,'MG': 524,'RR': 5261,'DF': 1239,'MS': 1892,'MT': 2119,'PR': 1300,'SC': 1597,'CE': 2397,'GO': 1428,'PB': 2001,'AP': None,'AL': 1684,'AM': 4476,'RN': 2178,'TO': 2214,'RS': 2001,'RO': 3575,'PE': 1831,'AC': 4109,'RJ': 521,'BA': 1202,'MA': 2607,'SP': 882,'PI': 2171,'ES': 0}
#}



# Tabela de alíquotas de ICMS interestadual por estado

tabela_icms = {
'AC':{'AC': 17,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'AL':{'AC': 12,'AL': 17,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'AM':{'AC': 12,'AL': 12,'AM': 18,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'AP':{'AC': 12,'AL': 12,'AM': 12,'AP': 18,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'BA':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 18,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'CE':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 18,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'DF':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 18,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'ES':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 17,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'GO':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 17,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'MA':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 18,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'MG':{'AC': 7,'AL': 7,'AM': 7,'AP': 7,'BA': 7,'CE': 7,'DF': 7,'ES': 7,'GO': 7,'MA': 7,'MG': 18,'MS': 7,'MT': 7,'PA': 7,'PB': 7,'PE': 7,'PI': 7,'PR': 12,'RJ': 12,'RN': 7,'RO': 7,'RR': 7,'RS': 12,'SC': 12,'SE': 7,'SP': 12,'TO': 7},
'MS':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 17,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'MT':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 17,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'PA':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 17,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'PB':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 18,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'PE':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 18,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'PI':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 18,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'PR':{'AC': 7,'AL': 7,'AM': 7,'AP': 7,'BA': 7,'CE': 7,'DF': 7,'ES': 7,'GO': 7,'MA': 7,'MG': 12,'MS': 7,'MT': 7,'PA': 7,'PB': 7,'PE': 7,'PI': 7,'PR': 18,'RJ': 12,'RN': 7,'RO': 7,'RR': 7,'RS': 12,'SC': 12,'SE': 7,'SP': 12,'TO': 7},
'RJ':{'AC': 7,'AL': 7,'AM': 7,'AP': 7,'BA': 7,'CE': 7,'DF': 7,'ES': 7,'GO': 7,'MA': 7,'MG': 12,'MS': 7,'MT': 7,'PA': 7,'PB': 7,'PE': 7,'PI': 7,'PR': 12,'RJ': 20,'RN': 7,'RO': 7,'RR': 7,'RS': 12,'SC': 12,'SE': 7,'SP': 12,'TO': 7},
'RN':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 18,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'RO':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 17,5,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'RR':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 17,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 12},
'RS':{'AC': 7,'AL': 7,'AM': 7,'AP': 7,'BA': 7,'CE': 7,'DF': 7,'ES': 7,'GO': 7,'MA': 7,'MG': 12,'MS': 7,'MT': 7,'PA': 7,'PB': 7,'PE': 7,'PI': 7,'PR': 12,'RJ': 12,'RN': 7,'RO': 7,'RR': 7,'RS': 18,'SC': 12,'SE': 7,'SP': 12,'TO': 7},
'SC':{'AC': 7,'AL': 7,'AM': 7,'AP': 7,'BA': 7,'CE': 7,'DF': 7,'ES': 7,'GO': 7,'MA': 7,'MG': 12,'MS': 7,'MT': 7,'PA': 7,'PB': 7,'PE': 7,'PI': 7,'PR': 12,'RJ': 12,'RN': 7,'RO': 7,'RR': 7,'RS': 12,'SC': 17,'SE': 7,'SP': 12,'TO': 7},
'SE':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 18,'SP': 12,'TO': 12},
'SP':{'AC': 7,'AL': 7,'AM': 7,'AP': 7,'BA': 7,'CE': 7,'DF': 7,'ES': 7,'GO': 7,'MA': 7,'MG': 12,'MS': 7,'MT': 7,'PA': 7,'PB': 7,'PE': 7,'PI': 7,'PR': 12,'RJ': 12,'RN': 7,'RO': 7,'RR': 7,'RS': 12,'SC': 12,'SE': 7,'SP': 18,'TO': 7},
'TO':{'AC': 12,'AL': 12,'AM': 12,'AP': 12,'BA': 12,'CE': 12,'DF': 12,'ES': 12,'GO': 12,'MA': 12,'MG': 12,'MS': 12,'MT': 12,'PA': 12,'PB': 12,'PE': 12,'PI': 12,'PR': 12,'RJ': 12,'RN': 12,'RO': 12,'RR': 12,'RS': 12,'SC': 12,'SE': 12,'SP': 12,'TO': 18}

}


# Tabela de preços do óleo diesel por estado
tabela_preco_diesel = {
    "AC": 6.52,
    "AL": 4.75,
    "AM": 5.16,
    "AP": 5.06,
    "BA": 5.12,
    "CE": 5.04,
    "DF": 4.79,
    "ES": 4.89,
    "GO": 4.80,
    "MA": 4.74,
    "MG": 4.79,
    "MS": 5.04,
    "MT": 5.12,
    "PA": 5.37,
    "PB": 4.75,
    "PE": 5.13,
    "PI": 4.87,
    "PR": 4.82,
    "RJ": 5.06,
    "RN": 5.02,
    "RO": 5.35,
    "RR": 5.37,
    "SC": 4.96,
    "SP": 4.91,
    "SE": 4.93,
    "TO": 4.95,
}



def dijkstra(start, end, distancias):
    # Variáveis para armazenar a distância total (f) e a distância acumulada (g) entre as cidades definidas como INÍCIO e FIM
    g = {node: float('inf') for node in distancias}
    f = {node: float('inf') for node in distancias}

    parents = {node: None for node in distancias} # nó superior ou nó anterior

    # PREDEFINIÇÃO de variáveis antes de começar a calcular
    g[start] = 0 # Distância total (f) e distância acumulada (g) a partir do ponto de INÍCIO
    f[start] = 0 # Distância total (f) e distância acumulada (g) a partir do ponto de INÍCIO
    closed = set() # Variável para armazenar os caminhos possíveis já testados
    open_set = {start} # Variável para armazenar os caminhos possíveis A SEREM testados

    ### LOOP PARA CALCULAR A MENOR DISTÂNCIA
    while open_set: # Enquanto houver caminhos não testados...
        # Verifica o caminho atual com a menor distância entre a cidade atual e a cidade vizinha e continue procurando
        current = min(open_set, key=lambda node: f[node])

        # SE a cidade atual (nó) for o destino (FIM), calcule do fim até o início o caminho completo usando os nós pais
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()
            return path
        # FIM DE # SE a cidade atual (nó) for o destino (FIM), calcule do fim até o início o caminho completo usando os nós pais

        # Para mover o nó testado de open_set (não testado) para closed (caminhos testados)
        open_set.remove(current)
        closed.add(current)
        
        # Identificar todas as cidades vizinhas da cidade/nó atual
        for neighbor in distancias[current]:
            if distancias[current][neighbor] is None:
                continue  # Ignora valores None
            
            tentative_g = g[current] + distancias[current][neighbor] # Calcular a distância acumulada do nó/cidade atual para o nó/cidade vizinho selecionado
            
            # SE a distância acumulada até o nó/cidade selecionado for menor (mas não igual) à distância acumulada atual, por favor, atualize "g[vizinho]"
            # e "f[vizinho]".
            if tentative_g < g[neighbor]:
                parents[neighbor] = current # Define o nó/cidade atual como pai do vizinho atual
                g[neighbor] = tentative_g # atualiza a distância acumulada
                f[neighbor] = g[neighbor] # estima a distância total restante para chegar à cidade/nó final
                
                # Teste se o vizinho atual não foi testado antes. Mova o vizinho atual testado de não testado
                if neighbor not in open_set:
                    open_set.add(neighbor)
                # FIM DE Teste se o vizinho atual não foi testado antes. Mova o vizinho atual testado de não testado

    return None # SE não houver caminho de INÍCIO para FIM, retorne None
    ### FIM DO LOOP PARA CALCULAR A MENOR DISTÂNCIA

# DEFINIÇÃO PELO USUÁRIO de INÍCIO (start) e FIM (end) como no Google Maps
start = 'SE' # digite o nome da cidade onde a viagem começará
end = 'SP' # digite o nome da cidade de destino

# Chame a função dijkstra para calcular a menor distância
path = dijkstra(start, end, distancias)

# Imprime a solução na tela para o usuário
print('\n\n############## SOLUÇÃO ##############')
print(f'O caminho mais curto de {start} para {end} é:\n{path}\n\n')

