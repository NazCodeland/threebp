# tsxsectors@gmail.com
# psql 'postgresql://tsxsectors:Fl0i5WKCQmZg@ep-shiny-pond-80219216.us-east-2.aws.neon.tech/neondb?sslmode=require'

# # timeframes: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
# # intervals: '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'
timeframes = ['d', 'wk', 'mo']

# Unix Timestamp date values, used for the range of historical data retrieval 
start_date = 1509744000  # corresponds to November 16, 2018
end_date = 1668748800  # corresponds to November 16, 2023

# email to receive google sheets 
email = "investingclarity@gmail.com"


exchanges = ["TSX"]

# barchart.com/ca sectors
sectors = [
	{ "symbol": "TTFS", "name": "TSX Financials Capped Index" },
	{ "symbol": "TTEN", "name": "TSX Energy Capped Index" },
	{ "symbol": "TTMT", "name": "TSX Materials Capped Index" },
	{ "symbol": "TTTK", "name": "TSX Information Tech Capped Index" },
	{ "symbol": "TTIN", "name": "TSX Industrials Capped Index" },
	{ "symbol": "TTCS", "name": "TSX Consumer Staples Capped Index" },
	{ "symbol": "TTUT", "name": "TSX Utilities Capped Index" },
	{ "symbol": "TTRE", "name": "TSX Real Estate Capped Index" },
	{ "symbol": "TTTS", "name": "TSX Communication Services Capped Index" },
	{ "symbol": "TTCD", "name": "TSX Consumer Discretionary Capped Index" },
	{ "symbol": "TTHC", "name": "TSX Health Care Capped Index" }
]

industries = [
	{ "symbol": "VHFF", "name": "TSX Home Furnishings & Fixture" },
	{ "symbol": "VEGM", "name": "TSX Electronic Gaming & Media" },
	{ "symbol": "VLOD", "name": "TSX Lodging" },
	{ "symbol": "VHPP", "name": "TSX Household & Personal Product" },
	{ "symbol": "VSEQ", "name": "TSX Semiconductor Equipment" },
	{ "symbol": "VAAS", "name": "TSX Airports & Air Services" },
	{ "symbol": "VMTF", "name": "TSX Metal Fabrication" },
	{ "symbol": "VPHR", "name": "TSX Pharmaceutical Retailers" },
	{ "symbol": "VSPS", "name": "TSX Security & Protection Srvs" },
	{ "symbol": "VSAP", "name": "TSX Software - Application" },
	{ "symbol": "VRED", "name": "TSX Real Estate - Diversified" },
	{ "symbol": "VPTC", "name": "TSX Pollution Treatment Controls" },
	{ "symbol": "VDCS", "name": "TSX Discount Stores" },
	{ "symbol": "VAAA", "name": "TSX Advertising Agencies" },
	{ "symbol": "VSTI", "name": "TSX Scientific & Technical Instr" },
	{ "symbol": "VIMM", "name": "TSX Industrial Metals Minerals" },
	{ "symbol": "VCSY", "name": "TSX Computer Systems" },
	{ "symbol": "VAPM", "name": "TSX Apparel Manufacturing" },
	{ "symbol": "VSCH", "name": "TSX Specialty Chemicals" },
	{ "symbol": "VBIO", "name": "TSX Biotechnology" },
	{ "symbol": "VCOC", "name": "TSX Coking Coal" },
	{ "symbol": "VRIS", "name": "TSX REIT - Specialty" },
	{ "symbol": "VGAM", "name": "TSX Gambling" },
	{ "symbol": "VRCA", "name": "TSX Resorts & Casinos" },
	{ "symbol": "VHIM", "name": "TSX Home Improvement Stores" },
	{ "symbol": "VPPP", "name": "TSX Paper & Paper Products" },
	{ "symbol": "VSPO", "name": "TSX Shipping & Ports" },
	{ "symbol": "VBWD", "name": "TSX Beverages - Wine & Distiller" },
	{ "symbol": "VCEQ", "name": "TSX Communication Equipment" },
	{ "symbol": "VHIS", "name": "TSX Health Information Services" },
	{ "symbol": "VDMM", "name": "TSX Drug Manufacturers - Major" },
	{ "symbol": "VSIN", "name": "TSX Software - Infrastructure" },
	{ "symbol": "VCHE", "name": "TSX Chemicals" },
	{ "symbol": "VASM", "name": "TSX Asset Management" },
	{ "symbol": "VBMT", "name": "TSX Building Materials" },
	{ "symbol": "VITS", "name": "TSX Information Technology Srvs" },
	{ "symbol": "VLUG", "name": "TSX Luxury Goods" },
	{ "symbol": "VFMP", "name": "TSX Farm Products" },
	{ "symbol": "VBPE", "name": "TSX Building Products & Equpment" },
	{ "symbol": "VCPM", "name": "TSX Capital Markets" },
	{ "symbol": "VOGR", "name": "TSX Oil & Gas Refining & Mrkt" },
	{ "symbol": "VINF", "name": "TSX Insurance - Life" },
	{ "symbol": "VITR", "name": "TSX Internet Retail" },
	{ "symbol": "VCOP", "name": "TSX Copper" },
	{ "symbol": "VBRE", "name": "TSX Banks - Regional" },
	{ "symbol": "VUDI", "name": "TSX Utilities Diversified" },
	{ "symbol": "VURE", "name": "TSX Utilities Regulated Electric" },
	{ "symbol": "VAGI", "name": "TSX Agricultural Inputs" },
	{ "symbol": "VFOA", "name": "TSX Footwear & Accessories" },
	{ "symbol": "VFCE", "name": "TSX Farm & Construction Equipt" },
	{ "symbol": "VROF", "name": "TSX REIT - Office" },
	{ "symbol": "VPUB", "name": "TSX Publishing" },
	{ "symbol": "VTRU", "name": "TSX Trucking" },
	{ "symbol": "VAAD", "name": "TSX Aerospace & Defense" },
	{ "symbol": "VPKC", "name": "TSX Packaging & Containers" },
	{ "symbol": "VOPM", "name": "TSX Other Precious Metals & Mine" },
	{ "symbol": "VGOL", "name": "TSX Gold" },
	{ "symbol": "VLWP", "name": "TSX Lumber & Wood Production" },
	{ "symbol": "VFIE", "name": "TSX Financial Exchanges" },
	{ "symbol": "VBAG", "name": "TSX Banks - Global" },
	{ "symbol": "VUTR", "name": "TSX Utilities - Renewable" },
	{ "symbol": "VIND", "name": "TSX Insurance - Diversified" },
	{ "symbol": "VCOE", "name": "TSX Consumer Electronics" },
	{ "symbol": "VHCP", "name": "TSX Health Care Plans" },
	{ "symbol": "VOGM", "name": "TSX Oil & Gas Midstream" },
	{ "symbol": "VBRO", "name": "TSX Broadcasting" },
	{ "symbol": "VRVE", "name": "TSX Recreational Vehicles" },
	{ "symbol": "VISS", "name": "TSX Insurance - Specialty" },
	{ "symbol": "VCOG", "name": "TSX Conglomerates" },
	{ "symbol": "VBSD", "name": "TSX Beverages - Soft Drinks" },
	{ "symbol": "VUIP", "name": "TSX Utilities Independent Power" },
	{ "symbol": "VRST", "name": "TSX Restaurants" },
	{ "symbol": "VAIR", "name": "TSX Airlines" },
	{ "symbol": "VRDV", "name": "TSX REIT - Diversified" },
	{ "symbol": "VRHF", "name": "TSX REIT - Healthcare Faciltes" },
	{ "symbol": "VIDD", "name": "TSX Industrial Distribution" },
	{ "symbol": "VMRF", "name": "TSX Mortgage Finance" },
	{ "symbol": "VURG", "name": "TSX Utilities Regulated Gas" },
	{ "symbol": "VTSE", "name": "TSX Telecom Services" },
	{ "symbol": "VSRE", "name": "TSX Specialty Retail" },
	{ "symbol": "VGST", "name": "TSX Grocery Stores" },
	{ "symbol": "VATD", "name": "TSX Auto & Truck Dealerships" },
	{ "symbol": "VTOB", "name": "TSX Tobacco" },
	{ "symbol": "VAMN", "name": "TSX Auto Manufacturers" },
	{ "symbol": "VTMA", "name": "TSX Textile Manufacturing" },
	{ "symbol": "VPSS", "name": "TSX Personal Services" },
	{ "symbol": "VRAI", "name": "TSX Railroads" },
	{ "symbol": "VLEI", "name": "TSX Leisure" },
	{ "symbol": "VEGC", "name": "TSX Engineering & Construction" },
	{ "symbol": "VOGI", "name": "TSX Oil & Gas Integrated" },
	{ "symbol": "VIPC", "name": "TSX Insurance - Property & Casu" },
	{ "symbol": "VMDC", "name": "TSX Medical Care" },
	{ "symbol": "VSIM", "name": "TSX Specialty Industrial Machine" },
	{ "symbol": "VRES", "name": "TSX Real Estate Services" },
	{ "symbol": "VRLS", "name": "TSX Rental & Leasing Services" },
	{ "symbol": "VDRE", "name": "TSX Diagnostics & Research" },
	{ "symbol": "VOGE", "name": "TSX Oil & Gas E&P" },
	{ "symbol": "VSIL", "name": "TSX Silver" },
	{ "symbol": "VDMS", "name": "TSX Drug Specialty & Generic" },
	{ "symbol": "VRRT", "name": "TSX REIT - Retail" },
	{ "symbol": "VMBS", "name": "TSX Business Services" },
	{ "symbol": "VOGS", "name": "TSX Oil & Gas Equipment & Srvs" },
	{ "symbol": "VINR", "name": "TSX Insurance - Reinsurance" },
	{ "symbol": "VENT", "name": "TSX Entertainment" },
	{ "symbol": "VICI", "name": "TSX Internet Content & Info" },
	{ "symbol": "VCSV", "name": "TSX Credit Services" },
	{ "symbol": "VSOL", "name": "TSX Solar" },
	{ "symbol": "VPKF", "name": "TSX Packaged Foods" },
	{ "symbol": "VISL", "name": "TSX Integrated Shipping & Logis" },
	{ "symbol": "VOGD", "name": "TSX Oil & Gas Drilling" },
	{ "symbol": "VEEP", "name": "TSX Electrical Equipment & Parts" },
	{ "symbol": "VWMA", "name": "TSX Waste Management" },
	{ "symbol": "VMIS", "name": "TSX Medical Instruments & Suppls" },
	{ "symbol": "VRIN", "name": "TSX REIT - Industrial" },
	{ "symbol": "VECO", "name": "TSX Electronic Components" },
	{ "symbol": "VREV", "name": "TSX Real Estate - Development" },
	{ "symbol": "VRRE", "name": "TSX REIT - Residential" },
	{ "symbol": "VSTL", "name": "TSX Steel" },
	{ "symbol": "VAUP", "name": "TSX Auto Parts" },
	{ "symbol": "VMDD", "name": "TSX Medical Devices" },
	{ "symbol": "VBVB", "name": "TSX Beverages - Brewers" },
	{ "symbol": "VTRS", "name": "TSX Travel Services" },
	{ "symbol": "VAPS", "name": "TSX Apparel Stores" },
	{ "symbol": "VFDD", "name": "TSX Food Distribution" },
	{ "symbol": "VTCO", "name": "TSX Thermal Coal" },
	{ "symbol": "VSEM", "name": "TSX Semiconductors" },
	{ "symbol": "VURA", "name": "TSX Uranium" },
	{ "symbol": "VCOF", "name": "TSX Confectioners" },
	{ "symbol": "VURW", "name": "TSX Utilities Regulated Water" }
]

