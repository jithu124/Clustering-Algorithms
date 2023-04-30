from typing import Callable, List, Optional, Tuple
from DrawFunctions import *
from random import randrange, random, sample
from collections import Counter

#points = [(0,0),(0.5,0),(-0.5,0),(0,0.5),(0,-0.5),(0,0.8)]
points  = [(-0.13791602796935326, -2.1580980140640156), (-0.17344729245637514, -2.376834892914444), (-0.6254601325143467, -1.933500706962515), (-0.5008198158320882, -1.8490975078786878), (0.010592133876235976, -2.242805162489601), (-0.11751870246788043, -1.907473969330577), (-0.2905185934993101, -2.1831986320310572), (-0.5554493479209202, -2.199600428029402), (-0.543412662319055, -2.163550416464434), (-0.21863176125220338, -2.141502486601749), (-0.11470398401928744, -2.370424940963247), (-0.1008964342163298, -2.3750418774463165), (-0.5271849624642465, -2.114991644046292), (-0.12093815140613826, -2.1475810645442874), (-0.6245320679358635, -2.067404221438425), (-0.562531854921317, -2.222692148417077), (-0.5503217181999767, -2.145004873991049), (-0.3306508724682153, -2.0131834333680776), (-0.10596081758363587, -1.9025105006342768), (-0.5463188592564343, -2.336412175444253), (-0.45029330163224013, -2.103170407772992), (-0.21558806493982213, -1.8422202141969608), (-0.43309317397336405, -2.1441969281524424), (-0.1987120134728857, -2.0778037605801014), (-0.302256564696169, -2.331731244737636), (-0.25353181570752986, -2.387615178657457), (-0.33767831417067373, -2.2523286033398975), (-0.18488366547993967, -1.8049795503773642), (-0.33880267893081006, -2.270089850967938), (-0.09988390178399867, -1.9672417636756125), (-0.6136158646948648, -2.111736024796336), (-0.37203307138450914, -2.172925153383551), (-0.5201910446217595, -2.03610379825293), (-0.15226681551878762, -2.0816377148619276), (-0.37886199951035227, -2.1340385038034837), (-0.4749599152851628, -2.199033978176444), (-0.3295018973353392, -1.9181337791359), (-0.12104666430074515, -2.137796763363507), (-0.17911542684725537, -2.3533751412073403), (-0.1660295000256919, -1.9321363293421243), (-0.20513342868009343, -2.0608554401508066), (-0.34648825331389693, -2.254267891269461), (-0.15877584975189454, -1.7976306077603128), (-0.5555751368817311, -1.943699600757416), (-0.24790542007100624, -1.9444991320714933), (-0.3854608829788192, -1.8232593774609864), (-0.2579738828867606, -2.2938548104067418), (-0.12150678735561166, -2.227042827796986), (-0.3108623496976454, -1.7589061437307043), (-0.10098474544613512, -2.209265283984697), (-0.5521497423887212, -2.340438173082463), (-0.13300824535977698, -1.9395670069123288), (-0.5153668530707403, -2.193621272239418), (-0.143777541104047, -1.8606097306123948), (-0.3959490676169664, -2.2913303989907616), (-0.12688742769032357, -1.9230498479754183), (-0.4876812720459365, -2.380980342962154), (-0.5130318684168729, -2.3286663068513227), (-0.525681438410638, -2.3052574605357474), (-0.31919808527793064, -1.9105991620018101), (-0.4082104701477375, -1.996107819619534), (-0.17503691360532733, -2.111302368714911), (-0.4446925386124754, -1.9880605761563992), (-0.18825813303601366, -2.0032832929470876), (0.0028139663590274755, -2.202705018846607), (-0.3757691452051859, -2.038225115402672), (-0.5242894567046633, -2.3885789918558147), (-0.21341411726949333, -1.7900050668662713), (-0.3407262551362887, -2.3876416267620666), (3.0401540537549487, -4.9626873443582324), (3.1976537926316912, -4.504952654454997), (3.318374679277505, -4.248642972642745), (2.9081526268720816, -5.204929699311646), (3.668548333946594, -4.881764422453396), (2.9884875200417182, -4.968058268169588), (3.023615961022653, -5.359733801457532), (2.8678042570091526, -5.006605086912318), (3.681148037306396, -4.521543248785437), (3.6806056155801468, -4.5319696421312985), (3.2775358585831134, -4.267140500279429), (3.596891224619912, -4.78929601929501), (3.0094474149493893, -4.621162537343714), (3.375276989707819, -5.1363517295387116), (3.224238213918548, -4.600303754581475), (3.1177322803012375, -4.828302672370604), (2.8888037078234055, -5.347802256462676), (3.056272021157214, -4.595656478834919), (2.736901811742097, -4.924492052114545), (3.7344550647138224, -4.9055471659269765), (3.3739207571143366, -5.027644631845353), (3.1472561259329326, -4.257693645096426), (0.9435274342089945, -0.8177020709048942), (0.5252895088488743, -2.3119101073416686), (1.552168374680277, -2.3171104271340726), (0.7190968150420701, -1.0211742663500805), (1.2647422529419168, -1.54240315465707), (0.7223964364585405, -1.5418621146643634), (1.9493239603948236, -1.5943748359619243), (1.7553725443907315, -2.2817419321412435), (1.9793280570952603, -1.9914065839864596), (0.3461632044260601, -2.180186673593372), (0.95916815372418, -1.4830554711321553), (1.35528910739284, -1.474927974225133), (1.6785746888328712, -1.2887379873729623), (1.4219433232232694, -1.5014230137757172), (0.6600789059325052, -1.1299683957877182), (1.7206906242860893, -1.7708272415547184), (0.9569621780741064, -1.7450413242002378), (1.4608721429849367, -2.0132077787145017), (0.8267889791794085, -2.631690041267471), (1.1420125315293965, -1.3093151555868257), (0.1285546328583711, -1.8334914696911273), (1.336238065319395, -1.8804785973702298), (1.0087366105909314, -1.888457704523096), (1.4797224054999032, -1.0307705060998886), (1.7785068025579394, -2.1927878722286724), (1.216015907692817, -1.9449475014296325), (1.2964355688515599, -2.0307041966306287), (1.116629011170268, -2.1465679106148143), (0.2829849924736306, -1.43772369394323), (1.487863483183585, -1.1185428361984697), (1.8692145834112925, -2.0238770878827577), (1.3964196350283684, -1.3906340639989816), (0.23013415432758755, -2.309963420433775), (0.5665107711933507, -2.447698056389983), (1.1657620270382403, -1.1304671559537645), (0.6177937836111014, -1.385063494325212), (1.4784495858348379, -1.0597775557192057), (0.7683791073094557, -2.450253433144592), (1.252470785518972, -0.9227437604393723), (1.3238645828788274, -2.611445975678328), (1.3892281852853003, -0.9592811274897366), (1.8444909242085692, -2.374280793207898), (1.9409333993407545, -2.145413632246247), (0.23834571846674835, -1.5210432512466143), (0.362718656124018, -1.6407037035156207), (0.9654749183535327, -0.7773281279682085), (1.10448934943397, -2.6813603764671248), (2.0156944885071395, -1.679542744996077), (1.5963869304076939, -1.1233487692993824), (0.8370882748498456, -1.8156872976453822), (0.3663223387378999, -1.2603314578956655), (0.21608521296152117, -1.8561188417878285), (1.3771856813758254, -2.663115840949703), (1.3947393180024892, -1.334435886221814), (0.3101375126372916, -1.1179617085295872), (0.9948973249341732, -1.5957813942816859), (1.309536438082359, -1.778004292702384), (1.0668867627716494, -0.7629962330054676), (1.0049988555259302, -1.329816572736628), (0.46651688162445004, -1.070839845874423), (1.1714770592854105, -1.4265323997673578), (1.4098083669514994, -1.1943681207544872), (1.566718104709396, -2.2172844270495435), (0.32832284352033747, -1.5110664786686563), (0.5621838952831106, -1.6266413560613089), (1.1941636693119742, -0.8162709214551203), (1.2107118233062928, -0.9877377924957503), (1.4450941353430156, -1.0851009916721235), (1.8962745267582939, -1.5835097052317548), (1.065701381910239, -1.692528146884881), (1.8286263337157354, -2.2407479540934605), (0.8655569524313498, -1.2390332271203692), (0.3218973825166951, -1.7976383288401216), (1.880206940539137, -2.35021829235375), (0.6097656469587416, -1.6521279240769537), (0.3963040327345868, -1.1956878415831764), (0.4182056298810948, -1.7074636060800272), (1.431403051426404, -1.8699077934491837), (-0.7663787139392466, 5.008021606134641), (-2.0168423272272182, 4.480788119483982), (-0.9279394747708922, 4.194609099791541), (-0.6904711727807411, 4.855811999070554), (-0.4949389933443117, 5.253197329733925), (-1.5109502035010036, 4.928034050646019), (-1.8764342680104162, 3.882346587839826), (-0.3505578840588446, 5.254596425173999), (-0.2672794271003601, 4.725043644761076), (-0.08222674310269551, 4.45197699489067), (-1.4513024977203044, 5.3256552254791805), (-1.052969700642474, 4.083818047600728), (-1.9170831211388826, 4.723518773483671), (-1.6673446654253476, 3.9742648368721856), (-1.2192580209780863, 4.595811131815573), (-1.5124898774820925, 5.3391074563871035), (-1.0216083782683962, 4.203436632550691), (-0.5970928663749167, 5.153232714343626), (-0.8307900959893821, 3.5595565975704178), (-1.5222151837899403, 5.531819203498866), (-0.8818796954044485, 5.172062644905613), (-1.4077703852930383, 4.319334549653352), (-1.1827911255893053, 4.239284692232665), (-0.5115912546759043, 4.477774994317836), (-1.2360242300198339, 3.999721622184753), (-0.5240511851400719, 3.8580587734837675), (-1.9024113123754645, 3.999607648259802), (-2.087634090821696, 4.058581615139451), (-1.3078514700235162, 5.305108635196823), (-0.22208147201303474, 4.883616564856828), (-1.1809116550174958, 5.377928882664875), (-0.9437788982302092, 4.97068924806127), (-1.480954175275309, 4.684019357791969), (-2.072241612356351, 4.581459018615244), (-1.0664050094924782, 3.956938077587815), (-1.3100676115437921, 3.829790257853523), (-1.3551245540156995, 5.507462493596411), (-0.9282463851826337, 5.2199933062789565), (-1.4596632035820507, 4.009123900092102), (-1.3137274505740288, 5.412396742220439), (-1.9742503883465434, 4.641154553699507), (-1.0559972097788568, 4.972493283206219), (-1.0741591569509796, 4.852449695378733), (-0.5529044828256764, 5.0134181232503705), (-2.62169818743995, -3.72167582848236), (-2.9018924449996164, -3.6881292376309367), (-2.9221278574323595, -3.032623761187301), (-2.828714644434392, -3.0229172283237196), (-2.620430209337933, -3.9792199687046104), (-2.226820793685099, -3.0052851675010275), (-3.2229684904948153, -2.458120088460684), (-2.583727303842725, -3.578133670859955), (-2.822568411451914, -3.2599454927285194), (-2.517602570781158, -2.580727778781868), (-2.237478520472778, -3.161890197501575), (-2.700933257916723, -3.2625817322057795), (-2.8239114304674198, -3.6585021864890583), (-1.9002527432197391, -3.1361492072117727), (-3.411556982457087, -2.6224055448754555), (-3.54284911145152, -2.5324040886471924), (-2.6193819605813715, -2.347107570486161), (-2.0775839680167705, -2.9809573476521245), (-3.4397263533217624, -3.378208278872183), (-2.2549933705966567, -2.8887790490382925), (-2.2788817929176313, -3.45022698464395), (-3.05170407383604, -2.6645257549826225), (-2.6820910444045785, -3.9742537458991), (-2.3193667645885387, -2.1181896668094677), (-2.281441236260883, -3.3036143377503806), (-3.565367987721769, -2.982322434623927), (-2.323620074152543, -2.916865143389516), (-3.4449675924616807, -2.4998443265330437), (-3.1040761331665974, -3.5914528423699053), (-2.3230021809451187, -3.6366670618893906), (-2.7414470530082222, -2.9786540724139607), (-3.516447308288441, -3.0431700433023794), (-2.7565728570227, -2.7567472680334886), (-2.2913322843867876, -3.2071586819590494), (-2.488658311933137, -3.0143315209028585), (-3.629916552793815, -3.238209014882103), (-2.4632243072545177, -2.9685292925206963), (-1.8767424453543833, -3.098738246205136), (-3.449111304998673, -2.6453807170906143), (-2.7103973816152056, -3.4258787640455077), (-2.4465185115409325, -2.856658139118765), (-3.1653774528504397, -2.4182240439127667), (-2.0413665586004575, -2.6553021700065638), (-2.0101776086117704, -2.463681473464867), (-2.769717683108797, -3.006544659205885), (-3.360788449813768, -2.4679268631629965), (-3.0467141688390953, -3.4689773386737968), (-3.5454457454166888, -2.653492444761291), (-2.951025120515495, -3.158498301527809), (-3.2000041097977387, -2.8914882354886178), (-2.7054279075122407, -2.430491006096198), (-3.2428228556045817, -3.457223403714855), (-2.2642418423305735, -2.9445112416828985), (-3.1291721826087544, -3.5319758673940775), (-2.5226916040704723, -3.806031256218063), (-3.2476674186725063, -3.4356986672317102), (-3.124071911423058, -3.6694279877014773), (-2.8507501381227125, -3.0316216181653646), (-2.544043119713204, -2.723181270334151), (-2.156752800297858, -2.965443223158805), (-1.9319504947207402, -3.2215430917037957), (-2.690240522030131, -2.569811050654486), (-3.60203234199032, -3.377432759828586), (-2.8871279596316577, -3.8087890142947547), (-1.9355310916420292, -3.3261676823105715), (-2.492880164649719, -3.8832086109166166), (-2.9141561812663563, -2.60902627418256), (-2.9297456320565307, -3.2974427072181913), (-2.8873692318296875, -3.9367653298641034), (-2.5195817993912204, -3.203819145871696), (-3.060766356387465, -2.314327513789918), (-1.8046619411763598, -3.2030195209735495), (-3.1321256657165106, -2.766604242334715), (-2.9419972652276205, -2.9180760904410845), (-2.2604889520475573, -2.771120566707732), (-3.175693897602074, -3.460055554337784), (-2.5433684971811266, -2.8161256537485424), (-1.977894546783102, -2.5991697110531184), (-2.6686335771698624, -2.5280712755063277), (-1.875457957016601, -3.516545622607312), (-2.9610011299329493, -3.142973499994016), (-2.979251864316896, -2.796814901077449), (-3.3687945154452197, -3.3897338497704075), (-2.500154855924993, -3.871376727175042), (-3.0560693317525023, -2.221184044187742), (-2.1390334743659403, -2.258875537427623), (-2.449819955065217, -2.9997542016050107), (-2.7291721231969035, -3.711084618084163), (-2.2391519446469794, -2.5441982741595957), (-2.596862079719888, -2.25269234570017), (-3.638278357088031, -3.1689845654466215), (0.004399753085801067, -2.8743070440788605), (-0.2924710755126515, -2.175946683108256), (-0.08273390775956393, -2.8950136067511765), (-0.8382702576638854, -1.9660216509985646), (-0.4255418808737782, -3.5689050483011515), (0.048415207699569085, -2.122759682151594), (0.4971431221991659, -3.2098599276099846), (0.43941126814211884, -2.4092578910979436), (0.3265791069231412, -2.2322920946303704), (0.1112547935180363, -3.1245669335896866), (-0.8606496878918148, -2.6637184676093018), (-0.9715019529668008, -2.8527484809516914), (-0.7604367060827706, -3.2808743340070565), (0.034974657149854926, -3.4210432784387605), (0.21731330733397963, -2.33671036132995), (-0.20111391783011298, -2.044587731164301), (-0.4385429063129883, -2.2761428395946655), (-1.1969107673808523, -2.882048301524835), (-0.9001091442055328, -2.775033885212885), (0.043972742091792416, -3.5318373536660412), (0.022900946381385734, -2.5425218071463926), (-0.7007802469412382, -3.180281102413864), (-0.48050139050599683, -2.553640851414108), (-0.7583714131951359, -3.2467484921946603), (-0.9594684210230663, -1.8189623918087077), (-0.5563657294582026, -2.646140337498253), (-0.4367613728324675, -1.7167151796072742), (-0.08530745565692152, -2.0742004535883782), (0.6547397857348012, -3.0610199643611313), (-0.38205161295036405, -2.9082178065010105), (0.09299290645676067, -1.5707041089842448), (0.7433812353317816, -2.270710331744653), (0.08637977733697594, -1.9432464322578649), (-0.42449999129662186, -1.7021728481447838), (-0.5362267122557569, -3.364302768663483), (-1.1210161831405103, -2.6088395073498765), (0.6096531593566996, -2.8535704320583184), (-0.25153403884940956, -3.186253988057335), (-0.4763739325127164, -1.9399436809876212), (-0.7972602839191956, -3.1459137590338844), (0.03333992498575011, -1.9226890076133814), (-0.13066878731173376, -3.0633103596949853), (-0.5150088662796378, -1.7366255872783636), (0.1308435915105064, -3.4518391326868025), (-0.5346361856308841, -3.4806317663733024), (-0.04530168615461777, -2.118420743385937), (-0.4327916924852978, -3.169655909811195), (-0.30429804887341255, -2.4971594135467226), (-0.5980780402933945, -2.6269052516471905), (-0.049304892547423845, -2.9257053089562475), (0.48353441716343537, -1.825406044763286), (-0.6007300410070253, -2.825710908713471), (-0.4380695711830638, -2.735349094181333), (-1.2359361429343396, -2.488094251793616), (-0.11031292902191031, -1.9735104396119563), (-0.12629411920789074, -2.873961225598232), (0.4065378987234247, -3.19049851182754), (0.43468199102586436, -2.125898778583834), (0.04315467305931647, -2.3107371592593715), (0.24579745278265902, -2.7928677932499864), (-0.7084437037798523, -2.846905474234939), (-0.23255132210848903, -1.8560225411309346), (-0.9635970332161633, -2.7976409034884244), (-0.6463803432138521, -1.993787488262862), (-0.8157492252057711, -2.0782414754824488), (-1.0276884087880842, -3.0160750000708854), (-0.5936511791030532, -2.7944915941812516), (0.12548561999125218, -2.0574072726970587), (0.8361698179118084, -2.5015978093847004), (-0.1019696791970156, -3.3823987050576263), (-0.045224426425569286, -2.96620580570294), (-1.1901869524135336, -2.0391417897446855), (-0.561888625452597, -1.5205038204122157), (-0.5747265271841657, -1.6335077318767954), (-0.8895496395133766, -2.7001728945096244), (-1.0155471582555102, -3.0327701445946142), (-0.5274386291592847, -2.1664734098344143), (0.2324809298344847, -1.5887041554605146), (-1.1249788234985734, -2.4697030526847965), (-0.3154112651366904, -1.5292965265996108), (-1.0891901162466624, -1.902258559559097), (0.7614995427123368, -2.30240186844481), (-0.5449819100846096, -3.2529914772049686), (-1.055102982576805, -1.889046601648816), (-0.32133129493110807, -2.5098285105501126), (-1.0112193685812183, -3.147283045277507), (-1.1137396584335804, -2.0092403943427852), (-0.9023502447839854, -1.6877058389057282), (-0.9333226643970344, -2.2932893673468957), (-0.6468746767992031, -1.9777443197118985), (-0.9334127357764042, -2.208345399968746), (-0.7684656099723178, -2.144295376168691), (-0.8593600055925361, -2.138492943937187), (-0.6177221668891097, -1.9577369238507885), (-1.1539514212284525, -2.1122876900838716), (-0.7461797523128306, -1.8495120094473392), (2.552711915363294, -3.7902357660370556), (2.571707717727003, -3.775380778918627), (2.668123928166729, -3.031061503593019), (2.6981206357264975, -2.775369759511814), (2.2479093265218215, -3.464255990982925), (1.409849326137768, -2.815874187960448), (2.397520813832761, -2.3062264463921256), (1.5335078110893359, -3.0846493654358498), (1.409555501641723, -3.676392024741583), (2.9647485473460087, -2.957040477376187), (2.323183827065189, -3.998703642377043), (2.0110248769429786, -2.6004398157760753), (2.30711592144085, -3.896679977075009), (2.6159608811075232, -2.71575585644153), (2.003431719790164, -3.0049175933036594), (1.8461732351287066, -2.830254542960779), (2.507632300657231, -3.975635287926444), (1.54551937260166, -2.4419551151982803), (2.852130979487179, -3.587176962388832), (1.9160963960528077, -4.000395023708594), (2.1995600857355577, -3.2883443088938593), (2.6247014593218676, -2.4119501803909187), (2.1758797406341532, -1.901607740686406), (1.2592535560812568, -3.394018062303669), (1.6133889527112255, -3.216384094736706), (2.3082451544007934, -3.4306372559926808), (1.7787416328104264, -3.3742535717607822), (1.7216069685253164, -3.882885035581883), (1.7660528696898372, -3.9302657631087903), (2.7143697611658886, -3.0020433972495733), (1.1065122184598963, -3.140356991621038), (3.038726748847933, -2.299641714135774), (2.9397713793893265, -3.0298785373853265), (2.345770848054266, -3.275970647228452), (2.822251904676076, -3.1295298760485433), (2.613759286028392, -2.923188437876241), (1.8346530753791008, -2.3433084348613527), (1.5951735968781375, -3.8463045026968454), (2.3933059152170797, -2.35499484237092), (2.836213102530164, -3.9177776637667194), (2.649786441239347, -3.03794011260795), (2.4909888454641615, -3.5568981548329894), (3.31007570935639, -3.258687869880478), (2.3834098419317833, -2.3890253582656307), (2.433239658998894, -1.9118452170361795), (2.8481266646905787, -2.818384053396566), (2.1648698615685245, -3.697412523470312), (2.692432162531856, -3.707660372770526), (1.6944685103983121, 3.8534071060222748), (1.9441414345337993, 3.318499399097387), (1.5311617330034313, 3.9834747021939516), (1.923454454807285, 2.833801678368554), (1.4839564655938096, 3.3197320901778467), (1.4661809718809529, 3.8079007077396736), (2.3199873024731152, 3.0601150529424097), (1.9358764726015927, 2.9982008730099876), (2.1160724968131355, 4.195757585818509), (0.7163719788850282, 3.633785168828558), (1.9953719274732307, 2.8142006427813837), (2.4354429195147125, 3.2811682091335324), (2.5158765166829546, 3.2034065628853243), (0.858222667637281, 3.47559027758647), (1.452810023034084, 2.8112185462929076), (1.523439988226773, 3.886203994739457), (2.4897675930978176, 3.4648853057979205), (1.3044093353305117, 4.267335394980063), (1.9188741326900929, 4.531403839480346), (2.5936287175446266, 3.143422076372398), (1.6476140687756335, 3.4652415616762053), (1.7075068065373509, 3.772606689282383), (2.716878542364393, 3.5667242913859116), (1.7543285966445186, 3.1435947151451398), (2.004199429720414, 4.220990675255283), (2.108260130960502, 3.9728075447222935), (2.1723905274813053, 4.329402544839365), (0.7322502553371348, 3.468546291393032), (2.000172526134585, 4.666683031933276), (2.1230316927097395, 4.308785688314831), (2.7511285275073116, 3.6837851750381927), (1.1151169370247769, 3.6247354167404042), (1.5194711443121487, 2.7708162245570676), (1.8193573913200591, 3.6724963014224956), (1.986108494346412, 4.653038196925302), (1.8047069935929052, 4.6715553268117445), (1.386156157542518, 3.202708557037243), (1.3074143604647892, 4.0349367019573394), (1.1720985198239966, 3.0301624127529916), (2.6576094326626496, 3.6053349363939384), (2.392802695031547, 4.006377656985175), (1.199454263507189, 4.50776066021007), (1.55958805256733, 3.0439102945903653), (2.0371676610379086, 4.167346171880372), (0.7510910514306426, 4.009812753803303), (2.038669664849283, 2.875160382714624), (0.8716441973509055, 3.2270182270022865), (1.4622029434712092, 3.7011104347047663), (2.663169330517222, 3.7549348536198233), (1.7080404107848373, 4.220449255124093), (2.422820820951187, 4.434806037205274), (1.5431865307704704, 3.4819286543590393), (2.30858199847612, 3.847650531863686), (-3.991448476616597, 3.912677576291104), (-4.2371907239418345, 3.5939873775525353), (-4.191543349553038, 3.7717138951727467), (-4.309531975750549, 3.5851153144418535), (-4.364783146071299, 3.76482437159436), (-4.3113805421889895, 3.8556891508569735), (-3.9768709211442466, 3.5669006574017494), (-4.193009316373434, 3.9360249026539624), (-4.236184798146996, 3.8928346535529044), (-4.141049180181023, 3.927470836523367), (-4.106969694255018, 3.7303989277812497), (-4.0846227494611025, 3.4536596133815842), (-4.04971057708576, 3.792732314267524), (-3.9654007677178487, 3.7631173737132206), (-4.019249658743374, 3.78694471899543), (-3.9666140790649282, 3.525549735773894), (-4.306471815073072, 3.5743266038011137), (-3.8908261859663202, 3.593333987012933), (-4.179902105510824, 3.92561400293895), (0.3178408135415358, -2.8404751473865684), (-4.92184757771041, 0.2094565886977282), (-0.26681747884390283, 1.2646813753486956), (-2.1228774444384033, 2.4563902123901897), (2.537272698550783, 4.372800589749211), (1.6355900804017107, 2.467584218960366), (1.5141249400142422, 1.580248515903512), (0.4425469535136397, -3.430583742856941), (4.6111154335305145, 2.816220210513749), (1.681367921884707, 1.0762556357994661), (-3.329271964670153, -4.845038024018786), (-4.521294367748535, 1.4083871900612142), (2.5006994116629544, 2.5838668613603355), (3.1512035061741397, 1.9976088659534135), (3.7648205149099123, 3.2718025492680862), (-1.8258591098214758, -3.496219856434599), (1.3791938780560216, 3.069551853008809), (3.513754297991918, 4.4093734514938046), (1.7037449874572825, 4.270907769250984), (3.7222961386921334, 4.547955883109964), (-4.308631560450316, 0.734135773761599), (1.3402914351484672, -4.794157446669249), (1.0043015978556316, -1.38076433593878), (3.580584566906124, -0.16054343447175157), (-4.246643295705594, -3.710356160808288), (-4.084565372537111, -4.602182038330205), (4.9098776041939285, 4.48622473099867), (3.540323470479814, -3.5070362547436296), (4.388479740917505, -3.037047174529648), (-0.9657683240577537, 3.6270764289222743), (4.313346162389225, -0.039427716442991034), (2.9824359967043215, -0.2865221605141022), (3.7795911456571076, -4.4254407051951254), (-1.2746601251148002, 0.1364850384922054), (2.582750210547882, -0.726449500487762), (2.4862756286042416, 4.959341454603942), (3.620016792462758, 4.852399433301141), (3.9045674501490115, -0.7053068160491165), (2.4471668636904003, 2.598688074680898), (2.792582115738539, -3.8164559606610005), (1.5411551244807065, -3.480417881592338), (-4.36035555248937, 3.4171096361159083), (0.7544174330326969, -3.921952036649131), (-0.31788855879762856, -4.523984858925575), (-4.2685341477015895, -0.4274899781107582), (2.468179460414297, -2.50212688445014), (-0.09261063850134921, -4.2504074401469065), (0.40606462074155747, -0.8150092314281911), (-4.434559009152357, -0.971432988793107), (-3.716687966694577, -0.10506942304140754)]

