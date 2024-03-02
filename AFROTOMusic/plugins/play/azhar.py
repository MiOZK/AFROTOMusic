import asyncio
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from AFROTOMusic import app
import random

chat = []


@app.on_message(filters.group, group = 768)
async def azkarr(c, msg):
  if msg.text == "تفعيل الاذكار":
    if msg.chat.id in chat:
      return await msg.reply_text("- الاذكار متقعله من قبل")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("تم تفعيل الاذكار")
  elif msg.text == "تعطيل الاذكار":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("تم تعطيل الاذكار")
    else:
      return await msg.reply_text("- الاذكار متعطله من قبل")
      


async def azkar():
   azkarl = [
   "لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
   "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
   "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
   "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "سبحان الله وبحمده سبحان الله العظيم🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
   "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
   "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
   "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
   "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
   "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
   "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
   "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
   "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
   "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
   "استغفر الله العظيم وأتوبُ إليه.",
   "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
   " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
   "ماتستغفر ربنا كده🥺❤️",
   "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
   "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
   "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
   "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
   "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
   "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
   "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
   "أصبحنا وأصبح الملك لله ولا اله الا الله.",
   "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
   "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
   "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
   "- اللهم القبول الذي لا يزول ❤️🍀.",
   "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
   "سبحان الله وبحمده ،سبحان الله العظيم.",
   "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
   " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
   "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
   "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
   "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
   "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
   "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
   "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
   "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
   "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
   "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت 🌿💜.",
   "- وبك أصبحنا يا عظيم الشأن 🍃❤️.",
   "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
   "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
   "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
   "صلي على النبي بنيه الفرج❤️",
   "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
   "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
   "لا اله الا الله سيدنا محمد رسول الله🌿💜",
   "قول معايا - استغفر الله استفر الله استغفر الله -",
   "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
   "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
   "صلي على اشرف الخلق سيدنا محمد صلاةً الله عليه وسلم تسليما كثيرا ❤️",
   "ربي اجعلني مقيم الصلاة ومن ذريتي ربنا وتقبل دعاءنا . ربنا تقبل منا إنك أنت السميع العليم وتب علينا إنك أنت التواب الرحيم",
   "رب اغفر لي خطيئتي يوم الدين❤️",
   "اللهم اهدني فيمن هديت، وعافني فيمن عافيت، وتولني فيمن توليت، وبارك لي فيما أعطيت، وقني شرما قضيت، إنه لا يذل من واليت، تباركت ربنا وتعاليت",
   "اللهم إني أعوذ بك من عذاب النار، وأعوذ بك من عذاب القبر، وأعوذ بك من الفتن ما ظهر منها وما بطن، وأعوذ بك من فتنة الدجال",
   "اللهم إني أعوذ بك من علم لا ينفع وعمل لا يرفع وقلب لا يخشع وقول لا يسمع",
   "اللهم لا تخزني يوم القيامة",
   "اللهم إني أعوذ بك من صلاة لا تنفع",
   "اللهم إني أسألك الفردوس أعلى الجنة",
   "أَعـوذُ بِكَ مِنْ شَـرِّ ما صَنَـعْت، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ. مرة واحدة",
   "اللهم يا رحمن يا حنان يا منان استودعك يا رب قلبي فلا تجعل فيه أحدا سواك واستودعتك شهادة لا إله إلا الله فألهمني بها يا رب عند الممات واستودعك اللهم نفسي فلا تجعلني أخطو خطوة واحدة إلا في مرضاتك واستودعك روقي وعافيتي فاحفظها لي.",
   "اللهم يا كريم يا ودود يا رحيم يا عظيم انك قادر على كل شيء انك تقول للشيء كن فيكون ارحم اهلي رحمة دائمة واجعلهم من أهل الجنه في الفردوس لأعلي اللهم تقبلهم إليك واسعدهم بلقائك",
   "اللهم يا رحمن يارحيم ارحمني برحمتك الواسعه يارب ونقني من زنوبي مثل نقاء الثوب الأبيض من الدنس",
   "رَبَّنَا اغفِر لي وَلِوالِدَيَّ وَلِلمُؤمِنينَ يَومَ يَقومُ الحِسابُ",
   "رَّبِّ اغْفِرْ لِي وَلِوَالِدَيَّ وَلِمَن دَخَلَ بَيْتِيَ مُؤْمِنًا وَلِلْمُؤْمِنِينَ وَالْمُؤْمِنَاتِ وَلَا تَزِدِ الظَّالِمِينَ إِلَّا تَبَارًا",
   "اللهمَّ اغفر لوالدي وارحمهما كما ربّياني صغيراً، اللهمّ يا باسط اليدين بالعطايا ابسط على والدي من فضلك العظيم وجودك الواسع ما تشرح به صدرهما لعبادتك وطاعتك، والأنس بك والعمل بما يُرضيك، وبارك لهما في عُمرها، واغنهما من فضلك، وأعنهما في حلّهما وترحالهما وذهابهما وإيابهما، وأطل في عمرهما مع العافية في صحتهما ودِينهما، واجعل اللهمَّ آخر كلامهما من الدنيا لا إله إلّا الله محمدٌ رسول الله",
   "(اللَّهُمَّ إِنِّي أَسْأَلُكَ الْعَفْوَ وَالْعَافِيَةَ فِي الدُّنْيَا وَالآخِرَةِ، اللَّهُمَّ إِنِّي أَسْأَلُكَ الْعَفْوَ وَالْعَافِيَةَ: فِي دِينِي وَدُنْيَايَ وَأَهْلِي، وَمَالِي، اللَّهُمَّ اسْتُرْ عَوْرَاتِي، وَآمِنْ رَوْعَاتِي، اللَّهُمَّ احْفَظْنِي مِنْ بَينِ يَدَيَّ، وَمِنْ خَلْفِي، وَعَنْ يَمِينِي، وَعَنْ شِمَالِي، وَمِنْ فَوْقِي، وَأَعُوذُ بِعَظَمَتِكَ أَنْ أُغْتَالَ مِنْ تَحْتِي)).",
   "يا حيّ يا قيّوم برحمتك أستغيث أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عينٍ أبداً ...",
   "‏﴿ وَاذْكُر ربّكَ إِذَا نَسِيتَ ﴾ ",
   "- اللهم صلِ وسلم على نبينآ محمد ❥⇣",
   "((اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَى نَبَيِّنَا مُحَمَّدٍ)) (عشرَ مرَّاتٍ).",
   "اللهم يا عزيز يا جبار اجعل قلوبنا تخشع من تقواك واجعل عيوننا تدمع من خشياك واجعلنا يا رب من أهل التقوى وأهل المغفر",
   "استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب الي",
   "اللهم إنك عفو تُحب العفو فاعفُ عن",
   "اللهم إني أسألك الثبات في الامر والعزيمة على الرشد واسالك قلبا سليما ولسانا صادقا واسالك شكر نعمتك و حسن عبادت",
   "اللهم إني أسألك العافية في الدنيا والآخرة، اللهم إني أسألك العفو والعافية في ديني ودنياي، وأهلي ومالي، اللهم استُر عوراتي، وآمِن رَوعاتي، اللهم احفظني من بين يدي ومن خلفي، وعن يميني وعن شمالي، ومن فوقي، وأعوذ بعظمتك أن أُغتال من تحتي",
   "((اللَّهُمَّ قِنِي عَذَابَكَ يَوْمَ تَبْعَثُ عِبَادَكَ)).",
   "((لاَ إِلَهَ إِلاَّ اللَّهُ، وَحْدَهُ لاَ شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ)) (مائةَ مرَّةٍ).",
   "((اللَّهُمَّ عَالِمَ الغَيْبِ وَالشَّهَادَةِ فَاطِرَ السَّمَوَاتِ وَالْأَرْضِ، رَبَّ كُلِّ شَيْءٍ وَمَلِيكَهُ، أَشْهَدُ أَنْ لاَ إِلَهَ إِلاَّ أَنْتَ، أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي، وَمِنْ شَرِّ الشَّيْطانِ وَشِرْكِهِ، وَأَنْ أَقْتَرِفَ عَلَى نَفْسِي سُوءاً، أَوْ أَجُرَّهُ إِلَى مُسْلِمٍ))",
   "اللهم اكفني بحلالك عن حرامك، وأغنني بفضلك عمن سواك",
   "(بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، وَلَاَ حَوْلَ وَلَا قُوَّةَ إِلاَّ بِاللَّهِ)",
   "((أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ)) (مِائَةَ مَرَّةٍ فِي الْيَوْمِ).",
   "اللهم نشكوا إليك ضعفنا وقلة حيلتنا من امرنا فأغثنا وارحمنا واغفرلنا ولا تكل امرنا لمن لايخافك ولا يرحمنا ولا تؤخذنا بما فعل السفهاء منا",
   "مَنْ كَانَ آخِرُ كَلاَمِهِ لاَ إِلَهَ إِلاَّ اللَّهُ دَخَلَ الْجَنَّة"
   "االلَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞 ",
"من الأدعية النبوية المأثورة:اللهمَّ زَيِّنا بزينة الإيمان",
"اااللهم يا من رويت الأرض مطرا أمطر قلوبنا فرحا 🍂 ",
"اا‏اللَّهُـمَّ لَڪَ الحَمْـدُ مِنْ قَـا؏ِ الفُـؤَادِ إلىٰ ؏َـرشِڪَ المُقـدَّس حَمْـدَاً يُوَافِي نِـ؏ـمَڪ 💙🌸",
"﴿وَاذْكُرِ اسْمَ رَبِّكَ وَتَبَتَّلْ إِلَيْهِ تَبْتِيلًا﴾🌿✨",
"﴿وَمَن يَتَّقِ اللهَ يُكَفِّرْ عَنْهُ سَيِّئَاتِهِ وَيُعْظِمْ لَهُ أَجْرًا﴾",
"«سُبْحَانَ اللهِ ، وَالحَمْدُ للهِ ، وَلَا إلَهَ إلَّا اللهُ ، وَاللهُ أكْبَرُ ، وَلَا حَوْلَ وَلَا قُوَّةَ إلَّا بِاللهِ»🍃",
"وذُنُوبًا شوَّهتْ طُهْرَ قُلوبِنا؛ اغفِرها يا ربّ واعفُ عنَّا ❤️",
"«اللَّهُمَّ اتِ نُفُوسَنَا تَقْوَاهَا ، وَزَكِّهَا أنْتَ خَيْرُ مَنْ زَكَّاهَا ، أنْتَ وَلِيُّهَا وَمَوْلَاهَا»🌹",
"۝‏﷽إن اللَّه وملائكته يُصلُّون على النبي ياأيُّها الذين امنوا صلُّوا عليه وسلِّموا تسليما۝",
"فُسِبًحً بًحًمًدٍ ربًکْ وٌکْنِ مًنِ الَسِاجّدٍيَنِ 🌿✨",
"اأقُمً الَصّلَاةّ لَدٍلَوٌکْ الَشُمًسِ إلَيَ غُسِقُ الَلَيَلَ🥀🌺",
"نِسِتٌغُفُرکْ ربًيَ حًيَتٌ تٌلَهّيَنِا الَدٍنِيَا عٌنِ ذِکْرکْ🥺😢",
"وٌمًنِ أعٌرض عٌنِ ذِکْريَ فُإنِ لَهّ مًعٌيَشُةّ ضنِکْا 😢",
"وٌقُرأنِ الَفُجّر إنِ قُرانِ الَفُجّر کْانِ مًشُهّوٌدٍا🎀🌲",
"اأّذّأّ أّلَدِنِيِّأّ نَِّستّګوِ أّصٌلَګوِ زِّوِروِ أّلَمَقِأّبِر💔",
"حًتٌيَ لَوٌ لَمًتٌتٌقُنِ الَخِفُظُ فُمًصّاحًبًتٌ لَلَقُرانِ تٌجّعٌلَکْ مًنِ اهّلَ الَلَهّ وٌخِاصّتٌهّ❤🌱",
"وٌإذِا رضيَتٌ وٌصّبًرتٌ فُهّوٌ إرتٌقُاء وٌنِعٌمًةّ✨??",
"«ربً اجّعٌلَنِيَ مًقُيَمً الَصّلَاةّ وٌمًنِ ذِريَتٌيَ ربًنِا وٌتٌقُبًلَ دٍعٌاء 🤲",
"ااعٌلَمً انِ رحًلَةّ صّبًرکْ لَهّا نِهّايَهّ عٌظُيَمًهّ مًحًمًلَهّ بًجّوٌائزٍ ربًانِيَهّ مًدٍهّشُهّ🌚☺️",
"اإيَاکْ وٌدٍعٌوٌةّ الَمًظُلَوٌمً فُ إنِهّا تٌصّعٌدٍ الَيَ الَلَهّ کْأنِهّا شُرارهّ مًنِ نِار 🔥🥺",
"االَلَهّمً انِقُذِ صّدٍوٌرنِا مًنِ هّيَمًنِهّ الَقُلَقُ وٌصّبً عٌلَيَهّا فُيَضا مًنِ الَطِمًأنِيَنِهّ✨🌺",
"يَابًنِيَ إنِ صّلَاح الَحًيَاةّ فُ أتٌجّاهّ الَقُبًلَهّ 🥀🌿",
"الَلَهّمً ردٍنِا إلَيَکْ ردٍا جّمًيَلَا💔🥺"
   ]
   while not await asyncio.sleep(1200):
     for i in chat:
       try:
         await app.send_message(i, random.choice(azkarl))
       except:
         pass
    
     
asyncio.create_task(azkar())