industry_equities = [
	{
		"symbol": "DII-B.TO",
		"name": "Dorel Industries Inc Cl B Sv",
		"industry": "VHFF"
	},
	{ "symbol": "RCH.TO", "name": "Richelieu Hardware Ltd", "industry": "VHFF" },
	{ "symbol": "BRAG.TO", "name": "Bragg Gaming Group Inc", "industry": "VEGM" },
	{
		"symbol": "GET.CN",
		"name": "Gameon Entertainmnet Technologies Inc",
		"industry": "VEGM"
	},
	{
		"symbol": "TIDL.CN",
		"name": "Tiidal Gaming Group Corp",
		"industry": "VEGM"
	},
	{
		"symbol": "VST.CN",
		"name": "Victory Square Technologies Inc",
		"industry": "VEGM"
	},
	{ "symbol": "GAME.V", "name": "Gamesquare Holdings Inc", "industry": "VEGM" },
	{ "symbol": "CKI.TO", "name": "Clarke Inc", "industry": "VLOD" },
	{
		"symbol": "PG.NE",
		"name": "Procter & Gamble Cdr [Cad Hedged]",
		"industry": "VHPP"
	},
	{ "symbol": "KPT.TO", "name": "Kp Tissue Inc", "industry": "VHPP" },
	{
		"symbol": "CGII.CN",
		"name": "Cleango Innovations Inc.",
		"industry": "VHPP"
	},
	{
		"symbol": "SEV.V",
		"name": "Spectra7 Microsystems Inc",
		"industry": "VSEQ"
	},
	{ "symbol": "CHR.TO", "name": "Chorus Aviation Inc", "industry": "VAAS" },
	{ "symbol": "DRX.TO", "name": "Adf Group Inc Sv", "industry": "VMTF" },
	{ "symbol": "CYM.V", "name": "Cymat Technologies Ltd", "industry": "VMTF" },
	{ "symbol": "IVX.V", "name": "Inventronics Ltd", "industry": "VMTF" },
	{ "symbol": "HITI.V", "name": "High Tide Inc", "industry": "VPHR" },
	{ "symbol": "LOTA.CN", "name": "Delota Corp", "industry": "VPHR" },
	{
		"symbol": "NBLY.TO",
		"name": "Neighbourly Pharmacy Inc",
		"industry": "VPHR"
	},
	{ "symbol": "IWIN.CN", "name": "Irwin Naturals Inc", "industry": "VPHR" },
	{ "symbol": "GSI.V", "name": "Gatekeeper Systems Inc", "industry": "VSPS" },
	{ "symbol": "ZDC.V", "name": "Zedcor Inc", "industry": "VSPS" },
	{ "symbol": "XX.V", "name": "Avante Corp", "industry": "VSPS" },
	{
		"symbol": "SECU.V",
		"name": "Ssc Security Services Corp",
		"industry": "VSPS"
	},
	{
		"symbol": "SCAN.V",
		"name": "Liberty Defense Holdings Ltd",
		"industry": "VSPS"
	},
	{ "symbol": "THNC.TO", "name": "Thinkific Labs Inc", "industry": "VSAP" },
	{ "symbol": "UBER.NE", "name": "Uber Cdr [Cad Hedged]", "industry": "VSAP" },
	{ "symbol": "QFOR.TO", "name": "Q4 Inc", "industry": "VSAP" },
	{
		"symbol": "CRM.NE",
		"name": "Salesforce.com Cdr [Cad Hedged]",
		"industry": "VSAP"
	},
	{ "symbol": "IQ.V", "name": "Airiq Inc", "industry": "VSAP" },
	{ "symbol": "BLN.TO", "name": "Blackline Safety Corp", "industry": "VSAP" },
	{ "symbol": "SHOP.TO", "name": "Shopify Inc", "industry": "VSAP" },
	{
		"symbol": "CMG.TO",
		"name": "Computer Modelling Group Ltd",
		"industry": "VSAP"
	},
	{
		"symbol": "CSU.TO",
		"name": "Constellation Software Inc",
		"industry": "VSAP"
	},
	{
		"symbol": "URL.CN",
		"name": "Namesilo Technologies Corp",
		"industry": "VSAP"
	},
	{ "symbol": "OSS.V", "name": "Onesoft Solutions Inc", "industry": "VSAP" },
	{ "symbol": "DCBO.TO", "name": "Docebo Inc", "industry": "VSAP" },
	{ "symbol": "LMN.V", "name": "Lumine Group Inc.", "industry": "VSAP" },
	{ "symbol": "REAL.TO", "name": "Real Matters Inc", "industry": "VSAP" },
	{ "symbol": "CTZ.V", "name": "Namsys Inc", "industry": "VSAP" },
	{ "symbol": "ABXX.NE", "name": "Abaxx Technologies Inc", "industry": "VSAP" },
	{ "symbol": "OTEX.TO", "name": "Open Text Corp", "industry": "VSAP" },
	{ "symbol": "TCXT.V", "name": "Truecontext Corporation", "industry": "VSAP" },
	{ "symbol": "DTOL.TO", "name": "D2L Inc", "industry": "VSAP" },
	{
		"symbol": "LSPD.TO",
		"name": "Lightspeed Commerce Inc.",
		"industry": "VSAP"
	},
	{ "symbol": "DSG.TO", "name": "Descartes Sys", "industry": "VSAP" },
	{ "symbol": "MVP.TO", "name": "Mediavalet Inc", "industry": "VSAP" },
	{ "symbol": "TCS.TO", "name": "Tecsys Inc J", "industry": "VSAP" },
	{ "symbol": "SYZ.TO", "name": "Sylogist Ltd", "industry": "VSAP" },
	{ "symbol": "ENGH.TO", "name": "Enghouse Systems Ltd", "industry": "VSAP" },
	{ "symbol": "DND.TO", "name": "Dye & Durham Ltd", "industry": "VSAP" },
	{
		"symbol": "CDAY.TO",
		"name": "Ceridian Hcm Holdings Inc",
		"industry": "VSAP"
	},
	{
		"symbol": "INSP.V",
		"name": "Inspire Semiconductor Holdings Inc",
		"industry": "VSAP"
	},
	{ "symbol": "RSS.V", "name": "Resaas Services Inc", "industry": "VSAP" },
	{ "symbol": "RIWI.V", "name": "Riwi Corp", "industry": "VSAP" },
	{ "symbol": "KXS.TO", "name": "Kinaxis Inc", "industry": "VSAP" },
	{ "symbol": "DGHI.V", "name": "Digihost Technology Inc", "industry": "VSAP" },
	{ "symbol": "INX.V", "name": "Intouch Insight Ltd", "industry": "VSAP" },
	{
		"symbol": "INXD.NE",
		"name": "The Inx Digital Company Inc.",
		"industry": "VSAP"
	},
	{
		"symbol": "QIS.V",
		"name": "Quorum Information Technologies Inc",
		"industry": "VSAP"
	},
	{ "symbol": "MAPS.V", "name": "Prostar Holdings Inc", "industry": "VSAP" },
	{ "symbol": "LQWD.V", "name": "Lqwd Fintech Corp", "industry": "VSAP" },
	{
		"symbol": "IFSS.NE",
		"name": "Interfield Global Software Inc",
		"industry": "VSAP"
	},
	{ "symbol": "UI.V", "name": "Urbanimmersive Inc", "industry": "VSAP" },
	{ "symbol": "METG.CN", "name": "Metaguest.Ai Inc", "industry": "VSAP" },
	{
		"symbol": "WISH.V",
		"name": "Wishpond Technologies Ltd",
		"industry": "VSAP"
	},
	{ "symbol": "AXE.V", "name": "Acceleware Ltd", "industry": "VSAP" },
	{
		"symbol": "WFLD.V",
		"name": "Wellfield Technologies Inc",
		"industry": "VSAP"
	},
	{
		"symbol": "MHUB.V",
		"name": "Minehub Technologies Inc",
		"industry": "VSAP"
	},
	{ "symbol": "VXTR.V", "name": "Voxtur Analytics Corp", "industry": "VSAP" },
	{
		"symbol": "BWLK.V",
		"name": "Boardwalktech Software Corp",
		"industry": "VSAP"
	},
	{ "symbol": "ALY.V", "name": "Analytixinsight Inc", "industry": "VSAP" },
	{
		"symbol": "AICO.CN",
		"name": "Generative Ai Solutions Corp",
		"industry": "VSAP"
	},
	{
		"symbol": "PLRB.V",
		"name": "Pluribus Technologies Corp",
		"industry": "VSAP"
	},
	{ "symbol": "TWOH.CN", "name": "Two Hands Corporation", "industry": "VSAP" },
	{ "symbol": "ARWY.CN", "name": "Arway Corporation", "industry": "VSAP" },
	{
		"symbol": "VSBY.CN",
		"name": "Vsblty Groupe Technologies Corp",
		"industry": "VSAP"
	},
	{ "symbol": "UFC.V", "name": "Urbanfund Corp", "industry": "VRED" },
	{ "symbol": "MRC.TO", "name": "Morguard Corp", "industry": "VRED" },
	{ "symbol": "YEG.V", "name": "Yorkton Equity Group Inc", "industry": "VRED" },
	{
		"symbol": "TMG.V",
		"name": "Thermal Energy International Inc",
		"industry": "VPTC"
	},
	{
		"symbol": "ACT.CN",
		"name": "Aduro Clean Technologies Inc",
		"industry": "VPTC"
	},
	{ "symbol": "BRM.V", "name": "Biorem Inc", "industry": "VPTC" },
	{
		"symbol": "SHRC.CN",
		"name": "Sharc International Systems Inc",
		"industry": "VPTC"
	},
	{
		"symbol": "DST.CN",
		"name": "Dundee Sustainable Technologies Inc",
		"industry": "VPTC"
	},
	{ "symbol": "QST.V", "name": "Questor Technology Inc", "industry": "VPTC" },
	{
		"symbol": "DESG.NE",
		"name": "Devvstream Holdings Inc.",
		"industry": "VPTC"
	},
	{
		"symbol": "COST.NE",
		"name": "Costco Cdr [Cad Hedged]",
		"industry": "VDCS"
	},
	{ "symbol": "DOL.TO", "name": "Dollarama Inc", "industry": "VDCS" },
	{ "symbol": "PESO.V", "name": "Pesorama Inc", "industry": "VDCS" },
	{
		"symbol": "WMT.NE",
		"name": "Walmart Cdr (Cad Hedged)",
		"industry": "VDCS"
	},
	{ "symbol": "ILLM.TO", "name": "Acuityads Holdings Inc", "industry": "VAAA" },
	{ "symbol": "EQ.V", "name": "Eq Inc", "industry": "VAAA" },
	{ "symbol": "PNG.V", "name": "Kraken Robotics Inc", "industry": "VSTI" },
	{
		"symbol": "NSCI.V",
		"name": "Nanalysis Scientific Corp",
		"industry": "VSTI"
	},
	{ "symbol": "MSR.V", "name": "Minsud Resources Corp", "industry": "VIMM" },
	{ "symbol": "MML.CN", "name": "Moonbound Mining Ltd.", "industry": "VIMM" },
	{
		"symbol": "NCX.V",
		"name": "Northisle Copper and Gold Inc",
		"industry": "VIMM"
	},
	{
		"symbol": "ZNG.V",
		"name": "Group Eleven Resources Corp",
		"industry": "VIMM"
	},
	{ "symbol": "SHOW.CN", "name": "Showcase Minerals Inc.", "industry": "VIMM" },
	{ "symbol": "NGEX.V", "name": "Ngex Minerals Ltd", "industry": "VIMM" },
	{ "symbol": "DMX.V", "name": "District Metals Corp", "industry": "VIMM" },
	{ "symbol": "COSA.V", "name": "Cosa Resources Corp.", "industry": "VIMM" },
	{
		"symbol": "MON.V",
		"name": "Montero Mining and Exploration Ltd",
		"industry": "VIMM"
	},
	{
		"symbol": "NILI.V",
		"name": "Surge Battery Metals Inc",
		"industry": "VIMM"
	},
	{ "symbol": "ALLI.NE", "name": "Alpha Lithium Corp", "industry": "VIMM" },
	{ "symbol": "WMK.V", "name": "Whitemud Resources Inc", "industry": "VIMM" },
	{ "symbol": "CUR.V", "name": "Consolidated Uranium Inc", "industry": "VIMM" },
	{ "symbol": "PJX.V", "name": "Pjx Resources Inc", "industry": "VIMM" },
	{ "symbol": "GMA.V", "name": "Geomega Resources Inc", "industry": "VIMM" },
	{ "symbol": "FOM.TO", "name": "Foran Mining Corp", "industry": "VIMM" },
	{ "symbol": "FAR.TO", "name": "Foraco International Sa", "industry": "VIMM" },
	{
		"symbol": "VBAM.CN",
		"name": "Vital Battery Metals Inc.",
		"industry": "VIMM"
	},
	{ "symbol": "LITS.NE", "name": "Lithos Energy Ltd", "industry": "VIMM" },
	{ "symbol": "SYH.V", "name": "Skyharbour Resources Ltd", "industry": "VIMM" },
	{ "symbol": "NIO.V", "name": "Niocan Inc", "industry": "VIMM" },
	{ "symbol": "STS.V", "name": "South Star Mining Corp", "industry": "VIMM" },
	{ "symbol": "BY.CN", "name": "Beyond Minerals Inc.", "industry": "VIMM" },
	{ "symbol": "IVN.TO", "name": "Ivanhoe Mines Ltd", "industry": "VIMM" },
	{ "symbol": "TIG.V", "name": "Triumph Gold Corp", "industry": "VIMM" },
	{ "symbol": "FWZ.V", "name": "Fireweed Metals Corp", "industry": "VIMM" },
	{
		"symbol": "JUGR.V",
		"name": "Juggernaut Exploration Ltd",
		"industry": "VIMM"
	},
	{
		"symbol": "CD.V",
		"name": "Cantex Mine Development Corp",
		"industry": "VIMM"
	},
	{ "symbol": "SRG.V", "name": "Srg Graphite Inc", "industry": "VIMM" },
	{
		"symbol": "TECK-B.TO",
		"name": "Teck Resources Ltd Cl B",
		"industry": "VIMM"
	},
	{ "symbol": "REG.V", "name": "Regulus Resources Inc", "industry": "VIMM" },
	{
		"symbol": "HERC.CN",
		"name": "Hercules Resources Corp.",
		"industry": "VIMM"
	},
	{ "symbol": "GLO.TO", "name": "Global Atomic Corp", "industry": "VIMM" },
	{ "symbol": "CVV.V", "name": "Canalaska Uranium Ltd", "industry": "VIMM" },
	{ "symbol": "MUN.V", "name": "Mundoro Capital Inc", "industry": "VIMM" },
	{ "symbol": "AFM.V", "name": "Alphamin Resources Corp", "industry": "VIMM" },
	{ "symbol": "MMA.V", "name": "Midnight Sun Mining Corp", "industry": "VIMM" },
	{ "symbol": "BATX.CN", "name": "Battery X Metals Inc", "industry": "VIMM" },
	{ "symbol": "ALDE.V", "name": "Aldebaran Resources Inc", "industry": "VIMM" },
	{ "symbol": "FPC.V", "name": "Falco Resources Ltd", "industry": "VIMM" },
	{ "symbol": "ERKA.CN", "name": "Eureka Lithium Corp", "industry": "VIMM" },
	{ "symbol": "OIII.V", "name": "O3 Mining Inc", "industry": "VIMM" },
	{ "symbol": "ETG.TO", "name": "Entree Resources Ltd", "industry": "VIMM" },
	{ "symbol": "PNPN.V", "name": "Power Nickel Inc", "industry": "VIMM" },
	{ "symbol": "STUD.V", "name": "Stallion Uranium Corp", "industry": "VIMM" },
	{ "symbol": "FIL.TO", "name": "Filo Mining Corp", "industry": "VIMM" },
	{ "symbol": "AAN.V", "name": "Aton Resources Inc", "industry": "VIMM" },
	{ "symbol": "FMC.V", "name": "Forum Energy Metals Corp", "industry": "VIMM" },
	{ "symbol": "NOVR.V", "name": "Nova Royalty Corp", "industry": "VIMM" },
	{ "symbol": "DBG.V", "name": "Doubleview Gold Corp", "industry": "VIMM" },
	{ "symbol": "EVNI.V", "name": "Ev Nickel Inc", "industry": "VIMM" },
	{ "symbol": "NKG.V", "name": "Nevada King Gold Corp", "industry": "VIMM" },
	{ "symbol": "MDI.TO", "name": "Major Drilling Grp", "industry": "VIMM" },
	{ "symbol": "M.CN", "name": "Myriad Uranium Corp.", "industry": "VIMM" },
	{
		"symbol": "VOY.CN",
		"name": "Voyageur Mineral Explorers Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "PMET.V",
		"name": "Patriot Battery Metals Inc",
		"industry": "VIMM"
	},
	{ "symbol": "GLAD.V", "name": "Gladiator Metals Corp", "industry": "VIMM" },
	{ "symbol": "LLG.V", "name": "Mason Resources Inc", "industry": "VIMM" },
	{
		"symbol": "PGE.V",
		"name": "Stillwater Critical Minerals",
		"industry": "VIMM"
	},
	{ "symbol": "TDG.V", "name": "Tdg Gold Corp", "industry": "VIMM" },
	{
		"symbol": "NVLH.CN",
		"name": "Nevada Lithium Resources Inc.",
		"industry": "VIMM"
	},
	{ "symbol": "UCU.V", "name": "Ucore Rare Metals Inc", "industry": "VIMM" },
	{ "symbol": "VZLA.V", "name": "Vizsla Resources Corp", "industry": "VIMM" },
	{ "symbol": "CXC.CN", "name": "Cmx Gold & Silver Corp.", "industry": "VIMM" },
	{ "symbol": "EMX.V", "name": "Emx Royalty Corp", "industry": "VIMM" },
	{ "symbol": "DLP.V", "name": "Dlp Resources Inc", "industry": "VIMM" },
	{ "symbol": "AAG.V", "name": "Aftermath Silver Ltd", "industry": "VIMM" },
	{ "symbol": "NIM.V", "name": "Nicola Mining Inc", "industry": "VIMM" },
	{ "symbol": "ESPN.V", "name": "Hispania Resoucres Inc", "industry": "VIMM" },
	{ "symbol": "ETL.V", "name": "E3 Lithium Ltd", "industry": "VIMM" },
	{ "symbol": "BRO.V", "name": "Barksdale Resources Corp", "industry": "VIMM" },
	{ "symbol": "AKE.TO", "name": "Orocobre Limited", "industry": "VIMM" },
	{ "symbol": "ALS.TO", "name": "Altius Minerals Corp", "industry": "VIMM" },
	{ "symbol": "AGX.V", "name": "Silver X Mining Corp", "industry": "VIMM" },
	{
		"symbol": "CNRI.V",
		"name": "Canadian North Resources Inc",
		"industry": "VIMM"
	},
	{ "symbol": "RR.CN", "name": "Recharge Resources Ltd", "industry": "VIMM" },
	{ "symbol": "AZM.V", "name": "Azimut Exploration Inc", "industry": "VIMM" },
	{
		"symbol": "PNRL.V",
		"name": "Premium Nickel Resources Ltd",
		"industry": "VIMM"
	},
	{ "symbol": "FNI.CN", "name": "Fathom Nickel Inc", "industry": "VIMM" },
	{ "symbol": "GEO.TO", "name": "Geodrill Ltd", "industry": "VIMM" },
	{
		"symbol": "WRN.TO",
		"name": "Western Copper and Gold Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "OM.V",
		"name": "Osisko Metals Incorporated",
		"industry": "VIMM"
	},
	{ "symbol": "CCE.V", "name": "Commerce Resources Corp", "industry": "VIMM" },
	{ "symbol": "EMO.V", "name": "Emerita Resources Corp", "industry": "VIMM" },
	{ "symbol": "SKE.TO", "name": "Skeena Resources Ltd", "industry": "VIMM" },
	{ "symbol": "DG.V", "name": "Dixie Gold Inc", "industry": "VIMM" },
	{
		"symbol": "LBNK.V",
		"name": "Lithiumbank Resources Corp",
		"industry": "VIMM"
	},
	{ "symbol": "PRYM.TO", "name": "Prime Mining Corp", "industry": "VIMM" },
	{ "symbol": "KLD.V", "name": "Kenorland Minerals Ltd", "industry": "VIMM" },
	{ "symbol": "LITH.V", "name": "Lithium Chile Inc", "industry": "VIMM" },
	{ "symbol": "MD.V", "name": "Midland Exploration Inc", "industry": "VIMM" },
	{
		"symbol": "FLYN.V",
		"name": "Flying Nickel Mining Corp",
		"industry": "VIMM"
	},
	{ "symbol": "AJN.CN", "name": "Ajn Resources Inc", "industry": "VIMM" },
	{ "symbol": "INTR.V", "name": "Intrepid Metals Corp", "industry": "VIMM" },
	{ "symbol": "PGX.V", "name": "Prosper Gold Corp", "industry": "VIMM" },
	{
		"symbol": "SME.V",
		"name": "Sama Resources Inc Ressources Sama Inc",
		"industry": "VIMM"
	},
	{ "symbol": "NWX.V", "name": "Newport Exloration Ltd", "industry": "VIMM" },
	{ "symbol": "SMD.V", "name": "Strategic Metals Ltd", "industry": "VIMM" },
	{ "symbol": "GQC.V", "name": "Goldquest Mining Corp", "industry": "VIMM" },
	{ "symbol": "HZ.CN", "name": "Hertz Lithium Inc.", "industry": "VIMM" },
	{ "symbol": "MKR.V", "name": "Melkior Resources Inc", "industry": "VIMM" },
	{
		"symbol": "MOLY.NE",
		"name": "Greenland Resources Inc.",
		"industry": "VIMM"
	},
	{ "symbol": "PML.V", "name": "Panoro Minerals Ltd", "industry": "VIMM" },
	{ "symbol": "LTH.V", "name": "Lithium Ionic Corp", "industry": "VIMM" },
	{
		"symbol": "BULL.CN",
		"name": "Canadian Palladium Resources Inc",
		"industry": "VIMM"
	},
	{ "symbol": "HPQ.V", "name": "Hpq Silicon Inc.", "industry": "VIMM" },
	{
		"symbol": "ARS.CN",
		"name": "Ares Strategic Mining Inc",
		"industry": "VIMM"
	},
	{
		"symbol": "CNC.V",
		"name": "Canada Nickel Company Inc",
		"industry": "VIMM"
	},
	{ "symbol": "TOC.CN", "name": "Tocvan Ventures Corp", "industry": "VIMM" },
	{ "symbol": "HAR.V", "name": "Harfang Exploration Inc", "industry": "VIMM" },
	{
		"symbol": "PRR.CN",
		"name": "Prospect Ridge Resources Corp",
		"industry": "VIMM"
	},
	{ "symbol": "MKA.V", "name": "Mkango Resources Ltd", "industry": "VIMM" },
	{ "symbol": "EMM.V", "name": "Giyani Metals Corp", "industry": "VIMM" },
	{ "symbol": "DEC.V", "name": "Decade Resources Ltd", "industry": "VIMM" },
	{ "symbol": "NKL.V", "name": "Conic Metals Corp", "industry": "VIMM" },
	{ "symbol": "QTWO.V", "name": "Q2 Metals Corp", "industry": "VIMM" },
	{ "symbol": "CVW.V", "name": "Cvw Cleantech Inc", "industry": "VIMM" },
	{
		"symbol": "SDCU.V",
		"name": "Sonoran Desert Copper Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "FOX.CN",
		"name": "Fox River Resources Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "BMR.V",
		"name": "Battery Mineral Resources Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "STGX.CN",
		"name": "Strategx Elements Corp.",
		"industry": "VIMM"
	},
	{ "symbol": "ULTH.CN", "name": "United Lithium Corp", "industry": "VIMM" },
	{
		"symbol": "LEXI.V",
		"name": "Lithium Energi Exploration Inc",
		"industry": "VIMM"
	},
	{
		"symbol": "HUNT.CN",
		"name": "Gold Hunter Resources Inc",
		"industry": "VIMM"
	},
	{ "symbol": "TWR.V", "name": "Tower Resources Ltd", "industry": "VIMM" },
	{ "symbol": "PWM.V", "name": "Power Metals Corp", "industry": "VIMM" },
	{ "symbol": "SGML.V", "name": "Sigma Lithium Corp", "industry": "VIMM" },
	{ "symbol": "CC.CN", "name": "Core Assets Corp", "industry": "VIMM" },
	{ "symbol": "RMR.V", "name": "Rome Resources Ltd", "industry": "VIMM" },
	{ "symbol": "CPAU.V", "name": "Copaur Minerals Inc", "industry": "VIMM" },
	{
		"symbol": "CPS.V",
		"name": "Canadian Premium Sand Inc",
		"industry": "VIMM"
	},
	{ "symbol": "NOAL.V", "name": "Noa Lithium Brines Inc", "industry": "VIMM" },
	{
		"symbol": "BKM.V",
		"name": "Pacific Booker Minerals Inc",
		"industry": "VIMM"
	},
	{
		"symbol": "LEM.V",
		"name": "Leading Edge Materials Corp",
		"industry": "VIMM"
	},
	{ "symbol": "CUSN.V", "name": "Cornish Metals Inc", "industry": "VIMM" },
	{ "symbol": "NWST.V", "name": "Northwest Copper Corp", "industry": "VIMM" },
	{ "symbol": "MAXX.CN", "name": "Max Power Mining Corp", "industry": "VIMM" },
	{ "symbol": "NRM.V", "name": "Noram Lithium Corp", "industry": "VIMM" },
	{ "symbol": "MMS.V", "name": "Macarthur Minerals Ltd", "industry": "VIMM" },
	{ "symbol": "LIM.CN", "name": "Li-Metal Corp.", "industry": "VIMM" },
	{ "symbol": "GIGA.V", "name": "Giga Metals Corp", "industry": "VIMM" },
	{
		"symbol": "LIT.V",
		"name": "Argentina Lithium and Energy Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "ECOR.TO",
		"name": "Anglo Pacific Group Plc",
		"industry": "VIMM"
	},
	{ "symbol": "BEX.V", "name": "Benton Resources Inc", "industry": "VIMM" },
	{ "symbol": "TAU.V", "name": "Thesis Gold Holdings Inc", "industry": "VIMM" },
	{ "symbol": "GPH.V", "name": "Graphite One Inc", "industry": "VIMM" },
	{ "symbol": "PEGA.V", "name": "Pegasus Resources Inc", "industry": "VIMM" },
	{ "symbol": "NVLI.CN", "name": "Nova Lithium Corp.", "industry": "VIMM" },
	{
		"symbol": "PNRG.CN",
		"name": "Pan American Energy Corp",
		"industry": "VIMM"
	},
	{ "symbol": "ELEC.V", "name": "Electric Royalties Ltd", "industry": "VIMM" },
	{ "symbol": "LRA.V", "name": "Lara Exploration Ltd", "industry": "VIMM" },
	{ "symbol": "CDB.V", "name": "Cordoba Minerals Corp", "industry": "VIMM" },
	{
		"symbol": "WHY.V",
		"name": "West High Yield Resources Ltd",
		"industry": "VIMM"
	},
	{ "symbol": "CNX.V", "name": "Callinex Mines Inc", "industry": "VIMM" },
	{
		"symbol": "EPL.V",
		"name": "Eagle Plains Resources Ltd",
		"industry": "VIMM"
	},
	{ "symbol": "LUCA.V", "name": "Luca Mining Corp", "industry": "VIMM" },
	{ "symbol": "BOLT.CN", "name": "Bolt Metals Corp", "industry": "VIMM" },
	{ "symbol": "DEFN.V", "name": "Defense Metals Corp", "industry": "VIMM" },
	{ "symbol": "FPX.V", "name": "Fpx Nickel Corp", "industry": "VIMM" },
	{ "symbol": "TN.CN", "name": "Tartisan Nickel Corp", "industry": "VIMM" },
	{
		"symbol": "LIS.V",
		"name": "Lithium South Development Corp",
		"industry": "VIMM"
	},
	{ "symbol": "VRTX.CN", "name": "Vortex Energy Corp.", "industry": "VIMM" },
	{
		"symbol": "SLV.CN",
		"name": "Silver Dollar Resources Inc",
		"industry": "VIMM"
	},
	{ "symbol": "EDM.V", "name": "Edm Resources Inc", "industry": "VIMM" },
	{ "symbol": "SRS.CN", "name": "Sorrento Resources Ltd.", "industry": "VIMM" },
	{
		"symbol": "FCLI.V",
		"name": "Full Circle Lithium Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "FIN.V",
		"name": "European Energy Metals Corp",
		"industry": "VIMM"
	},
	{ "symbol": "RCK.V", "name": "Rock Tech Lithium Inc", "industry": "VIMM" },
	{ "symbol": "VLT.V", "name": "Volt Lithium Corp", "industry": "VIMM" },
	{ "symbol": "APN.V", "name": "Altiplano Minerals Ltd", "industry": "VIMM" },
	{
		"symbol": "LIRC.TO",
		"name": "Lithium Royalty Corp WI",
		"industry": "VIMM"
	},
	{ "symbol": "ATOM.V", "name": "Atomic Minerals Corp", "industry": "VIMM" },
	{ "symbol": "UUSA.CN", "name": "Kraken Energy Corp", "industry": "VIMM" },
	{
		"symbol": "NOU.V",
		"name": "Nouveau Monde Graphite Inc",
		"industry": "VIMM"
	},
	{ "symbol": "MLP.V", "name": "Millennial Potash Corp", "industry": "VIMM" },
	{ "symbol": "AMC.TO", "name": "Arizona Metals Corp", "industry": "VIMM" },
	{
		"symbol": "SCZ.V",
		"name": "Santacruz Silver Mining Ltd",
		"industry": "VIMM"
	},
	{ "symbol": "TMAS.CN", "name": "Temas Resources Corp", "industry": "VIMM" },
	{ "symbol": "BZ.V", "name": "Benz Mining Corp", "industry": "VIMM" },
	{ "symbol": "STU.V", "name": "Stuhini Exploration Ltd", "industry": "VIMM" },
	{ "symbol": "AZT.V", "name": "Aztec Minerals Corp", "industry": "VIMM" },
	{ "symbol": "NICU.V", "name": "Magna Mining Inc", "industry": "VIMM" },
	{ "symbol": "HAN.V", "name": "Hannan Metals Ltd", "industry": "VIMM" },
	{ "symbol": "SLI.V", "name": "Standard Lithium Ltd", "industry": "VIMM" },
	{ "symbol": "WML.V", "name": "Wealth Minerals Ltd", "industry": "VIMM" },
	{ "symbol": "XRI.CN", "name": "Xcite Resources Inc.", "industry": "VIMM" },
	{ "symbol": "STE.V", "name": "Starr Peak Mining Ltd", "industry": "VIMM" },
	{ "symbol": "CDN.CN", "name": "Caelan Capital Corp", "industry": "VIMM" },
	{ "symbol": "DAN.V", "name": "Arianne Phosphate Inc", "industry": "VIMM" },
	{
		"symbol": "PLAN.V",
		"name": "Progressive Planet Solutions Inc",
		"industry": "VIMM"
	},
	{ "symbol": "EMNT.V", "name": "Eminent Gold Corp", "industry": "VIMM" },
	{ "symbol": "LR.V", "name": "Luminex Resources Corp", "industry": "VIMM" },
	{ "symbol": "ATY.V", "name": "Atico Mining Corp", "industry": "VIMM" },
	{ "symbol": "PHOS.CN", "name": "First Phosphate Corp.", "industry": "VIMM" },
	{
		"symbol": "AMPS.CN",
		"name": "American Future Fuel Corp",
		"industry": "VIMM"
	},
	{ "symbol": "GEL.V", "name": "Graphano Energy Ltd", "industry": "VIMM" },
	{
		"symbol": "USCM.CN",
		"name": "US Critical Metals Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "CCC.CN",
		"name": "Carlyle Commodities Corp",
		"industry": "VIMM"
	},
	{ "symbol": "LCE.V", "name": "Century Lithium Corp", "industry": "VIMM" },
	{
		"symbol": "GDIG.CN",
		"name": "Gold Digger Resources Inc.",
		"industry": "VIMM"
	},
	{ "symbol": "ADZN.V", "name": "Adventus Mining Corp", "industry": "VIMM" },
	{ "symbol": "ION.V", "name": "ION Energy Ltd", "industry": "VIMM" },
	{ "symbol": "LI.V", "name": "American Lithium Corp", "industry": "VIMM" },
	{ "symbol": "KC.V", "name": "Kutcho Copper Corp", "industry": "VIMM" },
	{ "symbol": "GRAT.V", "name": "Gratomic Inc", "industry": "VIMM" },
	{ "symbol": "PE.V", "name": "Pure Energy Minerals Ltd", "industry": "VIMM" },
	{ "symbol": "TRAC.CN", "name": "Traction Uranium Corp", "industry": "VIMM" },
	{ "symbol": "VUL.V", "name": "Vulcan Minerals Inc", "industry": "VIMM" },
	{ "symbol": "LIFT.V", "name": "Li-Ft Power Ltd.", "industry": "VIMM" },
	{
		"symbol": "NEXT.TO",
		"name": "Nextsource Materials Inc",
		"industry": "VIMM"
	},
	{ "symbol": "SRA.V", "name": "Stria Lithium Inc", "industry": "VIMM" },
	{ "symbol": "UDI.CN", "name": "Umdoni Exploration Inc.", "industry": "VIMM" },
	{
		"symbol": "QREE.CN",
		"name": "Quebec Rare Earth Elements Corp",
		"industry": "VIMM"
	},
	{ "symbol": "ABR.V", "name": "Arbor Metals Corp", "industry": "VIMM" },
	{ "symbol": "REX.V", "name": "Orex Minerals Inc", "industry": "VIMM" },
	{ "symbol": "FMS.V", "name": "Focus Graphite Inc", "industry": "VIMM" },
	{ "symbol": "OCO.V", "name": "Oroco Resource Corp", "industry": "VIMM" },
	{ "symbol": "PGZ.V", "name": "Pan Global Resources Inc", "industry": "VIMM" },
	{
		"symbol": "AMY.V",
		"name": "Recylico Battery Materials Inc",
		"industry": "VIMM"
	},
	{ "symbol": "PRIZ.CN", "name": "Prismo Metals Inc", "industry": "VIMM" },
	{ "symbol": "ESK.V", "name": "Eskay Mining Corp", "industry": "VIMM" },
	{
		"symbol": "TCEC.CN",
		"name": "Tisdale Clean Energy Corp",
		"industry": "VIMM"
	},
	{ "symbol": "NGC.V", "name": "Northern Graphite Corp", "industry": "VIMM" },
	{
		"symbol": "RFLX.CN",
		"name": "Reflex Advanced Materials Corp.",
		"industry": "VIMM"
	},
	{ "symbol": "TORQ.V", "name": "Torq Resources Inc", "industry": "VIMM" },
	{ "symbol": "IMCX.CN", "name": "Interra Copper Corp", "industry": "VIMM" },
	{ "symbol": "NB.TO", "name": "Niocorp Developments Ltd", "industry": "VIMM" },
	{ "symbol": "LGO.TO", "name": "Largo Resources Ltd", "industry": "VIMM" },
	{
		"symbol": "SX.CN",
		"name": "St-Georges Eco-Mining Corp",
		"industry": "VIMM"
	},
	{ "symbol": "SALT.V", "name": "Atlas Salt Inc", "industry": "VIMM" },
	{ "symbol": "JZR.V", "name": "Jzr Gold Inc", "industry": "VIMM" },
	{
		"symbol": "IBAT.CN",
		"name": "International Battery Metals Ltd",
		"industry": "VIMM"
	},
	{ "symbol": "LAC.TO", "name": "Lithium Americas Corp", "industry": "VIMM" },
	{
		"symbol": "CRE.V",
		"name": "Critical Elements Lithium Corp",
		"industry": "VIMM"
	},
	{ "symbol": "FL.V", "name": "Frontier Lithium Inc", "industry": "VIMM" },
	{
		"symbol": "EBR.CN",
		"name": "Eagle Bay Resources Corp.",
		"industry": "VIMM"
	},
	{
		"symbol": "EDDY.V",
		"name": "Edison Battery Metals Corp",
		"industry": "VIMM"
	},
	{
		"symbol": "TCO.V",
		"name": "Transatlantic Mining Corp",
		"industry": "VIMM"
	},
	{ "symbol": "EMN.V", "name": "Euro Manganese Inc", "industry": "VIMM" },
	{ "symbol": "FE.CN", "name": "Fe Battery Metals Corp", "industry": "VIMM" },
	{
		"symbol": "QBAT.CN",
		"name": "Quantum Battery Metals Corp",
		"industry": "VIMM"
	},
	{ "symbol": "HECO.CN", "name": "Global Helium Corp", "industry": "VIMM" },
	{ "symbol": "SAGE.V", "name": "Sage Potash Corp", "industry": "VIMM" },
	{ "symbol": "AWLI.CN", "name": "Ameriwest Lithium Inc", "industry": "VIMM" },
	{ "symbol": "WEST.CN", "name": "West Mining Corp", "industry": "VIMM" },
	{
		"symbol": "MEGA.CN",
		"name": "Megawatt Lithium & Battery Metals Corp",
		"industry": "VIMM"
	},
	{ "symbol": "POWR.CN", "name": "Powr Lithium Corp", "industry": "VIMM" },
	{ "symbol": "PM.CN", "name": "Pampa Metals Corp", "industry": "VIMM" },
	{
		"symbol": "ELBM.V",
		"name": "Electra Battery Metals Corp",
		"industry": "VIMM"
	},
	{ "symbol": "EPR.CN", "name": "E-Power Resources Inc.", "industry": "VIMM" },
	{ "symbol": "ALCU.CN", "name": "Alpha Copper Corp", "industry": "VIMM" },
	{ "symbol": "TEX.CN", "name": "Targa Exploration Corp.", "industry": "VIMM" },
	{ "symbol": "VRAI.CN", "name": "Xr Immersive Tech Inc", "industry": "VCSY" },
	{
		"symbol": "UAV.CN",
		"name": "Global Uav Technologies Ltd",
		"industry": "VCSY"
	},
	{
		"symbol": "FLT.V",
		"name": "Drone Delivery Canada Corp",
		"industry": "VCSY"
	},
	{ "symbol": "RDRS.CN", "name": "Rdars Inc.", "industry": "VCSY" },
	{ "symbol": "IFA.TO", "name": "Ifabric Corp", "industry": "VAPM" },
	{ "symbol": "GIL.TO", "name": "Gildan Activewear Inc", "industry": "VAPM" },
	{ "symbol": "UNI.TO", "name": "Unisync Corp Class B", "industry": "VAPM" },
	{
		"symbol": "GOOS.TO",
		"name": "Canada Goose Holdings Inc",
		"industry": "VAPM"
	},
	{
		"symbol": "CNO.V",
		"name": "California Nanotechnologies Corp",
		"industry": "VSCH"
	},
	{ "symbol": "VNP.TO", "name": "5N Plus Inc", "industry": "VSCH" },
	{ "symbol": "ECO.TO", "name": "Ecosynthetix Inc", "industry": "VSCH" },
	{
		"symbol": "NANO.TO",
		"name": "Nano One Materials Corp",
		"industry": "VSCH"
	},
	{
		"symbol": "NEO.TO",
		"name": "NEO Performance Materials Inc",
		"industry": "VSCH"
	},
	{
		"symbol": "HG.CN",
		"name": "Hydrograph Clean Power Inc",
		"industry": "VSCH"
	},
	{ "symbol": "BOS.TO", "name": "Airboss America J", "industry": "VSCH" },
	{
		"symbol": "GMG.V",
		"name": "Graphene Manufacturing Group Ltd",
		"industry": "VSCH"
	},
	{
		"symbol": "FNDX.CN",
		"name": "Fendx Technologies Inc.",
		"industry": "VSCH"
	},
	{ "symbol": "GGG.V", "name": "G6 Materials Corp", "industry": "VSCH" },
	{ "symbol": "IBT.V", "name": "Ibex Technologies Inc", "industry": "VBIO" },
	{
		"symbol": "TTI.V",
		"name": "Thiogenesis Therapeutics Corp",
		"industry": "VBIO"
	},
	{
		"symbol": "EPRX.TO",
		"name": "Eupraxia Pharmaceuticals Inc",
		"industry": "VBIO"
	},
	{ "symbol": "MIR.V", "name": "Medmira Inc", "industry": "VBIO" },
	{
		"symbol": "FRX.TO",
		"name": "Fennec Pharmaceuticals Inc",
		"industry": "VBIO"
	},
	{ "symbol": "MSCL.V", "name": "Satellos Bioscience Inc", "industry": "VBIO" },
	{
		"symbol": "MDMA.CN",
		"name": "Pharmala Biotech Holdings Inc.",
		"industry": "VBIO"
	},
	{ "symbol": "MMED.NE", "name": "Mind Medicine Inc", "industry": "VBIO" },
	{ "symbol": "ACOG.CN", "name": "Alpha Cognition Inc", "industry": "VBIO" },
	{
		"symbol": "GLAB.CN",
		"name": "Gemina Laboratories Ltd",
		"industry": "VBIO"
	},
	{ "symbol": "NGEN.V", "name": "Nervgen Pharma Corp", "industry": "VBIO" },
	{ "symbol": "PHRM.CN", "name": "Pharmather Hldgs Ltd", "industry": "VBIO" },
	{
		"symbol": "TELI.CN",
		"name": "Telescope Innovations Corp.",
		"industry": "VBIO"
	},
	{
		"symbol": "DTC.CN",
		"name": "Defence Therapeutics Inc",
		"industry": "VBIO"
	},
	{ "symbol": "SBM.V", "name": "Sirona Biochem Corp", "industry": "VBIO" },
	{ "symbol": "CYBN.NE", "name": "Cybin Inc", "industry": "VBIO" },
	{
		"symbol": "DOSE.CN",
		"name": "Rapid Dose Therapeutics Corp.",
		"industry": "VBIO"
	},
	{
		"symbol": "BCT.TO",
		"name": "Briacell Therapeutics Corp",
		"industry": "VBIO"
	},
	{ "symbol": "ONC.TO", "name": "Oncolytics Bio", "industry": "VBIO" },
	{ "symbol": "COOL.CN", "name": "Core One Labs Inc", "industry": "VBIO" },
	{ "symbol": "AEZS.TO", "name": "Aeterna Zentaris Inc", "industry": "VBIO" },
	{ "symbol": "ARCH.V", "name": "Arch Biopartners Inc", "industry": "VBIO" },
	{ "symbol": "XRTX.V", "name": "Xortx Therapeutics Inc", "industry": "VBIO" },
	{ "symbol": "COV.V", "name": "Covalon Technologies Ltd", "industry": "VBIO" },
	{ "symbol": "BMND.NE", "name": "Biomind Labs Inc", "industry": "VBIO" },
	{
		"symbol": "DRUG.CN",
		"name": "Bright Minds Biosciences Inc",
		"industry": "VBIO"
	},
	{ "symbol": "CZO.V", "name": "Ceapro Inc", "industry": "VBIO" },
	{
		"symbol": "AWKN.NE",
		"name": "Awakn Life Sciences Corp",
		"industry": "VBIO"
	},
	{
		"symbol": "ASEP.CN",
		"name": "Asep Medical Holdings Inc.",
		"industry": "VBIO"
	},
	{ "symbol": "TH.TO", "name": "Theratechnologies", "industry": "VBIO" },
	{ "symbol": "APS.TO", "name": "Aptose Biosciences Inc", "industry": "VBIO" },
	{ "symbol": "CMND.CN", "name": "Clearmind Medicine Inc", "industry": "VBIO" },
	{ "symbol": "CSO.V", "name": "Corsa Coal Corp", "industry": "VCOC" },
	{
		"symbol": "CAD.V",
		"name": "Colonial Coal International Corp",
		"industry": "VCOC"
	},
	{
		"symbol": "APR-UN.TO",
		"name": "Automotive Properties REIT",
		"industry": "VRIS"
	},
	{ "symbol": "PBL.TO", "name": "Pollard Banknote Ltd", "industry": "VGAM" },
	{ "symbol": "PMKR.V", "name": "Playmaker Capital Inc", "industry": "VGAM" },
	{ "symbol": "RVLY.V", "name": "Rivalry Corp", "industry": "VGAM" },
	{ "symbol": "GH.TO", "name": "Gamehost Inc", "industry": "VRCA" },
	{
		"symbol": "HD.NE",
		"name": "Home Depot Cdr (Cad Hedged)",
		"industry": "VHIM"
	},
	{
		"symbol": "WBE.V",
		"name": "Westbond Enterprises Corp",
		"industry": "VPPP"
	},
	{
		"symbol": "CFX.TO",
		"name": "Canfor Pulp Products Inc",
		"industry": "VPPP"
	},
	{ "symbol": "LGT-B.TO", "name": "Logistec Corp Cl B Sv", "industry": "VSPO" },
	{
		"symbol": "WTE.TO",
		"name": "Westshore Terminals Investment Corp",
		"industry": "VSPO"
	},
	{ "symbol": "ALC.TO", "name": "Algoma Central", "industry": "VSPO" },
	{
		"symbol": "DWS.V",
		"name": "Diamond Estates Wines and Spirits Inc",
		"industry": "VBWD"
	},
	{ "symbol": "TTZ.V", "name": "Total Telcom Inc", "industry": "VCEQ" },
	{ "symbol": "QTRH.TO", "name": "Quarterhill Inc", "industry": "VCEQ" },
	{ "symbol": "BEW.V", "name": "Bewhere Holdings Inc", "industry": "VCEQ" },
	{ "symbol": "ET.TO", "name": "Evertz Technologies Ltd", "industry": "VCEQ" },
	{ "symbol": "TSAT.TO", "name": "Telesat Corp", "industry": "VCEQ" },
	{ "symbol": "CSCO.NE", "name": "Cisco Cdr [Cad Hedged]", "industry": "VCEQ" },
	{ "symbol": "VCM.TO", "name": "Vecima Networks Inc", "industry": "VCEQ" },
	{
		"symbol": "CMI.V",
		"name": "C-COM Satellite Systems Inc",
		"industry": "VCEQ"
	},
	{
		"symbol": "MMAX.CN",
		"name": "Metamaterial Exchangeco Inc",
		"industry": "VCEQ"
	},
	{ "symbol": "NUR.CN", "name": "Nuran Wireless Inc", "industry": "VCEQ" },
	{ "symbol": "TRUE.CN", "name": "Treatment.com Ai Inc", "industry": "VHIS" },
	{ "symbol": "VHI.TO", "name": "Vitalhub Corp", "industry": "VHIS" },
	{ "symbol": "ADK.V", "name": "Diagnos Inc", "industry": "VHIS" },
	{ "symbol": "KSI.TO", "name": "Kneat.com Inc", "industry": "VHIS" },
	{ "symbol": "CDX.V", "name": "Cloud Dx Inc", "industry": "VHIS" },
	{ "symbol": "AIAI.CN", "name": "Netramark Holdings Inc", "industry": "VHIS" },
	{
		"symbol": "NURS.V",
		"name": "Hydreight Technologies Inc",
		"industry": "VHIS"
	},
	{
		"symbol": "RHT.V",
		"name": "Reliq Health Technologies Inc",
		"industry": "VHIS"
	},
	{ "symbol": "THNK.V", "name": "Think Research Corp", "industry": "VHIS" },
	{ "symbol": "UDOC.CN", "name": "Unidoc Health Corp.", "industry": "VHIS" },
	{
		"symbol": "TMED.CN",
		"name": "Egf Theramed Health Corp",
		"industry": "VHIS"
	},
	{ "symbol": "XYBN.V", "name": "Xybion Digital Inc", "industry": "VHIS" },
	{ "symbol": "NDAT.CN", "name": "Ndatalyze Corp", "industry": "VHIS" },
	{
		"symbol": "ABBV.NE",
		"name": "Abbvie Cdr [Cad Hedged]",
		"industry": "VDMM"
	},
	{ "symbol": "PFE.NE", "name": "Pfizer Cdr [Cad Hedged]", "industry": "VDMM" },
	{
		"symbol": "MSFT.NE",
		"name": "Microsoft Canadian Depositary Receipts [Cad Hedg",
		"industry": "VSIN"
	},
	{ "symbol": "NVEI.TO", "name": "Nuvei Corp", "industry": "VSIN" },
	{ "symbol": "TOI.V", "name": "Topicus.com Inc", "industry": "VSIN" },
	{ "symbol": "CVO.TO", "name": "Coveo Solutions Inc", "industry": "VSIN" },
	{
		"symbol": "CPLF.TO",
		"name": "Copperleaf Technologies Inc",
		"industry": "VSIN"
	},
	{ "symbol": "MDF.TO", "name": "Mdf Commerce Inc", "industry": "VSIN" },
	{ "symbol": "HAI.TO", "name": "Haivision Systems Inc", "industry": "VSIN" },
	{ "symbol": "MOGO.TO", "name": "Mogo Inc", "industry": "VSIN" },
	{ "symbol": "PAY.TO", "name": "Payfare Inc", "industry": "VSIN" },
	{ "symbol": "BB.TO", "name": "Blackberry Ltd", "industry": "VSIN" },
	{ "symbol": "SCPE.CN", "name": "Scope Carbon Corp.", "industry": "VSIN" },
	{ "symbol": "TC.TO", "name": "Tucows Inc", "industry": "VSIN" },
	{
		"symbol": "VERS.NE",
		"name": "Verses Technologies Inc",
		"industry": "VSIN"
	},
	{
		"symbol": "STC.TO",
		"name": "Sangoma Technologies Corp",
		"industry": "VSIN"
	},
	{
		"symbol": "PLUG.CN",
		"name": "Energy Plug Technologies Corp",
		"industry": "VSIN"
	},
	{ "symbol": "NOW.V", "name": "Nowvertical Group Inc", "industry": "VSIN" },
	{ "symbol": "BTQ.NE", "name": "Btq Technologies Corp", "industry": "VSIN" },
	{ "symbol": "MIM.V", "name": "Mimedia Holdings Inc", "industry": "VSIN" },
	{
		"symbol": "CTRL.V",
		"name": "Edge Total Intelligence Inc",
		"industry": "VSIN"
	},
	{
		"symbol": "BYND.CN",
		"name": "Bynd Cannasoft Enterprises Inc",
		"industry": "VSIN"
	},
	{
		"symbol": "RAIL.CN",
		"name": "Railtown Ai Technologies Inc",
		"industry": "VSIN"
	},
	{
		"symbol": "TIXT.TO",
		"name": "Telus International [Cda] Inc",
		"industry": "VSIN"
	},
	{
		"symbol": "NFTX.NE",
		"name": "Looking Glass Labs Ltd.",
		"industry": "VSIN"
	},
	{
		"symbol": "BVCI.CN",
		"name": "Blockchain Venture Capital Inc.",
		"industry": "VSIN"
	},
	{ "symbol": "CLIP.V", "name": "Clip Money Inc", "industry": "VSIN" },
	{ "symbol": "FOBI.V", "name": "Fobi Ai Inc", "industry": "VSIN" },
	{ "symbol": "PKK.CN", "name": "Peak Fintech Group Inc", "industry": "VSIN" },
	{ "symbol": "NBVA.V", "name": "Nubeva Technologies Ltd", "industry": "VSIN" },
	{
		"symbol": "CYBT.CN",
		"name": "Cybeats Technologies Corp.",
		"industry": "VSIN"
	},
	{ "symbol": "MX.TO", "name": "Methanex Corp", "industry": "VCHE" },
	{
		"symbol": "CHE-UN.TO",
		"name": "Chemtrade Logistics Income Fund",
		"industry": "VCHE"
	},
	{ "symbol": "GRA.TO", "name": "Nanoxplore Inc", "industry": "VCHE" },
	{ "symbol": "FAT.CN", "name": "Far Resources Ltd", "industry": "VCHE" },
	{ "symbol": "ETHC.NE", "name": "Ether Capital Corp", "industry": "VASM" },
	{
		"symbol": "MBAI.CN",
		"name": "Medbright Ai Investments Inc",
		"industry": "VASM"
	},
	{
		"symbol": "LFE.TO",
		"name": "Canadian Life Companies Split Corp",
		"industry": "VASM"
	},
	{ "symbol": "WED.V", "name": "The Westaim Corp", "industry": "VASM" },
	{ "symbol": "ONEX.TO", "name": "Onex Corp", "industry": "VASM" },
	{
		"symbol": "LCS.TO",
		"name": "Brompton Lifeco Split Corp Class A",
		"industry": "VASM"
	},
	{
		"symbol": "OLY.TO",
		"name": "Olympia Financial Group Inc",
		"industry": "VASM"
	},
	{
		"symbol": "AIVC.V",
		"name": "Ai Artificial Intelligence Ventures Inc",
		"industry": "VASM"
	},
	{
		"symbol": "BAM.TO",
		"name": "Brookfield Asset Management Ltd",
		"industry": "VASM"
	},
	{
		"symbol": "STCK.TO",
		"name": "Stack Capital Group Inc",
		"industry": "VASM"
	},
	{ "symbol": "BN.TO", "name": "Brookfield Corporation", "industry": "VASM" },
	{
		"symbol": "BBUC.TO",
		"name": "Brookfield Business Corporation",
		"industry": "VASM"
	},
	{
		"symbol": "FIH-U.TO",
		"name": "Fairfax India Holdings Corp USD",
		"industry": "VASM"
	},
	{ "symbol": "URB.TO", "name": "Urbana Corp", "industry": "VASM" },
	{
		"symbol": "WI.V",
		"name": "The Western Investment CO of Cda Ltd",
		"industry": "VASM"
	},
	{ "symbol": "GCG.TO", "name": "Guardian Capital", "industry": "VASM" },
	{ "symbol": "UNC.TO", "name": "United Corp Ltd", "industry": "VASM" },
	{
		"symbol": "PHYS-U.TO",
		"name": "Sprott Physical Gold Trust USD",
		"industry": "VASM"
	},
	{ "symbol": "IDK.CN", "name": "Threed Capital Inc", "industry": "VASM" },
	{
		"symbol": "AGF-B.TO",
		"name": "AGF Management Ltd Cl B NV",
		"industry": "VASM"
	},
	{
		"symbol": "PHYS.TO",
		"name": "Sprott Physical Gold Trust CAD",
		"industry": "VASM"
	},
	{ "symbol": "CIX.TO", "name": "CI Financial Corp", "industry": "VASM" },
	{ "symbol": "CYB.TO", "name": "Cymbria Corp Cl A", "industry": "VASM" },
	{
		"symbol": "CEF.TO",
		"name": "Sprott Physical Gold Silver Trust",
		"industry": "VASM"
	},
	{
		"symbol": "CEF-U.TO",
		"name": "Central Fund of Canada Ltd Cl U NV",
		"industry": "VASM"
	},
	{ "symbol": "CGI.TO", "name": "CDN General Inv", "industry": "VASM" },
	{
		"symbol": "FAP.TO",
		"name": "Aberdeen Asia-Pacific Income Invest Ltd",
		"industry": "VASM"
	},
	{
		"symbol": "AD-UN.TO",
		"name": "Alaris Equity Partners Income Trust",
		"industry": "VASM"
	},
	{
		"symbol": "PSLV-U.TO",
		"name": "Sprott Physical Silver Trust USD",
		"industry": "VASM"
	},
	{
		"symbol": "PSLV.TO",
		"name": "Sprott Physical Silver Trust CAD",
		"industry": "VASM"
	},
	{
		"symbol": "RBN-UN.TO",
		"name": "Blue Ribbon Income Fund",
		"industry": "VASM"
	},
	{
		"symbol": "FFN.TO",
		"name": "North American Financial 15 Split Corp",
		"industry": "VASM"
	},
	{
		"symbol": "EIT-UN.TO",
		"name": "Canoe Eit Income Fund Units",
		"industry": "VASM"
	},
	{
		"symbol": "HFPC-U.TO",
		"name": "Helios Fairfax Partners Corp",
		"industry": "VASM"
	},
	{ "symbol": "CVG.TO", "name": "Clairvest Group", "industry": "VASM" },
	{ "symbol": "SII.TO", "name": "Sprott Inc", "industry": "VASM" },
	{
		"symbol": "MSRE-UN.TO",
		"name": "Sustainable Real Estate Dividend Fund",
		"industry": "VASM"
	},
	{ "symbol": "PRM.TO", "name": "Big Pharma Split Corp", "industry": "VASM" },
	{
		"symbol": "DF.TO",
		"name": "Dividend 15 Split Corp II",
		"industry": "VASM"
	},
	{ "symbol": "IGM.TO", "name": "Igm Financial Inc", "industry": "VASM" },
	{ "symbol": "MID-UN.TO", "name": "Mint Income Fund", "industry": "VASM" },
	{
		"symbol": "BNK.TO",
		"name": "Big Banc Split Corp Cl A",
		"industry": "VASM"
	},
	{
		"symbol": "DGS.TO",
		"name": "Dividend Growth Split Corp Class A",
		"industry": "VASM"
	},
	{
		"symbol": "PTI-UN.TO",
		"name": "Pimco Tactical Income Fund",
		"industry": "VASM"
	},
	{
		"symbol": "RS.TO",
		"name": "Real Estate and Ecommerce Split Corp",
		"industry": "VASM"
	},
	{ "symbol": "AIM.TO", "name": "Aimia Inc", "industry": "VASM" },
	{
		"symbol": "CLP-UN.TO",
		"name": "International Clean Power Dividend Fund",
		"industry": "VASM"
	},
	{ "symbol": "LBS.TO", "name": "Life & Banc Split Corp", "industry": "VASM" },
	{ "symbol": "ENI-UN.TO", "name": "Energy Income Fund", "industry": "VASM" },
	{
		"symbol": "GDV.TO",
		"name": "Global Dividend Growth Split Corp",
		"industry": "VASM"
	},
	{
		"symbol": "PWI.TO",
		"name": "Sustainable Power Infra Split Corp Cl A",
		"industry": "VASM"
	},
	{ "symbol": "DS.TO", "name": "Dividend Select 15 Corp", "industry": "VASM" },
	{ "symbol": "FTN.TO", "name": "Financial 15 Split Corp", "industry": "VASM" },
	{ "symbol": "ENS.TO", "name": "E Split Corp", "industry": "VASM" },
	{
		"symbol": "BGI-UN.TO",
		"name": "Brookfield Glbl Infras Sec Inc Fd",
		"industry": "VASM"
	},
	{ "symbol": "FW.V", "name": "Flow Capital Corp", "industry": "VASM" },
	{
		"symbol": "MMP-UN.TO",
		"name": "Precious Metals and Mining Trust",
		"industry": "VASM"
	},
	{
		"symbol": "SBC.TO",
		"name": "Brompton Split Banc Corp Cl A",
		"industry": "VASM"
	},
	{
		"symbol": "SPPP.TO",
		"name": "Sprott Physical Platinum Palladium CAD",
		"industry": "VASM"
	},
	{ "symbol": "BCBN.NE", "name": "Base Carbon Inc.", "industry": "VASM" },
	{ "symbol": "BK.TO", "name": "Canadian Banc Corp", "industry": "VASM" },
	{
		"symbol": "TIE.V",
		"name": "Coloured Ties Capital Inc",
		"industry": "VASM"
	},
	{ "symbol": "DFN.TO", "name": "Dividend 15 Split Corp", "industry": "VASM" },
	{ "symbol": "FSZ.TO", "name": "Fiera Capital Corp", "industry": "VASM" },
	{
		"symbol": "PDV.TO",
		"name": "Prime Dividend Corp Cl A",
		"industry": "VASM"
	},
	{ "symbol": "TINY.V", "name": "Tiny Ltd", "industry": "VASM" },
	{ "symbol": "INC-UN.TO", "name": "Income Fin Un", "industry": "VASM" },
	{
		"symbol": "BVOF-B.CN",
		"name": "B.E.S.T. Venture Opportunities Fund Inc.",
		"industry": "VASM"
	},
	{
		"symbol": "TLP-UN.CN",
		"name": "Tier One Capital Ltd Partnership",
		"industry": "VASM"
	},
	{ "symbol": "ELC.V", "name": "Elysee Development Corp", "industry": "VASM" },
	{
		"symbol": "XTD.TO",
		"name": "Tdb Split Corp Class A Shares",
		"industry": "VASM"
	},
	{ "symbol": "RCG.TO", "name": "RF Capital Group Inc", "industry": "VASM" },
	{
		"symbol": "LITT.V",
		"name": "Right Season Investments Corp",
		"industry": "VASM"
	},
	{ "symbol": "OSP.TO", "name": "Brompton Oil Split Corp", "industry": "VASM" },
	{ "symbol": "SOL.CN", "name": "Sol Global Investments", "industry": "VASM" },
	{ "symbol": "MLC.NE", "name": "Mount Logan Capital Inc", "industry": "VASM" },
	{ "symbol": "NETZ.NE", "name": "Carbon Streaming Corp", "industry": "VASM" },
	{
		"symbol": "TEAM.CN",
		"name": "Canadian Nexus Team Ventures Corp",
		"industry": "VASM"
	},
	{ "symbol": "MONT.V", "name": "Montfort Capital Corp", "industry": "VASM" },
	{ "symbol": "CVX.V", "name": "Cematrix Corp", "industry": "VBMT" },
	{
		"symbol": "TBL.TO",
		"name": "Taiga Building Products Ltd",
		"industry": "VBMT"
	},
	{ "symbol": "FBF.V", "name": "Fab-Form Industries Ltd", "industry": "VBMT" },
	{ "symbol": "IBM.NE", "name": "IBM Cdr [Cad Hedged]", "industry": "VITS" },
	{
		"symbol": "CTS.TO",
		"name": "Converge Technology Solutions Corp",
		"industry": "VITS"
	},
	{ "symbol": "SFTC.TO", "name": "Softchoice Corp", "industry": "VITS" },
	{ "symbol": "SPOT.V", "name": "Earthlabs Inc", "industry": "VITS" },
	{ "symbol": "ALYA.TO", "name": "Alithya Group", "industry": "VITS" },
	{ "symbol": "PBIT.CN", "name": "Posabit Systems Corp", "industry": "VITS" },
	{ "symbol": "PVT.V", "name": "Pivotree Inc", "industry": "VITS" },
	{
		"symbol": "KNR.NE",
		"name": "Kontrol Technologies Corp",
		"industry": "VITS"
	},
	{
		"symbol": "QUIS.V",
		"name": "Quisitive Technology Solutions Inc",
		"industry": "VITS"
	},
	{ "symbol": "FARM.V", "name": "Deveron Corp", "industry": "VITS" },
	{
		"symbol": "DCSI.CN",
		"name": "Direct Communication Solutions Inc",
		"industry": "VITS"
	},
	{ "symbol": "MENE.V", "name": "Mene Inc", "industry": "VLUG" },
	{ "symbol": "OPTI.CN", "name": "Optimi Health Corp", "industry": "VFMP" },
	{
		"symbol": "PEAS.V",
		"name": "Global Food and Ingredients Ltd",
		"industry": "VFMP"
	},
	{
		"symbol": "AEP.V",
		"name": "Atlas Engineered Products Ltd",
		"industry": "VBPE"
	},
	{
		"symbol": "GLXY.TO",
		"name": "Galaxy Digital Holdings Ltd",
		"industry": "VCPM"
	},
	{ "symbol": "BITF.TO", "name": "Bitfarms Ltd", "industry": "VCPM" },
	{
		"symbol": "SATO.V",
		"name": "Canada Computational Unlimited Corp",
		"industry": "VCPM"
	},
	{ "symbol": "DEFI.NE", "name": "Valour Inc", "industry": "VCPM" },
	{
		"symbol": "NDA.V",
		"name": "Neptune Digital Assets Corp",
		"industry": "VCPM"
	},
	{
		"symbol": "GS.NE",
		"name": "Goldman Sachs Cdr (Cad Hedged)",
		"industry": "VCPM"
	},
	{
		"symbol": "DMGI.V",
		"name": "Dmg Blockchain Solutions Inc",
		"industry": "VCPM"
	},
	{
		"symbol": "HIVE.V",
		"name": "Hive Blockchain Technologies Inc",
		"industry": "VCPM"
	},
	{
		"symbol": "CXI.TO",
		"name": "Currency Exchange International Corp",
		"industry": "VCPM"
	},
	{ "symbol": "HUT.TO", "name": "Hut 8 Corp", "industry": "VCPM" },
	{
		"symbol": "DELX.V",
		"name": "Delphx Capital Markets Inc",
		"industry": "VCPM"
	},
	{ "symbol": "PNP.TO", "name": "Pinetree Capital Ltd", "industry": "VCPM" },
	{
		"symbol": "MNT.TO",
		"name": "Royal Canadian Mint CDN Gold Reserves",
		"industry": "VCPM"
	},
	{
		"symbol": "MNS.TO",
		"name": "Royal CDN Mint CDN Silver Reserves Etr",
		"industry": "VCPM"
	},
	{ "symbol": "HODL.CN", "name": "Cypherpunk Holdingsinc", "industry": "VCPM" },
	{ "symbol": "BITK.V", "name": "Blockchaink2 Corp", "industry": "VCPM" },
	{ "symbol": "XAU.TO", "name": "Goldmoney Inc", "industry": "VCPM" },
	{
		"symbol": "CF.TO",
		"name": "Canaccord Genuity Group Inc",
		"industry": "VCPM"
	},
	{ "symbol": "HOLD.NE", "name": "Immutable Holdings Inc", "industry": "VCPM" },
	{
		"symbol": "BIGG.CN",
		"name": "Bigg Digital Assets Inc",
		"industry": "VCPM"
	},
	{ "symbol": "COIN.NE", "name": "Tokens.com Corp", "industry": "VCPM" },
	{ "symbol": "FRNT.V", "name": "Frnt Financial Inc", "industry": "VCPM" },
	{ "symbol": "CBIT.V", "name": "Cathedra Bitcoin Inc", "industry": "VCPM" },
	{ "symbol": "SPTZ.CN", "name": "Spetz Inc", "industry": "VCPM" },
	{ "symbol": "PKI.TO", "name": "Parkland Fuel Corp", "industry": "VOGR" },
	{ "symbol": "GIII.V", "name": "Regen III Corp", "industry": "VOGR" },
	{ "symbol": "GWO.TO", "name": "Great-West Lifeco Inc", "industry": "VINF" },
	{ "symbol": "MFC.TO", "name": "Manulife Fin", "industry": "VINF" },
	{
		"symbol": "SFC.TO",
		"name": "Sagicor Financial Company Ltd",
		"industry": "VINF"
	},
	{ "symbol": "POW.TO", "name": "Power Corp of Canada Sv", "industry": "VINF" },
	{ "symbol": "ELF.TO", "name": "E-L Financial", "industry": "VINF" },
	{
		"symbol": "AMZN.NE",
		"name": "Amazon.com Cdr [Cad Hedged]",
		"industry": "VITR"
	},
	{ "symbol": "NTAR.CN", "name": "Nextech3D.Ai Corp", "industry": "VITR" },
	{ "symbol": "TM.V", "name": "Trigon Metals Inc", "industry": "VCOP" },
	{ "symbol": "CS.TO", "name": "Capstone Mining Corp", "industry": "VCOP" },
	{ "symbol": "LUN.TO", "name": "Lundin Mining Corp", "industry": "VCOP" },
	{ "symbol": "III.TO", "name": "Imperial Metals Corp", "industry": "VCOP" },
	{ "symbol": "HBM.TO", "name": "Hudbay Minerals Inc", "industry": "VCOP" },
	{ "symbol": "ERO.TO", "name": "Ero Copper Corp", "industry": "VCOP" },
	{ "symbol": "TKO.TO", "name": "Taseko Mines Ltd", "industry": "VCOP" },
	{ "symbol": "ARG.TO", "name": "Amerigo Resources Ltd", "industry": "VCOP" },
	{ "symbol": "MARI.TO", "name": "Marimaca Copper Corp", "industry": "VCOP" },
	{
		"symbol": "ASCU.TO",
		"name": "Arizona Sonoran Copper Company Inc",
		"industry": "VCOP"
	},
	{ "symbol": "CUU.V", "name": "Copper Fox Metals Inc", "industry": "VCOP" },
	{ "symbol": "ECU.V", "name": "Element 29 Resources Inc", "industry": "VCOP" },
	{ "symbol": "HCH.V", "name": "Hot Chili Limited", "industry": "VCOP" },
	{ "symbol": "QCCU.V", "name": "QC Copper and Gold Inc", "industry": "VCOP" },
	{ "symbol": "IE.TO", "name": "Ivanhoe Electric Inc", "industry": "VCOP" },
	{ "symbol": "LA.V", "name": "Los Andes Copper Ltd", "industry": "VCOP" },
	{ "symbol": "BCU.V", "name": "Bell Copper Corp", "industry": "VCOP" },
	{ "symbol": "DCMC.V", "name": "Dore Copper Mining Corp", "industry": "VCOP" },
	{
		"symbol": "FM.TO",
		"name": "First Quantum Minerals Ltd",
		"industry": "VCOP"
	},
	{ "symbol": "SLMN.V", "name": "Solis Minerals Ltd", "industry": "VCOP" },
	{ "symbol": "TWO.V", "name": "T2 Metals Corp", "industry": "VCOP" },
	{ "symbol": "VCU.V", "name": "Vizsla Copper Corp", "industry": "VCOP" },
	{ "symbol": "EQB.TO", "name": "EQB Inc", "industry": "VBRE" },
	{ "symbol": "VBNK.TO", "name": "Versabank", "industry": "VBRE" },
	{ "symbol": "CWB.TO", "name": "CDN Western Bank", "industry": "VBRE" },
	{ "symbol": "LB.TO", "name": "Laurentian Bank", "industry": "VBRE" },
	{ "symbol": "CU-X.TO", "name": "CDN Util Cl B", "industry": "VUDI" },
	{ "symbol": "ACO-Y.TO", "name": "Atco Ltd Cl II", "industry": "VUDI" },
	{ "symbol": "ACO-X.TO", "name": "Atco Ltd Cl I NV", "industry": "VUDI" },
	{
		"symbol": "CU.TO",
		"name": "Canadian Utilities Ltd Cl A NV",
		"industry": "VUDI"
	},
	{
		"symbol": "BIP-UN.TO",
		"name": "Brookfield Infra Partners LP Units",
		"industry": "VUDI"
	},
	{ "symbol": "H.TO", "name": "Hydro One Ltd", "industry": "VURE" },
	{ "symbol": "FTS.TO", "name": "Fortis Inc", "industry": "VURE" },
	{ "symbol": "EMA.TO", "name": "Emera Incorporated", "industry": "VURE" },
	{ "symbol": "CUP-U.TO", "name": "Caribbean Util US", "industry": "VURE" },
	{ "symbol": "IFOS.V", "name": "Itafos", "industry": "VAGI" },
	{ "symbol": "NTR.TO", "name": "Nutrien Ltd", "industry": "VAGI" },
	{ "symbol": "MGRO.V", "name": "Mustgrow Biologics Corp", "industry": "VAGI" },
	{ "symbol": "NPK.TO", "name": "Verde Agritech Plc", "industry": "VAGI" },
	{ "symbol": "NKE.NE", "name": "Nike Cdr [Cad Hedged]", "industry": "VFOA" },
	{
		"symbol": "SHOE.CN",
		"name": "Grounded People Apparel Inc.",
		"industry": "VFOA"
	},
	{ "symbol": "BUI.TO", "name": "Buhler Ind", "industry": "VFCE" },
	{
		"symbol": "AFN.TO",
		"name": "Ag Growth International Inc",
		"industry": "VFCE"
	},
	{
		"symbol": "TGH.V",
		"name": "Tornado Global Hydrovacs Ltd",
		"industry": "VFCE"
	},
	{ "symbol": "LEV.TO", "name": "Lion Electric CO [The]", "industry": "VFCE" },
	{
		"symbol": "GPV.V",
		"name": "Greenpower Motor Company Inc",
		"industry": "VFCE"
	},
	{ "symbol": "BTB-UN.TO", "name": "Btb REIT Units", "industry": "VROF" },
	{
		"symbol": "AP-UN.TO",
		"name": "Allied Properties Real Estate Inv Trust",
		"industry": "VROF"
	},
	{ "symbol": "D-UN.TO", "name": "Dream Office REIT", "industry": "VROF" },
	{ "symbol": "INO-UN.TO", "name": "Inovalis REIT", "industry": "VROF" },
	{
		"symbol": "TNT-UN.TO",
		"name": "True North Commercial REIT",
		"industry": "VROF"
	},
	{ "symbol": "READ.CN", "name": "Legible Inc.", "industry": "VPUB" },
	{ "symbol": "Y.TO", "name": "Yellow Pages Ltd", "industry": "VPUB" },
	{ "symbol": "TFII.TO", "name": "Tfi International Inc", "industry": "VTRU" },
	{ "symbol": "MTL.TO", "name": "Mullen Group Ltd", "industry": "VTRU" },
	{
		"symbol": "FTG.TO",
		"name": "Firan Technology Group Corp",
		"industry": "VAAD"
	},
	{ "symbol": "MDA.TO", "name": "Mda Ltd", "industry": "VAAD" },
	{ "symbol": "BA.NE", "name": "Boeing Cdr [Cad Hedged]", "industry": "VAAD" },
	{ "symbol": "HRX.TO", "name": "Heroux-Devtek", "industry": "VAAD" },
	{ "symbol": "CAE.TO", "name": "Cae Inc", "industry": "VAAD" },
	{ "symbol": "MAL.TO", "name": "Magellan Aero", "industry": "VAAD" },
	{
		"symbol": "BBD-B.TO",
		"name": "Bombardier Inc Cl B Sv",
		"industry": "VAAD"
	},
	{
		"symbol": "AZ.V",
		"name": "A2Z Smart Technologies Corp",
		"industry": "VAAD"
	},
	{
		"symbol": "FLY.V",
		"name": "Flyht Aerospace Solutions Ltd",
		"industry": "VAAD"
	},
	{
		"symbol": "MAXQ.NE",
		"name": "Maritime Launch Services Inc.",
		"industry": "VAAD"
	},
	{ "symbol": "DPRO.CN", "name": "Draganfly Inc", "industry": "VAAD" },
	{ "symbol": "VOL.V", "name": "Volatus Aerospace Corp", "industry": "VAAD" },
	{ "symbol": "KWE.V", "name": "Kwesst Micro Systems Inc", "industry": "VAAD" },
	{ "symbol": "CAS.TO", "name": "Cascades Inc", "industry": "VPKC" },
	{
		"symbol": "CCL-B.TO",
		"name": "Ccl Industries Inc Cl B NV",
		"industry": "VPKC"
	},
	{ "symbol": "WPK.TO", "name": "Winpak Ltd", "industry": "VPKC" },
	{
		"symbol": "RPI-UN.TO",
		"name": "Richards Packaging Income Fund",
		"industry": "VPKC"
	},
	{ "symbol": "SXP.TO", "name": "Supremex Inc", "industry": "VPKC" },
	{ "symbol": "NEXE.V", "name": "Nexe Innovations Inc", "industry": "VPKC" },
	{ "symbol": "IFX.V", "name": "Imaflex Inc", "industry": "VPKC" },
	{ "symbol": "CN.V", "name": "Condor Resources Inc", "industry": "VOPM" },
	{ "symbol": "GMIN.V", "name": "G Mining Ventures Corp", "industry": "VOPM" },
	{
		"symbol": "AZS.V",
		"name": "Arizona Gold & Silver Inc",
		"industry": "VOPM"
	},
	{ "symbol": "GATO.TO", "name": "Gatos Silver Inc", "industry": "VOPM" },
	{ "symbol": "GBU.V", "name": "Gabriel Res J", "industry": "VOPM" },
	{ "symbol": "EMPS.CN", "name": "Emp Metals Corp.", "industry": "VOPM" },
	{ "symbol": "ASTR.V", "name": "Astra Exploration Inc", "industry": "VOPM" },
	{
		"symbol": "CGG.TO",
		"name": "China Gold Int Resources Corp",
		"industry": "VOPM"
	},
	{ "symbol": "MUX.TO", "name": "Mcewen Mining Inc", "industry": "VOPM" },
	{ "symbol": "BRVO.V", "name": "Bravo Mining Corp", "industry": "VOPM" },
	{ "symbol": "SIL.TO", "name": "Silvercrest Metals Inc", "industry": "VOPM" },
	{
		"symbol": "PPTA.TO",
		"name": "Perpetua Resources Corp",
		"industry": "VOPM"
	},
	{ "symbol": "NAU.V", "name": "Nevgold Corp", "industry": "VOPM" },
	{ "symbol": "MMG.V", "name": "Metallic Minerals Corp", "industry": "VOPM" },
	{
		"symbol": "ABRA.V",
		"name": "Abrasilver Resource Corp",
		"industry": "VOPM"
	},
	{
		"symbol": "TFPM.TO",
		"name": "Triple Flag Precious Metals Corp",
		"industry": "VOPM"
	},
	{ "symbol": "RRI.V", "name": "Riverside Resources Inc", "industry": "VOPM" },
	{ "symbol": "GSPR.V", "name": "Gsp Resource Corp", "industry": "VOPM" },
	{
		"symbol": "AUCU.CN",
		"name": "Inflection Resources Ltd",
		"industry": "VOPM"
	},
	{ "symbol": "VML.V", "name": "Viscount Mining Corp", "industry": "VOPM" },
	{ "symbol": "ALEX.V", "name": "Alpha Exploration Ltd", "industry": "VOPM" },
	{
		"symbol": "AEMC.V",
		"name": "Alaska Energy Metals Corp",
		"industry": "VOPM"
	},
	{
		"symbol": "SM.V",
		"name": "Sierra Madre Gold and Silver Ltd",
		"industry": "VOPM"
	},
	{ "symbol": "TUO.V", "name": "Teuton Resources Corp", "industry": "VOPM" },
	{ "symbol": "EMPR.V", "name": "Empress Royalty Corp", "industry": "VOPM" },
	{
		"symbol": "SNAG.V",
		"name": "Silver North Resources Ltd",
		"industry": "VOPM"
	},
	{
		"symbol": "SSV.V",
		"name": "Southern Silver Exploration Corp",
		"industry": "VOPM"
	},
	{ "symbol": "VOXR.TO", "name": "Vox Royalty Corp", "industry": "VOPM" },
	{ "symbol": "COMT.CN", "name": "Collective Metals Inc", "industry": "VOPM" },
	{ "symbol": "NEXU.CN", "name": "Nexus Uranium Corp", "industry": "VOPM" },
	{ "symbol": "DSLV.V", "name": "Denarius Silver Corp", "industry": "VOPM" },
	{ "symbol": "BRC.V", "name": "Blackrock Silver Corp", "industry": "VOPM" },
	{ "symbol": "STRR.V", "name": "Star Royalties Ltd", "industry": "VOPM" },
	{ "symbol": "EQTY.V", "name": "Equity Metals Corp", "industry": "VOPM" },
	{ "symbol": "NVRO.CN", "name": "Envirogold Global Ltd", "industry": "VOPM" },
	{ "symbol": "SCOT.V", "name": "Scottie Resources Corp", "industry": "VOPM" },
	{
		"symbol": "AMK.V",
		"name": "American Creek Resources Ltd",
		"industry": "VOPM"
	},
	{
		"symbol": "BWCG.V",
		"name": "Blackwolf Copper and Gold Ltd",
		"industry": "VOPM"
	},
	{
		"symbol": "PTM.TO",
		"name": "Platinum Group Metals Ltd",
		"industry": "VOPM"
	},
	{ "symbol": "DEF.V", "name": "Defiance Silver Corp", "industry": "VOPM" },
	{ "symbol": "CKG.V", "name": "Chesapeake Gold Corp", "industry": "VOPM" },
	{ "symbol": "SLVR.V", "name": "Silver Tiger Metals Inc", "industry": "VOPM" },
	{
		"symbol": "NUAG.TO",
		"name": "New Pacific Metals Corp",
		"industry": "VOPM"
	},
	{
		"symbol": "PEX.V",
		"name": "Pacific Ridge Exploration Ltd",
		"industry": "VOPM"
	},
	{ "symbol": "SSVR.V", "name": "Summa Silver Corp", "industry": "VOPM" },
	{ "symbol": "SLS.TO", "name": "Solaris Resources Inc", "industry": "VOPM" },
	{ "symbol": "TUF.V", "name": "Honey Badger Silver Inc", "industry": "VOPM" },
	{ "symbol": "MRZ.V", "name": "Mirasol Resources Ltd", "industry": "VOPM" },
	{ "symbol": "BBB.V", "name": "Brixton Metals Corp", "industry": "VOPM" },
	{
		"symbol": "MTA.V",
		"name": "Metalla Royalty & Streaming Ltd",
		"industry": "VOPM"
	},
	{
		"symbol": "OCG.V",
		"name": "Outcrop Silver & Gold Corp",
		"industry": "VOPM"
	},
	{
		"symbol": "SBMI.V",
		"name": "Silver Bullet Mines Corp",
		"industry": "VOPM"
	},
	{ "symbol": "ITR.V", "name": "Integra Resources Corp", "industry": "VOPM" },
	{ "symbol": "CLIC.V", "name": "Comet Lithium Corp.", "industry": "VOPM" },
	{ "symbol": "CAPT.V", "name": "Captain Silver Corp", "industry": "VOPM" },
	{ "symbol": "EDR.TO", "name": "Endeavour Silver Corp", "industry": "VOPM" },
	{ "symbol": "BME.V", "name": "Barsele Minerals Corp", "industry": "VOPM" },
	{
		"symbol": "VIPR.V",
		"name": "Silver Viper Minerals Corp",
		"industry": "VOPM"
	},
	{ "symbol": "KDK.V", "name": "Kodiak Copper Corp", "industry": "VOPM" },
	{ "symbol": "GOT.V", "name": "Goliath Resources Ltd", "industry": "VOPM" },
	{ "symbol": "GGD.TO", "name": "Gogold Resources Inc", "industry": "VOPM" },
	{ "symbol": "MAX.V", "name": "Max Resource Corp", "industry": "VOPM" },
	{ "symbol": "PGLD.V", "name": "P2 Gold Inc", "industry": "VOPM" },
	{ "symbol": "WEX.V", "name": "Western Exploration Inc", "industry": "VOPM" },
	{ "symbol": "AWM.V", "name": "Angel Wing Metals Inc", "industry": "VOPM" },
	{ "symbol": "TBX.V", "name": "Turmalina Metals Corp", "industry": "VOPM" },
	{ "symbol": "CFE.CN", "name": "Cartier Silver Corp", "industry": "VOPM" },
	{ "symbol": "ARK.V", "name": "Arras Minerals Corp", "industry": "VOPM" },
	{
		"symbol": "WAM.V",
		"name": "Western Alaska Minerals Corp",
		"industry": "VOPM"
	},
	{ "symbol": "ARU.V", "name": "Aurania Resources Ltd", "industry": "VOPM" },
	{ "symbol": "ESAU.CN", "name": "Esgold Corp", "industry": "VOPM" },
	{
		"symbol": "AUAG.CN",
		"name": "Auxico Resources Canada Inc",
		"industry": "VOPM"
	},
	{ "symbol": "AMQ.CN", "name": "Abitibi Metals Corp", "industry": "VGOL" },
	{ "symbol": "TROY.CN", "name": "Troy Minerals Inc.", "industry": "VGOL" },
	{ "symbol": "RML.V", "name": "Rusoro Mining Ltd", "industry": "VGOL" },
	{
		"symbol": "TBK.V",
		"name": "Trailbreaker Resources Ltd",
		"industry": "VGOL"
	},
	{
		"symbol": "RSM.V",
		"name": "Resouro Strategic Metals Inc",
		"industry": "VGOL"
	},
	{ "symbol": "HMR.V", "name": "Homerun Resources Inc", "industry": "VGOL" },
	{ "symbol": "GRZ.V", "name": "Gold Reserve Inc", "industry": "VGOL" },
	{ "symbol": "NPR.V", "name": "North Peak Resources Ltd", "industry": "VGOL" },
	{
		"symbol": "VSR.V",
		"name": "Vanstar Mining Resources Inc",
		"industry": "VGOL"
	},
	{ "symbol": "SOMA.V", "name": "Soma Gold Corp", "industry": "VGOL" },
	{ "symbol": "SIG.CN", "name": "Sitka Gold Corp", "industry": "VGOL" },
	{ "symbol": "MKO.V", "name": "Mako Mining Corp", "industry": "VGOL" },
	{ "symbol": "IGO.V", "name": "Independence Gold Corp", "industry": "VGOL" },
	{ "symbol": "AMRQ.V", "name": "Amaroq Minerals Ltd", "industry": "VGOL" },
	{ "symbol": "MMY.V", "name": "Monument Mining Ltd", "industry": "VGOL" },
	{ "symbol": "MFG.V", "name": "Mayfair Gold Corp", "industry": "VGOL" },
	{ "symbol": "NGD.TO", "name": "New Gold Inc", "industry": "VGOL" },
	{ "symbol": "ELD.TO", "name": "Eldorado Gold", "industry": "VGOL" },
	{ "symbol": "RGC.V", "name": "Regenx Tech Corp", "industry": "VGOL" },
	{
		"symbol": "BNN.CN",
		"name": "Benjamin Hill Mining Corp",
		"industry": "VGOL"
	},
	{ "symbol": "K.TO", "name": "Kinross Gold Corp", "industry": "VGOL" },
	{ "symbol": "SGD.V", "name": "Snowline Gold Corp", "industry": "VGOL" },
	{
		"symbol": "DPM.TO",
		"name": "Dundee Precious Metals Inc",
		"industry": "VGOL"
	},
	{ "symbol": "DNG.TO", "name": "Dynacor Gold Mines Inc", "industry": "VGOL" },
	{ "symbol": "ARTG.V", "name": "Artemis Gold Inc", "industry": "VGOL" },
	{ "symbol": "FDR.V", "name": "Founders Metals Inc", "industry": "VGOL" },
	{ "symbol": "AGI.TO", "name": "Alamos Gold Inc Cls A", "industry": "VGOL" },
	{ "symbol": "CBR.V", "name": "Cabr AL Gold Inc", "industry": "VGOL" },
	{ "symbol": "GPAC.V", "name": "Great Pacific Gold Corp", "industry": "VGOL" },
	{ "symbol": "OSI.V", "name": "Osino Resources Corp", "industry": "VGOL" },
	{ "symbol": "CXB.TO", "name": "Calibre Mining Corp", "industry": "VGOL" },
	{ "symbol": "LUG.TO", "name": "Lundin Gold Inc", "industry": "VGOL" },
	{ "symbol": "WG.CN", "name": "Westward Gold Inc", "industry": "VGOL" },
	{ "symbol": "RISE.CN", "name": "Rise Gold Corp", "industry": "VGOL" },
	{
		"symbol": "WPM.TO",
		"name": "Wheaton Precious Metals Corp",
		"industry": "VGOL"
	},
	{ "symbol": "OGN.V", "name": "Orogen Royalties Inc", "industry": "VGOL" },
	{ "symbol": "ARIS.TO", "name": "Aris Gold Corporation", "industry": "VGOL" },
	{ "symbol": "EQX.TO", "name": "Equinox Gold Corp", "industry": "VGOL" },
	{ "symbol": "CG.TO", "name": "Centerra Gold Inc", "industry": "VGOL" },
	{ "symbol": "VIO.V", "name": "Vior Inc", "industry": "VGOL" },
	{
		"symbol": "FVI.TO",
		"name": "Fortuna Silver Mines Inc",
		"industry": "VGOL"
	},
	{ "symbol": "WDO.TO", "name": "Wesdome Gold Mines Ltd", "industry": "VGOL" },
	{
		"symbol": "OR.TO",
		"name": "Osisko Gold Royalties Ltd",
		"industry": "VGOL"
	},
	{ "symbol": "FISH.V", "name": "Sailfish Royalty Corp", "industry": "VGOL" },
	{ "symbol": "KRR.TO", "name": "Karora Resources Inc", "industry": "VGOL" },
	{ "symbol": "RIO.V", "name": "Rio2 Ltd", "industry": "VGOL" },
	{ "symbol": "JKS.CN", "name": "Jks Resources Inc.", "industry": "VGOL" },
	{ "symbol": "AEM.TO", "name": "Agnico Eagle Mines Ltd", "industry": "VGOL" },
	{ "symbol": "IMG.TO", "name": "Iamgold Corp", "industry": "VGOL" },
	{ "symbol": "VGD.V", "name": "Visible Gold Mines Inc", "industry": "VGOL" },
	{ "symbol": "MAU.V", "name": "Montage Gold Corp", "industry": "VGOL" },
	{ "symbol": "SEA.TO", "name": "Seabridge Gold Inc", "industry": "VGOL" },
	{ "symbol": "ORA.TO", "name": "Aura Minerals Inc", "industry": "VGOL" },
	{
		"symbol": "RDS.V",
		"name": "Radisson Mining Resources Inc",
		"industry": "VGOL"
	},
	{ "symbol": "CGC.V", "name": "Canadian Gold Corp", "industry": "VGOL" },
	{ "symbol": "CNL.TO", "name": "Collective Mining Ltd", "industry": "VGOL" },
	{ "symbol": "ASE.CN", "name": "Asante Gold Corp", "industry": "VGOL" },
	{ "symbol": "BAU.V", "name": "Blue Star Gold Corp", "industry": "VGOL" },
	{ "symbol": "ABX.TO", "name": "Barrick Gold Corp", "industry": "VGOL" },
	{
		"symbol": "BRW.V",
		"name": "Brunswick Exploration Inc",
		"industry": "VGOL"
	},
	{ "symbol": "EDV.TO", "name": "Endeavour Mining Corp", "industry": "VGOL" },
	{ "symbol": "ECR.V", "name": "Cartier Resources Inc", "industry": "VGOL" },
	{ "symbol": "CEE.TO", "name": "Centamin Plc", "industry": "VGOL" },
	{
		"symbol": "GPG.V",
		"name": "Grande Portage Resources Ltd",
		"industry": "VGOL"
	},
	{ "symbol": "AE.V", "name": "American Eagle Gold Corp", "industry": "VGOL" },
	{
		"symbol": "PAAS.TO",
		"name": "Pan American Silver Corp",
		"industry": "VGOL"
	},
	{ "symbol": "LIO.V", "name": "Lion One Metals Ltd", "industry": "VGOL" },
	{
		"symbol": "SUP.V",
		"name": "Northern Superior Resources Inc",
		"industry": "VGOL"
	},
	{ "symbol": "OGC.TO", "name": "Oceanagold Corp", "industry": "VGOL" },
	{ "symbol": "RGD.V", "name": "Reunion Gold Corp", "industry": "VGOL" },
	{ "symbol": "WVM.V", "name": "West Vault Mining Inc", "industry": "VGOL" },
	{ "symbol": "RUSH.V", "name": "Carolina Rush Corp", "industry": "VGOL" },
	{ "symbol": "PRB.TO", "name": "Probe Gold Inc", "industry": "VGOL" },
	{ "symbol": "SSL.TO", "name": "Sandstorm Gold Ltd", "industry": "VGOL" },
	{ "symbol": "PMC.CN", "name": "Peloton Minerals Corp", "industry": "VGOL" },
	{ "symbol": "TEM.V", "name": "Tembo Gold Corp", "industry": "VGOL" },
	{ "symbol": "GOLD.TO", "name": "Goldmining Inc", "industry": "VGOL" },
	{ "symbol": "RPX.V", "name": "Red Pine Exploration Inc", "industry": "VGOL" },
	{ "symbol": "GFG.V", "name": "Gfg Resources Inc", "industry": "VGOL" },
	{ "symbol": "VGCX.TO", "name": "Victoria Gold Corp", "industry": "VGOL" },
	{
		"symbol": "ELE.V",
		"name": "Elemental Altus Royalties Corp",
		"industry": "VGOL"
	},
	{ "symbol": "NGT.TO", "name": "Newmont Corp", "industry": "VGOL" },
	{ "symbol": "BTO.TO", "name": "B2Gold Corp", "industry": "VGOL" },
	{ "symbol": "PRU.TO", "name": "Perseus Mining Ltd", "industry": "VGOL" },
	{ "symbol": "THX.V", "name": "Thor Explorations Ltd", "industry": "VGOL" },
	{ "symbol": "GTWO.V", "name": "G2 Goldfields Inc", "industry": "VGOL" },
	{
		"symbol": "SPA.V",
		"name": "Spanish Mountain Gold Ltd",
		"industry": "VGOL"
	},
	{ "symbol": "KRI.V", "name": "Kobo Resources Inc", "industry": "VGOL" },
	{ "symbol": "RBX.V", "name": "Robex Resources Inc", "industry": "VGOL" },
	{ "symbol": "JAG.TO", "name": "Jaguar Mining Inc", "industry": "VGOL" },
	{ "symbol": "VG.V", "name": "Volcanic Gold Mines Inc", "industry": "VGOL" },
	{ "symbol": "AU.V", "name": "Aurion Resources Ltd", "industry": "VGOL" },
	{
		"symbol": "TXG.TO",
		"name": "Torex Gold Resources Inc",
		"industry": "VGOL"
	},
	{ "symbol": "KNT.TO", "name": "K92 Mining Inc", "industry": "VGOL" },
	{ "symbol": "NFG.V", "name": "New Found Gold Corp", "industry": "VGOL" },
	{ "symbol": "BYN.V", "name": "Banyan Gold Corp", "industry": "VGOL" },
	{
		"symbol": "USGD.CN",
		"name": "American Pacific Mining Corp",
		"industry": "VGOL"
	},
	{ "symbol": "RUP.TO", "name": "Rupert Resources Ltd", "industry": "VGOL" },
	{ "symbol": "HSTR.V", "name": "Heliostar Metals Ltd", "industry": "VGOL" },
	{ "symbol": "ATX.V", "name": "Atex Resources Inc", "industry": "VGOL" },
	{ "symbol": "DYG.V", "name": "Dynasty Gold Corp", "industry": "VGOL" },
	{ "symbol": "GMV.V", "name": "Gmv Minerals Inc", "industry": "VGOL" },
	{ "symbol": "FOR.V", "name": "Fortune Bay Corp", "industry": "VGOL" },
	{ "symbol": "VAU.V", "name": "Viva Gold Corp", "industry": "VGOL" },
	{ "symbol": "LUM.V", "name": "Lumina Gold Corp", "industry": "VGOL" },
	{ "symbol": "NGE.V", "name": "Nevada Exploration Inc", "industry": "VGOL" },
	{ "symbol": "FNV.TO", "name": "Franco-Nevada Corp", "industry": "VGOL" },
	{ "symbol": "WGO.V", "name": "White Gold Corp", "industry": "VGOL" },
	{ "symbol": "PA.V", "name": "Palamina Corp", "industry": "VGOL" },
	{ "symbol": "AMX.V", "name": "AMEX Exploration Inc", "industry": "VGOL" },
	{ "symbol": "MAI.V", "name": "Minera Alamos Inc", "industry": "VGOL" },
	{ "symbol": "OSK.TO", "name": "Osisko Mining Inc", "industry": "VGOL" },
	{
		"symbol": "LME.V",
		"name": "Laurion Mineral Exploration Inc",
		"industry": "VGOL"
	},
	{ "symbol": "LORD.V", "name": "ST James Gold Corp", "industry": "VGOL" },
	{
		"symbol": "HARD.CN",
		"name": "Hardcore Discoveries Ltd",
		"industry": "VGOL"
	},
	{ "symbol": "QIM.CN", "name": "Quimbaya Gold Inc.", "industry": "VGOL" },
	{ "symbol": "GSTM.V", "name": "Goldstorm Metals Corp", "industry": "VGOL" },
	{ "symbol": "OLA.TO", "name": "Orla Mining Ltd", "industry": "VGOL" },
	{ "symbol": "MGG.V", "name": "Minaurum Gold Inc", "industry": "VGOL" },
	{ "symbol": "PALI.V", "name": "Palisades Goldcorp Ltd", "industry": "VGOL" },
	{ "symbol": "INCA.V", "name": "Inca One Gold Corp", "industry": "VGOL" },
	{ "symbol": "DLTA.V", "name": "Delta Resources Ltd", "industry": "VGOL" },
	{ "symbol": "HWG.CN", "name": "Headwater Gold Inc", "industry": "VGOL" },
	{ "symbol": "FMAN.V", "name": "Freeman Gold Corp", "industry": "VGOL" },
	{ "symbol": "BTR.V", "name": "Bonterra Resources Inc", "industry": "VGOL" },
	{
		"symbol": "ELVT.V",
		"name": "Elevation Gold Mining Corp.",
		"industry": "VGOL"
	},
	{ "symbol": "PUMA.V", "name": "Puma Exploration Inc", "industry": "VGOL" },
	{ "symbol": "SSRM.TO", "name": "Ssr Mining Inc", "industry": "VGOL" },
	{ "symbol": "GGO.V", "name": "Galleon Gold Corp", "industry": "VGOL" },
	{
		"symbol": "WRLG.V",
		"name": "West Red Lake Gold Mines Ltd",
		"industry": "VGOL"
	},
	{ "symbol": "GLDL.V", "name": "Gold Line Resources Ltd", "industry": "VGOL" },
	{ "symbol": "NCAU.V", "name": "Newcore Gold Ltd", "industry": "VGOL" },
	{ "symbol": "CERT.V", "name": "Cerrado Gold Inc", "industry": "VGOL" },
	{ "symbol": "ARIC.V", "name": "Awale Resources Ltd", "industry": "VGOL" },
	{ "symbol": "TUD.V", "name": "Tudor Gold Corp", "industry": "VGOL" },
	{ "symbol": "DEX.V", "name": "Almadex Minerals Ltd", "industry": "VGOL" },
	{ "symbol": "NCLR.CN", "name": "Basin Uranium Corp", "industry": "VGOL" },
	{ "symbol": "IAU.TO", "name": "I-80 Gold Corp", "industry": "VGOL" },
	{
		"symbol": "AUEN.V",
		"name": "Golden Sky Minerals Corp",
		"industry": "VGOL"
	},
	{
		"symbol": "GXX.V",
		"name": "Gold Basin Resources Corp",
		"industry": "VGOL"
	},
	{ "symbol": "AUAU.V", "name": "Allegiant Gold Ltd", "industry": "VGOL" },
	{ "symbol": "WHN.V", "name": "Westhaven Gold Corp", "industry": "VGOL" },
	{ "symbol": "TIN.V", "name": "Tincorp Metals Inc", "industry": "VGOL" },
	{ "symbol": "NINE.CN", "name": "Nine Mile Metals Inc", "industry": "VGOL" },
	{ "symbol": "LAB.V", "name": "Labrador Gold Corp", "industry": "VGOL" },
	{ "symbol": "ROS.V", "name": "Roscan Gold Corp", "industry": "VGOL" },
	{ "symbol": "ODV.V", "name": "Osisko Development Corp", "industry": "VGOL" },
	{ "symbol": "GUS.V", "name": "Angus Gold Inc", "industry": "VGOL" },
	{ "symbol": "LGC.V", "name": "Lavras Gold Corp", "industry": "VGOL" },
	{ "symbol": "TECT.V", "name": "Tectonic Metals Inc", "industry": "VGOL" },
	{ "symbol": "ALTA.V", "name": "Altamira Gold Corp", "industry": "VGOL" },
	{ "symbol": "NG.TO", "name": "Novagold Res Inc", "industry": "VGOL" },
	{ "symbol": "EDG.V", "name": "Endurance Gold Corp", "industry": "VGOL" },
	{ "symbol": "MND.TO", "name": "Mandalay Resources Corp", "industry": "VGOL" },
	{ "symbol": "ELO.TO", "name": "Eloro Resources Ltd", "industry": "VGOL" },
	{ "symbol": "RVG.V", "name": "Revival Gold Inc", "industry": "VGOL" },
	{
		"symbol": "MLM.NE",
		"name": "Mcfarlane Lake Mining Limited",
		"industry": "VGOL"
	},
	{ "symbol": "GAL.V", "name": "Galantas Gold Corp", "industry": "VGOL" },
	{
		"symbol": "BLLG.CN",
		"name": "Blue Lagoon Resourcesinc",
		"industry": "VGOL"
	},
	{ "symbol": "RDU.V", "name": "Radius Gold Inc", "industry": "VGOL" },
	{ "symbol": "GSHR.V", "name": "Goldshore Resources Inc", "industry": "VGOL" },
	{ "symbol": "GLDC.V", "name": "Cassiar Gold Corp", "industry": "VGOL" },
	{ "symbol": "IRV.CN", "name": "Irving Resources Inc", "industry": "VGOL" },
	{ "symbol": "BLDS.V", "name": "Badlands Resources Inc", "industry": "VGOL" },
	{ "symbol": "FNAU.CN", "name": "Four Nines Gold Inc", "industry": "VGOL" },
	{ "symbol": "LVX.V", "name": "Leviathan Gold Ltd", "industry": "VGOL" },
	{ "symbol": "GXS.V", "name": "Goldsource Mines Inc", "industry": "VGOL" },
	{ "symbol": "PHNM.V", "name": "Phenom Resources Corp", "industry": "VGOL" },
	{ "symbol": "GMR.CN", "name": "Gelum Resources Ltd.", "industry": "VGOL" },
	{ "symbol": "GWM.V", "name": "Galway Metals Inc", "industry": "VGOL" },
	{ "symbol": "HIGH.V", "name": "Highgold Mining Inc", "industry": "VGOL" },
	{ "symbol": "ABM.V", "name": "Aben Minerals Ltd", "industry": "VGOL" },
	{
		"symbol": "GRHK.CN",
		"name": "Greenhawk Resources Inc",
		"industry": "VGOL"
	},
	{
		"symbol": "WRR.V",
		"name": "Walker River Resources Corp",
		"industry": "VGOL"
	},
	{ "symbol": "GG.V", "name": "Golconda Gold Ltd", "industry": "VGOL" },
	{
		"symbol": "GBRC.V",
		"name": "Gold Bull Resources Corp",
		"industry": "VGOL"
	},
	{ "symbol": "XIM.V", "name": "Ximen Mining Corp", "industry": "VGOL" },
	{ "symbol": "NOM.CN", "name": "Norsemont Mining Inc", "industry": "VGOL" },
	{
		"symbol": "GSRI.CN",
		"name": "Golden Shield Resources Inc.",
		"industry": "VGOL"
	},
	{
		"symbol": "SUI.V",
		"name": "Superior Mining International Corp",
		"industry": "VGOL"
	},
	{ "symbol": "DCLI.CN", "name": "Discovery Lithium Inc", "industry": "VGOL" },
	{ "symbol": "AAU.V", "name": "Angold Resources Ltd", "industry": "VGOL" },
	{ "symbol": "RAK.V", "name": "Rackla Metals Inc", "industry": "VGOL" },
	{ "symbol": "BSR.V", "name": "Bluestone Resources Inc", "industry": "VGOL" },
	{ "symbol": "RDG.V", "name": "Ridgeline Minerals Corp", "industry": "VGOL" },
	{
		"symbol": "SF.CN",
		"name": "Silverfish Resources Inc.",
		"industry": "VGOL"
	},
	{ "symbol": "GTCH.CN", "name": "Getchell Gold Corp", "industry": "VGOL" },
	{ "symbol": "OPHR.V", "name": "Ophir Gold Corp", "industry": "VGOL" },
	{ "symbol": "PATH.CN", "name": "Newpath Resources Inc", "industry": "VGOL" },
	{ "symbol": "AGC.CN", "name": "Avanti Gold Corp.", "industry": "VGOL" },
	{
		"symbol": "NFLD.CN",
		"name": "Exploits Discovery Corp",
		"industry": "VGOL"
	},
	{ "symbol": "BCM.V", "name": "Bear Creek Mining Corp", "industry": "VGOL" },
	{ "symbol": "RAGE.V", "name": "Renegade Gold Inc", "industry": "VGOL" },
	{ "symbol": "ELEM.CN", "name": "Element79 Gold Corp", "industry": "VGOL" },
	{ "symbol": "SJ.TO", "name": "Stella Jones Inc", "industry": "VLWP" },
	{ "symbol": "GDL.TO", "name": "Goodfellow Inc", "industry": "VLWP" },
	{ "symbol": "ADN.TO", "name": "Acadian Timber Corp", "industry": "VLWP" },
	{
		"symbol": "WFG.TO",
		"name": "West Fraser Timber CO Ltd",
		"industry": "VLWP"
	},
	{ "symbol": "IFP.TO", "name": "Interfor Corp", "industry": "VLWP" },
	{ "symbol": "CFP.TO", "name": "Canfor Corp", "industry": "VLWP" },
	{ "symbol": "KLX.V", "name": "Klimat X Development Inc", "industry": "VLWP" },
	{ "symbol": "X.TO", "name": "TMX Group Ltd", "industry": "VFIE" },
	{
		"symbol": "JPM.NE",
		"name": "Jpmorgan Cdr [Cad Hedged]",
		"industry": "VBAG"
	},
	{
		"symbol": "CM.TO",
		"name": "Canadian Imperial Bank of Commerce",
		"industry": "VBAG"
	},
	{
		"symbol": "BOFA.NE",
		"name": "Bank of America Cdr (Cad Hedged)",
		"industry": "VBAG"
	},
	{
		"symbol": "CITI.NE",
		"name": "Citigroup Cdr [Cad Hedged]",
		"industry": "VBAG"
	},
	{ "symbol": "NA.TO", "name": "National Bank of Canada", "industry": "VBAG" },
	{ "symbol": "RY.TO", "name": "Royal Bank of Canada", "industry": "VBAG" },
	{ "symbol": "BMO.TO", "name": "Bank of Montreal", "industry": "VBAG" },
	{ "symbol": "TD.TO", "name": "Toronto-Dominion Bank", "industry": "VBAG" },
	{ "symbol": "BNS.TO", "name": "Bank of Nova Scotia", "industry": "VBAG" },
	{
		"symbol": "WEB.V",
		"name": "Westbridge Renewable Energy Corp",
		"industry": "VUTR"
	},
	{ "symbol": "SUNN.CN", "name": "Solarbank Corporation", "industry": "VUTR" },
	{
		"symbol": "BEP-UN.TO",
		"name": "Brookfield Renewable Partners LP",
		"industry": "VUTR"
	},
	{
		"symbol": "BEPC.TO",
		"name": "Brookfield Renewable Corp",
		"industry": "VUTR"
	},
	{
		"symbol": "PIF.TO",
		"name": "Polaris Infrastructure Inc",
		"industry": "VUTR"
	},
	{ "symbol": "BLX.TO", "name": "Boralex Inc", "industry": "VUTR" },
	{
		"symbol": "ARR.TO",
		"name": "Altius Renewable Royalties Corp",
		"industry": "VUTR"
	},
	{
		"symbol": "AQN.TO",
		"name": "Algonquin Power and Utilities Corp",
		"industry": "VUTR"
	},
	{ "symbol": "RE.V", "name": "Re Royalties Ltd", "industry": "VUTR" },
	{
		"symbol": "GIP.V",
		"name": "Green Impact Partners Inc",
		"industry": "VUTR"
	},
	{ "symbol": "NPI.TO", "name": "Northland Power Inc", "industry": "VUTR" },
	{
		"symbol": "LCFS.TO",
		"name": "Tidewater Renewables Ltd",
		"industry": "VUTR"
	},
	{
		"symbol": "GRB.V",
		"name": "Greenbriar Sustainable Living Inc",
		"industry": "VUTR"
	},
	{ "symbol": "UGE.V", "name": "Uge International Ltd", "industry": "VUTR" },
	{
		"symbol": "REVV.V",
		"name": "Revolve Renewable Power Corp",
		"industry": "VUTR"
	},
	{
		"symbol": "INE.TO",
		"name": "Innergex Renewable Energy Inc",
		"industry": "VUTR"
	},
	{
		"symbol": "MOVE.NE",
		"name": "Powertap Hydrogen Capital Corp",
		"industry": "VUTR"
	},
	{ "symbol": "IAG.TO", "name": "IA Financial Corp Inc", "industry": "VIND" },
	{
		"symbol": "BRK.NE",
		"name": "Berkshire Hathaway Cdr [Cad Hedged]",
		"industry": "VIND"
	},
	{ "symbol": "SLF.TO", "name": "Sun Life Financial Inc", "industry": "VIND" },
	{ "symbol": "AAPL.NE", "name": "Apple Cdr [Cad Hedged]", "industry": "VCOE" },
	{
		"symbol": "UNH.NE",
		"name": "Unitedhealth Cdr [Cad Hedged]",
		"industry": "VHCP"
	},
	{
		"symbol": "CVS.NE",
		"name": "CVS Health Cdr [Cad Hedged]",
		"industry": "VHCP"
	},
	{ "symbol": "ALA.TO", "name": "AltaGas Ltd", "industry": "VOGM" },
	{ "symbol": "KEY.TO", "name": "Keyera Corp", "industry": "VOGM" },
	{
		"symbol": "SRR.V",
		"name": "Source Rock Royalties Ltd",
		"industry": "VOGM"
	},
	{ "symbol": "PPL.TO", "name": "Pembina Pipeline Corp", "industry": "VOGM" },
	{ "symbol": "TRP.TO", "name": "TC Energy Corp", "industry": "VOGM" },
	{ "symbol": "ENB.TO", "name": "Enbridge Inc", "industry": "VOGM" },
	{ "symbol": "GEI.TO", "name": "Gibson Energy Inc", "industry": "VOGM" },
	{ "symbol": "TPZ.TO", "name": "Topaz Energy Corp", "industry": "VOGM" },
	{ "symbol": "TVA-B.TO", "name": "Tva Group Inc Cl B NV", "industry": "VBRO" },
	{ "symbol": "DOO.TO", "name": "Brp Inc", "industry": "VRVE" },
	{ "symbol": "TSU.TO", "name": "Trisura Group Ltd", "industry": "VISS" },
	{ "symbol": "DE.V", "name": "Decisive Dividend Corp", "industry": "VCOG" },
	{
		"symbol": "BBU-UN.TO",
		"name": "Brookfield Business Partners LP",
		"industry": "VCOG"
	},
	{
		"symbol": "HON.NE",
		"name": "Honeywell Cdr [Cad Hedged]",
		"industry": "VCOG"
	},
	{
		"symbol": "DIV.TO",
		"name": "Diversified Royalty Corp",
		"industry": "VCOG"
	},
	{ "symbol": "MUSH.V", "name": "The Good Shroom CO Inc", "industry": "VBSD" },
	{ "symbol": "PRMW.TO", "name": "Primo Water Corp", "industry": "VBSD" },
	{
		"symbol": "COLA.NE",
		"name": "Coca-Cola Cdr [Cad Hedged]",
		"industry": "VBSD"
	},
	{
		"symbol": "GURU.TO",
		"name": "Guru Organic Energy Corp",
		"industry": "VBSD"
	},
	{
		"symbol": "YERB-U.V",
		"name": "Yerbae Brands Corp USD",
		"industry": "VBSD"
	},
	{ "symbol": "JSDA.CN", "name": "Jones Soda CO", "industry": "VBSD" },
	{ "symbol": "HILL.V", "name": "Hill Inc", "industry": "VBSD" },
	{ "symbol": "MXG.TO", "name": "Maxim Power Corp", "industry": "VUIP" },
	{ "symbol": "TA.TO", "name": "Transalta Corp", "industry": "VUIP" },
	{ "symbol": "CPX.TO", "name": "Capital Power Corp", "industry": "VUIP" },
	{
		"symbol": "QSR.TO",
		"name": "Restaurant Brands International Inc",
		"industry": "VRST"
	},
	{
		"symbol": "MCDS.NE",
		"name": "McDonald's Cdr [Cad Hedged]",
		"industry": "VRST"
	},
	{
		"symbol": "PZA.TO",
		"name": "Pizza Pizza Royalty Corp",
		"industry": "VRST"
	},
	{
		"symbol": "SRV-UN.TO",
		"name": "Sir Royalty Income Fund",
		"industry": "VRST"
	},
	{
		"symbol": "BPF-UN.TO",
		"name": "Boston Pizza Royalties Income Fund",
		"industry": "VRST"
	},
	{
		"symbol": "SBUX.NE",
		"name": "Starbucks Cdr [Cad Hedged]",
		"industry": "VRST"
	},
	{ "symbol": "MTY.TO", "name": "Mty Food Group Inc", "industry": "VRST" },
	{
		"symbol": "AW-UN.TO",
		"name": "A&W Revenue Royalties Income Fund",
		"industry": "VRST"
	},
	{
		"symbol": "KEG-UN.TO",
		"name": "Keg Royalties Income Fund",
		"industry": "VRST"
	},
	{
		"symbol": "COHO.V",
		"name": "Coho Collective Kitchens Inc",
		"industry": "VRST"
	},
	{ "symbol": "ODD.V", "name": "Odd Burger Corp", "industry": "VRST" },
	{ "symbol": "AC.TO", "name": "Air Canada", "industry": "VAIR" },
	{ "symbol": "EIF.TO", "name": "Exchange Income Corp", "industry": "VAIR" },
	{
		"symbol": "JET-B.NE",
		"name": "Global Crossing Airlines Group Inc",
		"industry": "VAIR"
	},
	{
		"symbol": "JET.NE",
		"name": "Global Crossing Airlines Group Inc",
		"industry": "VAIR"
	},
	{
		"symbol": "CJET.NE",
		"name": "Canada Jetlines Operations Ltd.",
		"industry": "VAIR"
	},
	{ "symbol": "MRT-UN.TO", "name": "Morguard Un", "industry": "VRDV" },
	{
		"symbol": "CRR-UN.TO",
		"name": "Crombie Real Estate Investment Trust",
		"industry": "VRDV"
	},
	{
		"symbol": "HR-UN.TO",
		"name": "H&R Real Estate Inv Trust",
		"industry": "VRDV"
	},
	{
		"symbol": "NET-UN.V",
		"name": "Canadian Net Real Estate Investment Trust",
		"industry": "VRDV"
	},
	{ "symbol": "MR-UN.TO", "name": "Melcor REIT", "industry": "VRDV" },
	{
		"symbol": "AX-UN.TO",
		"name": "Artis Real Estate Investment Trust Units",
		"industry": "VRDV"
	},
	{
		"symbol": "MPCT-UN.TO",
		"name": "Dream Impact Trust Units",
		"industry": "VRDV"
	},
	{
		"symbol": "NWH-UN.TO",
		"name": "Northwest Healthcare Prop REIT",
		"industry": "VRHF"
	},
	{ "symbol": "RUS.TO", "name": "Russel Metals", "industry": "VIDD" },
	{
		"symbol": "DBM.TO",
		"name": "Doman Building Materials Group Ltd.",
		"industry": "VIDD"
	},
	{ "symbol": "WJX.TO", "name": "Wajax Corp", "industry": "VIDD" },
	{ "symbol": "TIH.TO", "name": "Toromont Ind", "industry": "VIDD" },
	{ "symbol": "FTT.TO", "name": "Finning Intl", "industry": "VIDD" },
	{ "symbol": "ADEN.TO", "name": "Adentra Inc", "industry": "VIDD" },
	{
		"symbol": "FN.TO",
		"name": "First National Financial Corp",
		"industry": "VMRF"
	},
	{ "symbol": "MKP.TO", "name": "Mcan Mortgage Corp", "industry": "VMRF" },
	{
		"symbol": "FC.TO",
		"name": "Firm Capital Mortgage Inv. Corp",
		"industry": "VMRF"
	},
	{
		"symbol": "AI.TO",
		"name": "Atrium Mortgage Investment Corp",
		"industry": "VMRF"
	},
	{ "symbol": "ECN.TO", "name": "Ecn Capital Corp", "industry": "VMRF" },
	{
		"symbol": "TF.TO",
		"name": "Timbercreek Financial Corp",
		"industry": "VMRF"
	},
	{
		"symbol": "DLCG.TO",
		"name": "Dominion Lending Centres Inc",
		"industry": "VMRF"
	},
	{ "symbol": "SPB.TO", "name": "Superior Plus Corp", "industry": "VURG" },
	{
		"symbol": "EVGN.V",
		"name": "Evergen Infrastructure Corp",
		"industry": "VURG"
	},
	{
		"symbol": "BIPC.TO",
		"name": "Brookfield Infrastructure Corp",
		"industry": "VURG"
	},
	{ "symbol": "QBR-B.TO", "name": "Quebecor Inc Cl B Sv", "industry": "VTSE" },
	{ "symbol": "VZ.NE", "name": "Verizon Cdr [Cad Hedged]", "industry": "VTSE" },
	{
		"symbol": "RCI-B.TO",
		"name": "Rogers Communications Inc Cl B NV",
		"industry": "VTSE"
	},
	{ "symbol": "CGO.TO", "name": "Cogeco Inc Sv", "industry": "VTSE" },
	{ "symbol": "T.TO", "name": "Telus Corp", "industry": "VTSE" },
	{ "symbol": "BCE.TO", "name": "BCE Inc", "industry": "VTSE" },
	{
		"symbol": "CCA.TO",
		"name": "Cogeco Communications Inc",
		"industry": "VTSE"
	},
	{ "symbol": "TGO.TO", "name": "Terago Inc", "industry": "VTSE" },
	{ "symbol": "KITS.TO", "name": "Kits Eyecare Ltd", "industry": "VSRE" },
	{
		"symbol": "ATD.TO",
		"name": "Alimentation Couche-Tard Inc.",
		"industry": "VSRE"
	},
	{
		"symbol": "ZZZ.TO",
		"name": "Sleep Country Canada Holdings Inc",
		"industry": "VSRE"
	},
	{ "symbol": "LNF.TO", "name": "Leons Furniture", "industry": "VSRE" },
	{ "symbol": "CTC.TO", "name": "Canadian Tire Corp Ltd", "industry": "VSRE" },
	{ "symbol": "GBT.TO", "name": "Bmtc Group Inc", "industry": "VSRE" },
	{ "symbol": "PET.TO", "name": "Pet Valu Holdings Ltd", "industry": "VSRE" },
	{
		"symbol": "IDG.TO",
		"name": "Indigo Books & Music Inc",
		"industry": "VSRE"
	},
	{ "symbol": "AMB.CN", "name": "Ambari Brands Inc.", "industry": "VSRE" },
	{
		"symbol": "NWC.TO",
		"name": "The North West Company Inc",
		"industry": "VGST"
	},
	{ "symbol": "L.TO", "name": "Loblaw CO", "industry": "VGST" },
	{ "symbol": "WN.TO", "name": "George Weston Limited", "industry": "VGST" },
	{ "symbol": "MRU.TO", "name": "Metro Inc", "industry": "VGST" },
	{ "symbol": "ACQ.TO", "name": "Autocanada Inc", "industry": "VATD" },
	{
		"symbol": "GRAM.NE",
		"name": "Tpco [The Parent Company] Holding Corp.",
		"industry": "VTOB"
	},
	{
		"symbol": "TAAT.CN",
		"name": "Taat Global Alternatives Inc",
		"industry": "VTOB"
	},
	{ "symbol": "NFI.TO", "name": "Nfi Group Inc.", "industry": "VAMN" },
	{
		"symbol": "TSLA.NE",
		"name": "Tesla Inc. Cdr [Cad Hedged]",
		"industry": "VAMN"
	},
	{ "symbol": "VMC.V", "name": "Vicinity Motor Corp", "industry": "VAMN" },
	{ "symbol": "FHYD.V", "name": "First Hydrogen Corp", "industry": "VAMN" },
	{ "symbol": "AUUA.V", "name": "Aluula Composites Inc", "industry": "VTMA" },
	{ "symbol": "BYD.TO", "name": "Boyd Group Services Inc", "industry": "VPSS" },
	{
		"symbol": "WOLF.V",
		"name": "Grey Wolf Animal Health Corp",
		"industry": "VPSS"
	},
	{ "symbol": "PLC.TO", "name": "Park Lawn Corp", "industry": "VPSS" },
	{
		"symbol": "CNR.TO",
		"name": "Canadian National Railway Co.",
		"industry": "VRAI"
	},
	{
		"symbol": "CP.TO",
		"name": "Canadian Pacific Railway Ltd",
		"industry": "VRAI"
	},
	{ "symbol": "TOY.TO", "name": "Spin Master Corp", "industry": "VLEI" },
	{ "symbol": "TWC.TO", "name": "Twc Enterprises Ltd", "industry": "VLEI" },
	{ "symbol": "BDT.TO", "name": "Bird Construction Inc", "industry": "VEGC" },
	{ "symbol": "ATRL.TO", "name": "Snc-Lavalin Group Inc", "industry": "VEGC" },
	{
		"symbol": "BDGI.TO",
		"name": "Badger Infrastructure Solutions Ltd",
		"industry": "VEGC"
	},
	{ "symbol": "STN.TO", "name": "Stantec Inc", "industry": "VEGC" },
	{ "symbol": "ARE.TO", "name": "Aecon Group Inc", "industry": "VEGC" },
	{ "symbol": "WSP.TO", "name": "WSP Global Inc", "industry": "VEGC" },
	{ "symbol": "IMO.TO", "name": "Imperial Oil", "industry": "VOGI" },
	{ "symbol": "SU.TO", "name": "Suncor Energy Inc", "industry": "VOGI" },
	{
		"symbol": "XOM.NE",
		"name": "Exxon Mobil Cdr [Cad Hedged]",
		"industry": "VOGI"
	},
	{
		"symbol": "CHEV.NE",
		"name": "Chevron Cdr [Cad Hedged]",
		"industry": "VOGI"
	},
	{ "symbol": "CVE.TO", "name": "Cenovus Energy Inc", "industry": "VOGI" },
	{
		"symbol": "FFH.TO",
		"name": "Fairfax Financial Holdings Ltd",
		"industry": "VIPC"
	},
	{ "symbol": "IFC.TO", "name": "Intact Financial Corp", "industry": "VIPC" },
	{
		"symbol": "DFY.TO",
		"name": "Definity Financial Corporation",
		"industry": "VIPC"
	},
	{ "symbol": "KDA.V", "name": "Kda Group Inc", "industry": "VMDC" },
	{ "symbol": "NPTH.V", "name": "Neupath Health Inc", "industry": "VMDC" },
	{
		"symbol": "WELL.TO",
		"name": "Well Health Technologies Corp",
		"industry": "VMDC"
	},
	{ "symbol": "EXE.TO", "name": "Extendicare Inc", "industry": "VMDC" },
	{ "symbol": "DR.TO", "name": "Medical Facilities Corp", "industry": "VMDC" },
	{
		"symbol": "SIA.TO",
		"name": "Sienna Senior Living Inc",
		"industry": "VMDC"
	},
	{ "symbol": "NLH.V", "name": "Nova Leap Health Corp", "industry": "VMDC" },
	{
		"symbol": "DNTL.TO",
		"name": "Dentalcorp Holdings Ltd",
		"industry": "VMDC"
	},
	{
		"symbol": "PHA.V",
		"name": "Premier Health of America Inc",
		"industry": "VMDC"
	},
	{ "symbol": "CRRX.TO", "name": "Carerx Corp", "industry": "VMDC" },
	{ "symbol": "ATS.TO", "name": "Ats Corp", "industry": "VSIM" },
	{ "symbol": "SIS.TO", "name": "Savaria Corp", "industry": "VSIM" },
	{ "symbol": "TLA.V", "name": "Titan Logix Corp", "industry": "VSIM" },
	{ "symbol": "VLN.TO", "name": "Velan Inc Sv", "industry": "VSIM" },
	{ "symbol": "ENW.V", "name": "Enwave Corp", "industry": "VSIM" },
	{
		"symbol": "BLDP.TO",
		"name": "Ballard Power Systems Inc",
		"industry": "VSIM"
	},
	{
		"symbol": "NXH.V",
		"name": "Next Hydrogen Solutions Inc",
		"industry": "VSIM"
	},
	{
		"symbol": "CSH-UN.TO",
		"name": "Chartwell Retirement Residences",
		"industry": "VRES"
	},
	{
		"symbol": "CIGI.TO",
		"name": "Colliers International Group Inc",
		"industry": "VRES"
	},
	{ "symbol": "FSV.TO", "name": "Firstservice Corp", "industry": "VRES" },
	{ "symbol": "MEQ.TO", "name": "Mainstreet Eq J", "industry": "VRES" },
	{
		"symbol": "TCN.TO",
		"name": "Tricon Capital Group Inc",
		"industry": "VRES"
	},
	{
		"symbol": "YAK.V",
		"name": "Mongolia Growth Group Ltd",
		"industry": "VRES"
	},
	{ "symbol": "SVI.TO", "name": "Storagevault Canada Inc", "industry": "VRES" },
	{
		"symbol": "BRE.TO",
		"name": "Bridgemarq Real Estate Services Inc",
		"industry": "VRES"
	},
	{ "symbol": "AIF.TO", "name": "Altus Group Ltd", "industry": "VRES" },
	{ "symbol": "PKT.V", "name": "Parkit Enterprise Inc", "industry": "VRES" },
	{
		"symbol": "NXLV.V",
		"name": "Nexliving Communities Inc",
		"industry": "VRES"
	},
	{
		"symbol": "TRBE.V",
		"name": "Tribe Property Technologies Inc",
		"industry": "VRES"
	},
	{ "symbol": "BDI.TO", "name": "Black Diamond Group Ltd", "industry": "VRLS" },
	{
		"symbol": "EFN.TO",
		"name": "Element Fleet Management Corp",
		"industry": "VRLS"
	},
	{ "symbol": "BUX.CN", "name": "Biomark Diagnostics Inc", "industry": "VDRE" },
	{ "symbol": "SONA.CN", "name": "Sona Nanotech Inc", "industry": "VDRE" },
	{ "symbol": "AVCR.V", "name": "Avricore Health Inc", "industry": "VDRE" },
	{ "symbol": "TELO.V", "name": "Telo Genomics Corp", "industry": "VDRE" },
	{ "symbol": "IZO.CN", "name": "Izotropic Corp", "industry": "VDRE" },
	{ "symbol": "NSE.V", "name": "New Stratus Energy Inc", "industry": "VOGE" },
	{ "symbol": "CDR.TO", "name": "Condor Energies Inc", "industry": "VOGE" },
	{ "symbol": "SEI.V", "name": "Sintana Energy Inc", "industry": "VOGE" },
	{ "symbol": "HHRS.TO", "name": "Hammerhead Energy Inc.", "industry": "VOGE" },
	{ "symbol": "TNZ.TO", "name": "Tenaz Energy Corp", "industry": "VOGE" },
	{ "symbol": "ATH.TO", "name": "Athabasca Oil Corp", "industry": "VOGE" },
	{
		"symbol": "WOGC.CN",
		"name": "Waskahigan Oil & Gas Corp.",
		"industry": "VOGE"
	},
	{ "symbol": "FO.V", "name": "Falcon Oil & Gas Ltd", "industry": "VOGE" },
	{ "symbol": "VLE.TO", "name": "Valeura Energy Inc", "industry": "VOGE" },
	{ "symbol": "MEG.TO", "name": "Meg Energy Corp", "industry": "VOGE" },
	{ "symbol": "PXT.TO", "name": "Parex Resources Inc", "industry": "VOGE" },
	{ "symbol": "AXL.V", "name": "Arrow Exploration Corp", "industry": "VOGE" },
	{
		"symbol": "CNQ.TO",
		"name": "Canadian Natural Resources Ltd.",
		"industry": "VOGE"
	},
	{ "symbol": "LOU.V", "name": "Lucero Energy Corp", "industry": "VOGE" },
	{ "symbol": "KEL.TO", "name": "Kelt Exploration Ltd", "industry": "VOGE" },
	{ "symbol": "PSK.TO", "name": "Prairiesky Royalty Ltd", "industry": "VOGE" },
	{ "symbol": "ARX.TO", "name": "Arc Resources Ltd", "industry": "VOGE" },
	{
		"symbol": "IPCO.TO",
		"name": "International Petroleum Corp",
		"industry": "VOGE"
	},
	{
		"symbol": "HWX.TO",
		"name": "Headwater Exploration Inc",
		"industry": "VOGE"
	},
	{ "symbol": "HME.V", "name": "Hemisphere Energy Corp", "industry": "VOGE" },
	{ "symbol": "OBE.TO", "name": "Obsidian Energy Ltd", "industry": "VOGE" },
	{ "symbol": "RBY.TO", "name": "Rubellite Energy Inc", "industry": "VOGE" },
	{
		"symbol": "KEI.TO",
		"name": "Kolibri Global Energy Inc",
		"industry": "VOGE"
	},
	{ "symbol": "CDA.V", "name": "Canuc Resources Corp", "industry": "VOGE" },
	{
		"symbol": "CPG.TO",
		"name": "Crescent Point Energy Corp",
		"industry": "VOGE"
	},
	{ "symbol": "SOIL.TO", "name": "Saturn Oil and Gas Inc", "industry": "VOGE" },
	{ "symbol": "CEI.V", "name": "Coelacanth Energy Inc.", "industry": "VOGE" },
	{
		"symbol": "PEY.TO",
		"name": "Peyto Exploration and Dvlpmnt Corp",
		"industry": "VOGE"
	},
	{
		"symbol": "ORC-B.V",
		"name": "Orca Energy Group Inc Cl B",
		"industry": "VOGE"
	},
	{ "symbol": "OVV.TO", "name": "Ovintiv Inc", "industry": "VOGE" },
	{ "symbol": "POU.TO", "name": "Paramount Resources Ltd", "industry": "VOGE" },
	{ "symbol": "AOI.TO", "name": "Africa Oil Corp", "industry": "VOGE" },
	{ "symbol": "NVA.TO", "name": "Nuvista Energy Ltd", "industry": "VOGE" },
	{ "symbol": "PNE.TO", "name": "Pine Cliff Energy Ltd", "industry": "VOGE" },
	{ "symbol": "ERF.TO", "name": "Enerplus Corp", "industry": "VOGE" },
	{ "symbol": "GTE.TO", "name": "Gran Tierra Energy Inc", "industry": "VOGE" },
	{ "symbol": "WCP.TO", "name": "Whitecap Resources Inc", "industry": "VOGE" },
	{ "symbol": "FRU.TO", "name": "Freehold Royalties Ltd", "industry": "VOGE" },
	{
		"symbol": "HEVI.V",
		"name": "Helium Evolution Incorporated",
		"industry": "VOGE"
	},
	{ "symbol": "KEC.TO", "name": "Kiwetinohk Energy Corp", "industry": "VOGE" },
	{ "symbol": "AAV.TO", "name": "Advantage Oil & Gas Ltd", "industry": "VOGE" },
	{ "symbol": "TOU.TO", "name": "Tourmaline Oil Corp", "industry": "VOGE" },
	{ "symbol": "CJ.TO", "name": "Cardinal Energy Ltd", "industry": "VOGE" },
	{ "symbol": "ALV.V", "name": "Alvopetro Energy Ltd", "industry": "VOGE" },
	{ "symbol": "GASX.V", "name": "Ng Energy Intl Corp", "industry": "VOGE" },
	{ "symbol": "FEC.TO", "name": "Frontera Energy Corp", "industry": "VOGE" },
	{ "symbol": "AVN.V", "name": "Avanti Helium Corp", "industry": "VOGE" },
	{ "symbol": "BNE.TO", "name": "Bonterra Energy Corp", "industry": "VOGE" },
	{ "symbol": "IPO.TO", "name": "Inplay Oil Corp", "industry": "VOGE" },
	{ "symbol": "LCX.V", "name": "Lycos Energy Inc", "industry": "VOGE" },
	{ "symbol": "BTE.TO", "name": "Baytex Energy Corp", "industry": "VOGE" },
	{ "symbol": "TPL.V", "name": "Tethys Petroleum Ltd", "industry": "VOGE" },
	{ "symbol": "CR.TO", "name": "Crew Energy Inc", "industry": "VOGE" },
	{ "symbol": "VET.TO", "name": "Vermilion Energy Inc", "industry": "VOGE" },
	{ "symbol": "VUX.V", "name": "Vital Energy Inc", "industry": "VOGE" },
	{ "symbol": "SGY.TO", "name": "Surge Energy Inc", "industry": "VOGE" },
	{ "symbol": "ROK.V", "name": "Rok Resources Inc", "industry": "VOGE" },
	{
		"symbol": "TVE.TO",
		"name": "Tamarack Valley Energy Ltd",
		"industry": "VOGE"
	},
	{ "symbol": "TAO.V", "name": "Tag Oil Ltd", "industry": "VOGE" },
	{ "symbol": "RHC.V", "name": "Royal Helium Ltd", "industry": "VOGE" },
	{ "symbol": "JOY.TO", "name": "Journey Energy Inc", "industry": "VOGE" },
	{ "symbol": "AFE.V", "name": "Africa Energy Corp", "industry": "VOGE" },
	{
		"symbol": "RECO.V",
		"name": "Reconnaissance Energy Africa Ltd",
		"industry": "VOGE"
	},
	{ "symbol": "PRQ.TO", "name": "Petrus Resources Ltd", "industry": "VOGE" },
	{ "symbol": "BIR.TO", "name": "Birchcliff Energy Ltd", "industry": "VOGE" },
	{ "symbol": "CNE.TO", "name": "Canacol Energy Ltd", "industry": "VOGE" },
	{
		"symbol": "JEV.V",
		"name": "Jericho Energy Ventures Inc",
		"industry": "VOGE"
	},
	{
		"symbol": "HAM.V",
		"name": "Highwood Asset Management Ltd",
		"industry": "VOGE"
	},
	{
		"symbol": "EOG.V",
		"name": "Eco Atlantic Oil and Gas Ltd",
		"industry": "VOGE"
	},
	{ "symbol": "SDE.TO", "name": "Spartan Delta Corp", "industry": "VOGE" },
	{ "symbol": "CEC.V", "name": "Canasia Energy Corp", "industry": "VOGE" },
	{ "symbol": "WIL.V", "name": "Wilton Resources Inc", "industry": "VOGE" },
	{ "symbol": "YGR.TO", "name": "Yangarra Resources Ltd", "industry": "VOGE" },
	{
		"symbol": "TPC.V",
		"name": "Tenth Avenue Petroleum Corp",
		"industry": "VOGE"
	},
	{ "symbol": "CEQ.V", "name": "Criterium Energy Ltd", "industry": "VOGE" },
	{ "symbol": "OYL.V", "name": "Cgx Energy Inc", "industry": "VOGE" },
	{ "symbol": "MCF.V", "name": "Mcf Energy Ltd", "industry": "VOGE" },
	{ "symbol": "SOU.V", "name": "Southern Energy Corp", "industry": "VOGE" },
	{ "symbol": "TOH.V", "name": "Total Helium Ltd", "industry": "VOGE" },
	{ "symbol": "OIL.CN", "name": "Permex Petroleum Corp", "industry": "VOGE" },
	{
		"symbol": "DME.V",
		"name": "Desert Mountain Energy Corp",
		"industry": "VOGE"
	},
	{ "symbol": "RZE.V", "name": "Razor Energy Corp", "industry": "VOGE" },
	{
		"symbol": "TCF.CN",
		"name": "Trillion Energy International Inc",
		"industry": "VOGE"
	},
	{ "symbol": "BIG.V", "name": "Hercules Silver Corp", "industry": "VSIL" },
	{ "symbol": "AYA.TO", "name": "Aya Gold and Silver Inc", "industry": "VSIL" },
	{ "symbol": "SVM.TO", "name": "Silvercorp Metals Inc", "industry": "VSIL" },
	{ "symbol": "DV.V", "name": "Dolly Varden Silver Corp", "industry": "VSIL" },
	{ "symbol": "RSMX.V", "name": "Regency Silver Corp", "industry": "VSIL" },
	{ "symbol": "APGO.V", "name": "Apollo Silver Corp", "industry": "VSIL" },
	{
		"symbol": "FR.TO",
		"name": "First Majestic Silver Corp Common",
		"industry": "VSIL"
	},
	{ "symbol": "SVRS.V", "name": "Silver Storm Mining Ltd", "industry": "VSIL" },
	{ "symbol": "MAG.TO", "name": "MAG Silver Corp", "industry": "VSIL" },
	{ "symbol": "RSLV.V", "name": "Reyna Silver Corp", "industry": "VSIL" },
	{ "symbol": "SVE.V", "name": "Silver One Resources Inc", "industry": "VSIL" },
	{ "symbol": "KTN.V", "name": "Kootenay Silver Inc", "industry": "VSIL" },
	{
		"symbol": "GSVR.V",
		"name": "Guanajuato Silver CO Ltd",
		"industry": "VSIL"
	},
	{
		"symbol": "EML.V",
		"name": "Electric Metals [Usa] Ltd",
		"industry": "VSIL"
	},
	{ "symbol": "IPT.V", "name": "Impact Silver Corp", "industry": "VSIL" },
	{
		"symbol": "APM.V",
		"name": "00Neandean Precious Metals Corp",
		"industry": "VSIL"
	},
	{ "symbol": "BNKR.V", "name": "Bunker Hill Mining Corp", "industry": "VSIL" },
	{ "symbol": "KUYA.CN", "name": "Kuya Silver Corp", "industry": "VSIL" },
	{
		"symbol": "AGMR.V",
		"name": "Silver Mountain Resources Inc",
		"industry": "VSIL"
	},
	{ "symbol": "ZAC.V", "name": "Zacatecas Silver Corp", "industry": "VSIL" },
	{
		"symbol": "GRIN.CN",
		"name": "Grown Rogue International Inc",
		"industry": "VDMS"
	},
	{ "symbol": "CANB.V", "name": "Canadabis Capital Inc", "industry": "VDMS" },
	{
		"symbol": "CPH.TO",
		"name": "Cipher Pharmaceuticals Inc",
		"industry": "VDMS"
	},
	{ "symbol": "DHT-UN.TO", "name": "Dri Healthcare Trust", "industry": "VDMS" },
	{ "symbol": "MPH.V", "name": "Medicure Inc", "industry": "VDMS" },
	{ "symbol": "RX.V", "name": "Biosyent Inc", "industry": "VDMS" },
	{
		"symbol": "DB.V",
		"name": "Decibel Cannabis Company Inc",
		"industry": "VDMS"
	},
	{ "symbol": "VEXT.CN", "name": "Vext Science Inc", "industry": "VDMS" },
	{ "symbol": "FH.NE", "name": "Filament Health Corp", "industry": "VDMS" },
	{ "symbol": "GUD.TO", "name": "Knight Therapeutics Inc", "industry": "VDMS" },
	{ "symbol": "EPIC.CN", "name": "1Cm Inc", "industry": "VDMS" },
	{
		"symbol": "CRDL.TO",
		"name": "Cardiol Therapeutics Inc",
		"industry": "VDMS"
	},
	{
		"symbol": "GTII.CN",
		"name": "Green Thumb Industries Inc",
		"industry": "VDMS"
	},
	{
		"symbol": "HUGE.CN",
		"name": "Fsd Pharma Inc Subordinate Voting Share",
		"industry": "VDMS"
	},
	{ "symbol": "LOVE.V", "name": "Cannara Biotech Inc", "industry": "VDMS" },
	{ "symbol": "VRNO.NE", "name": "Verano Holdings Corp", "industry": "VDMS" },
	{ "symbol": "INNO.CN", "name": "Innocan Pharma Corp", "industry": "VDMS" },
	{
		"symbol": "BHC.TO",
		"name": "Bausch Health Companies Inc",
		"industry": "VDMS"
	},
	{ "symbol": "CRON.TO", "name": "Cronos Group Inc", "industry": "VDMS" },
	{ "symbol": "CXXI.CN", "name": "C21 Investments Inc", "industry": "VDMS" },
	{
		"symbol": "GDNS.CN",
		"name": "Goodness Growth Hldgs Inc",
		"industry": "VDMS"
	},
	{
		"symbol": "SBBC.V",
		"name": "Simply Better Brands Corp",
		"industry": "VDMS"
	},
	{ "symbol": "TIUM-U.CN", "name": "Cansortiuminc", "industry": "VDMS" },
	{ "symbol": "BNXT.CN", "name": "Bionxt Solutions Inc.", "industry": "VDMS" },
	{
		"symbol": "MDP.TO",
		"name": "Medexus Pharmaceuticals Inc",
		"industry": "VDMS"
	},
	{ "symbol": "TLRY.TO", "name": "Tilray Inc", "industry": "VDMS" },
	{
		"symbol": "AAWH-U.CN",
		"name": "Ascend Wellness Holdings Inc",
		"industry": "VDMS"
	},
	{ "symbol": "ROMJ.V", "name": "Rubicon Organics Inc", "industry": "VDMS" },
	{ "symbol": "LSL.V", "name": "Lsl Pharma Group Inc", "industry": "VDMS" },
	{ "symbol": "TRUL.CN", "name": "Trulieve Cannabis Corp", "industry": "VDMS" },
	{ "symbol": "CDVA.CN", "name": "Cordovacann Corp", "industry": "VDMS" },
	{ "symbol": "PCLO.V", "name": "Pharmacielo Ltd", "industry": "VDMS" },
	{ "symbol": "OGI.TO", "name": "Organigram Holdings Inc", "industry": "VDMS" },
	{ "symbol": "XTRX.CN", "name": "Adastra Hldgs Inc", "industry": "VDMS" },
	{ "symbol": "PLTH.CN", "name": "Planet 13 Holdings Inc", "industry": "VDMS" },
	{ "symbol": "MRMD.CN", "name": "Marimed Inc.", "industry": "VDMS" },
	{ "symbol": "CL.CN", "name": "Cresco Labs Inc", "industry": "VDMS" },
	{ "symbol": "RIV.CN", "name": "Canopy Rivers Inc", "industry": "VDMS" },
	{
		"symbol": "SHWZ.NE",
		"name": "Medicine Man Technologies Inc.",
		"industry": "VDMS"
	},
	{ "symbol": "HLS.TO", "name": "Hls Therapeutics Inc", "industry": "VDMS" },
	{ "symbol": "BZAM.CN", "name": "Bzam Ltd", "industry": "VDMS" },
	{
		"symbol": "GWAY.CN",
		"name": "Greenway Greenhouse Cannabis Corporation",
		"industry": "VDMS"
	},
	{
		"symbol": "JUSH.CN",
		"name": "Jushi Holdings Inc Class B Subordinate",
		"industry": "VDMS"
	},
	{ "symbol": "LOWL.CN", "name": "Lowell Farms Inc", "industry": "VDMS" },
	{
		"symbol": "MYCO.CN",
		"name": "Mydecine Innovations Group Inc",
		"industry": "VDMS"
	},
	{ "symbol": "FFNT.CN", "name": "4Front Ventures Corp", "industry": "VDMS" },
	{ "symbol": "IMCC.CN", "name": "IM Cannabis Corp", "industry": "VDMS" },
	{
		"symbol": "PBF.CN",
		"name": "Planet Based Foods Global Inc.",
		"industry": "VDMS"
	},
	{
		"symbol": "ACRG-B-U.CN",
		"name": "Acreage Holdings Inc Floating S.V.",
		"industry": "VDMS"
	},
	{ "symbol": "PMZ-UN.TO", "name": "Primaris REIT", "industry": "VRRT" },
	{
		"symbol": "CRT-UN.TO",
		"name": "CT Real Estate Investment Trust",
		"industry": "VRRT"
	},
	{
		"symbol": "SRU-UN.TO",
		"name": "Smartcentres Real Estate Investment Trust",
		"industry": "VRRT"
	},
	{
		"symbol": "CHP-UN.TO",
		"name": "Choice Properties REIT",
		"industry": "VRRT"
	},
	{
		"symbol": "FCR-UN.TO",
		"name": "First Capital REIT Units",
		"industry": "VRRT"
	},
	{ "symbol": "REI-UN.TO", "name": "Riocan Real Est Un", "industry": "VRRT" },
	{ "symbol": "PLZ-UN.TO", "name": "Plaza Retail REIT", "industry": "VRRT" },
	{
		"symbol": "FCD-UN.TO",
		"name": "Firm Capital Property Trust",
		"industry": "VRRT"
	},
	{
		"symbol": "SGR-U.TO",
		"name": "Slate Grocery REIT USD",
		"industry": "VRRT"
	},
	{ "symbol": "SGR-UN.TO", "name": "Slate Grocery REIT", "industry": "VRRT" },
	{
		"symbol": "DCM.TO",
		"name": "Data Communications Mgmt Corp",
		"industry": "VMBS"
	},
	{ "symbol": "KBL.TO", "name": "Kbro Linen Inc", "industry": "VMBS" },
	{ "symbol": "TRI.TO", "name": "Thomson Reuters Corp", "industry": "VMBS" },
	{ "symbol": "RBA.TO", "name": "Rb Global Inc", "industry": "VMBS" },
	{ "symbol": "DXT.TO", "name": "Dexterra Group Inc", "industry": "VMBS" },
	{
		"symbol": "ISV.TO",
		"name": "Information Services Corp",
		"industry": "VMBS"
	},
	{ "symbol": "CGY.TO", "name": "Calian Group Ltd", "industry": "VMBS" },
	{
		"symbol": "GDI.TO",
		"name": "Gdi Integrated Facility Services Inc",
		"industry": "VMBS"
	},
	{ "symbol": "KUT.V", "name": "Redishred Capital Corp", "industry": "VMBS" },
	{
		"symbol": "SHLE.TO",
		"name": "Source Energy Services Ltd",
		"industry": "VOGS"
	},
	{ "symbol": "MCB.TO", "name": "Mccoy Global Inc", "industry": "VOGS" },
	{ "symbol": "TVK.TO", "name": "Terravest Capital Inc", "industry": "VOGS" },
	{
		"symbol": "NOA.TO",
		"name": "North American Construction Group Ltd",
		"industry": "VOGS"
	},
	{
		"symbol": "CEU.TO",
		"name": "Ces Energy Solutions Corp",
		"industry": "VOGS"
	},
	{ "symbol": "PSD.TO", "name": "Pulse Seismic Inc", "industry": "VOGS" },
	{ "symbol": "TCW.TO", "name": "Trican Well", "industry": "VOGS" },
	{ "symbol": "PSI.TO", "name": "Pason Systems Inc", "industry": "VOGS" },
	{ "symbol": "MATR.TO", "name": "Shawcor Ltd", "industry": "VOGS" },
	{
		"symbol": "TOT.TO",
		"name": "Total Energy Services Inc",
		"industry": "VOGS"
	},
	{
		"symbol": "STEP.TO",
		"name": "Step Energy Services Ltd",
		"industry": "VOGS"
	},
	{ "symbol": "EFX.TO", "name": "Enerflex Ltd", "industry": "VOGS" },
	{
		"symbol": "HWO.TO",
		"name": "High Arctic Energy Services Inc",
		"industry": "VOGS"
	},
	{
		"symbol": "CFW.TO",
		"name": "Calfrac Well Services Ltd",
		"industry": "VOGS"
	},
	{
		"symbol": "BNRE.TO",
		"name": "Brookfield Reinsurance Ltd. Class A",
		"industry": "VINR"
	},
	{
		"symbol": "NFLX.NE",
		"name": "Netflix Cdr [Cad Hedged]",
		"industry": "VENT"
	},
	{
		"symbol": "DIS.NE",
		"name": "Walt Disney Canadian Depositary Receipts [Cad He",
		"industry": "VENT"
	},
	{ "symbol": "CGX.TO", "name": "Cineplex Inc", "industry": "VENT" },
	{
		"symbol": "TBRD.V",
		"name": "Thunderbird Entertainment Group Inc",
		"industry": "VENT"
	},
	{ "symbol": "NTE.V", "name": "Network Media Group Inc", "industry": "VENT" },
	{ "symbol": "OAM.V", "name": "Overactive Media Corp", "industry": "VENT" },
	{ "symbol": "BRMI.TO", "name": "Boat Rocker Media Inc", "industry": "VENT" },
	{ "symbol": "WILD.TO", "name": "Wildbrain Ltd", "industry": "VENT" },
	{
		"symbol": "AMEN.NE",
		"name": "Amcomri Entertainment Inc.",
		"industry": "VENT"
	},
	{ "symbol": "META.NE", "name": "Meta Cdr [Cad Hedged]", "industry": "VICI" },
	{
		"symbol": "BILD.V",
		"name": "Builddirect.com Technologies Inc",
		"industry": "VICI"
	},
	{
		"symbol": "GOOG.NE",
		"name": "Alphabet Inc. Cdr [Cad Hedged]",
		"industry": "VICI"
	},
	{
		"symbol": "FORA.TO",
		"name": "Verticalscope Holdings Inc",
		"industry": "VICI"
	},
	{ "symbol": "APLV.CN", "name": "Apartmentlove Inc.", "industry": "VICI" },
	{ "symbol": "SBIO.V", "name": "Sabio Holdings Inc", "industry": "VICI" },
	{ "symbol": "PRL.TO", "name": "Propel Holdings Inc", "industry": "VCSV" },
	{ "symbol": "GSY.TO", "name": "Goeasy Ltd", "industry": "VCSV" },
	{
		"symbol": "EPF.V",
		"name": "Everyday People Financial Corp",
		"industry": "VCSV"
	},
	{
		"symbol": "VISA.NE",
		"name": "Visa Canadian Depositary Receipts [Cad Hedged]",
		"industry": "VCSV"
	},
	{
		"symbol": "MA.NE",
		"name": "Mastercard Cdr [Cad Hedged]",
		"industry": "VCSV"
	},
	{
		"symbol": "PYPL.NE",
		"name": "Paypal Canadian Depositary Receipts [Cad Hedged]",
		"industry": "VCSV"
	},
	{ "symbol": "CHW.TO", "name": "Chesswood Group Ltd", "industry": "VCSV" },
	{
		"symbol": "CRWN.TO",
		"name": "Crown Capital Partners Inc",
		"industry": "VCSV"
	},
	{ "symbol": "ACD.TO", "name": "Accord Financial", "industry": "VCSV" },
	{ "symbol": "AFCC-H.V", "name": "Automotive Finco Corp", "industry": "VCSV" },
	{ "symbol": "VSOL.NE", "name": "Three Sixty Solar Ltd.", "industry": "VSOL" },
	{
		"symbol": "HBFG.CN",
		"name": "Happy Belly Food Group Inc.",
		"industry": "VPKF"
	},
	{
		"symbol": "SWP.TO",
		"name": "Swiss Water Decaffeinated Coffee Inc",
		"industry": "VPKF"
	},
	{
		"symbol": "PBH.TO",
		"name": "Premium Brands Holdings Corp",
		"industry": "VPKF"
	},
	{ "symbol": "MFI.TO", "name": "Maple Leaf Foods", "industry": "VPKF" },
	{ "symbol": "JWEL.TO", "name": "Jamieson Wellness Inc", "industry": "VPKF" },
	{ "symbol": "SAP.TO", "name": "Saputo Inc", "industry": "VPKF" },
	{ "symbol": "HLF.TO", "name": "High Liner", "industry": "VPKF" },
	{
		"symbol": "BHSC.CN",
		"name": "Bioharvest Sciences Inc",
		"industry": "VPKF"
	},
	{
		"symbol": "FRSH.V",
		"name": "The Fresh Factory B.C Ltd.",
		"industry": "VPKF"
	},
	{ "symbol": "BOIL.CN", "name": "Beyond Oil Ltd.", "industry": "VPKF" },
	{ "symbol": "SOY.TO", "name": "Sunopta Inc", "industry": "VPKF" },
	{
		"symbol": "PNGA.CN",
		"name": "Pangea Natural Foods Inc.",
		"industry": "VPKF"
	},
	{ "symbol": "MOOO.CN", "name": "Bettermood Food Corp", "industry": "VPKF" },
	{
		"symbol": "MEAT.CN",
		"name": "Modern Plant Based Foods Inc",
		"industry": "VPKF"
	},
	{
		"symbol": "NGRB.NE",
		"name": "Nextgen Food Robotics Corp",
		"industry": "VPKF"
	},
	{ "symbol": "BITE.CN", "name": "Blender Bites Limited", "industry": "VPKF" },
	{ "symbol": "GFCO.CN", "name": "The Good Flour Corp.", "industry": "VPKF" },
	{ "symbol": "CJT.TO", "name": "Cargojet Inc", "industry": "VISL" },
	{
		"symbol": "TTNM.TO",
		"name": "Titanium Transportation Group Inc",
		"industry": "VISL"
	},
	{ "symbol": "UPS.NE", "name": "Ups Cdr [Cad Hedged]", "industry": "VISL" },
	{
		"symbol": "AND.TO",
		"name": "Andlauer Healthcare Group Inc",
		"industry": "VISL"
	},
	{ "symbol": "PDO.CN", "name": "Pudo Inc", "industry": "VISL" },
	{
		"symbol": "PHX.TO",
		"name": "Phx Energy Services Corp",
		"industry": "VOGD"
	},
	{
		"symbol": "WRG.TO",
		"name": "Western Energy Services Corp",
		"industry": "VOGD"
	},
	{ "symbol": "PD.TO", "name": "Precision Drilling Corp", "industry": "VOGD" },
	{ "symbol": "SDI.V", "name": "Stampede Drilling Inc", "industry": "VOGD" },
	{
		"symbol": "ESI.TO",
		"name": "Ensign Energy Services Inc",
		"industry": "VOGD"
	},
	{ "symbol": "EXRO.TO", "name": "Exro Technologies Inc", "industry": "VEEP" },
	{ "symbol": "LPS.V", "name": "Legend Power Systems Inc", "industry": "VEEP" },
	{
		"symbol": "ZAIR.CN",
		"name": "Zinc8 Energy Solutions Inc",
		"industry": "VEEP"
	},
	{
		"symbol": "SES.TO",
		"name": "Secure Energy Services Inc",
		"industry": "VWMA"
	},
	{ "symbol": "VCI.V", "name": "Vitreous Glass Inc", "industry": "VWMA" },
	{ "symbol": "GFL.TO", "name": "Gfl Environmental Inc", "industry": "VWMA" },
	{ "symbol": "WCN.TO", "name": "Waste Connections Inc", "industry": "VWMA" },
	{
		"symbol": "EWK.V",
		"name": "Earthworks Industries Inc",
		"industry": "VWMA"
	},
	{
		"symbol": "VTX.V",
		"name": "Vertex Resource Group Ltd",
		"industry": "VWMA"
	},
	{ "symbol": "YES.V", "name": "Char Technologies Ltd", "industry": "VWMA" },
	{
		"symbol": "BLM.V",
		"name": "Blumetric Environmental Inc",
		"industry": "VWMA"
	},
	{
		"symbol": "LUX.CN",
		"name": "Newlox Gold Ventures Corp",
		"industry": "VWMA"
	},
	{
		"symbol": "ROOF.V",
		"name": "Northstar Clean Technologies Inc",
		"industry": "VWMA"
	},
	{ "symbol": "ECM.V", "name": "Ecolomondo Corp", "industry": "VWMA" },
	{ "symbol": "OPS.TO", "name": "Opsens Inc", "industry": "VMIS" },
	{
		"symbol": "BLCO.TO",
		"name": "Bausch Lomb Corporation",
		"industry": "VMIS"
	},
	{
		"symbol": "OTC.V",
		"name": "Ocumetics Technology Corp",
		"industry": "VMIS"
	},
	{ "symbol": "ZEN.V", "name": "Zentek Ltd", "industry": "VMIS" },
	{
		"symbol": "DIR-UN.TO",
		"name": "Dream Industrial REIT",
		"industry": "VRIN"
	},
	{
		"symbol": "GRT-UN.TO",
		"name": "Granite Real Estate Investment Trust",
		"industry": "VRIN"
	},
	{
		"symbol": "NXR-UN.TO",
		"name": "Nexus Real Estate Investment Trust",
		"industry": "VRIN"
	},
	{
		"symbol": "PRV-UN.TO",
		"name": "Pro Real Estate Investment Trust",
		"industry": "VRIN"
	},
	{ "symbol": "CLS.TO", "name": "Celestica Inc Sv", "industry": "VECO" },
	{ "symbol": "ZTE.CN", "name": "Ztest Electronics Inc", "industry": "VECO" },
	{
		"symbol": "HEAT.CN",
		"name": "Hillcrest Energy Technologies Ltd",
		"industry": "VECO"
	},
	{ "symbol": "WIFI.CN", "name": "American Aires Inc.", "industry": "VECO" },
	{ "symbol": "WFC.TO", "name": "Wall Financial", "industry": "VREV" },
	{ "symbol": "GDC.TO", "name": "Genesis Land J", "industry": "VREV" },
	{ "symbol": "MRD.TO", "name": "Melcor Dev", "industry": "VREV" },
	{ "symbol": "DRM.TO", "name": "Dream Unlimited Corp", "industry": "VREV" },
	{
		"symbol": "BEI-UN.TO",
		"name": "Boardwalk Real Estate Investment Trust",
		"industry": "VRRE"
	},
	{ "symbol": "CAR-UN.TO", "name": "CDN Apartment Un", "industry": "VRRE" },
	{ "symbol": "MI-UN.TO", "name": "Minto Apartment REIT", "industry": "VRRE" },
	{
		"symbol": "KMP-UN.TO",
		"name": "Killam Apartment REIT",
		"industry": "VRRE"
	},
	{
		"symbol": "MHC-U.TO",
		"name": "Flagship Communities Real Estate Investm",
		"industry": "VRRE"
	},
	{
		"symbol": "MHC-UN.TO",
		"name": "Flagship Communites REIT",
		"industry": "VRRE"
	},
	{
		"symbol": "IIP-UN.TO",
		"name": "Interrent Real Estate Investment Trust",
		"industry": "VRRE"
	},
	{
		"symbol": "MAR-UN.V",
		"name": "Marwest Apartment REIT",
		"industry": "VRRE"
	},
	{
		"symbol": "DRR-U.TO",
		"name": "Dream Residential Real Estate Investment",
		"industry": "VRRE"
	},
	{
		"symbol": "MRG-UN.TO",
		"name": "Morguard Na Residential REIT Units",
		"industry": "VRRE"
	},
	{
		"symbol": "HOM-UN.TO",
		"name": "Bsr Real Estate Investment Trust",
		"industry": "VRRE"
	},
	{
		"symbol": "HOM-U.TO",
		"name": "Bsr Real Estate Investment Trust",
		"industry": "VRRE"
	},
	{
		"symbol": "ERE-UN.TO",
		"name": "European Residential Real Estate Invs. Trust",
		"industry": "VRRE"
	},
	{ "symbol": "ASTL.TO", "name": "Algoma Steel Group Inc", "industry": "VSTL" },
	{ "symbol": "CIA.TO", "name": "Champion Iron Ltd", "industry": "VSTL" },
	{ "symbol": "STLC.TO", "name": "Stelco Holdings Inc", "industry": "VSTL" },
	{
		"symbol": "LIF.TO",
		"name": "Labrador Iron Ore Royalty Corp",
		"industry": "VSTL"
	},
	{ "symbol": "TSL.TO", "name": "Tree Island Steel Ltd", "industry": "VSTL" },
	{
		"symbol": "MRE.TO",
		"name": "Martinrea International Inc",
		"industry": "VAUP"
	},
	{ "symbol": "XTC.TO", "name": "Exco Tech", "industry": "VAUP" },
	{ "symbol": "MG.TO", "name": "Magna International Inc", "industry": "VAUP" },
	{ "symbol": "LNR.TO", "name": "Linamar Corp", "industry": "VAUP" },
	{
		"symbol": "WPRT.TO",
		"name": "Westport Fuel Systems Inc",
		"industry": "VAUP"
	},
	{
		"symbol": "HC.NE",
		"name": "Hypercharge Networks Corp.",
		"industry": "VAUP"
	},
	{ "symbol": "VMD.TO", "name": "Viemed Healthcare Inc", "industry": "VMDD" },
	{ "symbol": "ASG.V", "name": "Aurora Spine Corp", "industry": "VMDD" },
	{
		"symbol": "QIPT.TO",
		"name": "Quipt Home Medical Corp",
		"industry": "VMDD"
	},
	{ "symbol": "HTL.TO", "name": "Hamilton Thorne Ltd", "industry": "VMDD" },
	{
		"symbol": "VPT.V",
		"name": "Ventripoint Diagnostics Ltd",
		"industry": "VMDD"
	},
	{
		"symbol": "NGMD.V",
		"name": "Nugen Medical Devices Inc",
		"industry": "VMDD"
	},
	{
		"symbol": "PINK.V",
		"name": "Perimeter Medical Imaging Ai Inc",
		"industry": "VMDD"
	},
	{
		"symbol": "TLT.V",
		"name": "Theralase Technologies Inc",
		"industry": "VMDD"
	},
	{
		"symbol": "BLO.CN",
		"name": "Cannabix Technologies Inc",
		"industry": "VMDD"
	},
	{
		"symbol": "SGMD.V",
		"name": "Salona Global Medical Device Corp",
		"industry": "VMDD"
	},
	{
		"symbol": "TPX-B.TO",
		"name": "Molson Coors Canada Inc Cl B NV",
		"industry": "VBVB"
	},
	{ "symbol": "BR.TO", "name": "Big Rock Brewery Inc", "industry": "VBVB" },
	{ "symbol": "TRZ.TO", "name": "Transat At Inc", "industry": "VTRS" },
	{ "symbol": "RET.V", "name": "Reitmans Canada", "industry": "VAPS" },
	{ "symbol": "ROOT.TO", "name": "Roots Corp", "industry": "VAPS" },
	{ "symbol": "ATZ.TO", "name": "Aritzia Inc", "industry": "VAPS" },
	{ "symbol": "GCL.TO", "name": "Colabor Group Inc", "industry": "VFDD" },
	{ "symbol": "CRP.TO", "name": "Ceres Global Ag Corp", "industry": "VFDD" },
	{ "symbol": "OGO.V", "name": "Organto Foods Inc", "industry": "VFDD" },
	{ "symbol": "CTH.V", "name": "Cotec Holdings Corp", "industry": "VTCO" },
	{ "symbol": "SGQ.V", "name": "Southgobi Resources Ltd", "industry": "VTCO" },
	{ "symbol": "MOX.V", "name": "Morien Resources Corp", "industry": "VTCO" },
	{
		"symbol": "NVDA.NE",
		"name": "Nvidia Cdr (Cad Hedged)",
		"industry": "VSEM"
	},
	{
		"symbol": "AMD.NE",
		"name": "Advanced Micro Devices Cdr [Cad Hedged]",
		"industry": "VSEM"
	},
	{ "symbol": "INTC.NE", "name": "Intel Cdr [Cad Hedged]", "industry": "VSEM" },
	{
		"symbol": "MRM.CN",
		"name": "Micromem Technologies Inc",
		"industry": "VSEM"
	},
	{ "symbol": "PTK.V", "name": "Poet Technologies Inc", "industry": "VSEM" },
	{
		"symbol": "U-U.TO",
		"name": "Sprott Physical Uranium Trust USD",
		"industry": "VURA"
	},
	{ "symbol": "CCO.TO", "name": "Cameco Corp", "industry": "VURA" },
	{
		"symbol": "U-UN.TO",
		"name": "Sprott Physical Uranium Trust",
		"industry": "VURA"
	},
	{ "symbol": "EU.V", "name": "Encore Energy Corp", "industry": "VURA" },
	{ "symbol": "NXE.TO", "name": "Nexgen Energy Ltd", "industry": "VURA" },
	{ "symbol": "DML.TO", "name": "Denison Mines Corp", "industry": "VURA" },
	{ "symbol": "FCU.TO", "name": "Fission Uranium Corp", "industry": "VURA" },
	{ "symbol": "FUU.V", "name": "F3 Uranium Corp", "industry": "VURA" },
	{
		"symbol": "CAKE.CN",
		"name": "Radio Fuels Energy Corp.",
		"industry": "VURA"
	},
	{ "symbol": "URE.TO", "name": "Ur-Energy Inc", "industry": "VURA" },
	{
		"symbol": "WUC.CN",
		"name": "Western Uranium & Vanadium Corp",
		"industry": "VURA"
	},
	{ "symbol": "URC.TO", "name": "Uranium Royalty Corp", "industry": "VURA" },
	{ "symbol": "ISO.V", "name": "Isoenergy Ltd", "industry": "VURA" },
	{ "symbol": "EFR.TO", "name": "Energy Fuels Inc", "industry": "VURA" },
	{
		"symbol": "SUU.V",
		"name": "Strathmore Plus Uranium Corp",
		"industry": "VURA"
	},
	{ "symbol": "GREN.CN", "name": "Madison Metals Inc.", "industry": "VURA" },
	{ "symbol": "FIND.V", "name": "Baselode Energy Corp", "industry": "VURA" },
	{
		"symbol": "API.CN",
		"name": "Appia Rare Earths and Uranium Corp",
		"industry": "VURA"
	},
	{ "symbol": "SASK.CN", "name": "Atha Energy Corp.", "industry": "VURA" },
	{ "symbol": "LUR.CN", "name": "Latitude Uranium Inc", "industry": "VURA" },
	{ "symbol": "GXU.V", "name": "Goviex Uranium Inc", "industry": "VURA" },
	{ "symbol": "TMC.V", "name": "Trench Metals Corp", "industry": "VURA" },
	{ "symbol": "RSI.TO", "name": "Rogers Sugar Inc", "industry": "VCOF" },
	{ "symbol": "TYUM.CN", "name": "The Yumy Candy CO Inc", "industry": "VCOF" },
	{ "symbol": "HEO.TO", "name": "H2O Innovation Inc", "industry": "VURW" },
	{ "symbol": "PRME.CN", "name": "Prime Drink Group Corp.", "industry": "VURW" }
]

