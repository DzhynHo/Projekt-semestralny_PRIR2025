from pymongo import MongoClient

client = MongoClient("mongodb+srv://valeriiakhylchenko:E4JSfcv8ytUWtBlH@cluster0.b6hq2v2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['buddhist']
coll = db['monasteries']
#E4JSfcv8ytUWtBlH
monasteries = [
    {
        "name": "Wat Pho",
        "location": "Bangkok, Thailand",
        "gps": {"lat": 13.7466, "lon": 100.4930},
        "website": "https://watpho.com",
        "image": "Wat_Pho.jpg",
        "description": (
            "Wat Pho to jedna z najstarszych i największych świątyń w Bangkoku. "
            "Jest znana przede wszystkim z ogromnego posągu Leżącego Buddy, mierzącego 46 metrów długości. "
            "To także miejsce narodzin tradycyjnego masażu tajskiego, a szkoła masażu przy świątyni jest uznawana na całym świecie. "
            "Wnętrza świątyni są bogato zdobione licznymi freskami i rzeźbami, które opowiadają historię buddyzmu. "
            "Wat Pho to obowiązkowy punkt dla każdego turysty odwiedzającego Bangkok."
        )
    },
    {
        "name": "Shwedagon Pagoda",
        "location": "Yangon, Myanmar",
        "gps": {"lat": 16.7983, "lon": 96.1498},
        "website": "https://www.shwedagonpagoda.com",
        "image": "Shwedagon_Pagoda.jpg",
        "description": (
            "Shwedagon Pagoda jest najważniejszym i najświętszym miejscem buddyzmu w Mjanmie. "
            "Jej złoty pagoda, sięgająca ponad 99 metrów, lśni w słońcu dzięki tysiącom złotych płytek i cennych kamieni szlachetnych. "
            "To miejsce pielgrzymek setek tysięcy wiernych oraz turystów z całego świata. "
            "Legenda głosi, że pagoda ma ponad 2500 lat i zawiera relikwie samego Buddy. "
            "Odwiedzający mogą uczestniczyć w rytuałach, medytacjach i podziwiać niesamowitą architekturę."
        )
    },
    {
        "name": "Boudhanath Stupa",
        "location": "Kathmandu, Nepal",
        "gps": {"lat": 27.7215, "lon": 85.3620},
        "website": "https://www.welcomenepal.com/places-to-see/boudhanath.html",
        "image": "Boudhanath_stupa.jpg",
        "description": (
            "Boudhanath to jedna z największych stup na świecie i ważne miejsce kultu buddyjskiego w Nepalu. "
            "Jej ogromna, biała kopuła dominuje nad okolicą i jest otoczona przez mnóstwo modlących się pielgrzymów. "
            "Stupa została wpisana na listę światowego dziedzictwa UNESCO i jest centrum życia religijnego tybetańskiej diaspory. "
            "Wokół stupy znajdują się liczne klasztory, sklepy z rękodziełem i kawiarnie, tworząc unikalną atmosferę. "
            "To idealne miejsce, by poznać buddyjskie tradycje i kulturę Nepalu."
        )
    },
    {
        "name": "Tōdai-ji",
        "location": "Nara, Japan",
        "gps": {"lat": 34.6889, "lon": 135.8399},
        "website": "https://www.japan-guide.com/e/e4100.html",
        "image": "Todai_ji.jpg",
        "description": (
            "Tōdai-ji to jedna z najsłynniejszych świątyń buddyjskich w Japonii, słynąca z ogromnego posągu Wielkiego Buddy – Daibutsu. "
            "Świątynia została zbudowana w VIII wieku i odgrywa ważną rolę w historii i kulturze Japonii. "
            "Budowla jest znana z imponującej architektury oraz pięknych ogrodów otaczających kompleks. "
            "Tōdai-ji pełni także funkcję klasztoru i centrum naukowego buddyzmu. "
            "Każdego roku przyciąga tłumy turystów i pielgrzymów, którzy chcą zobaczyć tę perłę japońskiego dziedzictwa."
        )
    },
    {
        "name": "Mahabodhi Temple",
        "location": "Bodh Gaya, India",
        "gps": {"lat": 24.6950, "lon": 84.9912},
        "website": "https://www.bodhgaya.gov.in",
        "image": "Mahabodhi_Temple.jpg",
        "description": (
            "Mahabodhi Temple jest miejscem, gdzie Budda Siddhartha osiągnął oświecenie pod Drzewem Bodhi. "
            "To jedno z najważniejszych miejsc pielgrzymkowych dla buddystów z całego świata. "
            "Świątynia ma ponad 2000 lat i jest wpisana na listę światowego dziedzictwa UNESCO. "
            "Architektura świątyni jest przykładem starożytnej indyjskiej sztuki sakralnej. "
            "Na terenie kompleksu znajdują się liczne posągi, kaplice i ogrody sprzyjające medytacji."
        )
    },
    {
        "name": "Jokhang Temple",
        "location": "Lhasa, Tibet",
        "gps": {"lat": 29.6536, "lon": 91.1171},
        "website": "https://en.wikipedia.org/wiki/Jokhang",
        "image": "Jokhang_Temple.jpg",
        "description": (
            "Jokhang to najświętsza świątynia tybetańskiego buddyzmu, zlokalizowana w sercu Lhasy. "
            "Świątynia przyciąga tysiące pielgrzymów, którzy przybywają, by oddać cześć Buddzie. "
            "Budowla pochodzi z VII wieku i łączy w sobie elementy architektury tybetańskiej, chińskiej i indyjskiej. "
            "Wewnątrz znajdują się cenne relikwie oraz słynne posągi buddyjskie. "
            "Jokhang jest również ważnym centrum duchowym i kulturowym Tybetu."
        )
    },
    {
        "name": "Borobudur",
        "location": "Magelang, Indonesia",
        "gps": {"lat": -7.6079, "lon": 110.2038},
        "website": "https://borobudurpark.com",
        "image": "Borobudur.jpg",
        "description": (
            "Borobudur jest największą buddyjską świątynią na świecie, zbudowaną w IX wieku. "
            "Świątynia ma formę ogromnej mandali i składa się z wielu poziomów ozdobionych reliefami. "
            "Jest miejscem pielgrzymek i ważnym symbolem kultury indonezyjskiej. "
            "Borobudur jest wpisany na listę światowego dziedzictwa UNESCO i co roku odwiedzany przez tysiące turystów. "
            "Jego architektura i sztuka są dowodem na rozwój buddyzmu w Azji Południowo-Wschodniej."
        )
    },
    {
        "name": "Haeinsa Temple",
        "location": "South Korea",
        "gps": {"lat": 35.8019, "lon": 128.0945},
        "website": "https://www.templestay.com",
        "image": "Haeinsa_Temple.jpg",
        "description": (
            "Haeinsa to jeden z najważniejszych klasztorów buddyjskich w Korei Południowej. "
            "Znany jest przede wszystkim z przechowywania Tripitaka Koreana – kompletu buddyjskich pism wydrukowanych na drewnianych tabliczkach. "
            "Klasztor znajduje się w malowniczym rejonie górskim i oferuje programy dla gości, którzy chcą poznać buddyjskie życie. "
            "Haeinsa jest ważnym centrum medytacji i praktyk duchowych. "
            "Jego unikalna kolekcja tekstów jest uważana za jedno z najważniejszych dziedzictw kulturowych Korei."
        )
    },
    {
        "name": "Fo Guang Shan",
        "location": "Kaohsiung, Taiwan",
        "gps": {"lat": 22.7522, "lon": 120.5136},
        "website": "https://www.fgs.org.tw",
        "image": "Fo_Guang_Shan.jpg",
        "description": (
            "Fo Guang Shan to nowoczesny klasztor buddyjski i centrum kulturalne na Tajwanie. "
            "Znany jest z ogromnego, 108-metrowego posągu Buddy, który jest jednym z najwyższych na świecie. "
            "Klasztor promuje humanistyczny buddyzm i prowadzi liczne działania edukacyjne i społeczne. "
            "Na terenie kompleksu znajdują się muzea, świątynie i ogrody, które przyciągają miliony odwiedzających rocznie. "
            "Fo Guang Shan jest ważnym miejscem spotkań i dialogu międzykulturowego."
        )
    },
    {
        "name": "Kek Lok Si",
        "location": "Penang, Malaysia",
        "gps": {"lat": 5.3994, "lon": 100.2736},
        "website": "https://www.penang.ws/penang-attractions/kek-lok-si.htm",
        "image": "Kek_Lok_Si.jpg",
        "description": (
            "Kek Lok Si jest największą świątynią buddyjską w Malezji, położoną na wzgórzu Penang. "
            "Jest znana z unikalnej architektury łączącej elementy chińskie, tajskie i birmańskie. "
            "W świątyni znajduje się ogromny posąg bogini Miłosierdzia Kuan Yin oraz wieża pagody o siedmiu piętrach. "
            "To popularne miejsce pielgrzymek oraz atrakcja turystyczna. "
            "Kek Lok Si słynie także z pięknych dekoracji podczas świąt buddyjskich."
        )
    },
    {
    "name": "Benchen Karma Kamtsang Centre",
    "location": "Grabnik, Poland",
    "gps": {"lat": 51.8242, "lon": 20.6445},
    "website": "https://www.benchen.org.pl/en/our-centres/benchen-centre-in-grabnik/",
    "image": "Grabnik.jpg",
    "description": (
        "Centrum Benchen Karma Kamtsang w Grabniku to buddyjski klasztor tradycji tybetańskiej Karma Kamtsang, "
        "założony w 1995 roku. Położone w malowniczej wsi Grabnik, około 40 km od Warszawy, centrum jest miejscem "
        "medytacji, retreatów oraz nauk pod przewodnictwem tybetańskich lamów. Regularnie organizowane są tutaj "
        "seminaria, praktyki medytacyjne oraz studiowanie klasycznych tekstów buddyjskich. Centrum jest także miejscem "
        "trzyletniego retreatu 'Benchen Drubde Osal Ling' oraz posiada bibliotekę materiałów do praktyki buddyjskiej."
    )
},
{
    "name": "Świątynia Białego Lotosu",
    "location": "Czerkasy, Ukraina",
    "gps": {"lat": 49.4444, "lon": 32.0598},
    "website": "https://uk.wikipedia.org/wiki/Храм_Білого_Лотоса",
    "image": "Bilyj_Lotos.jpg",
    "description": (
        "Świątynia Białego Lotosu to neobuddyjska świątynia w mieście Czerkasy na Ukrainie, "
        "gdzie działa również szkoła sztuk walki. Świątynia ta pełni funkcję centrum duchowego "
        "oraz miejsca nauki i praktykowania filozofii buddyjskiej."
    )
}
]


coll.delete_many({})
coll.insert_many(monasteries)


