import pandas as pd
df = pd.read_csv(r"C:\Users\jan03\PycharmProjects\maturarbeit\finaldatasetforprogram.csv")
print(df)
"def index_maker(name,pop,GDP1,GDP2,gini,unemp1,unemp2,life1,life2,fat,inf1,inf2,lit1,lit2,pisa,edu1,edu2,migra,GHG1,GHG2,fert,foss1,foss2):"
def base_development(pop,gini,unemp2,life2,fat,inf2,lit2,pisa,edu2,migra,hom,bat,fert):
    min_hom = 0
    max_hom = 50
    min_bat = 0
    max_bat = 10000
    min_gini = 22.7
    max_gini = 63
    max_emp = 33.6
    min_emp = 0.25
    life_min = 53.6
    life_max = 85.5
    fat_min = 2
    fat_max = 61
    inf_min = 1.5
    inf_max = 80.5
    lit_min = 22
    lit_max = 100
    pisa_max = 580
    pisa_oecd = 488
    edu_min = 1.5
    edu_max = 14.1
    migra_min = -41
    migra_max = 31
    fert_max, fert_min = 6.8, 0.8

    gini_score = (gini - min_gini)/(max_gini - min_gini)
    emp_score = (unemp2 - min_emp)/(max_emp - min_emp)   ######fix unemployment
    ec_score = 1 - (gini_score + emp_score)/2

    life_score = (life2 - life_min)/(life_max - life_min)
    fat_score = 1 - (fat - fat_min)/(fat_max - fat_min)
    inf_score = 1 - (inf2 - inf_min)/(inf_max - inf_min)
    health_score = (life_score + fat_score + inf_score)/3

    lit_score = (lit2 - lit_min)/(lit_max - lit_min)
    eduyear_score = (edu2 - edu_min)/(edu_max - edu_min)
    if pisa > pisa_oecd:
        pisa_coefficient = 1 + 0.2 * (pisa - pisa_oecd)/(pisa_max - pisa_oecd)
    else:
        pisa_coefficient=1
    edu_score = (pisa_coefficient*(lit_score + eduyear_score)/2)/1.2

    migration_score = (migra - migra_min)/(migra_max - migra_min)
    fert_score = 1 - (fert - fert_min) / (fert_max - fert_min)            ####fix fertility
    demographic_score = (migration_score + fert_score)/2

    homicide_score = 1 - (hom - min_hom)/(max_hom - min_hom)
    battle_score = 1 - (bat - min_bat)/(max_bat - min_bat)
    safety_score = (homicide_score + battle_score)/2

    base_development_score = (edu_score + health_score + ec_score + demographic_score + safety_score)/5
    return base_development_score
def growth_coefficient(name, pop,GDP1,GDP2,unemp1,unemp2,life1,life2,inf1,inf2,lit1,lit2,edu1,edu2,GHG1,GHG2,foss1,foss2):
    GDPspan_min,GDPspan_max = 0.5, 6.3
    unemp_span = 5
    life_span_min,life_span_max = 0.99, 1.5
    infspan_min, infspan_max = 0.4, 5
    litspan_min, litspan_max = 0.95, 3.1
    eduspan_min, eduspan_max = 0.95, 2.1
    GHGspan_min,GHGspan_max = 0.1, 3 ######################################ATTTENTIONNN
    GDPgrowth = ((GDP2/GDP1)-GDPspan_min)/(GDPspan_max-GDPspan_min)
    unemp_growth = (unemp1/unemp2)/unemp_span
    life_growth = ((life2/life1)-life_span_min)/(life_span_max-life_span_min)
    inf_growth = ((inf1/inf2)-infspan_min)/(infspan_max-infspan_min)
    lit_growth = ((lit2/lit1)-litspan_min)/(litspan_max-litspan_min)
    edu_growth = ((edu2/edu1)-eduspan_min)/(eduspan_max-eduspan_min)
    GHG_growth = ((GHG1/GHG2)-GHGspan_min)/(GHGspan_max-GHGspan_min)
    totalgrowth = (GDPgrowth + unemp_growth + life_growth +inf_growth + lit_growth + edu_growth +GHG_growth)/7
    growth_coeff = 1 + totalgrowth/2
    return growth_coeff, totalgrowth
def climate_divisor(name,pop,GHG2, foss2):
    GHGmax,GHGmin = 4*10**-5,0
    foss_min, foss_max = 0,100
    GHG_score = ((GHG2/pop)-GHGmin)/(GHGmax-GHGmin)
    foss_score = (foss2 - foss_min)/(foss_max-foss_min)
    sustainability_div = (GHG_score + foss_score)/2
    return sustainability_div

    #print(name,"ec score:", ec_score, "health score:", health_score, "edu_score:",edu_score, "pisacoeff:",pisa_coefficient,"lit:",lit_score, eduyear_score)
namelist = []
baselist = []
grlist = []
coeflist = []
sustlist = []
raw_indexlist = []
for i in range(0,176):
    name = df.loc[i][0]
    pop = df.loc[i][1]
    GDP1 = df.loc[i][2]
    GDP2 = df.loc[i][3]
    gini = df.loc[i][4]
    unemp1 = df.loc[i][5]
    unemp2 = df.loc[i][6]
    life1 = df.loc[i][7]
    life2 = df.loc[i][8]
    fat = df.loc[i][9]
    inf1 = df.loc[i][10]
    inf2 = df.loc[i][11]
    lit1 = df.loc[i][12]
    lit2 = df.loc[i][13]
    pisa = df.loc[i][14]
    edu1 = df.loc[i][15]
    edu2 = df.loc[i][16]
    migra = df.loc[i][17]
    GHG2 = df.loc[i][18]
    GHG1 = df.loc[i][19]
    fert = df.loc[i][20]
    foss1 = df.loc[i][21]
    foss2 = df.loc[i][22]
    hom = df.loc[i][23]
    bat = df.loc[i][24]

    base = base_development(pop,gini,unemp2,life2,fat,inf2,lit2,pisa,edu2,migra,hom,bat,fert)
    growth, gr = growth_coefficient(name, pop, GDP1, GDP2, unemp1, unemp2, life1, life2, inf1, inf2, lit1, lit2, edu1, edu2, GHG1,
                       GHG2, foss1, foss2)
    sustainabilty = climate_divisor(name,pop,GHG2,foss2)
    total_index = ((base)**2 * growth)/(1 + sustainabilty)
    namelist.append(name)
    baselist.append(base)
    grlist.append(gr)
    coeflist.append(growth)
    sustlist.append(sustainabilty)
    raw_indexlist.append(total_index)
    ##print(name, "base score:", base, "growth coefficient:",growth, "sustainability divisor:", sustainabilty, "INDEX:",total_index)
    print(name, "INDEX VALUE:",total_index, base, growth, sustainabilty)
index_max = max(raw_indexlist)
index_min = min(raw_indexlist)
index_norm_list = []
for i in range(len(raw_indexlist)):
    index_val = (raw_indexlist[i] - index_min)/(index_max - index_min)
    index_norm_list.append(index_val)
data = pd.DataFrame([namelist,baselist,grlist,coeflist,sustlist,raw_indexlist,index_norm_list],("Country Name","Base Development Index","Growth Index","Growth Coefficient","Climate Divisor","Raw Index","Normalized Index"))
print(data)

file_name = "results7.xlsx"
data.to_excel(file_name)