sector_industry_name_mapping = {
    'Energy': ['TSX Uranium', 'TSX Oil & Gas Integrated', 'TSX Indices Energy', 'TSX Oil & Gas Equipment & Srvs', 'TSX Oil & Gas Drilling', 'TSX Oil & Gas Refining & Mrkt', 'TSX Oil & Gas E&P', 'TSX Oil & Gas Midstream'],
    'HealthCare': ['TSX Pharmaceutical Retailers', 'TSX Medical Instruments & Suppls', 'TSX Drug Specialty & Generic', 'TSX Health Information Services', 'TSX Diagnostics & Research', 'TSX Medical Devices', 'TSX Biotechnology', 'TSX Drug Manufacturers - Major', 'TSX Health Care Plans', 'TSX Medical Care'],
    'Consumer Discretionary': ['TSX Luxury Goods', 'TSX Home Furnishings & Fixtures', 'TSX Travel Services', 'TSX Apparel Manufacturing', 'TSX Auto & Truck Dealerships', 'TSX Discount Stores', 'TSX Auto Manufacturers', 'TSX Recreational Vehicles', 'TSX Gambling', 'TSX Footwear & Accessories', 'TSX Beverages - Brewers', 'TSX Internet Retail', 'TSX Personal Services', 'TSX Electronic Gaming & Media', 'TSX Indices Consumer Discret', 'TSX Lodging', 'TSX Specialty Retail', 'TSX Apparel Stores', 'TSX Home Improvement Stores', 'TSX Consumer Electronics', 'TSX Restaurants', 'TSX Resorts & Casinos', 'TSX Entertainment', 'TSX Leisure'],
    'Financials': ['TSX Insurance - Life', 'TSX Insurance - Specialty', 'TSX Indices Financials', 'TSX Capital Markets', 'TSX Insurance - Property & Casu', 'TSX Mortgage Finance', 'TSX Banks - Regional', 'TSX Banks - Global', 'TSX Asset Management', 'TSX Credit Services', 'TSX Insurance - Diversified', 'TSX Insurance - Reinsurance', 'TSX Financial Exchanges'],
    'Communication Services': ['TSX Publishing', 'TSX Advertising Agencies', 'TSX Internet Content & Info', 'TSX Indices Telecom Services', 'TSX Telecom Services', 'TSX Broadcasting', 'TSX Communication Equipment'],
    'Real Estate': ['TSX Indices Real Estate', 'TSX Real Estate - Diversified', 'TSX REIT - Office', 'TSX REIT - Industrial', 'TSX REIT - Diversified', 'TSX REIT - Retail', 'TSX REIT - Residential', 'TSX Real Estate Services', 'TSX REIT - Healthcare Faciltes', 'TSX REIT - Specialty', 'TSX Real Estate - Development'],
    'Information Tech': ['TSX Semiconductor Equipment', 'TSX Electronic Components', 'TSX Semiconductors', 'TSX Indices Information Tech', 'TSX Software - Infrastructure', 'TSX Computer Systems', 'TSX Software - Application', 'TSX Information Technology Srvs'],
    'Industrials': ['TSX Waste Management', 'TSX Business Services', 'TSX Conglomerates', 'TSX Indices Industrials', 'TSX Airports & Air Services', 'TSX Airlines', 'TSX Security & Protection Srvs', 'TSX Pollution Treatment Controls', 'TSX Scientific & Technical Instr', 'TSX Steel', 'TSX Electrical Equipment & Parts', 'TSX Aerospace & Defense', 'TSX Auto Parts', 'TSX Specialty Industrial Machine', 'TSX Shipping & Ports', 'TSX Industrial Distribution', 'TSX Railroads', 'TSX Engineering & Construction', 'TSX Integrated Shipping & Logis', 'TSX Rental & Leasing Services', 'TSX Metal Fabrication', 'TSX Trucking', 'TSX Building Products & Equipment',  'TSX Farm & Construction Equipt', 'TSX Textile Manufacturing'],
    'Utilities': ['TSX Solar', 'TSX Indices Utilities', 'TSX Utilities Regulated Water', 'TSX Utilities Regulated Electric', 'TSX Utilities Diversified', 'TSX Utilities Independent Power', 'TSX Utilities - Renewable', 'TSX Utilities Regulated Gas'],
    'Consumer Staples': ['TSX Indices Consumer Staples', 'TSX Beverages - Soft Drinks', 'TSX Farm Products', 'TSX Packaged Foods', 'TSX Beverages - Wine & Distiller', 'TSX Confectioners', 'TSX Tobacco', 'TSX Grocery Stores', 'TSX Household & Personal Product', 'TSX Food Distribution'],
    'Materials': ['TSX Building Materials', 'TSX Indices Materials', 'TSX Specialty Chemicals', 'TSX Lumber & Wood Production', 'TSX Packaging & Containers', 'TSX Chemicals', 'TSX Coking Coal', 'TSX Agricultural Inputs', 'TSX Other Precious Metals & Mine', 'TSX Paper & Paper Products', 'TSX Industrial Metals Minerals', 'TSX Gold', 'TSX Silver', 'TSX Copper', 'TSX Thermal Coal'],
}

