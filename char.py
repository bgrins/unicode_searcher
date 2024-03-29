
class Char():
	""" Ugly names, got them from this statement: 
		http://www.unicode.org/reports/tr42/#w1aab9b1
		
		c = self.db.cursor()
		c.execute("PRAGMA table_info(ucd)")
		for x in c.fetchall():
			print "self.%s=c[%d]" % (x[1], x[0])
	"""
	
	def __init__(self, c):
		self.sc=c[0]
		self.JSN=c[1]
		self.CWKCF=c[2]
		self.Pat_Syn=c[3]
		self.IDS=c[4]
		self.CWL=c[5]
		self.Dep=c[6]
		self.OUpper=c[7]
		self.InMC=c[8]
		self.Lower=c[9]
		self.OAlpha=c[10]
		self.GCB=c[11]
		self.lb=c[12]
		self.AHex=c[13]
		self.DI=c[14]
		self.stc=c[15]
		self.OLower=c[16]
		self.CE=c[17]
		self.XO_NFKC=c[18]
		self.LOE=c[19]
		self.tc=c[20]
		self.WSpace=c[21]
		self.XO_NFC=c[22]
		self.Bidi_M=c[23]
		self.XIDC=c[24]
		self.Radical=c[25]
		self.Alpha=c[26]
		self.dm=c[27]
		self.slc=c[28]
		self.STerm=c[29]
		self.nt=c[30]
		self.Ext=c[31]
		self.ea=c[32]
		self.XO_NFD=c[33]
		self.OMath=c[34]
		self.ODI=c[35]
		self.uc=c[36]
		self.gc=c[37]
		self.IDSB=c[38]
		self.NChar=c[39]
		self.UIdeo=c[40]
		self.Term=c[41]
		self.Hyphen=c[42]
		self.QMark=c[43]
		self.CWCM=c[44]
		self.NFC_QC=c[45]
		self.XIDS=c[46]
		self.Dia=c[47]
		self.Bidi_C=c[48]
		self.hst=c[49]
		self.InSC=c[50]
		self.WB=c[51]
		self.na=c[52]
		self.FC_NFKC=c[53]
		self.Math=c[54]
		self.scf=c[55]
		self.Pat_WS=c[56]
		self.NFKC_CF=c[57]
		self.na1=c[58]
		self.SD=c[59]
		self.Upper=c[60]
		self.CWCF=c[61]
		self.OIDC=c[62]
		self.IDST=c[63]
		self.cf=c[64]
		self.Gr_Ext=c[65]
		self.Comp_Ex=c[66]
		self.CWU=c[67]
		self.NFD_QC=c[68]
		self.CI=c[69]
		self.VS=c[70]
		self.Cased=c[71]
		self.Join_C=c[72]
		self.CWT=c[73]
		self.ccc=c[74]
		self.dt=c[75]
		self.Ideo=c[76]
		self.age=c[77]
		self.Gr_Link=c[78]
		self.OGr_Ext=c[79]
		self.isc=c[80]
		self.XO_NFKD=c[81]
		self.NFKC_QC=c[82]
		self.bc=c[83]
		self.Dash=c[84]
		self.jt=c[85]
		self.NFKD_QC=c[86]
		self.IDC=c[87]
		self.cp=c[88]
		self.nv=c[89]
		self.suc=c[90]
		self.OIDS=c[91]
		self.bmg=c[92]
		self.Gr_Base=c[93]
		self.lc=c[94]
		self.SB=c[95]
		self.Hex=c[96]
		self.jg=c[97]
		self.kCantonese=c[98]
		self.kIRGKangXi=c[99]
		self.kSemanticVariant=c[100]
		self.kIRG_TSource=c[101]
		self.kIRG_KSource=c[102]
		self.kMandarin=c[103]
		self.kIRG_KPSource=c[104]
		self.kIRG_JSource=c[105]
		self.kDefinition=c[106]
		self.kIRG_HSource=c[107]
		self.kIRG_MSource=c[108]
		self.kTotalStrokes=c[109]
		self.kIRG_USource=c[110]
		self.kIRGHanyuDaZidian=c[111]
		self.kIRG_VSource=c[112]
		self.kHanYu=c[113]
		self.kCangjie=c[114]
		self.kRSUnicode=c[115]
		self.kCompatibilityVariant=c[116]
		self.kIRG_GSource=c[117]
		self.kHanyuPinyin=c[118]
		self.kSBGY=c[119]
		self.kCihaiT=c[120]
		self.kNelson=c[121]
		self.kJIS0213=c[122]
		self.kRSAdobe_Japan1_6=c[123]
		self.kOtherNumeric=c[124]
		self.kCowles=c[125]
		self.kPhonetic=c[126]
		self.kMatthews=c[127]
		self.kGSR=c[128]
		self.kKPS1=c[129]
		self.kFennIndex=c[130]
		self.kFenn=c[131]
		self.kKarlgren=c[132]
		self.kHKSCS=c[133]
		self.kXHC1983=c[134]
		self.kMeyerWempe=c[135]
		self.kTraditionalVariant=c[136]
		self.kVietnamese=c[137]
		self.kSimplifiedVariant=c[138]
		self.kSpecializedSemanticVariant=c[139]
		self.kLau=c[140]
		self.kRSKanWa=c[141]
		self.kCheungBauerIndex=c[142]
		self.kCheungBauer=c[143]
		self.kIICore=c[144]
		self.kTang=c[145]
		self.kZVariant=c[146]
		self.kRSKangXi=c[147]
		self.kJapaneseOn=c[148]
		self.kJapaneseKun=c[149]
		self.kKangXi=c[150]
		self.kKPS0=c[151]
		self.kMorohashi=c[152]
		self.kKSC0=c[153]
		self.kIRGDaeJaweon=c[154]
		self.kGradeLevel=c[155]
		self.kPrimaryNumeric=c[156]
		self.kCNS1986=c[157]
		self.kFourCornerCode=c[158]
		self.kMainlandTelegraph=c[159]
		self.kIRGDaiKanwaZiten=c[160]
		self.kGB0=c[161]
		self.kXerox=c[162]
		self.kFrequency=c[163]
		self.kJis0=c[164]
		self.kTaiwanTelegraph=c[165]
		self.kCNS1992=c[166]
		self.kHangul=c[167]
		self.kHKGlyph=c[168]
		self.kKorean=c[169]
		self.kDaeJaweon=c[170]
		self.kEACC=c[171]
		self.kHDZRadBreak=c[172]
		self.kCCCII=c[173]
		self.kHanyuPinlu=c[174]
		self.kBigFive=c[175]
		self.kGB1=c[176]
		self.kJis1=c[177]
		self.kGB5=c[178]
		self.kPseudoGB1=c[179]
		self.kGB8=c[180]
		self.kGB3=c[181]
		self.kKSC1=c[182]
		self.kIBMJapan=c[183]
		self.kRSJapanese=c[184]
		self.kAccountingNumeric=c[185]
		self.kRSKorean=c[186]
		self.kGB7=c[187]

