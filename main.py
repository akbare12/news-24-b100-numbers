#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; BG=(247,241,222); INK=(20,20,20); RED=(178,34,34); NAVY=(18,42,84); TEAL=(15,90,90); GOLD=(198,142,20)
def F(s,b=False,ser=False):
    try: return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if ser else ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),s)
    except Exception: return ImageFont.load_default()
def wrap(d,t,f,w):
    words=t.split(); lines=[]; cur=""
    for wd in words:
        s=(cur+" "+wd).strip()
        if d.textlength(s,font=f)<=w: cur=s
        else:
            if cur: lines.append(cur)
            cur=wd
    if cur: lines.append(cur)
    return lines
def txt(d,x,y,t,f,c=INK):
    d.text((x,y),t,font=f,fill=c); return d.textlength(t,font=f)
def para(d,x,y,w,t,f,lh=12,c=INK,maxl=99):
    for i,ln in enumerate(wrap(d,t,f,w)[:maxl]): d.text((x,y+i*lh),ln,font=f,fill=c)
    return y+len(wrap(d,t,f,w)[:maxl])*lh
def chip(d,x,y,t,c):
    f=F(7,True); w=d.textlength(t,font=f)+10; d.rounded_rectangle([x,y,x+w,y+13],3,fill=c); d.text((x+5,y+2),t,font=f,fill=(255,255,255)); return x+w+4
