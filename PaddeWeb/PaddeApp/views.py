from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now
    return render(
        request,
        "PaddeApp/index.html",
        {
            'content' : "Skildpadder (latin: Testudines) er en orden krybdyr/reptilier, og opstod for cirka 220 millioner år siden. Man inddeler skildpadder den dag i dag i 341 arter med 200 underarter. Skildpadder er vekselvarme æglæggere, som evolutionsmæssigt har en stor tilpasningevne. Skildpadder kan både leve på land og i vand, alt efter hvilken art de tilhører, og eksisterer både som vilde dyr og som kæledyr. Skildpadder er et helt almindeligt dansk husdyr. De er som regel lette at have med at gøre og passer for det meste sig selv. Nogle skildpadder kan dog godt være aggressive og kan finde på at bide. Trods navnet er skildpadder ikke padder.",
        }
        )
def udbredelse(request):
    now = datetime.now
    return render(
        request,
        "PaddeApp/udbredelse.html",
        {
            'content' : "Med undtagelse af de polare regioner bebor skildpadder alle kontinenter. De forekommer i mange forskellige slags omgivelser, i tropiske skove og sumpe, ørkener og halvørkener, søer, damme, floder, brakvandsområder og oceaner, i tempererede, tropiske og subtropiske klimaer."    
        }       
    )
def skjoldet(request):
    now = datetime.now
    return render(
        request,
        "PaddeApp/skjoldet.html",
        {
            'content' : "Skjoldet, som udgør omkring 30% af vægten, er uden tvivl det afgørende kendetegn. Ingen andre hvirveldyr har en sammenligneliganatomi. Ligesom insekternes exoskelet, omslutter skildpaddernes skjold, som består af rygskjoldet (carapax) og bugskjoldet (plastron), alle vigtige organer og kropsdele. Rygskjoldet består af massive knogleplader, som evolutionsmæssigt har udviklet sig fra ryghvirvler og ribben fra hvirveldyrs endoskelet. Skulderbladet (latin scapula), har skubbet sig ind under ribbenene, modsat alle andre hvirveldyr.[1] Dette ret stive rygskjold kræver en tilpasning af vejrtrækningen, som skal understøttes af ekstremiteternes bevægelse og deres kraftige muskler. Over knogleskjoldet findes enten et læderagtigt hudlag (fx hos blødskjoldskildpadder) eller et hornlag (scuta) af keratin. Bruskskjoldenes farve afhænger primært af, hvor ​​skildpadden stammer fra, for de fleste arter tilpasser deres farve til omgivelserne. I visse skildpaddearter fornyr hornskjoldet sig idet det gamle yderlag løsner sig og det nye kommer til syne. I andre skildpaddearter opstår der årringe og det yderste af hornskjoldet slides."
    }    
     )

def sanser(request):
    now = datetime.now
    return render(
        request,
        "PaddeApp/sanser.html",
        {
            'content' : "Skildpadder har et godt syn. De kan genkende flere farver end mennesker, fordi deres øjne har fire forskellige farvereceptorer, ligesom alle krybdyr. De er således også i stand til at opfatte dele af det infrarøde og det ultraviolette farvespektrum. Gråtoner synes de imidlertid at kunne skelne dårligere. Skildpadder er mestendels stumme. Undtagelsen er hvis de bliver forskrækkede. Visse skildpadder udstøder en hvæsende-hvislende lyd når de trækker hovedet tilbage i skjoldet. Vandskildpadder kan lejlighedsvis også udstøde truende hvæs. Mange hanner udstøder også ved parringen bip- eller stønnelyde, ligesom hunnerne ind i mellem gør det under kampen om de bedst ynglepladser med andre hunner. Landskildpadder kan få en slags kortvarig hikke hvis de i hast spiser frugt eller små snegle. Nyere forskning af et team ledet af Camila Ferrera fra det brasilianske Wildlife Conservation Society og Richard Vogt fra Amazonas Research Institute i Manaus har fundet ud af, at der i det lave frekvensområde foregår akustisk komtmellem individer. Hunner kommunikerer med nyklækkede. Embryoner udveksler oplysninger - før klækning - med hinanden akustisk, muligvis for atsynkronisere klækketidspunktet.[2]Ved 220 millioner og 160 millioner år gamle skildpaddefossiler har man opdaget tænder, som dog i løbet af evolutionen har trukket sig tilbage. Skildpadder har i dag ikke tænder, men hornnæb som kan bruges som kraftigt skæreværktøj. Som alle krybdyr tygger skildpadder ikke deres mad, men sluger dem enten i helt tilstand eller de river det i stykker med munden, hvor forbenene tages til hjælp."
        }
    )
def om(request):
    now = datetime.now
    return render(
        request,
        "PaddeApp/om.html",
        {
            'content' : "Om PaddeWeb"
        }
    )
# Create your views here.