# barchart.com/ca industry symbols
sector_industry_symbol_mapping = {
    'TTFS': ['VINF', 'VISS', 'VTFS', 'VCPM', 'VIPC', 'VMRF', 'VBRE', 'VBAG', 'VASM', 'VCSV', 'VIND', 'VINR', 'VFIE'],
    'TTEN': ['VURA', 'VOGI', 'VTEN', 'VOGS', 'VOGD', 'VOGR', 'VOGE', 'VOGM'],
    'TTMT': ['VBMT', 'VTMT', 'VSCH', 'VLWP', 'VPKC', 'VCHE', 'VCOC', 'VAGI', 'VOPM', 'VPPP', 'VIMM', 'VGOL', 'VSIL', 'VCOP', 'VTCO'],
    'TTTK': ['VSEQ', 'VECO', 'VSEM', 'VTTK', 'VSIN', 'VCSY', 'VSAP', 'VITS'],
    'TTIN': ['VWMA', 'VMBS', 'VCOG', 'VTIN', 'VAAS', 'VAIR', 'VSPS', 'VPTC', 'VSTI', 'VSTL', 'VEEP', 'VAAD', 'VAUP', 'VSIM', 'VSPO', 'VIDD', 'VRAI', 'VEGC', 'VISL', 'VRLS', 'VMTF', 'VTRU', 'VBPE', 'VFCE', 'VTMA'],
    'TTCS': ['VTCS', 'VBSD', 'VFMP', 'VPKF', 'VBWD', 'VCOF', 'VTOB', 'VGST', 'VHPP', 'VFDD'],
    'TTUT': ['VSOL', 'VTUT', 'VURW', 'VURE', 'VUDI', 'VUIP', 'VUTR', 'VURG'],
    'TTRE': ['VTRE', 'VRED', 'VROF', 'VRIN', 'VRDV', 'VRRT', 'VRRE', 'VRES', 'VRHF', 'VRIS', 'VREV'],
    'TTTS': ['VPUB', 'VAAA', 'VICI', 'VTTS', 'VTSE', 'VBRO', 'VCEQ'],
    'TTCD': ['VLUG', 'VHFF', 'VTRS', 'VAPM', 'VATD', 'VDCS', 'VAMN', 'VRVE', 'VGAM', 'VFOA', 'VBVB', 'VITR', 'VPSS', 'VEGM', 'VTCD', 'VLOD', 'VSRE', 'VAPS', 'VHIM', 'VCOE', 'VRST', 'VRCA', 'VENT', 'VLEI'],
    'TTHC': ['VPHR', 'VMIS', 'VDMS', 'VHIS', 'VDRE', 'VMDD', 'VBIO', 'VDMM', 'VHCP', 'VMDC'],
}

