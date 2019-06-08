import requests
import time
from bs4 import BeautifulSoup
from wordcloud_test import mysql as wcmysql
from Spiders import mysql
from Helper.ApiHelper import api


if __name__ == '__main__':
    # print(get_loccodes())

    # 歌曲评论词云生成
    # ids = wcmysql.get_ids()
    # for sid in ids:
    #     comments = wcmysql.get_comments(sid)
    #     partition_result = wcmysql.partition(comments)
    #     wordlist = wcmysql.word_count(partition_result)
    #     draw_picture = wcmysql.draw_picture(wordlist, sid)

    # wcmysql.request_loccodes()
    # citys = wcmysql.get_city()
    # points = wcmysql.getlnglat(citys)
    points = [{'lat': 39.910924547299565, 'lng': 116.4133836971231, 'count': 23}, {'lat': 39.93482727239599, 'lng': 116.4224009776628, 'count': 6762}, {'lat': 39.91812360584148, 'lng': 116.37251358116619, 'count': 27}, {'lat': 39.926374523079886, 'lng': 116.44955872950158, 'count': 240}, {'lat': 39.8649371975573, 'lng': 116.29240188731139, 'count': 22}, {'lat': 39.911353808778294, 'lng': 116.22961266775826, 'count': 46}, {'lat': 39.96548984110075, 'lng': 116.3054340544974, 'count': 502}, {'lat': 39.94614672003409, 'lng': 116.10760355576534, 'count': 20}, {'lat': 39.75432583977336, 'lng': 116.14944375184247, 'count': 35}, {'lat': 39.916017122432365, 'lng': 116.66341535785384, 'count': 19}, {'lat': 40.13635076223076, 'lng': 116.66142426369096, 'count': 5}, {'lat': 40.22641337159427, 'lng': 116.23761791731043, 'count': 29}, {'lat': 39.73255523655448, 'lng': 116.348625212231, 'count': 25}, {'lat': 40.32261840426579, 'lng': 116.63838587142932, 'count': 2}, {'lat': 40.146950735799116, 'lng': 117.12737910459967, 'count': 5}, {'lat': 39.143929903310074, 'lng': 117.21081309155257, 'count': 5}, {'lat': 39.12339025327971, 'lng': 117.22146699490091, 'count': 2014}, {'lat': 39.12662568466626, 'lng': 117.2616931652718, 'count': 14}, {'lat': 39.115718082215515, 'lng': 117.2294162800198, 'count': 20}, {'lat': 39.14410527976771, 'lng': 117.15651537432414, 'count': 184}, {'lat': 39.15348514470478, 'lng': 117.20359278135501, 'count': 48}, {'lat': 39.09233234281453, 'lng': 117.32056850791443, 'count': 2}, {'lat': 39.14872660896657, 'lng': 117.01441017993696, 'count': 10}, {'lat': 38.94414856811469, 'lng': 117.36338677903083, 'count': 6}, {'lat': 39.2303439099184, 'lng': 117.14140273157703, 'count': 3}, {'lat': 39.389871228788344, 'lng': 117.05059715977872, 'count': 58}, {'lat': 39.723194482933174, 'lng': 117.31660069247685, 'count': 9}, {'lat': 39.00941577364663, 'lng': 117.71739882966088, 'count': 4}, {'lat': 38.0483119268727, 'lng': 114.52153190157445, 'count': 1936}, {'lat': 39.63658372414733, 'lng': 118.18645947203979, 'count': 608}, {'lat': 39.941748102377936, 'lng': 119.60853063334328, 'count': 400}, {'lat': 36.631262731204046, 'lng': 114.5456282282352, 'count': 599}, {'lat': 37.07668595096609, 'lng': 114.51146225612979, 'count': 421}, {'lat': 38.87998776845534, 'lng': 115.47146383768579, 'count': 1012}, {'lat': 40.7732372026915, 'lng': 114.89257223145165, 'count': 239}, {'lat': 40.95785601233803, 'lng': 117.96939750996681, 'count': 236}, {'lat': 38.310215141107044, 'lng': 116.84558075595014, 'count': 330}, {'lat': 39.54336666275853, 'lng': 116.69058173342549, 'count': 463}, {'lat': 37.745191408077424, 'lng': 115.6754061376161, 'count': 225}, {'lat': 37.87698902884778, 'lng': 112.55639149167204, 'count': 1392}, {'lat': 40.0824687161612, 'lng': 113.30643625858623, 'count': 271}, {'lat': 37.862360847859385, 'lng': 113.58761666287546, 'count': 134}, {'lat': 36.2012683721548, 'lng': 113.12255886984902, 'count': 289}, {'lat': 35.49628458647257, 'lng': 112.85857823132879, 'count': 314}, {'lat': 39.337108370541735, 'lng': 112.4393709396677, 'count': 81}, {'lat': 37.69283940975972, 'lng': 112.75959475565928, 'count': 271}, {'lat': 35.03270691290923, 'lng': 111.01338945447925, 'count': 430}, {'lat': 38.42238338517772, 'lng': 112.74062416023847, 'count': 158}, {'lat': 36.093741895419726, 'lng': 111.52553022403073, 'count': 346}, {'lat': 37.524497749577115, 'lng': 111.15044967529185, 'count': 197}, {'lat': 40.84842299711348, 'lng': 111.75550856170946, 'count': 590}, {'lat': 40.66292878826139, 'lng': 109.84654350721243, 'count': 227}, {'lat': 39.6620063648907, 'lng': 106.80039104999656, 'count': 56}, {'lat': 42.2616861034116, 'lng': 118.8955203975195, 'count': 264}, {'lat': 43.657980083916655, 'lng': 122.25052178737633, 'count': 150}, {'lat': 39.61448231394889, 'lng': 109.78744317923602, 'count': 97}, {'lat': 49.21844647556481, 'lng': 119.77237049946636, 'count': 171}, {'lat': 40.7493594895728, 'lng': 107.39439808372491, 'count': 54}, {'lat': 41.00074832767381, 'lng': 113.13946767446333, 'count': 78}, {'lat': 46.08846371321896, 'lng': 122.04436452582519, 'count': 52}, {'lat': 43.93942266533856, 'lng': 116.05439144074573, 'count': 75}, {'lat': 38.858275883056955, 'lng': 105.73537746449358, 'count': 24}, {'lat': 41.720915668888956, 'lng': 123.4559899308919, 'count': 1589}, {'lat': 38.9189536667856, 'lng': 121.62163148459285, 'count': 1064}, {'lat': 41.11505359694933, 'lng': 123.00137251399407, 'count': 165}, {'lat': 41.88596959305694, 'lng': 123.9643746156145, 'count': 132}, {'lat': 41.49291646055291, 'lng': 123.69250712420832, 'count': 111}, {'lat': 40.00640870559368, 'lng': 124.36154728159079, 'count': 106}, {'lat': 41.10093149946208, 'lng': 121.13259630055518, 'count': 164}, {'lat': 40.67313683826707, 'lng': 122.24157466449694, 'count': 106}, {'lat': 42.02802190131842, 'lng': 121.67640799865809, 'count': 92}, {'lat': 41.27416129045421, 'lng': 123.24336640651318, 'count': 102}, {'lat': 41.14124802295616, 'lng': 122.07322781023007, 'count': 110}, {'lat': 42.22994799718447, 'lng': 123.73236520917769, 'count': 101}, {'lat': 41.57982086475567, 'lng': 120.45749949793277, 'count': 117}, {'lat': 40.71736443636189, 'lng': 120.8433983399283, 'count': 143}, {'lat': 43.82195350104314, 'lng': 125.3306020759069, 'count': 1297}, {'lat': 43.84356783457924, 'lng': 126.55563450495482, 'count': 344}, {'lat': 43.171993571561, 'lng': 124.35648155715893, 'count': 127}, {'lat': 42.89405500574631, 'lng': 125.15042516688747, 'count': 46}, {'lat': 41.733815801613424, 'lng': 125.94660627598029, 'count': 91}, {'lat': 41.93962720532889, 'lng': 126.42963008937573, 'count': 54}, {'lat': 45.14740419341382, 'lng': 124.83148187569292, 'count': 104}, {'lat': 45.62550435999602, 'lng': 122.8455906084976, 'count': 47}, {'lat': 42.91574303372181, 'lng': 129.4773763202274, 'count': 95}, {'lat': 45.808825827952184, 'lng': 126.54161509031663, 'count': 1907}, {'lat': 47.3599771860153, 'lng': 123.92457086841536, 'count': 226}, {'lat': 45.300872317823895, 'lng': 130.97561865876668, 'count': 67}, {'lat': 47.35605615768509, 'lng': 130.3044328986694, 'count': 50}, {'lat': 46.65318589588607, 'lng': 131.16534168078073, 'count': 51}, {'lat': 46.59363317672175, 'lng': 125.10865763402039, 'count': 212}, {'lat': 47.733318457230936, 'lng': 128.84754638019822, 'count': 46}, {'lat': 46.80568999085779, 'lng': 130.327359092573, 'count': 129}, {'lat': 45.77630032154785, 'lng': 131.01154459102744, 'count': 31}, {'lat': 44.55624570898632, 'lng': 129.6395397783469, 'count': 149}, {'lat': 50.25127231175015, 'lng': 127.53548988621854, 'count': 74}, {'lat': 46.6600321798244, 'lng': 126.97535687530133, 'count': 143}, {'lat': 50.42002595502784, 'lng': 124.15292785448057, 'count': 32}, {'lat': 31.235929042252014, 'lng': 121.48053886017651, 'count': 79}, {'lat': 31.23724715206362, 'lng': 121.49158559252436, 'count': 4572}, {'lat': 31.194556772822725, 'lng': 121.44339635276381, 'count': 53}, {'lat': 31.226847968225428, 'lng': 121.43045437545099, 'count': 30}, {'lat': 31.233844930401652, 'lng': 121.45343177276851, 'count': 18}, {'lat': 31.254973368279597, 'lng': 121.40356934916508, 'count': 48}, {'lat': 31.269746698931357, 'lng': 121.51158645453457, 'count': 40}, {'lat': 31.265524144657057, 'lng': 121.53251993732523, 'count': 40}, {'lat': 31.118842580087428, 'lng': 121.38861193361008, 'count': 72}, {'lat': 46.58359834024085, 'lng': 131.40737518857432, 'count': 68}, {'lat': 31.3801553396772, 'lng': 121.27259505835202, 'count': 82}, {'lat': 31.227348292436346, 'lng': 121.55045460683195, 'count': 130}, {'lat': 30.747852376570318, 'lng': 121.34848004512126, 'count': 26}, {'lat': 31.037135176464492, 'lng': 121.23447959624146, 'count': 32}, {'lat': 31.155454317980737, 'lng': 121.13055310467274, 'count': 51}, {'lat': 30.923720110285377, 'lng': 121.48050373643107, 'count': 59}, {'lat': 32.06465288561847, 'lng': 118.80242172124585, 'count': 4735}, {'lat': 31.498809732685714, 'lng': 120.31858328810601, 'count': 1050}, {'lat': 34.21266655011306, 'lng': 117.29057543439453, 'count': 943}, {'lat': 31.815795653327836, 'lng': 119.98148471327892, 'count': 815}, {'lat': 31.303564074441766, 'lng': 120.59241222959322, 'count': 2294}, {'lat': 31.98654943120089, 'lng': 120.90159173866185, 'count': 679}, {'lat': 34.60224952526725, 'lng': 119.22862133316607, 'count': 367}, {'lat': 33.61629530103313, 'lng': 119.02148367070623, 'count': 451}, {'lat': 33.355100917626196, 'lng': 120.167544265761, 'count': 590}, {'lat': 32.40067693609037, 'lng': 119.41941890822997, 'count': 668}, {'lat': 32.19471592052375, 'lng': 119.43048944567383, 'count': 415}, {'lat': 32.4606750493083, 'lng': 119.9295663378548, 'count': 483}, {'lat': 33.96774971569008, 'lng': 118.28157403570837, 'count': 396}, {'lat': 30.25308298169347, 'lng': 120.21551180372168, 'count': 4336}, {'lat': 29.866033045866054, 'lng': 121.62857249434141, 'count': 1233}, {'lat': 28.00108540447221, 'lng': 120.70647689035565, 'count': 977}, {'lat': 30.750974830920143, 'lng': 120.76355182586005, 'count': 540}, {'lat': 30.898963937294184, 'lng': 120.09451660915789, 'count': 406}, {'lat': 30.0363693113069, 'lng': 120.58547847885335, 'count': 636}, {'lat': 29.084639385513697, 'lng': 119.65343619052916, 'count': 895}, {'lat': 28.975545802265025, 'lng': 118.86659674035565, 'count': 230}, {'lat': 29.99091168016034, 'lng': 122.21355631852045, 'count': 146}, {'lat': 28.66219405599615, 'lng': 121.42743470427969, 'count': 607}, {'lat': 28.473278180563412, 'lng': 119.9295730584414, 'count': 228}, {'lat': 31.826577833686887, 'lng': 117.23344266497664, 'count': 5388}, {'lat': 31.358536655799266, 'lng': 118.43943137653523, 'count': 928}, {'lat': 32.921523704350825, 'lng': 117.39551332813694, 'count': 434}, {'lat': 32.63184739905333, 'lng': 117.00638885071616, 'count': 426}, {'lat': 31.676265597609103, 'lng': 118.5135795794315, 'count': 340}, {'lat': 33.96165630027632, 'lng': 116.8045372670298, 'count': 250}, {'lat': 30.95123323991339, 'lng': 117.81847679445747, 'count': 249}, {'lat': 30.53095656804304, 'lng': 117.06360390491879, 'count': 1004}, {'lat': 29.721889786591692, 'lng': 118.34543725314781, 'count': 339}, {'lat': 32.26127087204081, 'lng': 118.33940613596579, 'count': 481}, {'lat': 32.89606099485221, 'lng': 115.82043612491321, 'count': 804}, {'lat': 33.65209532645213, 'lng': 116.97054394561262, 'count': 439}, {'lat': 31.741450815322555, 'lng': 116.52640966418569, 'count': 596}, {'lat': 33.850642695788835, 'lng': 115.7844632112745, 'count': 341}, {'lat': 30.670883790764535, 'lng': 117.49842096159624, 'count': 284}, {'lat': 30.94660154529291, 'lng': 118.76553424276743, 'count': 389}, {'lat': 26.080429420698078, 'lng': 119.30346983854001, 'count': 1733}, {'lat': 24.485406605176305, 'lng': 118.09643549976651, 'count': 1056}, {'lat': 25.45986545592271, 'lng': 119.0145209781265, 'count': 257}, {'lat': 26.269736515991838, 'lng': 117.64552116782143, 'count': 152}, {'lat': 24.879952330498313, 'lng': 118.68244626680422, 'count': 763}, {'lat': 24.51892979117087, 'lng': 117.65357645298785, 'count': 315}, {'lat': 26.647772874203266, 'lng': 118.1843695481426, 'count': 188}, {'lat': 25.081219844871676, 'lng': 117.02344756677536, 'count': 193}, {'lat': 26.672241711408567, 'lng': 119.55451074542829, 'count': 271}, {'lat': 28.68945529506072, 'lng': 115.86458944231661, 'count': 3114}, {'lat': 29.274247711040953, 'lng': 117.18457644638579, 'count': 271}, {'lat': 27.6283927093972, 'lng': 113.8614964337543, 'count': 175}, {'lat': 29.711340559079343, 'lng': 116.00753491163063, 'count': 747}, {'lat': 27.823578697788587, 'lng': 114.9235346513963, 'count': 157}, {'lat': 28.265787063191418, 'lng': 117.0755754270272, 'count': 149}, {'lat': 25.835176103497655, 'lng': 114.9405033729825, 'count': 1465}, {'lat': 27.119726826070448, 'lng': 115.00051072001253, 'count': 506}, {'lat': 27.820856421848216, 'lng': 114.4235636759064, 'count': 501}, {'lat': 27.954892253419565, 'lng': 116.36453876864373, 'count': 391}, {'lat': 28.460625921851733, 'lng': 117.94945960312224, 'count': 671}, {'lat': 36.65655420178723, 'lng': 117.12639941261048, 'count': 2804}, {'lat': 36.072227496663224, 'lng': 120.38945519114627, 'count': 2009}, {'lat': 36.81908568332188, 'lng': 118.06145253489896, 'count': 619}, {'lat': 34.815994048435115, 'lng': 117.33054194483897, 'count': 300}, {'lat': 37.43964182632334, 'lng': 118.68138493513693, 'count': 259}, {'lat': 37.470038383730525, 'lng': 121.45441541730195, 'count': 787}, {'lat': 36.71265155126753, 'lng': 119.16837791142822, 'count': 820}, {'lat': 35.420177394529645, 'lng': 116.59361234853988, 'count': 717}, {'lat': 36.2058580448846, 'lng': 117.0944948347959, 'count': 675}, {'lat': 37.5164305480148, 'lng': 122.12754097831325, 'count': 335}, {'lat': 35.42283899843767, 'lng': 119.53341540456555, 'count': 335}, {'lat': 36.23365413364694, 'lng': 117.68466691247161, 'count': 126}, {'lat': 35.11067124236514, 'lng': 118.36353300501388, 'count': 894}, {'lat': 37.441308454576266, 'lng': 116.36555674397471, 'count': 327}, {'lat': 36.46275818769411, 'lng': 115.99158784830443, 'count': 381}, {'lat': 37.3881961960769, 'lng': 117.9774040171467, 'count': 220}, {'lat': 35.23940742476551, 'lng': 115.48754503343376, 'count': 457}, {'lat': 34.75343885045448, 'lng': 113.63141920733915, 'count': 4545}, {'lat': 34.80288581121172, 'lng': 114.31459258497121, 'count': 519}, {'lat': 34.62426277921943, 'lng': 112.4594212983115, 'count': 966}, {'lat': 33.772050748691015, 'lng': 113.19952856052156, 'count': 353}, {'lat': 36.10594098401491, 'lng': 114.39950042177432, 'count': 476}, {'lat': 35.7523574114, 'lng': 114.30359364247649, 'count': 165}, {'lat': 35.3096399303368, 'lng': 113.93360046733228, 'count': 697}, {'lat': 35.22096325403899, 'lng': 113.24854783457334, 'count': 478}, {'lat': 35.76759302890629, 'lng': 115.03559747034215, 'count': 268}, {'lat': 34.04143161161871, 'lng': 113.85847553685502, 'count': 389}, {'lat': 33.5877107071022, 'lng': 114.02342077764726, 'count': 216}, {'lat': 34.778327249459984, 'lng': 111.2065332238741, 'count': 203}, {'lat': 32.99656220465144, 'lng': 112.53450131351325, 'count': 864}, {'lat': 34.4202016658586, 'lng': 115.66244933826238, 'count': 528}, {'lat': 32.15301454753105, 'lng': 114.09748283304512, 'count': 953}, {'lat': 33.6318288757022, 'lng': 114.70348251482332, 'count': 659}, {'lat': 33.01784241674367, 'lng': 114.02847078173271, 'count': 516}, {'lat': 35.072907226846525, 'lng': 112.60858070620743, 'count': 72}, {'lat': 30.598466736400987, 'lng': 114.31158155473231, 'count': 6072}, {'lat': 30.205207848941598, 'lng': 115.04553290894361, 'count': 302}, {'lat': 32.63506185840116, 'lng': 110.80452956069568, 'count': 343}, {'lat': 30.697446484492378, 'lng': 111.29254921035434, 'count': 444}, {'lat': 32.014796804669224, 'lng': 112.12853720100244, 'count': 321}, {'lat': 30.39657217331699, 'lng': 114.90160738827099, 'count': 104}, {'lat': 31.041732575569622, 'lng': 112.20639298023002, 'count': 200}, {'lat': 30.930689227018295, 'lng': 113.92251007733665, 'count': 342}, {'lat': 30.340842107742912, 'lng': 112.24552262926137, 'count': 493}, {'lat': 30.4593588576181, 'lng': 114.87849048410779, 'count': 538}, {'lat': 29.847055947646492, 'lng': 114.32851909026844, 'count': 190}, {'lat': 31.6965167723283, 'lng': 113.38945001822157, 'count': 116}, {'lat': 30.277939575301094, 'lng': 109.49459261857503, 'count': 138}, {'lat': 30.368271921724794, 'lng': 113.46159059813357, 'count': 90}, {'lat': 30.40835793241892, 'lng': 112.9054740908161, 'count': 76}, {'lat': 30.669621830099477, 'lng': 113.17240916632808, 'count': 80}, {'lat': 31.750496011246412, 'lng': 110.68252485039976, 'count': 16}, {'lat': 28.23488939994364, 'lng': 112.94547319535287, 'count': 4020}, {'lat': 27.833567639016444, 'lng': 113.14047079776427, 'count': 358}, {'lat': 27.835702227135585, 'lng': 112.95046418076468, 'count': 375}, {'lat': 26.899576139189122, 'lng': 112.57844721325992, 'count': 710}, {'lat': 27.245270272808565, 'lng': 111.474432885931, 'count': 471}, {'lat': 29.3631782939259, 'lng': 113.13548942422142, 'count': 387}, {'lat': 29.037749999406877, 'lng': 111.70545217995837, 'count': 322}, {'lat': 29.122815562551878, 'lng': 110.48553254695402, 'count': 140}, {'lat': 28.559711178489888, 'lng': 112.36151595471031, 'count': 179}, {'lat': 25.776683273601865, 'lng': 113.02146049909462, 'count': 319}, {'lat': 26.425864117900094, 'lng': 111.61945505792227, 'count': 310}, {'lat': 27.575160902978517, 'lng': 110.00851426537254, 'count': 296}, {'lat': 27.703208596991583, 'lng': 112.00150349288418, 'count': 249}, {'lat': 28.317369104701186, 'lng': 109.74557664946683, 'count': 90}, {'lat': 23.135336306695006, 'lng': 113.27143134445974, 'count': 5827}, {'lat': 24.815881278583017, 'lng': 113.60352734562261, 'count': 239}, {'lat': 22.548456637984177, 'lng': 114.06455183658751, 'count': 3747}, {'lat': 22.27656465424921, 'lng': 113.58255478654918, 'count': 440}, {'lat': 23.35909171772515, 'lng': 116.68852864054833, 'count': 627}, {'lat': 23.02775875078891, 'lng': 113.12851219549718, 'count': 820}, {'lat': 22.584603880965, 'lng': 113.08855619524043, 'count': 259}, {'lat': 21.276723439012073, 'lng': 110.36555441392824, 'count': 466}, {'lat': 21.669064031332095, 'lng': 110.931542579969, 'count': 456}, {'lat': 23.052888771125616, 'lng': 112.47148894063035, 'count': 281}, {'lat': 23.116358854725593, 'lng': 114.4235580165817, 'count': 544}, {'lat': 24.294177532206206, 'lng': 116.12953737612247, 'count': 256}, {'lat': 22.77873050016389, 'lng': 115.3729242893998, 'count': 246}, {'lat': 23.749684370959752, 'lng': 114.70744627290641, 'count': 183}, {'lat': 21.864339726138933, 'lng': 111.98848929181268, 'count': 152}, {'lat': 23.688230292088083, 'lng': 113.06246832527266, 'count': 176}, {'lat': 23.02730841164339, 'lng': 113.75842045787648, 'count': 1075}, {'lat': 22.5223146707905, 'lng': 113.39942236263188, 'count': 389}, {'lat': 23.662623192615886, 'lng': 116.62947017362819, 'count': 219}, {'lat': 23.555740488275585, 'lng': 116.37851218033846, 'count': 418}, {'lat': 22.920911970342857, 'lng': 112.05151269959146, 'count': 133}, {'lat': 22.822606601187154, 'lng': 108.37345082581861, 'count': 1441}, {'lat': 24.331961386852413, 'lng': 109.43442194634564, 'count': 347}, {'lat': 25.242885724872647, 'lng': 110.20354537457943, 'count': 536}, {'lat': 23.48274528113516, 'lng': 111.28551681182014, 'count': 135}, {'lat': 21.48683649576942, 'lng': 109.126533212566, 'count': 112}, {'lat': 21.6930052899694, 'lng': 108.360418838298, 'count': 46}, {'lat': 21.986593539484296, 'lng': 108.66058016842224, 'count': 125}, {'lat': 23.117448382037534, 'lng': 109.60552031033306, 'count': 195}, {'lat': 22.659830509953142, 'lng': 110.1884531233724, 'count': 270}, {'lat': 23.908185934295958, 'lng': 106.62458932565383, 'count': 127}, {'lat': 24.409450902865487, 'lng': 111.57352631416218, 'count': 89}, {'lat': 24.698911731272894, 'lng': 108.09149994498661, 'count': 157}, {'lat': 23.75654676260728, 'lng': 109.22745819590091, 'count': 67}, {'lat': 22.383117234663302, 'lng': 107.3715202061015, 'count': 46}, {'lat': 20.025801964462914, 'lng': 110.35553651088428, 'count': 6}, {'lat': 20.04404943925674, 'lng': 110.32552547126409, 'count': 682}, {'lat': 18.258736291747855, 'lng': 109.51855670139908, 'count': 115}, {'lat': 18.780994100706135, 'lng': 109.52354032070569, 'count': 7}, {'lat': 19.26425401991763, 'lng': 110.4805445259504, 'count': 17}, {'lat': 19.527146110044196, 'lng': 109.58745583568611, 'count': 24}, {'lat': 19.549062083120717, 'lng': 110.80450870631743, 'count': 14}, {'lat': 18.800106988303387, 'lng': 110.39943436554806, 'count': 8}, {'lat': 19.10110473128863, 'lng': 108.65856652679174, 'count': 20}, {'lat': 19.687119947910173, 'lng': 110.36553348340986, 'count': 7}, {'lat': 19.35737492427829, 'lng': 110.1085773245709, 'count': 5}, {'lat': 19.74434867164637, 'lng': 110.01351091010905, 'count': 9}, {'lat': 19.919474770278047, 'lng': 109.69744301483321, 'count': 14}, {'lat': 19.231378733012683, 'lng': 109.45747066911305, 'count': 5}, {'lat': 19.303997876684264, 'lng': 109.06246408734343, 'count': 1}, {'lat': 18.755871493854865, 'lng': 109.18050798894576, 'count': 4}, {'lat': 18.512331595698807, 'lng': 110.04446409254778, 'count': 3}, {'lat': 19.039163789180616, 'lng': 109.84451062847003, 'count': 2}, {'lat': 29.568996245338923, 'lng': 106.55843415537664, 'count': 27}, {'lat': 30.813621636707666, 'lng': 108.41555837050288, 'count': 4386}, {'lat': 29.70927819797873, 'lng': 107.39641979754104, 'count': 12}, {'lat': 29.559090182993803, 'lng': 106.57544006681098, 'count': 85}, {'lat': 29.490107128556012, 'lng': 106.48853359010742, 'count': 2}, {'lat': 29.89294837947611, 'lng': 121.56042128922172, 'count': 105}, {'lat': 29.547192516541124, 'lng': 106.46446511092543, 'count': 22}, {'lat': 29.50792771555286, 'lng': 106.51755873943073, 'count': 12}, {'lat': 29.50268309883491, 'lng': 106.66842977859555, 'count': 16}, {'lat': 29.811602753904445, 'lng': 106.40356933974634, 'count': 29}, {'lat': 29.034113748311206, 'lng': 106.65748419545173, 'count': 1}, {'lat': 29.723927343006626, 'lng': 106.6375590606026, 'count': 234}, {'lat': 29.408474739770405, 'lng': 106.54745425696237, 'count': 4}, {'lat': 29.53881256766016, 'lng': 108.77759119834955, 'count': 17}, {'lat': 29.863520067323154, 'lng': 107.08753107006804, 'count': 3}, {'lat': 29.295884374464997, 'lng': 106.26559760837834, 'count': 2}, {'lat': 29.978181239534244, 'lng': 106.28254108757974, 'count': 4}, {'lat': 29.362046335949085, 'lng': 105.93349936145171, 'count': 85}, {'lat': 29.86941278921405, 'lng': 107.73748061819887, 'count': 14}, {'lat': 30.333293968500094, 'lng': 107.33956587471806, 'count': 2}, {'lat': 30.305268389356584, 'lng': 108.04453753385525, 'count': 21}, {'lat': 30.93661127197471, 'lng': 108.70344750000172, 'count': 6}, {'lat': 31.024601766549154, 'lng': 109.47047275630993, 'count': 2}, {'lat': 31.080518811735914, 'lng': 109.8855455070308, 'count': 2}, {'lat': 31.404880009858267, 'lng': 109.57640255899645, 'count': 1}, {'lat': 30.006108697868918, 'lng': 108.12041416638326, 'count': 9}, {'lat': 28.45344786428608, 'lng': 109.01357389980959, 'count': 57}, {'lat': 28.8470402586741, 'lng': 108.77458600709745, 'count': 1}, {'lat': 29.29946229044254, 'lng': 108.17257803588225, 'count': 45}, {'lat': 30.655821878416408, 'lng': 104.08153351042463, 'count': 6144}, {'lat': 29.345584921327575, 'lng': 104.78444884671711, 'count': 194}, {'lat': 26.58803317333301, 'lng': 101.72554117091441, 'count': 99}, {'lat': 28.87766830360723, 'lng': 105.4485240693266, 'count': 352}, {'lat': 31.133115003656755, 'lng': 104.40441936496448, 'count': 261}, {'lat': 31.473663048745863, 'lng': 104.6855618607612, 'count': 555}, {'lat': 32.44161630531542, 'lng': 105.85042318166482, 'count': 179}, {'lat': 30.53909767110912, 'lng': 105.5994215306444, 'count': 158}, {'lat': 29.58588653832045, 'lng': 105.06458802499718, 'count': 217}, {'lat': 29.55794071745811, 'lng': 103.7725376036347, 'count': 222}, {'lat': 30.843782508337036, 'lng': 106.11750261487227, 'count': 599}, {'lat': 30.082526119421058, 'lng': 103.85656331579456, 'count': 203}, {'lat': 28.75800702855183, 'lng': 104.6494037048691, 'count': 364}, {'lat': 30.461746110678995, 'lng': 106.63955268233484, 'count': 301}, {'lat': 31.214307723927455, 'lng': 107.47459385897544, 'count': 430}, {'lat': 30.01679254570607, 'lng': 103.04954262360451, 'count': 105}, {'lat': 31.872888585956545, 'lng': 106.7515853031645, 'count': 212}, {'lat': 30.13495655925314, 'lng': 104.6344353416441, 'count': 130}, {'lat': 31.905511577266523, 'lng': 102.23141546175019, 'count': 13}, {'lat': 30.05527884351838, 'lng': 101.96854674579022, 'count': 14}, {'lat': 27.88775230036972, 'lng': 102.2735026809702, 'count': 49}, {'lat': 26.653324822309752, 'lng': 106.63657676352776, 'count': 1336}, {'lat': 26.598833108257494, 'lng': 104.8375546023468, 'count': 154}, {'lat': 27.731700878916666, 'lng': 106.93342774801829, 'count': 369}, {'lat': 26.25925237871499, 'lng': 105.95441712388904, 'count': 119}, {'lat': 27.674902690624183, 'lng': 109.16855802826001, 'count': 157}, {'lat': 25.09396734941651, 'lng': 104.91249214626991, 'count': 59}, {'lat': 27.408562131330886, 'lng': 105.33332337116845, 'count': 219}, {'lat': 26.58970296982603, 'lng': 107.9894462407788, 'count': 108}, {'lat': 26.260616196073833, 'lng': 107.5284027057371, 'count': 73}, {'lat': 24.873998150044006, 'lng': 102.85244836500482, 'count': 1947}, {'lat': 25.496406931543667, 'lng': 103.80243482794681, 'count': 242}, {'lat': 24.35771094244625, 'lng': 102.55356029311, 'count': 131}, {'lat': 25.139038793265964, 'lng': 99.17727328581788, 'count': 76}, {'lat': 27.34408386024681, 'lng': 103.72351177196889, 'count': 148}, {'lat': 26.860657438064884, 'lng': 100.23246452903453, 'count': 98}, {'lat': 22.830979186010275, 'lng': 100.97256981472799, 'count': 75}, {'lat': 23.89046855627851, 'lng': 100.09544042014869, 'count': 44}, {'lat': 25.051773565340376, 'lng': 101.53441248050268, 'count': 63}, {'lat': 23.36999624760546, 'lng': 103.38154905257933, 'count': 90}, {'lat': 23.40599429361173, 'lng': 104.22256899109433, 'count': 51}, {'lat': 22.013601254764165, 'lng': 100.80344682455637, 'count': 44}, {'lat': 25.6121284181925, 'lng': 100.27458284048366, 'count': 198}, {'lat': 24.438010702758117, 'lng': 98.59135935611411, 'count': 22}, {'lat': 25.823707417657754, 'lng': 98.8632883813579, 'count': 7}, {'lat': 27.82518468364326, 'lng': 99.70952999013957, 'count': 10}, {'lat': 29.65004027476773, 'lng': 91.12082391546393, 'count': 116}, {'lat': 31.14734654932703, 'lng': 97.17958359408598, 'count': 12}, {'lat': 29.243026939249226, 'lng': 91.77867513851903, 'count': 14}, {'lat': 29.275657822511512, 'lng': 88.89370303482552, 'count': 53}, {'lat': 31.482438388454657, 'lng': 92.0573384981749, 'count': 15}, {'lat': 32.50686601763335, 'lng': 80.11277692192645, 'count': 36}, {'lat': 29.654042176951524, 'lng': 94.36805828713257, 'count': 45}, {'lat': 34.34726881662395, 'lng': 108.94646555063274, 'count': 4577}, {'lat': 34.902637080502906, 'lng': 108.95240424835922, 'count': 61}, {'lat': 34.36891564286998, 'lng': 107.2445753670404, 'count': 281}, {'lat': 34.335476293368586, 'lng': 108.71542245143303, 'count': 480}, {'lat': 34.50571551675255, 'lng': 109.51658960525897, 'count': 295}, {'lat': 36.59111103521779, 'lng': 109.49658191612687, 'count': 109}, {'lat': 33.073799907833795, 'lng': 107.02943020926463, 'count': 346}, {'lat': 38.290883835484046, 'lng': 109.74161603381395, 'count': 211}, {'lat': 32.69051277057377, 'lng': 109.03560108265746, 'count': 138}, {'lat': 33.87863385220776, 'lng': 109.92441788136406, 'count': 110}, {'lat': 36.067234693545565, 'lng': 103.84052119633628, 'count': 1377}, {'lat': 39.77796014739059, 'lng': 98.29620384300111, 'count': 39}, {'lat': 38.52582009209263, 'lng': 102.19460568669837, 'count': 37}, {'lat': 36.55082533041454, 'lng': 104.1444508283435, 'count': 129}, {'lat': 34.58741188165064, 'lng': 105.73141674566955, 'count': 227}, {'lat': 37.93437780815811, 'lng': 102.64455434036918, 'count': 91}, {'lat': 38.932066007004934, 'lng': 100.45641147405634, 'count': 81}, {'lat': 35.549232050463516, 'lng': 106.67144234827796, 'count': 106}, {'lat': 39.73846908071564, 'lng': 98.50068521606795, 'count': 78}, {'lat': 35.71521598356201, 'lng': 107.6493856959542, 'count': 87}, {'lat': 35.586832926561875, 'lng': 104.63242008306302, 'count': 78}, {'lat': 33.40662022995126, 'lng': 104.92857497071192, 'count': 109}, {'lat': 35.60756218350311, 'lng': 103.21639056529743, 'count': 40}, {'lat': 34.98913990996821, 'lng': 102.91758468825803, 'count': 10}, {'lat': 36.62338469651661, 'lng': 101.78445017050855, 'count': 357}, {'lat': 36.508511080941304, 'lng': 102.1104440722824, 'count': 48}, {'lat': 36.96066282412982, 'lng': 100.90743432145598, 'count': 7}, {'lat': 35.525804586515534, 'lng': 102.02242827807585, 'count': 5}, {'lat': 36.2921024798988, 'lng': 100.62662114445924, 'count': 10}, {'lat': 34.4771938664709, 'lng': 100.25159197879555, 'count': 4}, {'lat': 33.01097958514274, 'lng': 97.01318076277326, 'count': 3}, {'lat': 37.38275046252745, 'lng': 97.37629911601906, 'count': 23}, {'lat': 38.492460055509596, 'lng': 106.23849358740017, 'count': 496}, {'lat': 38.98968283991508, 'lng': 106.3906004255049, 'count': 59}, {'lat': 38.00371291345338, 'lng': 106.20537126663626, 'count': 58}, {'lat': 36.02161725801098, 'lng': 106.24857742607188, 'count': 46}, {'lat': 37.50570141870293, 'lng': 105.20357090088713, 'count': 54}, {'lat': 43.830763204290484, 'lng': 87.62443993536046, 'count': 1067}, {'lat': 45.58567523781376, 'lng': 84.89590053887504, 'count': 68}, {'lat': 42.678924820793675, 'lng': 89.26602548864244, 'count': 19}, {'lat': 42.34446710455244, 'lng': 93.52937301238876, 'count': 43}, {'lat': 44.01685415991987, 'lng': 87.3150016244744, 'count': 67}, {'lat': 44.9121964134647, 'lng': 82.07291475827434, 'count': 27}, {'lat': 41.7702873304504, 'lng': 86.1517138653326, 'count': 72}, {'lat': 41.17502986007749, 'lng': 80.26694348473501, 'count': 107}, {'lat': 39.72047120487073, 'lng': 76.17430867621205, 'count': 11}, {'lat': 39.47609674864479, 'lng': 75.99639055639747, 'count': 80}, {'lat': 37.12044646304192, 'lng': 79.9285070635119, 'count': 18}, {'lat': 43.92272313749215, 'lng': 81.3305377475322, 'count': 128}, {'lat': 46.750948254373434, 'lng': 82.9872355184064, 'count': 75}, {'lat': 47.85072787010195, 'lng': 88.14792620373527, 'count': 33}, {'lat': 44.31197647806301, 'lng': 86.08688567193293, 'count': 112}, {'lat': 40.55326389470602, 'lng': 81.28735422539545, 'count': 8}, {'lat': 39.87120907742499, 'lng': 79.07561628689639, 'count': 2}, {'lat': 44.17244451890095, 'lng': 87.54993663229611, 'count': 16}, {'lat': 24.086956718804895, 'lng': 121.97387097871568, 'count': 250}, {'lat': 31.211883015985016, 'lng': 121.39369436652443, 'count': 47}, {'lat': 26.10705674357276, 'lng': 119.30846756124312, 'count': 7}, {'lat': 30.87532711771733, 'lng': 121.13156576447413, 'count': 5}, {'lat': 26.095631255981797, 'lng': 119.33983605008171, 'count': 2}, {'lat': 19.437612087581975, 'lng': 110.47660228796693, 'count': 3}, {'lat': 22.29358599327966, 'lng': 114.18612410257077, 'count': 624}, {'lat': 22.204117988443336, 'lng': 113.55751910182492, 'count': 139}]
    wcmysql.generate_map(5771, points)
    print(points)

    # 测试
    # comments = wcmysql.get_comments(ids[0])
    # partition_result = wcmysql.partition(comments)
    # wordlist = wcmysql.word_count(partition_result)
    # draw_picture = wcmysql.draw_picture(wordlist, ids[0])