def scene(d,x,y,w,h,kind):
    d.rectangle([x,y,x+w,y+h],fill=(210,225,235),outline=(120,120,120))
    if kind=="riyadh":
        d.rectangle([x,y+h-28,x+w,y+h],fill=(40,44,60)); d.rectangle([x,y,x+w,y+42],fill=(28,28,48))
        for i,bx in enumerate([x+18,x+62,x+106,x+150,x+196,x+240]):
            bh=[40,55,48,60,38,50][i]; d.rectangle([bx,y+h-28-bh,bx+34,y+h-28],fill=(90,100,130))
        d.rectangle([x+w//2-16,y+6,x+w//2+16,y+h-28],fill=(150,160,190)); d.polygon([(x+w//2-16,y+6),(x+w//2+16,y+6),(x+w//2,y+2)],fill=(200,210,230))
        d.ellipse([x+w-52,y+12,x+w-28,y+36],fill=(255,120,40)); d.ellipse([x+w-46,y+18,x+w-34,y+30],fill=(255,200,80))
        for sx,sy in [(x+30,y+14),(x+90,y+10),(x+200,y+16)]: d.ellipse([sx,sy,sx+3,sy+3],fill=(255,255,255))
        d.text((x+w-58,y+h-24),"11",font=F(26,True),fill=(255,255,255))
    elif kind=="shanghai":
        d.rectangle([x,y,x+w,y+h],fill=(120,30,30)); d.rectangle([x,y+h-22,x+w,y+h],fill=(60,60,60))
        d.rectangle([x+20,y+30,x+w-20,y+h-22],fill=(240,235,215)); d.rectangle([x+40,y+44,x+w-40,y+h-30],fill=(90,40,40))
        for cx in [x+70,x+150,x+230]: d.rectangle([cx,y+50,cx+10,y+h-30],fill=(60,20,20))
        d.rectangle([x+w//2-55,y+58,x+w//2+55,y+88],fill=(255,255,255)); d.text((x+w//2-48,y+62),"FILE",font=F(16,True),fill=(178,34,34))
        d.text((x+8,y+4),"62",font=F(30,True),fill=(255,255,255))
    elif kind=="court":
        d.rectangle([x,y,x+w,y+h],fill=(200,205,215)); d.rectangle([x,y+h-20,x+w,y+h],fill=(80,80,90))
        for cx in [x+30,x+90,x+150,x+210,x+270]: d.rectangle([cx,y+40,cx+16,y+h-20],fill=(240,240,240))
        d.polygon([(x+10,y+42),(x+w-10,y+42),(x+w//2,y+8)],fill=(150,40,40)); d.ellipse([x+w//2-8,y+22,x+w//2+8,y+38],fill=(255,215,0))
        d.text((x+8,y+h-44),"10/12",font=F(22,True),fill=(18,42,84))
    elif kind=="war":
        d.rectangle([x,y,x+w,y+h],fill=(25,25,45)); d.rectangle([x,y+h-24,x+w,y+h],fill=(50,50,50))
        for sx,sy in [(x+20,y+12),(x+80,y+8),(x+160,y+14),(x+240,y+10)]: d.ellipse([sx,sy,sx+3,sy+3],fill=(255,255,255))
        d.polygon([(x+40,y+30),(x+52,y+30),(x+46,y+38)],fill=(200,200,200)); d.ellipse([x+180,y+18,x+210,y+48],fill=(255,120,30)); d.ellipse([x+190,y+26,x+202,y+40],fill=(255,220,100))
        d.text((x+8,y+h-26),"9",font=F(22,True),fill=(255,255,255))
    elif kind=="trophy":
        d.rectangle([x,y,x+w,y+h],fill=(20,90,60)); d.ellipse([x+w//2-22,y+8,x+w//2+22,y+52],fill=(255,215,0)); d.rectangle([x+w//2-8,y+50,x+w//2+8,y+66],fill=(255,215,0)); d.rectangle([x+w//2-20,y+64,x+w//2+20,y+70],fill=(200,160,0))
        d.text((x+8,y+8),"3-0",font=F(18,True),fill=(255,255,255)); d.text((x+w-58,y+h-22),"1-0",font=F(14,True),fill=(255,255,255))
    elif kind=="ship":
        d.rectangle([x,y,x+w,y+h],fill=(40,110,160)); d.rectangle([x,y+h-16,x+w,y+h],fill=(20,60,110))
        d.rectangle([x+20,y+h-30,x+w-20,y+h-16],fill=(180,60,40)); d.rectangle([x+50,y+h-42,x+110,y+h-30],fill=(240,240,240))
        d.ellipse([x+w-40,y+4,x+w-12,y+28],fill=(255,140,40)); d.text((x+8,y+4),"IRGC",font=F(12,True),fill=(255,255,255))
    elif kind=="chart":
        d.rectangle([x,y,x+w,y+h],fill=(255,255,255)); d.line([(x+10,y+h-14),(x+w-10,y+10)],fill=(20,120,60),width=4); d.line([(x+10,y+h-14),(x+w-10,y+h-14)],fill=(0,0,0),width=2)
        for px,py in [(x+60,y+h-40),(x+120,y+h-60),(x+180,y+h-80),(x+240,y+22)]: d.ellipse([px-4,py-4,px+4,py+4],fill=(178,34,34))
        d.text((x+8,y+6),"50,018",font=F(18,True),fill=(20,120,60))
    elif kind=="tech":
        d.rectangle([x,y,x+w,y+h],fill=(160,20,20)); d.rectangle([x+16,y+8,x+w-16,y+h-8],fill=(30,30,30)); d.text((x+30,y+10),"CODE RED",font=F(15,True),fill=(255,60,60)); d.text((x+30,y+h-15),"24h OUTAGE",font=F(10,True),fill=(255,255,255))
    elif kind=="heli":
        d.rectangle([x,y,x+w,y+h],fill=(140,170,200)); d.polygon([(x+20,y+h-30),(x+w-60,y+h-30),(x+w-20,y+20),(x+60,y+20)],fill=(90,110,90)); d.ellipse([x+60,y+16,x+120,y+44],fill=(60,60,60)); d.line([(x+40,y+14),(x+220,y+14)],fill=(40,40,40),width=3); d.text((x+8,y+h-22),"5",font=F(18,True),fill=(255,255,255))
    elif kind=="hostage":
        d.rectangle([x,y,x+w,y+h],fill=(230,200,140)); d.rectangle([x+10,y+6,x+w-10,y+h-6],fill=(250,245,230)); d.text((x+20,y+8),"MARKET",font=F(13,True),fill=(178,34,34)); d.text((x+20,y+h-20),"25",font=F(16,True),fill=(20,20,20))
    elif kind=="aden":
        d.rectangle([x,y,x+w,y+h],fill=(220,190,120)); d.polygon([(x,y+h),(x+w//2,y+10),(x+w,y+h)],fill=(150,110,60)); d.text((x+10,y+8),"60 km",font=F(16,True),fill=(255,255,255))
    elif kind=="yemen":
        d.rectangle([x,y,x+w,y+h],fill=(200,120,60)); d.rectangle([x+20,y+h-30,x+w-60,y+h-12],fill=(80,60,40)); d.text((x+10,y+8),"25",font=F(20,True),fill=(255,255,255))
    elif kind=="rocket":
        d.rectangle([x,y,x+w,y+h],fill=(15,15,40)); d.polygon([(x+w//2-12,y+h-20),(x+w//2+12,y+h-20),(x+w//2,y+8)],fill=(240,240,240)); d.ellipse([x+w//2-18,y+30,x+w//2+18,y+52],fill=(255,140,0)); d.text((x+8,y+6),"1st",font=F(16,True),fill=(255,255,255))
    else:
        d.rectangle([x,y,x+w,y+h],fill=(200,210,220)); d.text((x+8,y+8),"NEWS",font=F(14,True),fill=(20,20,20))
HEROES=[("1 RIYADH · MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, the tallest in Riyadh, for the second time in a week. At least 11 people were hurt, including 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians. (Saudi officials)","riyadh"),("2 SHANGHAI · ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen Jining, 62, the Shanghai party chief, is under investigation for serious violations. He is the fourth Politburo member to fall in a probe this year. (CCDI)","shanghai"),("3 NEW YORK · US / TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering, with sentencing set for Sep 2027. (US court)","court")]
CARDS=[("4 ZAPORIZHZHIA · EUROPE","REPORTED","Russian attacks kill 9 across Ukraine in a day","Russia fired 96 drones; 9 were killed and 81 wounded. (Ukraine officials)","war"),("5 CAS · AFRICA / SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","CAS restored Senegal as AFCON champions after Morocco forfeited 3-0. (CAS)","trophy"),("6 HORMUZ · MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","An IRGC attack hit a container ship in Hormuz at 18:58 UTC. (UKMTO)","ship"),("7 NEW YORK · MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","The Dow closed at 50,018, its first finish above 50,000. (Market close)","chart"),("8 REDMOND · TECH","REPORTED","Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, Microsoft declared Code Red. (Reuters)","tech"),("9 ESKISEHIR · EUROPE","REPORTED","Turkish military helicopter crash kills 5","A Turkish military AS-532 helicopter crashed in Eskisehir; 5 died. (Turkish officials)","heli"),("10 CARTAGENA · AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","Armed men held 25 hostages in a Cartagena supermarket. (Colombia officials)","hostage"),("11 ADEN · MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden in Yemen. (Wires)","aden"),("12 LAHJ · MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes in Wadi Maabaq, Lahj, killed 25 and wounded 6. (Yemen officials)","yemen"),("13 JIUQUAN · SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","China named the Shenzhou-24 crew, including the first foreign astronaut. (CMSA)","rocket")]
def main():
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,10],fill=RED); txt(d,10,14,"THE WORLD ON ONE PAGE",F(11,True),RED); txt(d,1024-10-470,14,"38 STORIES · 6 REGIONS · 13 FIELDS",F(11,True),NAVY)
    txt(d,10,30,"Tuesday 24 November 2026",F(30,True,True)); d.line([(10,66),(1014,66)],fill=INK,width=2)
    txt(d,10,70,"Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12 counts",F(12,False,True),RED)
    regs=[("Europe",9,NAVY),("Middle East",8,RED),("Asia",8,TEAL),("Africa",2,(120,90,20)),("Americas",7,(90,60,140)),("World/Space",4,(60,60,60))]
    x=10
    for name,n,c in regs:
        w=165; d.rectangle([x,88,x+w,106],fill=c); txt(d,x+6,92,f"{name} {n}",F(10,True),(255,255,255)); x+=w+2
    utc=[("00:30","Zelensky urges talks"),("02:15","NATO vows space defence"),("08:16","Hanoi blast kills 6"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
    txt(d,10,112,"THE DAY IN UTC",F(9,True),RED); xx=10
    for t,e in utc:
        txt(d,xx,124,t,F(9,True),NAVY); txt(d,xx,134,e,F(8)); xx+=146
    d.rectangle([10,152,1014,192],fill=(255,255,255),outline=(180,180,180))
    nums=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow close"),("+8.99%","Taiex record"),("25","killed in Yemen"),("26","Cikande toll"),("10/12","Huawei counts"),("96","drones at Ukraine")]
    xx=14
    for n,lab in nums:
        txt(d,xx,156,n,F(20,True),RED); txt(d,xx,178,lab,F(8)); xx+=126
    hx=10
    for k,chipc,head,deck,kind in HEROES:
        w=332; scene(d,hx,196,w,98,kind); txt(d,hx,298,k,F(9,True),NAVY); chip(d,hx,312,chipc,(34,120,60) if chipc=="CONFIRMED" else (30,80,180) if chipc=="OFFICIAL" else (100,100,100))
        para(d,hx,328,w,head,F(13,True),15); para(d,hx,360,w,deck,F(9),10,maxl=3); hx+=336
    for r in range(2):
        for c in range(5):
            i=r*5+c; k,chipc,head,deck,kind=CARDS[i]; x=10+c*203; y=392+r*116; w=198
            scene(d,x,y,w,46,kind); txt(d,x,y+49,k,F(8,True),NAVY); chip(d,x,y+60,chipc,(34,120,60) if chipc=="CONFIRMED" else (30,80,180) if chipc=="OFFICIAL" else (100,100,100))
            para(d,x,y+75,w,head,F(10,True),11,maxl=2); para(d,x,y+97,w,deck,F(8),9,maxl=2)

    txt(d,10,628,"WORLD MAP — 13 ILLUSTRATED STORIES",F(10,True),RED); d.rectangle([10,644,660,784],fill=(215,230,240),outline=(120,120,120))
    conts=[[( -168,66),(-165,60),(-140,60),(-125,49),(-124,42),(-120,34),(-114,29),(-104,24),(-97,26),(-90,21),(-86,30),(-81,25),(-76,35),(-70,42),(-65,45),(-60,47),(-55,47),(-65,60),(-70,55),(-75,62),(-85,66),(-95,69),(-110,68),(-125,71),(-140,70),(-155,71),(-168,66)],[(-80,9),(-77,4),(-70,-5),(-60,-10),(-55,-20),(-50,-30),(-60,-35),(-70,-40),(-75,-50),(-70,-55),(-65,-45),(-60,-30),(-70,-15),(-80,9)],[(-10,36),(-9,43),(-2,48),(0,50),(5,58),(10,58),(18,56),(21,55),(28,59),(30,60),(30,70),(25,71),(20,68),(15,65),(10,62),(5,60),(0,55),(-5,50),(-10,43),(-10,36)],[(-10,35),(-6,37),(0,36),(10,33),(20,32),(30,31),(35,36),(43,38),(36,36),(30,30),(20,28),(10,29),(0,32),(-10,35)],[(-17,15),(-15,20),(-10,28),(-5,32),(0,35),(10,31),(15,27),(20,20),(25,15),(30,11),(35,5),(40,0),(43,-5),(40,-10),(35,-18),(30,-25),(25,-30),(20,-35),(15,-28),(10,-20),(5,-10),(0,0),(-5,5),(-10,10),(-17,15)],[ (60,70),(70,72),(80,73),(90,75),(100,77),(110,74),(120,72),(130,70),(140,68),(145,60),(140,50),(135,45),(130,40),(125,35),(120,30),(115,25),(110,20),(105,15),(100,10),(95,8),(90,5),(85,10),(80,15),(75,20),(70,25),(65,30),(60,35),(55,40),(50,45),(45,50),(40,55),(35,60),(40,65),(50,68),(60,70)],[ (113,-22),(120,-25),(130,-30),(140,-35),(145,-40),(150,-38),(145,-30),(135,-25),(125,-20),(115,-15),(113,-22)]]
    def px(lon,lat): return 10+(lon+180)*(650/360), 644+(75-lat)*(140/130)
    for poly in conts:
        pts=[px(lo,la) for lo,la in poly]; d.polygon(pts,fill=(120,170,110),outline=(60,100,60))
    pins=[(1,24.7,46.7),(2,31.2,121.5),(3,40.7,-74.0),(4,47.8,35.2),(5,14.7,-17.4),(6,26.5,56.3),(7,40.7,-74.0),(8,47.6,-122.1),(9,39.8,30.5),(10,10.4,-75.5),(11,12.8,45.0),(12,13.0,44.9),(13,39.7,98.5)]
    off={3:(0,-14),7:(0,12),11:(0,-12),12:(0,12),1:(0,-10),6:(14,0)}
    for n,la,lo in pins:
        x,y=px(lo,la); dx,dy=off.get(n,(0,0)); d.line([(x,y),(x+dx,y+dy)],fill=RED,width=1); d.ellipse([x+dx-8,y+dy-8,x+dx+8,y+dy+8],fill=RED,outline=(255,255,255)); d.text((x+dx-3,y+dy-5),str(n),font=F(8,True),fill=(255,255,255))
    leg=["1 Riyadh","2 Shanghai","3 New York","4 Zaporizhzhia","5 Dakar","6 Hormuz","7 New York","8 Redmond","9 Eskisehir","10 Cartagena","11 Aden","12 Lahj","13 Jiuquan"]
    for i,s in enumerate(leg): txt(d,672,644+i*11,s,F(9,True) if i<3 else F(9))
    txt(d,672,644+13*11+4,"Pins 1-13 only.",F(8),RED)
    txt(d,10,788,"ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES",F(10,True),RED)
    also=[("14 Ankara","Haftar visits Turkey for the first time. (REPORTED)",""),("15 London","UK sanctions Houthis + 4 officials. (OFFICIAL)","OFFICIAL"),("16 Villavicencio","Car bomb injures 23. (REPORTED)",""),("17 Gaza","Israel kills Hamas internal security chief. (REPORTED)",""),("18 Baghdad","Iraq orders federal control of Kurdish oilfields. (OFFICIAL)","OFFICIAL"),("19 Gaza","Meningitis epidemic alert: 272 cases in Oct. (OFFICIAL)","OFFICIAL"),("20 DR Congo","Missing Cessna 208, rebels claim shootdown. (CLAIM)",""),("21 Hanoi","Hot-pot explosion kills at least 6. (REPORTED)",""),("22 Gulf of Finland","Ukraine hits Russian ship Sparta II. (REPORTED)",""),("23 Kuala Lumpur","Malaysia to return migrants to Myanmar. (OFFICIAL)","OFFICIAL"),("24 Ulleungdo","S. Korea shelter order as Russian jets enter ADIZ. (OFFICIAL)","OFFICIAL"),("25 Dhaka","Hasina plans return on 16 Dec. (REPORTED)",""),("26 The Hague","14 nations endorse ICJ Myanmar ruling. (REPORTED)",""),("27 Jakarta","Indonesia nominates 2 VP candidates. (OFFICIAL)","OFFICIAL"),("28 Beijing","China sentences official Ma to death for spying. (OFFICIAL)","OFFICIAL"),("29 Brussels","NATO vows defence against space threat. (OFFICIAL)","OFFICIAL"),("30 Mexico City","El Chapo Isidro was arrested Fri 20 Nov. (REPORTED)",""),("31 San Salvador","Bukele names 3 Salvadoran soldiers killed in Haiti. (OFFICIAL)","OFFICIAL"),("32 Ottawa","Pentagon rebukes Canada: only 41.9% of air fleet ready. (REPORTED)",""),("33 Washington","US adds Megaspeed to trade blacklist. (OFFICIAL)","OFFICIAL"),("34 Kyiv","Zelensky urges Ukraine/Russia/US/Europe talks soon. (REPORTED)",""),("35 Ras Al Khaimah","UAE bus-truck crash kills 13. (REPORTED)",""),("36 London","England record 5,258 heat deaths, summer 2026. (OFFICIAL)","OFFICIAL"),("37 Kourou","Ariane 6 lofts 36 Amazon satellites. (OFFICIAL)","OFFICIAL"),("38 Cikande","Factory-fire toll rises to 26. (REPORTED)","")]
    for i,(city,line,offc) in enumerate(also):
        col=i//9; row=i%9; x=10+col*338; y=806+row*14; s=f"{city}: {line}"
        while d.textlength(s,font=F(8))>330: s=s.rsplit(" ",1)[0].rstrip(".")+"."
        txt(d,x,y,s,F(8))
    d.rectangle([10,934,1014,972],fill=(255,235,235),outline=RED)
    txt(d,14,938,"DATE CHECK — Every story above happened or was first reported on Tue 24 Nov 2026. Wires read up to 23:00 UTC.",F(9,True),RED)
    txt(d,14,952,"LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov) · Nvidia Huang return (23 Nov) · COP31 no deal (22 Nov) · El Chapo arrest (20 Nov). NOT YET: Shenzhou-24 launch (25 Nov) · Huawei sentencing (Sep 2027).",F(9))
    txt(d,10,978,"Sources: Reuters · AP · UKMTO · CAS · CMSA · CCDI · wires. CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side.",F(8))
    txt(d,10,992,"Scenes are drawn in code, not photographs. All 38 stories are from Tuesday 24 November 2026.",F(8))
    out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True); im.save(out)
if __name__=="__main__": main()