# barchart.com/ca industry symbols
industry_symbols = [
    "VURA", "VPTC", "VCOC", "VBVB", "VSTI", "VSTL", "VEEP", "VOGI", "VAGI", "VTEN",
    "VOGS", "VDMS", "VHIS", "VAAD", "VITR", "VPSS", "VECO", "VEGM", "VTOP", "VDRE",
    "VRED", "VURW", "VMDD", "VROF", "VTCD", "VOGD", "VAAA", "VSEM", "VOGR", "VRIN",
    "VOGE", "VICI", "VSPS", "VTTK", "VLOD", "VAUP", "VOPM", "VBIO", "VAIR", "VCPM",
    "VSIN", "VPKF", "VURE", "VBWD", "VTXS", "VTTS", "VIPC", "VMIS", "VFMP", "VSRE",
    "VBRE", "VMRF", "VPHR", "VSIM", "VRDV", "VCOF", "VAPS", "VTSE", "VCMP", "VOGM",
    "VBAG", "VPPP", "VRRT", "VSPO", "VUDI", "VASM", "VDMM", "VFCE", "VTFS", "VCHE",
    "VRRE", "VIMM", "VTRE", "VUIP", "VHIM", "VCOE", "VRAI", "VRHF", "VBOT", "VTOB",
    "VISS", "VRES", "VTUT", "VIDD", "VPKC", "VLWP", "VHCP", "VINF", "VBSD", "VBPE",
    "VAAS", "VPUB", "VGAM", "VBRO", "VCSV", "VEGC", "VRVE", "VGST", "VTCS", "VGOL",
    "VUTR", "VTIN", "VCOG", "VRST", "VIND", "VRIS", "VRLS", "VSIL", "VCOP", "VSCH",
    "VAMN", "VDCS", "VCSY", "VTMT", "VSOL", "VISL", "VMDC", "VHPP", "VRCA", "VATD",
    "VSAP", "VURG", "VINR", "VAPM", "VFIE", "VENT", "VLEI", "VITS", "VREV", "VMTF",
    "VTRS", "VTCO", "VTRU", "VFDD", "VMBS", "VWMA", "VBMT", "VHFF", "VLUG", "VCEQ",
    "VSEQ", "VFOA"
]