NOISE = -1
def initcentroids(points, k):
    dim = len(points[0])
    sample_out = sample(points, k)
    return_centroids = [list(e) for e in sample_out]

    return return_centroids

def group_points_by_cluster(points: List[Tuple], cluster_indices: List[Tuple]) -> List[int]:
    """Takes a list of points and another list with their cluster_indices, groups the points by cluster_indices and
       returns the list of points.

    Args:
        points: The list of points to group.
        cluster_indices: The list of cluster indices for the points. Must reflect the order of `points`.

    Returns:
        A list of clusters, where each cluster is a list of points.
    """
    n = len(points)
    centroids = len(cluster_indices)
    dim = len(cluster_indices[0])
    indices = []
    for point in points:
        min_sum = 1000.0
        for i in range(centroids):
            euclidean_sum = 0
            for j in range(dim):
                euclidean_sum += (point[j] - cluster_indices[i][j])**2
            if(euclidean_sum < min_sum):
                index = i
                min_sum = euclidean_sum
        indices.append(index)
    return indices

def update_centroids(points: List[Tuple], labels: List[int],centroids : List[List[float]]) -> List[List[float]]:
    """Update the centroids for each cluster, by computing the center of mass for the cluster.

    Args:
        points: The list of points to group.
        labels: The list of cluster indices for the points. Must reflect the order of `points`.
        centroids : The current centroids


    Returns:
        The list of centroids for each cluster. The point at index `i` is the centroid for the `i`-th cluster.
    """
    dim = len(points[0])
    sum_centroids = [[0.0,0.0]]*len(centroids)
    len_labes = [0]*len(centroids)
    for point,label in zip(points,labels):
        for i in range(dim):
            sum_centroids[label][i] +=point[i]
        len_labes[label] += 1

    for l in range(len(len_labes)):
        if len_labes[l] > 0:
            for i in range(dim):
                centroids[l][i] = sum_centroids[l][i]/ len_labes[l]

    # clusters = __group_points_by_cluster(points, cluster_indices)
    return centroids

def k_means(points: List[Tuple], num_centroids: int, max_iter: int) -> Tuple[List[Tuple[float]], List[int]]:
    """K-means clustering method.

    Args:
        points: A list of points to cluster.
        num_centroids: The desired number of clusters.
        max_iter: The maximum number of iterations of k-mean's main cycle allowed.

    Returns:
        A list of the centroids, and a list of the indices for each point.
    """
    dim = len(points[0])
    centroids = initcentroids(points, num_centroids)
    labels = []
    for _ in range(max_iter):
        new_labels = group_points_by_cluster(points, centroids)
        #just checks for the number of clusters in each category are same
        if Counter(new_labels) == Counter(labels):
            break
        else:
            # update labels
            labels = new_labels
        centroids = update_centroids(points, labels,centroids)
    return centroids, labels

if __name__ == "__main__":

    centroids,labels = k_means(points,2,10)
    plot_clusters(points, labels)
    plt.show()