from collections import namedtuple
Result = namedtuple('Result', 'x_opt f_opt throughput_opt cost_opt fevals time')
RESULTS= [[Result(x_opt=[3, 9, 8, 1, 5, 3, 7], f_opt=-0.664, throughput_opt=0.9584, cost_opt=0.2944, fevals=1000, time=3.178858995437622), Result(x_opt=[8, 1, 1, 8, 5, 6, 1], f_opt=0.2664, throughput_opt=0.2268, cost_opt=0.4932, fevals=1000, time=2.769002914428711), Result(x_opt=[5, 8, 3, 9, 10, 1, 1], f_opt=-0.11662222222222221, throughput_opt=0.2128, cost_opt=0.09617777777777778, fevals=1000, time=2.579169988632202), Result(x_opt=[6, 10, 4, 1, 5, 3, 3], f_opt=-0.6788000000000001, throughput_opt=0.9604, cost_opt=0.2816, fevals=1000, time=3.10394287109375), Result(x_opt=[6, 5, 3, 1, 4, 3, 3], f_opt=-0.649, throughput_opt=0.9282, cost_opt=0.2792, fevals=1000, time=3.290811061859131), Result(x_opt=[1, 9, 6, 6, 3, 8, 9], f_opt=0.42746666666666666, throughput_opt=0.276, cost_opt=0.7034666666666667, fevals=1000, time=2.7811930179595947), Result(x_opt=[2, 4, 8, 7, 10, 3, 9], f_opt=-0.003114285714285736, throughput_opt=0.271, cost_opt=0.2678857142857143, fevals=1000, time=2.7008700370788574), Result(x_opt=[7, 4, 6, 8, 9, 4, 6], f_opt=0.11026666666666668, throughput_opt=0.236, cost_opt=0.34626666666666667, fevals=1000, time=2.828402042388916), Result(x_opt=[2, 3, 8, 2, 4, 4, 8], f_opt=-0.425, throughput_opt=0.7954, cost_opt=0.3704, fevals=1000, time=3.07463002204895), Result(x_opt=[7, 4, 5, 4, 8, 4, 4], f_opt=-0.12459999999999999, throughput_opt=0.4694, cost_opt=0.3448, fevals=1000, time=2.862442970275879), Result(x_opt=[5, 1, 1, 7, 10, 4, 4], f_opt=0.06268571428571423, throughput_opt=0.2716, cost_opt=0.33428571428571424, fevals=1000, time=2.7224040031433105), Result(x_opt=[2, 6, 10, 7, 6, 7, 3], f_opt=0.32268571428571435, throughput_opt=0.262, cost_opt=0.5846857142857144, fevals=1000, time=2.761209011077881), Result(x_opt=[6, 10, 6, 2, 4, 4, 10], f_opt=-0.48600000000000004, throughput_opt=0.8716, cost_opt=0.3856, fevals=1000, time=2.925382137298584), Result(x_opt=[1, 8, 9, 8, 8, 7, 6], f_opt=0.35320000000000007, throughput_opt=0.2352, cost_opt=0.5884, fevals=1000, time=2.637706995010376), Result(x_opt=[6, 5, 1, 9, 6, 1, 6], f_opt=-0.0966222222222222, throughput_opt=0.204, cost_opt=0.10737777777777778, fevals=1000, time=2.7419300079345703), Result(x_opt=[5, 4, 4, 4, 7, 5, 5], f_opt=-0.04077142857142857, throughput_opt=0.4666, cost_opt=0.42582857142857145, fevals=1000, time=2.8204948902130127), Result(x_opt=[1, 3, 2, 4, 9, 6, 8], f_opt=0.04342222222222225, throughput_opt=0.4596, cost_opt=0.5030222222222223, fevals=1000, time=2.9366888999938965), Result(x_opt=[9, 3, 9, 7, 2, 1, 1], f_opt=-0.0951142857142857, throughput_opt=0.2022, cost_opt=0.10708571428571428, fevals=1000, time=2.7456650733947754), Result(x_opt=[8, 3, 2, 6, 4, 1, 2], f_opt=-0.17273333333333332, throughput_opt=0.2738, cost_opt=0.10106666666666667, fevals=1000, time=2.9510750770568848), Result(x_opt=[6, 2, 3, 7, 5, 2, 5], f_opt=-0.07311428571428569, throughput_opt=0.2602, cost_opt=0.1870857142857143, fevals=1000, time=2.9771969318389893), Result(x_opt=[2, 4, 5, 1, 3, 7, 6], f_opt=-0.35719999999999996, throughput_opt=0.974, cost_opt=0.6168, fevals=1000, time=3.1847989559173584), Result(x_opt=[3, 7, 9, 1, 3, 3, 8], f_opt=-0.5987333333333333, throughput_opt=0.9126, cost_opt=0.3138666666666666, fevals=1000, time=3.224213123321533), Result(x_opt=[2, 8, 7, 4, 4, 8, 8], f_opt=0.2512, throughput_opt=0.4384, cost_opt=0.6896, fevals=1000, time=2.7883758544921875), Result(x_opt=[6, 3, 7, 1, 6, 3, 7], f_opt=-0.6521333333333333, throughput_opt=0.9396, cost_opt=0.28746666666666665, fevals=1000, time=3.3138840198516846), Result(x_opt=[1, 3, 10, 9, 4, 7, 4], f_opt=0.39417777777777774, throughput_opt=0.1948, cost_opt=0.5889777777777777, fevals=1000, time=2.7651848793029785), Result(x_opt=[10, 8, 6, 1, 3, 7, 2], f_opt=-0.3867333333333334, throughput_opt=0.9926, cost_opt=0.6058666666666667, fevals=1000, time=3.174459934234619), Result(x_opt=[9, 10, 6, 1, 9, 8, 8], f_opt=-0.2975777777777777, throughput_opt=0.9878, cost_opt=0.6902222222222223, fevals=1000, time=3.03930401802063), Result(x_opt=[6, 4, 4, 1, 7, 3, 3], f_opt=-0.6745428571428571, throughput_opt=0.9486, cost_opt=0.27405714285714283, fevals=1000, time=3.2701079845428467), Result(x_opt=[2, 7, 3, 2, 5, 7, 9], f_opt=-0.2125999999999999, throughput_opt=0.819, cost_opt=0.6064, fevals=1000, time=3.1738290786743164), Result(x_opt=[1, 3, 4, 9, 8, 2, 3], f_opt=-0.036022222222222205, throughput_opt=0.2102, cost_opt=0.1741777777777778, fevals=1000, time=2.7771260738372803), Result(x_opt=[7, 9, 10, 1, 9, 5, 5], f_opt=-0.5587111111111112, throughput_opt=1.0044, cost_opt=0.44568888888888886, fevals=1000, time=3.076375961303711), Result(x_opt=[10, 3, 8, 1, 3, 7, 3], f_opt=-0.3708, throughput_opt=0.9796, cost_opt=0.6088, fevals=1000, time=3.324923038482666), Result(x_opt=[8, 7, 10, 1, 5, 3, 9], f_opt=-0.6448, throughput_opt=0.9496, cost_opt=0.3048, fevals=1000, time=3.1761608123779297), Result(x_opt=[7, 10, 9, 1, 6, 3, 2], f_opt=-0.7108666666666666, throughput_opt=0.993, cost_opt=0.28213333333333335, fevals=1000, time=3.2331387996673584), Result(x_opt=[1, 9, 8, 8, 4, 5, 8], f_opt=0.2252, throughput_opt=0.2232, cost_opt=0.4484, fevals=1000, time=2.7437851428985596), Result(x_opt=[4, 6, 3, 1, 4, 7, 6], f_opt=-0.3812, throughput_opt=0.9916, cost_opt=0.6104, fevals=1000, time=3.2286839485168457), Result(x_opt=[10, 5, 3, 7, 9, 1, 7], f_opt=-0.15786984126984127, throughput_opt=0.267, cost_opt=0.10913015873015873, fevals=1000, time=2.7591772079467773), Result(x_opt=[3, 2, 9, 1, 4, 8, 5], f_opt=-0.3031999999999999, throughput_opt=0.9904, cost_opt=0.6872, fevals=1000, time=3.2932097911834717), Result(x_opt=[2, 2, 3, 7, 3, 8, 4], f_opt=0.4302190476190476, throughput_opt=0.239, cost_opt=0.6692190476190476, fevals=1000, time=2.9087350368499756), Result(x_opt=[10, 10, 3, 1, 5, 3, 7], f_opt=-0.6852, throughput_opt=0.982, cost_opt=0.2968, fevals=1000, time=3.0865378379821777), Result(x_opt=[2, 1, 10, 1, 6, 4, 4], f_opt=-0.6017333333333333, throughput_opt=0.9588, cost_opt=0.35706666666666664, fevals=1000, time=3.187596082687378), Result(x_opt=[1, 10, 10, 10, 3, 1, 7], f_opt=-0.03186666666666668, throughput_opt=0.1676, cost_opt=0.13573333333333332, fevals=1000, time=2.53813099861145), Result(x_opt=[10, 6, 7, 6, 4, 4, 4], f_opt=0.06546666666666662, throughput_opt=0.2916, cost_opt=0.35706666666666664, fevals=1000, time=2.6919219493865967), Result(x_opt=[3, 1, 3, 9, 5, 5, 7], f_opt=0.22897777777777775, throughput_opt=0.2008, cost_opt=0.42977777777777776, fevals=1000, time=2.769908905029297), Result(x_opt=[10, 4, 4, 1, 4, 7, 9], f_opt=-0.3632000000000001, throughput_opt=0.9896, cost_opt=0.6264, fevals=1000, time=3.0148491859436035), Result(x_opt=[4, 4, 6, 4, 6, 1, 1], f_opt=-0.23033333333333333, throughput_opt=0.3282, cost_opt=0.09786666666666666, fevals=1000, time=2.75451397895813), Result(x_opt=[4, 1, 6, 1, 3, 5, 2], f_opt=-0.5395333333333332, throughput_opt=0.975, cost_opt=0.4354666666666667, fevals=1000, time=3.1682331562042236), Result(x_opt=[8, 5, 9, 1, 6, 6, 2], f_opt=-0.4816666666666666, throughput_opt=1.0006, cost_opt=0.5189333333333334, fevals=1000, time=3.0087921619415283), Result(x_opt=[10, 2, 8, 9, 9, 2, 2], f_opt=-0.029866666666666652, throughput_opt=0.2112, cost_opt=0.18133333333333335, fevals=1000, time=2.729001045227051), Result(x_opt=[6, 10, 3, 9, 3, 8, 1], f_opt=0.47791111111111106, throughput_opt=0.1844, cost_opt=0.6623111111111111, fevals=1000, time=2.638982057571411), Result(x_opt=[4, 10, 9, 9, 9, 6, 7], f_opt=0.3018222222222222, throughput_opt=0.2108, cost_opt=0.5126222222222222, fevals=1000, time=2.679938793182373), Result(x_opt=[2, 5, 2, 7, 7, 1, 1], f_opt=-0.17202857142857142, throughput_opt=0.2638, cost_opt=0.09177142857142857, fevals=1000, time=2.741384983062744), Result(x_opt=[10, 9, 6, 4, 9, 3, 4], f_opt=-0.19948888888888888, throughput_opt=0.4706, cost_opt=0.27111111111111114, fevals=1000, time=2.8127050399780273), Result(x_opt=[4, 3, 2, 6, 5, 4, 1], f_opt=0.032866666666666655, throughput_opt=0.3002, cost_opt=0.3330666666666667, fevals=1000, time=2.816565990447998), Result(x_opt=[4, 2, 2, 1, 10, 3, 5], f_opt=-0.6588, throughput_opt=0.9292, cost_opt=0.2704, fevals=1000, time=3.275601863861084), Result(x_opt=[7, 3, 1, 4, 6, 5, 5], f_opt=-0.03426666666666667, throughput_opt=0.4604, cost_opt=0.4261333333333333, fevals=1000, time=2.9788429737091064), Result(x_opt=[7, 8, 3, 3, 5, 2, 5], f_opt=-0.3956666666666667, throughput_opt=0.5914, cost_opt=0.19573333333333331, fevals=1000, time=3.007561206817627), Result(x_opt=[6, 9, 10, 1, 6, 3, 2], f_opt=-0.6870666666666667, throughput_opt=0.9684, cost_opt=0.2813333333333333, fevals=1000, time=3.0574331283569336), Result(x_opt=[6, 9, 2, 7, 9, 2, 7], f_opt=-0.08446984126984125, throughput_opt=0.2728, cost_opt=0.18833015873015874, fevals=1000, time=2.903859853744507), Result(x_opt=[9, 4, 8, 8, 6, 7, 9], f_opt=0.37160000000000004, throughput_opt=0.2312, cost_opt=0.6028, fevals=1000, time=2.6981379985809326), Result(x_opt=[10, 6, 2, 1, 4, 4, 8], f_opt=-0.6104, throughput_opt=0.9928, cost_opt=0.3824, fevals=1000, time=3.243515968322754), Result(x_opt=[2, 7, 8, 2, 6, 2, 8], f_opt=-0.49706666666666666, throughput_opt=0.7, cost_opt=0.20293333333333333, fevals=1000, time=3.0748190879821777), Result(x_opt=[1, 10, 9, 6, 4, 8, 10], f_opt=0.40686666666666665, throughput_opt=0.2918, cost_opt=0.6986666666666667, fevals=1000, time=2.6004230976104736), Result(x_opt=[2, 8, 9, 6, 8, 3, 10], f_opt=-0.03653333333333336, throughput_opt=0.3144, cost_opt=0.27786666666666665, fevals=1000, time=2.6951470375061035), Result(x_opt=[9, 4, 9, 3, 3, 2, 2], f_opt=-0.3416, throughput_opt=0.5352, cost_opt=0.1936, fevals=1000, time=2.877865791320801), Result(x_opt=[10, 10, 2, 6, 5, 1, 3], f_opt=-0.19053333333333333, throughput_opt=0.3004, cost_opt=0.10986666666666665, fevals=1000, time=2.79721999168396), Result(x_opt=[3, 8, 1, 1, 5, 3, 7], f_opt=-0.6841999999999999, throughput_opt=0.9722, cost_opt=0.288, fevals=1000, time=3.1277718544006348), Result(x_opt=[7, 9, 3, 1, 6, 3, 6], f_opt=-0.6764, throughput_opt=0.9636, cost_opt=0.2872, fevals=1000, time=3.1501150131225586), Result(x_opt=[3, 7, 8, 8, 10, 4, 5], f_opt=0.10779999999999998, throughput_opt=0.2366, cost_opt=0.3444, fevals=1000, time=2.6514408588409424), Result(x_opt=[9, 8, 6, 2, 4, 3, 9], f_opt=-0.5668, throughput_opt=0.8692, cost_opt=0.3024, fevals=1000, time=3.083030939102173), Result(x_opt=[2, 8, 6, 9, 8, 8, 2], f_opt=0.4489777777777777, throughput_opt=0.2096, cost_opt=0.6585777777777777, fevals=1000, time=2.6773741245269775), Result(x_opt=[6, 6, 4, 4, 4, 4, 1], f_opt=-0.0988, throughput_opt=0.4396, cost_opt=0.3408, fevals=1000, time=2.7231640815734863), Result(x_opt=[5, 5, 4, 1, 8, 5, 5], f_opt=-0.5833999999999999, throughput_opt=1.0206, cost_opt=0.4372, fevals=1000, time=3.085951805114746), Result(x_opt=[7, 4, 3, 1, 4, 4, 9], f_opt=-0.6162, throughput_opt=0.9994, cost_opt=0.3832, fevals=1000, time=3.2256979942321777), Result(x_opt=[9, 6, 10, 1, 9, 3, 8], f_opt=-0.6745777777777777, throughput_opt=0.9648, cost_opt=0.2902222222222222, fevals=1000, time=3.0689640045166016), Result(x_opt=[10, 4, 2, 6, 6, 2, 1], f_opt=-0.1280666666666667, throughput_opt=0.3062, cost_opt=0.17813333333333334, fevals=1000, time=2.7798099517822266), Result(x_opt=[4, 5, 5, 8, 6, 6, 9], f_opt=0.28600000000000003, throughput_opt=0.2312, cost_opt=0.5172, fevals=1000, time=2.708777904510498), Result(x_opt=[8, 5, 8, 6, 7, 5, 5], f_opt=0.12009523809523814, throughput_opt=0.3108, cost_opt=0.43089523809523816, fevals=1000, time=2.785452127456665), Result(x_opt=[7, 7, 10, 7, 9, 6, 9], f_opt=0.24768571428571434, throughput_opt=0.2698, cost_opt=0.5174857142857143, fevals=1000, time=2.770888090133667), Result(x_opt=[7, 4, 3, 7, 9, 4, 2], f_opt=0.0674412698412698, throughput_opt=0.2696, cost_opt=0.3370412698412698, fevals=1000, time=2.818497896194458), Result(x_opt=[9, 5, 5, 1, 6, 6, 5], f_opt=-0.46706666666666674, throughput_opt=0.9916, cost_opt=0.5245333333333333, fevals=1000, time=3.047635793685913), Result(x_opt=[4, 7, 2, 4, 10, 5, 5], f_opt=-0.054400000000000004, throughput_opt=0.4768, cost_opt=0.4224, fevals=1000, time=2.8434019088745117), Result(x_opt=[7, 7, 3, 1, 9, 3, 3], f_opt=-0.6878666666666666, throughput_opt=0.9628, cost_opt=0.27493333333333336, fevals=1000, time=3.2561519145965576), Result(x_opt=[9, 6, 4, 5, 8, 1, 7], f_opt=-0.2304, throughput_opt=0.3428, cost_opt=0.1124, fevals=1000, time=2.8512299060821533), Result(x_opt=[8, 9, 3, 6, 4, 4, 2], f_opt=0.05506666666666665, throughput_opt=0.2916, cost_opt=0.3466666666666667, fevals=1000, time=2.8309948444366455), Result(x_opt=[8, 9, 4, 1, 10, 6, 9], f_opt=-0.4718, throughput_opt=0.999, cost_opt=0.5272, fevals=1000, time=2.9656829833984375), Result(x_opt=[2, 9, 7, 1, 6, 6, 8], f_opt=-0.4624666666666667, throughput_opt=0.9942, cost_opt=0.5317333333333333, fevals=1000, time=3.0703179836273193), Result(x_opt=[2, 7, 2, 10, 5, 8, 8], f_opt=0.49640000000000006, throughput_opt=0.1796, cost_opt=0.676, fevals=1000, time=2.8012771606445312), Result(x_opt=[7, 3, 6, 1, 3, 6, 4], f_opt=-0.46186666666666665, throughput_opt=0.992, cost_opt=0.5301333333333333, fevals=1000, time=3.2345519065856934), Result(x_opt=[8, 3, 8, 7, 4, 1, 4], f_opt=-0.1255142857142857, throughput_opt=0.239, cost_opt=0.11348571428571429, fevals=1000, time=2.7556309700012207), Result(x_opt=[5, 1, 2, 1, 6, 7, 3], f_opt=-0.4089999999999999, throughput_opt=0.9994, cost_opt=0.5904, fevals=1000, time=3.2492780685424805), Result(x_opt=[1, 8, 9, 9, 7, 2, 9], f_opt=-0.012050793650793645, throughput_opt=0.2088, cost_opt=0.19674920634920637, fevals=1000, time=2.6000490188598633), Result(x_opt=[3, 7, 2, 1, 5, 3, 2], f_opt=-0.6824, throughput_opt=0.9544, cost_opt=0.272, fevals=1000, time=3.23746919631958), Result(x_opt=[3, 9, 5, 4, 4, 6, 4], f_opt=0.07539999999999997, throughput_opt=0.4382, cost_opt=0.5136, fevals=1000, time=2.789783000946045), Result(x_opt=[6, 10, 10, 1, 8, 7, 4], f_opt=-0.387, throughput_opt=0.9918, cost_opt=0.6048, fevals=1000, time=3.097306966781616), Result(x_opt=[4, 6, 10, 1, 9, 6, 3], f_opt=-0.4716666666666667, throughput_opt=0.989, cost_opt=0.5173333333333333, fevals=1000, time=3.0615501403808594), Result(x_opt=[10, 1, 2, 6, 2, 2, 2], f_opt=-0.056333333333333346, throughput_opt=0.2454, cost_opt=0.18906666666666666, fevals=1000, time=2.8677151203155518), Result(x_opt=[5, 9, 9, 1, 3, 7, 2], f_opt=-0.3875333333333334, throughput_opt=0.9926, cost_opt=0.6050666666666666, fevals=1000, time=3.085590124130249), Result(x_opt=[3, 2, 1, 1, 7, 6, 7], f_opt=-0.48939999999999995, throughput_opt=1.0062, cost_opt=0.5168, fevals=1000, time=3.3846700191497803), Result(x_opt=[9, 7, 4, 6, 10, 5, 3], f_opt=0.10486666666666672, throughput_opt=0.3186, cost_opt=0.4234666666666667, fevals=1000, time=2.8091530799865723)]]
