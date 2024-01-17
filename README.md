# 231RDC045 (Vasilisa Živjuka RDCP0) skolnieces projekta darbs
  Kā visiem dtorspēlētājiem, tā arī man, patīk dažreiz uzspēlēt onlain spēlēs "klikerus", kas pēc savas būtības izskatās kā lieka laika tērēšana, bet dažreiz apakšspēles sižets ir tik aizraujošs, ka gribās tomēr pabeigt. Tāpēc es jau sen aizdomājos par "klikera" izveidošanu.

  Nedaudz par izstrādes procesu:
  
  Vispirms es gribēju automatizēt vienas konkrētas spēles gaitu, bet izmantojos 'selenium' bibleotēku nekādīgi nevarēje tikt pie atsevišķiem elementiem spēles laukumā (tos nebija HTML kodā), tāpēc aizdomājos par kursora atrašanas vietu un to izmantošanu tālākāja procesā. Es sāku pētīt un vairāk lasīt par bibliotēku 'mouse', kur parādās iespēja ar vienu rindiņu iedarbināt klikšķi. Tālāk radijās problēma ar komandas iedarbināšanu (muļķīgi likt time.sleep(..), jo nav zināms cik ilgu laiku terēs spēlētājs uz to aktivāciju), tāpēc prātā iešaujās ideja par karstām pogām jeb 'hotkey'. Izrādās kā biblieotēka 'keyboard' dod iespēju pašam izveidot tādus. Biju priecīgi pārsteigta, jo nezināju, ka to izdarīt ir tik viegli.
  
  Galu galā izveidoju divus failus. Vienā ar vārdu "CLICK.py" var apskatīt tikai klikera darbību. Kods nav liels, bet izpilda galveno prasību aktivizētie, kad nospiests 'Alt + C' un apstāties pēc atkārtotas.
  Otrā failā "231RDC045.py" var redzēt izlēcošo informāciju/instrukciju terminālā priekšs saņemēja, kā lietot 'automātisko-klikeru', kā arī ir iespēja uzreiz ievadīt saiti uz savu mīļāko spēli un sākt spēlēt.


  Bibliotēkas:

  'Selenijum' bibliotēka (tieši webdriver.chrome.service), lai tiktu klāt pie Chrome vides, atvert to un ievadīt url, kas dod piekļauju pie saitēm. 
  'Mouse' bibleotēka priekš vienas komandas (mouse.double_click(button='left')), lai kliksķinātu uz peles.
  'Keyboard' bibleotēka, lai izveidot karstu pogu.
  'Time' bibleotēka, lai noturēt pauzas pēc klikšķiem un infomācijas nodošanas.

  Nobeigumā:

  Man patika veidot savu mazu projektu tieši tāpēc kā izveidoju kaut ko priekš sevis un uzzināju klāt jaunas, interesējošas lietas. Godīgi sakot, ja ne šīs kurss diezvai es ķertos klāk Pyton valodai, bet tomēr saprotu, ka šīs projekts ir tālu no tēmām, ko apskatījām studiju programmā. Ceru, ka mana interpritācija automatizēšanas procesā būs pieņemta. :)
